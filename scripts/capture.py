import requests 
import sqlite3
import yaml
import pandas
import json

def create_tables(db):

    cur = db.cursor()

    query = """
    create table jams 
        (blockingAlertUuid    text,
        city                  text,
        country               text,
        delay                 integer,
        endNode               text,
        length                integer,
        level                 integer,
        line                  text,
        pubMillis             integer,
        roadType              integer,
        segments              text,
        speed                 real,
        speedKMH              real,
        startNode             text,
        street                text,
        turnType              text,
        type                  text,
        uuid                  integer,
        endTimeMillis         integer,
        startTimeMillis       integer,
        startTime             numeric,
        endTime               numeric)"""
    
    
    try:
        cur.execute(query)
        conn.commit()
    except:
        pass

    query = """
    create table alerts 
        (city                 text,
        confidence            integer,
        country               text,
        location.x            real,
        location.y            real,
        magvar                integer,
        nThumbsUp             integer,
        pubMillis             integer,
        reliability           integer,
        reportDescription     text,
        reportRating          integer,
        roadType              real,
        street                text,
        subtype               text,
        type                  text,
        uuid                  text,
        endTimeMillis         integer,
        startTimeMillis       integer,
        startTime             numeric,
        endTime               numeric)"""

    
    try:
        cur.execute(query)
        conn.commit()
    except:
        pass
    
    cur.close()

def request_url(url):

    headers = {'user-agent': "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",}

    response = requests.get(url, headers=headers)

    return response.text

def add_fields(df, res):

    df['endTimeMillis'] = res['endTimeMillis']
    df['startTimeMillis'] = res['startTimeMillis']
    df['startTime'] = res['startTime']
    df['endTime'] = res['endTime']

    if 'line' in df.columns:
        df['line'] = df['line'].apply(str)
        df['segments'] = df['segments'].apply(str)

    return df

def to_db(res, db):

    res = json.loads(res)
    
    for each in ['alerts', 'jams']:
        df = pandas.io.json.json_normalize(res[each])
        df = add_fields(df, res)
        df.to_sql(each, db, if_exists='append', index=False)

def load_yaml():

    res = yaml.load(open('../polygons.yaml', 'r'))
    base_url = res['url']
    polygons = res['polygons']

    return {city:base_url + polygon for city, polygon in polygons.items()}

def load_db():

    db = sqlite3.connect('../data/mydb')
    create_tables(db)
    return db

def main():
    
    db = load_db()
    urls = load_yaml()
    
    for url in urls.values():
        res = request_url(url)
        to_db(res, db)

if __name__ == '__main__':
    main()
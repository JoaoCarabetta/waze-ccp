from sqlalchemy import create_engine

db = create_engine('mysql://root:root@db:8000/db')
    # host="db",    # your host, usually localhost
    #                  user="root",         # your username
    #                  passwd="root",  # your password
    #                  db='waze')   
print(db)

# engine = create_engine(
#                 "mysql://scott:tiger@localhost/test",
#                 isolation_level="READ UNCOMMITTED"
#             )
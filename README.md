# Waze CCP CLI

Por enquanto, só um exemplo de uma pipeline bem simples: captura, armazenamento e análise dos dados do waze.

Em `scripts` está o `capture.py` que usa o arquivo `polygons.yaml` da raiz para fazer as capturas. Portanto, é preciso preencher esse arquivo que tem a seguinte estrutura:

```
url: <url>
cities: 
    a:<polygon>
    b:<polygon>
```

Uma vez rodado com `python3 scripts/capture.py`, esse script cria um arquivo SQLite em `data/mydb` que contém duas tabelas. Uma para `jams` outra para `alerts`. 

O arquivo `cron.txt` contém a string usada para ativar o cron. Como os dados do Waze são atualizados de minuto a minuto, o cron foi configurado assim. Cuidado para não esquecer as capturas rodando sem querer!

---

Já no `notebooks` encontraremos um nomeado `captura` que foi usado para desenvolver a captura mas não tem nada de útil. No  `accidents` tem uma análise beeeeeem tosca dos dados. Mas mostra um pouco de como os dados serão usados. 

Acredito que aí já tenha um pipeline básico do que deve ser feito pelo CLI. Na minha visão, ele deveria abstrair toda a parte de captura e montagem dos ambientes. Então, ele seria responsável por:

1. Montar os bancos para captura
2. Inicializar a captura 
3. Instalar ambiente de análise com Jupyter Notebook e alguns pacotes essenciais: pandas, geopandas, shapely, leaflet.
4. Esse ambiente, inicialmente python, deve permitir que o usuário instale outros pacotes facilmente.
5. Os projetos feitos através dessa plataforma são integráveis, portanto, o projeto de uma cidade pode ser usado para outra com tão facilmente quanto `waze-ccp get <url>`


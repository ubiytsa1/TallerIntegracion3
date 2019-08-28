#---------------------------------------------------------------------------------------------
from pymongo import MongoClient
#---------------------------------------------------------------------------------------------
client = MongoClient('mongodb://localhost:27017/')

legislaturas =[
    {'ID': 3, 'numero': 319,'tipo':'extraordinaria'},
    {'ID': 4, 'numero': 320,'tipo':'ordinaria'},
    {'ID': 5, 'numero': 321,'tipo':'extraordinaria'}
    ]

with client:
    db = client.testdb
    db.legislaturas.insert_many(legislaturas)
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
from pymongo import MongoClient
#---------------------------------------------------------------------------------------------
client = MongoClient('mongodb://localhost:27017/')
with client:
    db = client.testdb
    legislaturas = db.legislaturas.find()
    for item in legislaturas:
        print('|ID: {0} | Numero: {1} | Tipo: {2}|'.format(item['ID'], item['numero'], item['tipo']))
#---------------------------------------------------------------------------------------------

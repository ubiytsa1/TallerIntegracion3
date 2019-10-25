import json
import xmltodict
from pymongo import MongoClient

#Transformacion de XML a JSON
with open("SCD.xml", 'r') as archivo:
    xmlString = archivo.read()
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
with open("SCD.json", 'w') as d:
    d.write(jsonString)

#Conexion a Mongo e ingreso de json a bdd
MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI)

db = client['ti3db'] #crea bdd si no existe previamente
collection_SCD = db['Scraping'] #crea o guarda dentro de una coleccion

with open('SCD.json') as f:
    jsonSCD = json.load(f)

collection_SCD.insert_one(jsonSCD)#inserta en la coleccion
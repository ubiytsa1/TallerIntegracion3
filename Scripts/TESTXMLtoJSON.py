import json
import xmltodict

with open("legislaturas.xml", 'r') as archivo:
    xmlString = archivo.read()

jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)

with open("legislaturas.json", 'w') as f:
    f.write(jsonString)
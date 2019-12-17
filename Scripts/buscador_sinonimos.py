#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-

import requests
import sys
from bs4 import BeautifulSoup


"""def leer_archivo():
	arch1=open("palabras.txt","r")
	arch1.readlines()
	print arch1
	return arch1
"""
def buscar_sinonimos(enlace):
	palabras_claves=[]
	sinonimos=[]

	url='http://www.wordreference.com/sinonimos/'
	print "el sinonimo a buscar es: "+enlace
	buscar=url+enlace
	resp=requests.get(buscar)
	bs=BeautifulSoup(resp.text,'lxml')
	lista=bs.find_all(class_='trans clickable')
        

	for sin in lista:
	    sino=sin.find_all('li')
	    for fin in sino:

	        palabras_claves.append(fin.next_element)
	if len(palabras_claves)>0:
		arreglo=[]
		cadena=palabras_claves[0]
		if len(cadena)>1:
			arreglo=cadena.split(", ")
			for tex in arreglo:
				sinonimos.append(tex.strip())


		for i in sinonimos:
		    print i
		print "-----------------------------------------------------------------------"
	else:
		print "No se ha encontrado sinonimos para ",enlace


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
Palabras =  [['paz','social','seguridad','orden','seguridad','tráfico','microtráfico','patrullaje','comisaría','detenidos','penados','libertad','vecinos','comunitarias']
        	,['asesoría','decisiones','gestión','cuenta','gobernante','gobernados']
            ,['dolar','economia','turismo','peso','competitividad','fomento','mercados', 'comercio', 'libre','inversión','aduanas']
            ,['justicia','normas','leyes','derechos','políticas','proteccion','seguridad','penal','delitos','cohecho','soborno','terrorismo']
            ,['medicina','hospitales','consultorios','médico','recuperación','salud','enfermedades','COMPIN','hospital','órganos']
            ,['minera','recursos','naturales','mina','mineras','mercurio']
            ,['energético','energía','eléctrica','combustibles','sec','planta','solar','electro','climático','ahorrar','eléctrico','generadores','diesel']
            ,['mujeres','discriminación','género','Sernam','igualdad','equidad','emprendedoras','violencia','aborto','lactancia','materna']
            ,['relacionamiento','mundo','exterior','extranjero','embajador','alianza','extranjera','intercambio']
            ,['estabilidad','sustentable']
            ,['desarrollo','pobreza','social','vulnerables','niñez','adolescencia','aporte','micro','pyme']
            ,['trabajador','trabajo','laboral','trabajadores','obra']
            ,['casas','hogar','ciudades','barrio','familias']
            ,['transporte','locomoción','traslado',' comunicaciones','telecomunicaciones','urbanas','tránsito','velocidad','telecomunicaciones','vehículos','transporte','licencia']
            ,['ecología','ambiental','renovables','naturales','contaminación','ambiental']
            ,['composicion','patrimonio','Artes','cultural','artesanía','biblioteca','museo','artísticas','escénicas','audiovisuales']
            ,['ejercito','naval','fach','fuerzas','armadas','armada','defensa','armas','destrucción']
            ,['proyecto','congreso','secretaria','gestion']
            ,['mineduc','bicentenario','escolar','escuelas','educacion','gratuidad','alumnos','jardín','profesores','tecnica','humanidades','ciencias','enseñanza','educativo','educacionales','matrícula','docente']
            ,['obras','públicas','aeropuertos','hidráulicas','vialidad','sanitarios','aguas','pavimentación']
            ,['agrícola','animales','agricultores','agroalimentario','lácteos','acuicultura','pesca']
            ,['inmuebles','patrimoniales','terreno','bienes','nacionales','geoespacial','monumento','territorio','nacional']
            ,['deporte','deportivas','actividad']
            ,['ciencia','innovación','tecnología','conicyt']]

for Ministerios in Palabras:
	for i in Ministerios:
		buscar_sinonimos(normalize(i))







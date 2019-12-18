#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-

import requests
import sys
from bs4 import BeautifulSoup

cadena_palabras=[]
def buscar_sinonimos(palabra):
	palabras_claves=[]
	sinonimos=[]

	url='http://www.wordreference.com/sinonimos/'
	print "el sinonimo a buscar es: "+palabra
	buscar=url+palabra
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
		cadena_palabras.append(sinonimos)
		for i in sinonimos:
		    print i
	else:
		print "No se ha encontrado sinonimos para ",palabra
	print "-----------------------------------------------------------------------"

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
ministerios =  ["Interior","Secretaria del gobierno","Economia","Justicia","Salud","Mineria","Energia","Mujer","Relaciones",
             "Hacienda","DesarrolloF","Trabajo","Vivienda",
             "Transporte","Ambiente","Cultura","Defensa",
             "Secretaria general de la Presidencia ","Educacion","Obras","Agricultura",
             "Bienes","Deporte","Ciencias"]

Palabras =  [['seguridad','orden']
            ,['asesoría','decisiones','gestión','gobernante']
            ,['economia','mercados','inversión']
            ,['justicia','derechos','delitos','terrorismo']
            ,['medicina','hospitales','médico','salud','enfermedades','COMPIN','órganos']
            ,['minera','naturales']
            ,['energía','eléctrica','combustibles']
            ,['mujeres','discriminación','Sernam','igualdad','equidad']
            ,['relacionamiento','exterior','extranjero','embajador','alianza']
            ,['estabilidad','sustentable']
            ,['desarrollo','pobreza','vulnerables']
            ,['trabajador','trabajo','laboral']
            ,['casas','barrio','familias']
            ,['transporte',' comunicaciones','telecomunicaciones']
            ,['ecología','ambiental','renovables','naturales','contaminación']
            ,['patrimonio','Artes','cultural','artesanía','biblioteca','museo']
            ,['ejercito','armadas','armas']
            ,['proyecto','congreso','secretaria','gestion']
            ,['escolar','escuelas','educacion','gratuidad','alumnos','profesores']
            ,['obras','públicas','aguas','pavimentación']
            ,['agrícola','animales','agricultores','pesca']
            ,['patrimoniales','terreno','bienes','monumento']
            ,['deporte','deportivas','actividad']
            ,['ciencia','innovación','tecnología','conicyt']]           




palabras_ministerios=[]
cadenita=[]
cadena_ministerio=[]
contador=0
for Ministerios in Palabras:
	for i in Ministerios:
		buscar_sinonimos(normalize(i))
        #cadena_palabras
        for xleb in cadena_palabras:
            for y in xleb:
                cadenita.append(y)
                pass
            pass
        cadena_ministerio.append(cadenita)
        cadenita=[]
        cadena_palabras=[]
        contador+=1    


for x in cadena_ministerio:
    print x
    pass



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

palabras_c="hidráulicas"



buscar_sinonimos(normalize(palabras_c))


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-

import requests
import sys
from bs4 import BeautifulSoup

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

	#print palabras_claves[0]
	arreglo=[]
	for palabra in range(len(palabras_claves)):
	    cadena=palabras_claves[palabra]
	    if len(cadena)>1:
	        arreglo=cadena.split(", ")
	        for tex in arreglo:
	        	sinonimos.append(tex.strip())


	for i in sinonimos:
	    print i
	print "-----------------------------------------------------------------------"

palabras_claves=["economia","deporte","ciencia","agricultura"]

for pala in palabras_claves:
	buscar_sinonimos(pala)
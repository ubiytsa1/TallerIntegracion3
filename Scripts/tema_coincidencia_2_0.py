# -*- coding: cp1252 -*-
import numpy as np
from xml.dom import minidom
import xml.etree.cElementTree as ET
import json

#----------------Funcion distancia entre palabras ----------#

def tema (str_proyecto):

    #Funcion para la distancia entre palabras#
    def levenshtein(seq1, seq2):
        size_x = len(seq1) + 1
        size_y = len(seq2) + 1
        matrix = np.zeros ((size_x, size_y))
        for x in xrange(size_x):
            matrix [x, 0] = x
        for y in xrange(size_y):
            matrix [0, y] = y

        for x in xrange(1, size_x):
            for y in xrange(1, size_y):
                if seq1[x-1] == seq2[y-1]:
                    matrix [x,y] = min(
                        matrix[x-1, y] + 1,
                        matrix[x-1, y-1],
                        matrix[x, y-1] + 1
                    )
                else:
                    matrix [x,y] = min(
                        matrix[x-1,y] + 1,
                        matrix[x-1,y-1] + 1,
                        matrix[x,y-1] + 1
                    )
        return (matrix[size_x - 1, size_y - 1])


    #Limpia los string de caracteres de puntuacion#
    palabras_str= str_proyecto.replace(';',' ').replace('.',' ').replace(',',' ').split()
    palabras_str= [x.lower() for x in palabras_str]

    #Temas
    temas = ["MInterior","MSecretariaG","MEconomia","MJusticia",
             "MSalud","MMineria","MEnergia","MMujer","MRelaciones",
             "MHacienda","MDesarrolloF","MTrabajo","MVivienda",
             "MTransporte","MMAmbiente","MCultura","MDefensa",
             "MSecretariaP","MEducacion","MObras","MAgricultura",
             "MBienesN","MDeporte","MCiencias"]

    #Palabras de los temas (aqui irian los temas con sus palabras obviamente no asi#
    Palabras =  [['paz','social','seguridad','orden','seguridad','tr�fico','microtr�fico','patrullaje','comisar�a','detenidos','penados','libertad','vecinos','comunitarias']
                ,['asesor�a','decisiones','gesti�n','cuenta','gobernante','gobernados']
                ,['dolar','economia','turismo','peso','competitividad','fomento','mercados', 'comercio', 'libre','inversi�n','aduanas']
                ,['justicia','normas','leyes','derechos','pol�ticas','proteccion','seguridad','penal','delitos','cohecho','soborno','terrorismo']
                ,['medicina','hospitales','consultorios','m�dico','recuperaci�n','salud','enfermedades','COMPIN','hospital','�rganos']
                ,['minera','recursos','naturales','mina','mineras','mercurio']
                ,['energ�tico','energ�a','el�ctrica','combustibles','sec','planta','solar','electro','clim�tico','ahorrar','el�ctrico','generadores','diesel']
                ,['mujeres','discriminaci�n','g�nero','Sernam','igualdad','equidad','emprendedoras','violencia','aborto','lactancia','materna']
                ,['relacionamiento','mundo','exterior','extranjero','embajador','alianza','extranjera','intercambio']
                ,['estabilidad','sustentable']
                ,['desarrollo','pobreza','social','vulnerables','ni�ez','adolescencia','aporte','micro','pyme']
                ,['trabajador','trabajo','laboral','trabajadores','obra']
                ,['casas','hogar','ciudades','barrio','familias']
                ,['transporte','locomoci�n','traslado',' comunicaciones','telecomunicaciones','urbanas','tr�nsito','velocidad','telecomunicaciones','veh�culos','transporte','licencia']
                ,['ecolog�a','ambiental','renovables','naturales','contaminaci�n','ambiental']
                ,['composicion','patrimonio','Artes','cultural','artesan�a','biblioteca','museo','art�sticas','esc�nicas','audiovisuales']
                ,['ejercito','naval','fach','fuerzas','armadas','armada','defensa','armas','destrucci�n']
                ,['proyecto','congreso','secretaria','gestion']
                ,['mineduc','bicentenario','escolar','escuelas','educacion','gratuidad','alumnos','jard�n','profesores','tecnica','humanidades','ciencias','ense�anza','educativo','educacionales','matr�cula','docente']
                ,['obras','p�blicas','aeropuertos','hidr�ulicas','vialidad','sanitarios','aguas','pavimentaci�n']
                ,['agr�cola','animales','agricultores','agroalimentario','l�cteos','acuicultura','pesca']
                ,['inmuebles','patrimoniales','terreno','bienes','nacionales','geoespacial','monumento','territorio','nacional']
                ,['deporte','deportivas','actividad']
                ,['ciencia','innovaci�n','tecnolog�a','conicyt']]

    #Aplica la funcion de distancia y coloca el resultado en un arreglo#
    val_dist = []
    for i in range(len(Palabras)):
        val_dist.append(levenshtein(palabras_str,Palabras[i]))

    #Asigna el tema segun el mayor numero encontrado y lo imprime#
    tema = temas[np.argmin(val_dist)]
    return "<coincidencia_tema>El tema con el que mas coincidencia tiene es "+tema+"</coincidencia_tema>"


#Abre el archivo XML
doc = ET.parse("SCD.xml").getroot()


#Toma los elementos que tienen la etiqueta "votacion_tema" y les asigna el tema
xml = ""
xml += "<temas>"
xml += "\n"
for item in doc.iter("votacion_tema"):
    elemento_str = ET.tostring(item)
    xml += elemento_str
    xml += "\n"
    xml += tema(elemento_str)
    xml += "\n"
xml += "</temas>"
    
#Guarda en un archivo XML
archivo = open("temas_coincidencia.xml", "w")
archivo.write(xml)



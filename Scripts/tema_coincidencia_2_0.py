# -*- coding: cp1252 -*-
import numpy as np
from xml.dom import minidom
import xml.etree.cElementTree as ET


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

    #Aplica la funcion de distancia y coloca el resultado en un arreglo#
    val_dist = []
    for i in range(len(Palabras)):
        val_dist.append(levenshtein(palabras_str,Palabras[i]))

    #Asigna el tema segun el mayor numero encontrado y lo imprime#
    tema = temas[np.argmin(val_dist)]
    print "El tema con el que mas coincidencia tiene es ",tema


#Abre el archivo XML
doc = ET.parse("SCD.xml").getroot()

#Toma los elementos que tienen la etiqueta "votacion_tema" y les asigna el tema
for item in doc.iter("votacion_tema"):
    elemento_str = ET.tostring(item)
    print elemento_str
    print "------"
    tema(elemento_str)
    print "############################"





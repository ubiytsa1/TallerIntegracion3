# encoding: utf-8
#----------------------------------------------(IMPORTS)----------------------------------------------
import urllib2
import sys
import xml.etree.cElementTree as ET
import os.path as path
import os
import time as ti
#---------------------------------------------(FUNCIONES)---------------------------------------------
#Recibe url>>retorna codigo fuente
def ObtenerFuente(url):
    pagina = urllib2.urlopen(url)
    CodigoFuente = pagina.read()
    return CodigoFuente

#Recibe string>>retorna ID's en array
def ObtenerID(string):
    arreglo=[]
    for line in string.splitlines():
        if "<ID>" in line or "<Id>" in line or "<id>" in line:
            line = line[line.find(">")+1:len(line)]
            line = line[0:line.find("<")]
            if line!="":
                arreglo.append(line)
    arreglo = list(dict.fromkeys(arreglo))
    return arreglo
#recibe string>>retorna ID's de boletines en array
def ObtenerIDBoletin(string):
    arreglo=[]
    while True:
        indice= string.find("BOLETIN=")
        if indice==-1:
            break
        linea=string[indice:len(string)]
        corte1=linea[0:linea.find(">")-1]
        corte2=corte1[9:len(corte1)]
        corte2=CorteEspacios(corte2)
        if "y" in corte2 or "Y" in corte2 or "," in corte2:
            separados=SeparadorElementos(corte2)
            if separados.count!=0:
                arreglo.extend(separados)
        elif corte2!="":
            corte2=CorteSoloNumeros(corte2)
            arreglo.append(corte2)
        string=string[indice+20:len(string)]
    arreglo = list(dict.fromkeys(arreglo))
    return arreglo
#Recibe string>>retorna el string sin espacios por adelante ni por atras
def CorteEspacios(string):
    if string=="":
        return string;
    inicio_sin_espacios=False
    final_sin_espacios=False
    while (inicio_sin_espacios==False or final_sin_espacios==False):
        if string[0]==" ":
            string=string[1:len(string)]
        else:
            inicio_sin_espacios=True
        if string[len(string)-1]==" ":
            string=string[0:len(string)-1]
        else:
            final_sin_espacios=True
    return string
#Recibe string con numero dentro>>retorna solo el numero dentro del string, recortando texto por el inicio y por el final
def CorteSoloNumeros(string):
    if string=="":
        return string;
    inicio_solo_numeros=False
    final_solo_numeros=False
    while(inicio_solo_numeros==False or final_solo_numeros==False):
        if string[0].isdigit()==False :
            string=string[1:len(string)]
        else:
            inicio_solo_numeros=True
        if string[len(string)-1].isdigit()==False:
            string=string[0:len(string)-1]
        else:
            final_solo_numeros=True
    return string
#Recibe string con elementos separados por Y y comas>>retorna elementos separados en array
def SeparadorElementos(string):
    arreglo=[]
    if (string.find("Y"))!=-1 or (string.find("y"))!=-1 or (string.find(","))!=-1:
        cantidad_boletines=string.count("Y") + string.count("y") + string.count(",") + 1
        for x in range (0,cantidad_boletines):
            if x!=cantidad_boletines -1:#si no es el ultimo boletin
                if string.find("Y")!=-1:
                    Y=string.find("Y")
                else:
                    Y=100
                if string.find("y")!=-1:
                    y=string.find("y")
                else:
                    y=100
                if string.find(",")!=-1:
                    coma=string.find(",")
                else:
                    coma=100
                siguiente_elemento=min([Y,y,coma])
                boletin_cortado=string[0:siguiente_elemento-1]
                string=string[siguiente_elemento +1:len(string)]
                boletin_cortado=CorteSoloNumeros(boletin_cortado)
                arreglo.append(boletin_cortado)
            else: #si es ultimo boletin
                boletin_cortado=CorteEspacios(string)
                boletin_cortado=CorteSoloNumeros(boletin_cortado)
                arreglo.append(boletin_cortado)
    return arreglo
#Recibe boletin>>retorna proyecto de ley tratados siesque hay, sino 0
def ObtenerProyectoLey(string):
    veces=string.count("<TEMA>")
    tema=""
    if veces!=0:
        for x in range(0,veces):
            index_tema=string.find("<TEMA>")
            string=string[index_tema + 6: len(string)]
            index_tema=string.find("</TEMA>")
            string=string[0:index_tema]
            tema=tema+string
        return tema
    return 0
#limpia pantalla y escribe
def escribe(string):
    os.system("cls")
    print string
#Recibe string>>devuelve strning sin caracteres no ascii
def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)
#-----------------------------------------------(CODIGO)----------------------------------------------
#Flush de Input/Output
sys.stdout.flush()
escribe("Limpiando I/O")
#Obtencion de ID's
escribe("Obteniendo ID's")
ID_Legislaturas=ObtenerID(ObtenerFuente("http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturas"))
ID_UltimaLegislatura=ID_Legislaturas[len(ID_Legislaturas)-1]
ID_Sesiones=ObtenerID(ObtenerFuente("http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+ID_UltimaLegislatura))
ID_Boletines=[]
#Verificacion de ultima sesion
escribe("Verificando ultima sesion")
index_ultima_sesion=0
if path.exists("ultima_sesion.txt"):
    archivo = open("ultima_sesion.txt","r")
    ultima_sesion=archivo.read()
    index_ultima_sesion=ID_Sesiones.index(ultima_sesion)
    sesion_actual=ID_Sesiones[len(ID_Sesiones)-1]
    archivo.close()
    print "| Ultima Sesion:",ultima_sesion," | Sesion Actual:",sesion_actual
    if ultima_sesion==sesion_actual:
        print "| No hay sesiones nuevas, Cerrando script..."
        for x in [3,2,1,0]:
            ti.sleep(1)
            print x
        sys.exit(0)
#Archivo ultima sesion
escribe("Actualizando archivo de ultima sesion")
f= open("ultima_sesion.txt","w+")
f.write(ID_Sesiones[len(ID_Sesiones)-1])
f.close()
contador=0
#Obtener boletines de sesiones
escribe("Obteniendo boletines")
for sesion in ID_Sesiones:
    if contador>=index_ultima_sesion:
        ID_Boletines_Sesion=ObtenerIDBoletin(ObtenerFuente("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=" + sesion))
        if len(ID_Boletines_Sesion)!=0:
            print "| ID de sesion: ",sesion," | ID boletines: ",ID_Boletines_Sesion
            ID_Boletines.extend(ID_Boletines_Sesion)
    contador=contador+1
#Elimina boletines repetidos
escribe("Eliminando boletines repetidos")
ID_Boletines = list(dict.fromkeys(ID_Boletines))
#Obtencion de temas de proyectos de ley y escritura de archivo XML
escribe("Obteniendo proyectos de ley")
SCD = ET.Element("SCD")
XMLboletin = ET.SubElement(SCD, "BOLETINES")
for boletin in ID_Boletines:
    tema=ObtenerProyectoLey( ObtenerFuente("https://www.senado.cl/wspublico/tramitacion.php?boletin="+boletin[0:boletin.find("-")]))
    if tema!=0:
        saltar=0
        try:
            tema=unicode(tema, "utf-8").encode('utf-8').strip()
        except:
            print "| ERROR UNICODE | ID:",boletin
            try:
                tema=tema.encode('utf-8').strip()
            except:
                print "| ERROR ASCII | ID:",boletin
                try:
                    tema=removeNonAscii(tema)
                except:
                    print "| ERROR QUITANDO CARACTERES NO ASCII | ID:",boletin
                    saltar=1
        if saltar==0:
            ET.SubElement(XMLboletin, "BOLETIN", ID=boletin).text = tema.decode("utf8")
            print "| proyecto de ley extraido en boletin: ",boletin
escribe("Guardando archivo XML")
try:
    tree = ET.ElementTree(SCD)
    tree.write("SCD.xml")
    escribe("archivo XML guardado")
except:
    escribe("Error fatal guardando datos en archivo XML")
ti.sleep(1)
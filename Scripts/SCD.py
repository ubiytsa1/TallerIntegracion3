#----------------------------------------------(IMPORTS)----------------------------------------------
import urllib2
import sys
import time
#---------------------------------------------(FUNCIONES)---------------------------------------------
#Recibe url>>devuelve codigo fuente
def ObtenerFuente(url):
    pagina = urllib2.urlopen(url)
    CodigoFuente = pagina.read()
    return CodigoFuente

#Recibe string>>devuelve ID's' en array
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

def ObtenerIDBoletin(string):
    arreglo=[]
    while True:
        indice= string.find("olet")
        if indice==-1:
            break
        corte1=string[indice:len(string)]
        corte2=corte1[0:corte1.find("-")+5]
        if len(corte2)<30:
            for x in corte2:
                if x.isdigit():
                    break
                else:
                    corte2=corte2[1:len(corte2)]
            corte2revertido=corte2[::-1]
            for x in corte2revertido:
                if x.isdigit():
                    break
                else:
                    corte2=corte2[:-1]
            if corte2!="":
                arreglo.append(corte2)
        string=string[indice+20:len(string)]
    arreglo = list(dict.fromkeys(arreglo))
    return arreglo
#-----------------------------------------------(CODIGO)----------------------------------------------
sys.stdout.flush()

ID_Legislaturas=ObtenerID(ObtenerFuente("http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturas"))
ID_UltimaLegislatura=ID_Legislaturas[len(ID_Legislaturas)-1]
ID_Sesiones=ObtenerID(ObtenerFuente("http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+ID_UltimaLegislatura))
SUPER=[]
for sesion in ID_Sesiones:
    ID_Boletines=ObtenerIDBoletin(ObtenerFuente("http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=" + sesion))
    print "ID de sesion: ",sesion," | ID boletines: ",ID_Boletines

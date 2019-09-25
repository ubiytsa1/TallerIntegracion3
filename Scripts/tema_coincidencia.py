# encoding: utf-8
from difflib import SequenceMatcher as SM                           #Importacion de libreria

#difflib es una libreria dedicada a la identificacion de secuencias y coincidencias dentro de un
#texto dado, en este caso usaremos el ratio, que se aplica mas adelante, el cual entrega un numero
#del 0 al 1 segun el grado de coincidencia que tenga con un conjunto de palabras o una en particular

def tema_proyecto(str_proyecto):

    #----------------------------------------TEMAS SEGUN MINISTERIO----------------------------------------#
    temas = ['Interior y Seguridad Publica','Secretaria general del gobierno','Economia, Fomento y Turismo','Justicia y Derechos Humanos',
             'Salud','Mineria','Energia','Mujer y la Equidad de Genero','Relaciones exteriores','Hacienda','Desarrollo Social y Familia',
             'Trabajo y Prevision Social','Vivienda y Urbanismo','Transportes y Telecomunicaciones','Medio Ambiente','Culturas, Artes y el Patrimonio',
             'Defensa Nacional','Secretaria general de la Presidencia','Educacion','Obras Publicas','Agricultura','Bienes Nacionales',
             'Deporte','Ciencia, Tecnologia, Conocimiento e Innovacion']

    #----------------------------------------PALABRAS CLAVE----------------------------------------#
    MInterior=['paz','social','seguridad','orden','seguridad','tráfico','microtráfico','patrullaje','comisaría','detenidos','penados','libertad','vecinos','comunitarias']
    MSecretariaG=['asesoría','decisiones','gestión','cuenta','gobernante','gobernados']
    MEconomia=['dolar','economia','turismo','peso','competitividad','fomento','mercados', 'comercio', 'libre','inversión','aduanas']
    MJusticia=['justicia','normas','leyes','derechos','políticas','proteccion','seguridad','penal','delitos','cohecho','soborno','terrorismo']
    MSalud=['medicina','hospitales','consultorios','médico','recuperación','salud','enfermedades','COMPIN','hospital','órganos']
    MMineria=['minera','recursos','naturales','mina','mineras','mercurio']
    MEnergia=['energético','energía','eléctrica','combustibles','SEC','planta','solar','electro','climático','ahorrar','eléctrico','generadores','diesel']
    MMujer=['mujeres','discriminación','género','Sernam','igualdad','equidad','emprendedoras','violencia','aborto','lactancia','materna']
    MRelaciones=['relacionamiento','mundo','exterior','extranjero','embajador','alianza','extranjera','intercambio']
    MHacienda=['estabilidad','sustentable']
    MDesarrolloF=['desarrollo','pobreza','social','vulnerables','niñez','adolescencia','aporte','micro','pyme']
    MTrabajo=['trabajador','trabajo','laboral','trabajadores','obra']
    MVivienda=['casas','hogar','ciudades','barrio','familias']
    MTransporte=['transporte','locomoción','traslado',' comunicaciones','telecomunicaciones','urbanas','tránsito','velocidad','telecomunicaciones','vehículos','transporte','licencia']
    MMAmbiente =['ecología','ambiental','renovables','naturales','contaminación','ambiental']
    MCultura=['composicion','patrimonio','Artes','cultural','artesanía','biblioteca','museo','artísticas','escénicas','audiovisuales']
    MDefensa=['ejercito','naval','fach','fuerzas','armadas','armada','defensa','armas','destrucción']
    MSecretariaP=['proyecto','congreso','secretaria','gestion']
    MEducacion=['mineduc','bicentenario','escolar','escuelas','educacion','gratuidad','alumnos','jardín','profesores','tecnica','humanidades','ciencias','enseñanza','educativo','educacionales','matrícula','docente']
    MObras=['obras','públicas','aeropuertos','hidráulicas','vialidad','sanitarios','aguas','pavimentación']
    MAgricultura=['agrícola','animales','agricultores','agroalimentario','lácteos','acuicultura','pesca']
    MBienesN=['inmuebles','patrimoniales','terreno','bienes','nacionales','geoespacial','monumento','territorio','nacional']
    MDeporte=['deporte','deportivas','actividad']
    MCiencias=['ciencia','innovación','tecnología','conicyt']


    #Recepcion del string, separacion de palabras para analisis y eliminacion de puntuaciones
    palabras= str_proyecto.lower().replace(';',' ').replace('.',' ').replace(',',' ').split()

    #arreglo que guardara lo valores de coincidencia                                                                                                                                                  #por espacios
    lista_coinc = []
       
    #el ratio entrega un numero entre 0 y 1, esto segun el grado de coincidencia que entregue
    coinc_interior = (lista_coinc.append((SM(None,palabras,MInterior).ratio())))
    coinc_secregg = (lista_coinc.append((SM(None,palabras,MSecretariaG).ratio())))
    coinc_economia = (lista_coinc.append((SM(None,palabras,MEconomia).ratio())))
    coinc_justicia = (lista_coinc.append((SM(None,palabras,MJusticia).ratio())))
    coinc_salud = (lista_coinc.append((SM(None,palabras,MSalud).ratio())))
    coinc_mineria = (lista_coinc.append((SM(None,palabras,MMineria).ratio())))
    coinc_energia = (lista_coinc.append((SM(None,palabras,MEnergia).ratio())))
    coinc_mujer = (lista_coinc.append((SM(None,palabras,MMujer).ratio())))
    coinc_relaciones = (lista_coinc.append((SM(None,palabras,MRelaciones).ratio())))
    coinc_hacienda = (lista_coinc.append((SM(None,palabras,MHacienda).ratio())))
    coinc_desarrollo = (lista_coinc.append((SM(None,palabras,MDesarrolloF).ratio())))
    coinc_trabajo = (lista_coinc.append((SM(None,palabras,MTrabajo).ratio())))
    coinc_vivienda = (lista_coinc.append((SM(None,palabras,MVivienda).ratio())))
    coinc_transporte = (lista_coinc.append((SM(None,palabras,MTransporte).ratio())))
    coinc_mambiente = (lista_coinc.append((SM(None,palabras,MMAmbiente).ratio())))
    coinc_cultura = (lista_coinc.append((SM(None,palabras,MCultura).ratio())))
    coinc_defensa = (lista_coinc.append((SM(None,palabras,MDefensa).ratio())))
    coinc_secregp = (lista_coinc.append((SM(None,palabras,MSecretariaP).ratio())))
    coinc_educacion = (lista_coinc.append((SM(None,palabras,MEducacion).ratio())))
    coinc_obras = (lista_coinc.append((SM(None,palabras,MObras).ratio())))
    coinc_agricultura = (lista_coinc.append((SM(None,palabras,MAgricultura).ratio())))
    coinc_bienesn = (lista_coinc.append((SM(None,palabras,MBienesN).ratio())))
    coinc_deporte = (lista_coinc.append((SM(None,palabras,MDeporte).ratio())))
    coinc_ciencias = (lista_coinc.append((SM(None,palabras,MCiencias).ratio())))

    #Imprime todos los temas y el grado de coincidencia encontrado
    print "Datos de coincidencia:"
    for i in range(24):
        print temas[i]+' = '+str(lista_coinc[i])


    #indica la posicion del mayor valor de coincidencia dentro del arreglo lista_coinc
    id_tema = lista_coinc.index(max(lista_coinc))

    #Imprime el tema de mayor coincidencia con el texto dado
    print "###############################"
    print "Tema mayor coincidencia: ",temas[id_tema]



str_boletin = 'MODIFICA LA LEY N° 19.070 QUE APROBÓ EL ESTATUTO DE LOS PROFESIONALES DE LA EDUCACIÓN, Y DE LAS LEYES QUE LA COMPLEMENTAN Y MODIFICAN,PARA PERFECCIONAR LA CAUSAL DE TÉRMINO DE LA RELACIÓN LABORAL DE LOS DOCENTES MUNICIPALES, DETERMINADA POR SALUD INCOMPATIBLE'


tema_proyecto(str_boletin)

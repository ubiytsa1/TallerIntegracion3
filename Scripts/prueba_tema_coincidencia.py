from difflib import SequenceMatcher as SM                           #Importacion de libreria

#difflib es una libreria dedicada a la identificacion de secuencias y coincidencias dentro de un
#texto dado, en este caso usaremos el ratio, que se aplica mas adelante, el cual entrega un numero
#del 0 al 1 segun el grado de coincidencia que tenga con un conjunto de palabras o una en particular

def tema_proyecto(str_proyecto):
    saludo = ['hola','como']            #Conjunto de palabras clave 1
    despedida = ['chao']                #Conjunto de palabras clave 2
    palabras= str_proyecto.replace(';',' ').replace('.',' ').replace(',',' ').split()   #Separacion del string
                                                                                        #Reemplazar puntuaciones                                                                              #por espacios
    lista_coinc = []                    #arreglo que guardara lo valores de coincidencia
    temas = ['saludo','despedida']      #arreglo de temas
    

    #el ratio entrega un numero entre 0 y 1, esto dado el porcentaje de coincidencia, ese es multiplicado por 100
    #luego redondeado y transformado a un int de 2 digitos
    coinc_saludo = (lista_coinc.append(int(round((SM(None,palabras,saludo).ratio())*100))))      
    coinc_despedida = (lista_coinc.append(int(round((SM(None,palabras,despedida).ratio())*100)))) 

    print lista_coinc

    id_tema = lista_coinc.index(max(lista_coinc)) #indica la posicion del mayor valor

    print temas[id_tema]    #imprime el tema de mayor coincidencia




str_proyecto = 'hola hola como calcetin, calcetin.... chao chao chao'


tema_proyecto(str_proyecto)

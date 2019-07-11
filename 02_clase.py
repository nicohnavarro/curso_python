#Tipos de datos
#Numericos -> Enteros(int),ComaFlotante(float),Complejos
#Textos ->'' "" """ """
#Booleanos -> True False
#Variable ->Espacio de la memoria del ordenador, ese valor puede cambiar
#   durante la ejecucion del programa
#TODO es un objeto
#funcion type()
nombre="Nicolas"
type(nombre)

mensaje="""Esto es un mensaje
...con tres saltos
...de linea"""
print (mensaje)
print("\n")
print("----------------------Funciones----------------------")
#FUNCIONES
#def nombre_funcion():
    #instrucciones
    #return(opcional)
#def nombre_funcion(parametros):
    #instrucciones
    #return(opcional)

def mi_funcion(nombre):
    print(nombre)

mi_funcion(nombre)
print("\n")
#Funciones predefinidas propias del lenguaje 

#LISTAS
print("----------------------Listas----------------------")
print("\n")
miLista=["Maria","Nicolas","Mirta","Omar","Aline"]
print(miLista[0]) #Primer elemento de la lista
print(miLista[-2]) #Tambien puede ir de atras para adelante (Anteultimo elemento)
print(miLista[0:3]) #Varios elementos desde 0 incluido hasta 3 excluido
print(miLista[:3]) #Se sobrentiende que comienza en 0
print(miLista[2:]) #Desde indice 2 hasta el final

#Agregar a la lista al final de la lista
miLista.append("Melissa")
#Insertar a la lista en cualquier lugar o indice
miLista.insert(2,"Adrian")
print(miLista[2:])
#Concatenar a la lista
miLista.extend(["Pepe","Juan","Lucia"])
print(miLista[0:])
#Para saber el indice
print(miLista.index("Nicolas"))
miLista.insert(0,"Nicolas")
print(miLista.index("Nicolas"))
print(miLista)
print("Melissa" in miLista)
#Eliminar elementos
miLista.remove("Nicolas")
print(miLista[:])
#Eliminar el ultimo de la lista
miLista.pop()
print(miLista)

#Suma de  lista y multiplicacion
milista_2=["Nicolas","Nicolas","Nicolas"]*3
miLista_3=miLista+milista_2
print(miLista_3)
print(milista_2)

#TUPLAS
#Inmutables no se puede
#   Añadir
#   Eliminar
#   Mover
#   No busquedas index
#Utilidades
#   Mas rapido
#   Menos espacio
#   Formatear Strings
#   Claves en un diccionario (Listas no)
#   Si comprobar si un elemento se encuentra en la tupla
#Importante
#   Si permite extraer porciones pero devuelve otra tupla
print("\n")
print("----------------------Tuplas----------------------")
print("\n")
mi_tupla=("nico","meli","1234")
print(mi_tupla)
mi_lista=list(mi_tupla) #Hago una lista con la tupla
print(mi_lista)
mi_lista.append("11111")
mi_tupla=tuple(mi_lista) #Modifico la tupla
print(mi_tupla)
print(mi_tupla.count("11111")) #Cuantas veces esta el elemento en la tupla
print(len(mi_tupla)) #Cantidad de elementos en la tupla
mi_tupla_2="Nico","1234",12,310 #Empaquetado de tupla
nombre,identidad,mes,precio=mi_tupla_2 #Desempaquetado de tupla
print(precio,identidad,nombre,mes)
print(mi_tupla_2)

print("\n")
print("----------------------Diccionarios----------------------")
print("\n")
#DICCIONARIOS
#Variables de clave-valor
#diccionario={clave:valor,clave:valor,clave:valor}
midiccionario={"Argentina":"Buenos Aires","España":"Madrid","Peru":"Lima","Francia":"Paris"}
print(midiccionario)
print(midiccionario["Peru"])
#Agregar mas elementos al diccionario
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
#Nunca se modifica la clave, no hay 2 claves iguales siempre se sobreescriben 
print(midiccionario)
#Eliminar elementos
del midiccionario["Peru"]
print(midiccionario)
#Diferentes tipos de datos
midiccionario_2={"Argentina":"Buenos Aires",23:"Jordan",10:"Messi","Cristiano":7}
print(midiccionario_2)
#Tuplas - Listas Diccionario
mitupla=["Argentina","Peru","Uruguay","Colombia"]
midiccionario_3={mitupla[0]:"Buenos Aires",mitupla[1]:"Lima",mitupla[3]:"Bogota"}
print(midiccionario_3)
#Diccionario adentro de Diccionario
midiccionario_messi={"Nombre":"Messi","Numero":10,"Nacimiento":"Rosario","Balones de Oro":{"Años":[2001,2003,2004,2006,2008]}}
print(midiccionario_messi)
#Metodos Importantes
#Claves
print(midiccionario_messi.keys())
#Valores
print(midiccionario_messi.values())
#Cantidad de valores
print(len(midiccionario_messi))
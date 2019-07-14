#Modulos
#Son archivos que tiene su propio namespace y puede tener funciones,clase,variable, incluso otros modulos
#Modularizacion y reutilizacion de codigo
#Dividir en codigo en varias partes
#import modulos.funciones_matematicas
    #como evitar utilizar el nombre del modulo para utilizar la funcion...
#from modulos.funciones_matematicas import sumar
    #pero para utilizar todas las funciones se utiliza...
from modulos.funciones_matematicas import * #El * sirve para utilizar todo el codigo del modulo
from modulos.modulo_vehiculos import Moto
#modulos.funciones_matematicas.sumar(7,1)
print("-----------------Modulo de Operaciones-----------------")
sumar(1,10)
restar(1,10)
multiplicar(1,10)
print("\n-----------------Modulo de Vehiculos-------------------")
miCoche=Moto("Kawasaki","Ninja-600")
miCoche.estado()
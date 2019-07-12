#Objetos Clase 25
#Definimos la clase
class Coche():

    #Estado inicial atravez del constructor...
    def __init__(self):
        #Propiedades
        self.__largoChasis=250  
        self.__anchoChasis=120
        self.__ruedas=4   #Con __ lo haces privado (Encapsulacion)
        self.__enMarcha=False
        self.color="Negro"

    #Comportamiento o Metodos
    #Diferencia entre metodo y funcion ->La funcion no depende de una clase
    def Arrancar(self,arrancamos): #el self hace referencia al propio objeto(la instancia) perteneciente a la clase
        self.__enMarcha=arrancamos
        if(self.__enMarcha):
            print("El coche esta en marcha")
            chequeo=self.__chequeo_interno()
            if(chequeo):
                print("El chequeo ha sido positivo")
        else:
            return "El coche esta parado"

    def Estado(self):
        print("El coche tiene ",self.__ruedas,"ruedas")
        print("Un ancho de ",self.__anchoChasis)
        print("Un largo de ",self.__largoChasis)
        print("Color :",self.color)
        print("Estado :",self.__enMarcha)
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="Ok"
        self.aceite="Ok"
        self.puertas="Cerradas"
        if(self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas"):
            return True
        else:
            return False


#Mi programa
print("--------------------------Objetos--------------------------")
miCoche1=Coche()
miCoche1.Arrancar(True)
miCoche1.Estado()


#Estado inicial del objeto
#Encapsulacion
print("--------------------------Segundo objeto--------------------------")
miCoche2=Coche()
miCoche2.Arrancar(False)
miCoche2.Estado()
miCoche2.Arrancar(True)

#HERENCIA
class Vehiculos():

    def __init__(self,marca,modelo):
        self.__marca=marca
        self.__modelo=modelo
        self.__enmarcha=False
        self.__acelera=False
        self.__frena=False
    
    def arrancar(self):
        self.__enmarcha=True

    def acelerar(self):
        self.__acelera=True

    def frenar(self):
        self.__frena=True
    
    def estado(self):
        print("Marca: ",self.__marca,"\nModelo: ",self.__modelo)
        print("En Marcha:",self.__enmarcha,"\nAcelerando: ",self.__acelera,"\nFrenando: ",self.__frena)

print("\n------------------------Herencia------------------------")
class Moto(Vehiculos): #Entre parentesis le pasamos la clase padre
    pass

#Mi Programa
miMoto=Moto("Honda","FR125")
miMoto.estado()
print("\n")
miMoto.acelerar()
miMoto.estado()

#PYTHON ADMITE HERENCIA MULTIPLE
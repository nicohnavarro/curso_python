import pickle #->Importar para serializar
from modulos.modulo_vehiculos import Vehiculos #Necesitamos saber que tipo de archivo vamos a tener

coche1=Vehiculos("Chevrolet","Camaro")
coche2=Vehiculos("Renault","Sandero")
coche3=Vehiculos("Ford","Ranger")

coches=[coche1,coche2,coche3]

fichero1=open("lista_autos","wb") #Creamos el fichero
pickle.dump(coches,fichero1) #Volcamos esa informacion en el fichero
fichero1.close() #Cerramos el fichero
del(fichero1)#Borrar el fichero del disco duro

fichero2=open("lista_autos","rb")
mis_coches=pickle.load(fichero2)
fichero2.close()
#print(mis_coches)
for coche in mis_coches:
    coche.estado()
    print("")
#Biblioteca Pickle para Serializar Collecciones
import pickle
print("----------------Serializar Colecciones-----------------")
lista_nombres=["Pedro","Ana","Mirta","Omar"]
#Crear un fichero externo de escritura binaria
fichero_binario=open("lista_nombres","wb") #->wb=escritura binaria
#Volcar 
pickle.dump(lista_nombres,fichero_binario)
fichero_binario.close()#Siempre hay que cerrarlo

del(fichero_binario) #Borrarlo de la memoria

#Ahora lo vamos a leer
fichero_binario=open("lista_nombres","rb") #->rb=lectura binaria
lista_nombres=pickle.load(fichero_binario)
print(lista_nombres)
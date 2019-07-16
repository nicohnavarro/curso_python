#Importamos pickle
import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se creo una persona : ",self.nombre)
    
    def __str__(self): #Convertir en cadena de texto un objeto
        return "{}-{}-{}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    personas=[]
    
    def __init__(self):
        listaDePersonas=open("lista_personas","ab+") #Agregar informacion binaria
        listaDePersonas.seek(0) #Posicionamos el cursor al principio del archivo
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self,persona):
        self.personas.append(persona)
        self.guardarPersonasEnFichero(persona)
    
    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)

    def guardarPersonasEnFichero(self,persona):
        listaDePersonas=open("lista_personas","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFichero(self):
        print("La informacion del fichero externo es :")
        for person in self.personas:
            print(person)

print("------------Guardar Lista--------------")
miLista=ListaPersonas()
persona1=Persona("Nicolas","Masculino",25)
miLista.agregarPersonas(persona1)
persona2=Persona("Melissa","Femenino",24)
miLista.agregarPersonas(persona2)
print("------------Mi lista---------------")
miLista.mostrarPersonas()
miLista=ListaPersonas()
miLista.mostrarInfoFichero()
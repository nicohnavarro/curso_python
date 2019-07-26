#Funciones decoradores 
#Son tres funciones 
#Añaden funcionalidades a otras funciones
#def funcion_decorador(funcion):
#   def funcion_interna():
#       #codigo de la funcion interna
#       return funcion_interna

#Le queremos dar las mismas funcionalidades añadidas
#para no modificar a cada una de las funciones usamos el decorador

def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        #Accciones adicionales que decoran o agregan
        print("Vamos a Realizar un calculo: ")
        funcion_parametro()

        #Acciones adicionales que decoran
        print("Se ha terminado el calculo\n")

    return funcion_interior

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()
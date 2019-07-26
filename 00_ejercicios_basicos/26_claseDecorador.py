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
    def funcion_interior(*args,**kwargs): #*args un numero indeterminado de parametros!**kwargs-> por convencion keywords arguments
        #Accciones adicionales que decoran o agregan
        print("Vamos a Realizar un calculo: ")
        funcion_parametro(*args,**kwargs)

        #Acciones adicionales que decoran
        print("Se ha terminado el calculo\n")

    return funcion_interior

#@funcion_decoradora
def suma(num1,num2,num3):
    """
    Documentacion:
    Suma tres numeros 
    """
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))


suma(10,5,7)
resta(12,10)
potencia(base=2,exponente=5)
help(suma)

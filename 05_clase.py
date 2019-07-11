#EXCEPCIONES
#   Error en tiempo de ejecucion
print("\n------------------EXCEPTIONS------------------\n")
def dividir(num1,num2):
    try:
        num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "Operacion Erronea"
    except ValueError:
        print("No ingresaste un numero")

try:
    print(dividir(1,1))
    raise ZeroDivisionError("Lanzamos una exception") #Lanzamos la exception con un mensaje
except ZeroDivisionError as ErrorPropio: #La atrapamos
    print(ErrorPropio)
finally:
    print("Bloque finally") #Esto siempre se ejecuta
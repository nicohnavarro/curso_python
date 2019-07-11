#Control de Flujo
#Condicionales
#IF ELSE ELIF
def  evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Desaprobado"
    return valoracion

def evaluacionStr(notaStr):
    valoracion="Aprobado"
    if int(notaStr)<5:
        valoracion="Desaprobado"
    return valoracion

print("\n---------------------Parte I---------------------\n")
print(evaluacion(4))
print(evaluacion(9))

print("Programa de evaluacion de notas de alumnos")
nota_alumno=input("Nota: ")
#Se tiene que castear para  valor numero porque sino lo toma como string
print(evaluacion(int(nota_alumno)))

nota_alumno=input("Nota: ")
print(evaluacionStr(nota_alumno))

print("\n---------------------Parte II---------------------\n")
print("Verificacion de acceso")
edad_usuario=int(input("Introduce tu edad, por favor: "))
if edad_usuario<18:
    print("No puedes pasar")
elif edad_usuario>100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

if 7<edad_usuario<14:
    print("Sos adolescente")
if 20<edad_usuario<30:
    print("Estas un poco viejo")

print("Salarios")
salario_presidente=int(input("Introduce el salario presidente: "))
print("Tu salario es: $"+str(salario_presidente))
salario_diputado=int(input("Introduce el salario diputado: "))
print("Tu salario es: $%d"%(salario_diputado))

if salario_presidente>100 and salario_diputado>100:
    print("Economicamente y estamos bien")
if salario_presidente>100 or salario_diputado>100:
    print("Economicamente o estamos bien")

#Todos los condicionales con minuscula y pasar el parametro string con el metodo lower()
opcion=input("Ingrese materia: ")
asignatura=opcion.lower()
if asignatura in ("programacion","matematica","lengua","arte"):
    print("Esta dentro de las opciones...")
else:
    print("No estan entre las opciones")

#yield from
#bucles anidados adentro del generador
#nos devuelve un objeto generador donde se almacenan valores uno a uno
#puede ser listas, tuplas, diccionarios 
#si queremos ingresar en esos campos hay que usar el from
def devuelve_ciudadesI(*ciudades): # * Numero inderterminado de elementos en forma de tupla
    for elemento in ciudades: #Padre o Principal
        for subElemento in elemento: #Hijo
            yield subElemento
def devuelve_ciudadesII(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas=devuelve_ciudadesI("Madrid","Barcelona","Bilbao","Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
ciudades_devueltas=devuelve_ciudadesII("Argentina","Bolivia","Chile","Colombia")
print(next(ciudades_devueltas))
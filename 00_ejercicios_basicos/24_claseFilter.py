#Las funcion filter forma parte del grupo de Orden Superior
#Paradigma de Programacion funcional
#Comprobar los elementos de una secuencia cumplen con una condicion

"""def numero_par(num):
    if num%2==0:
        return True
"""

numeros=[17,24,7,32,39,51,2,10]
#Primer parametro la funcion que queremos comparar y el segundo la lista.
#print(list(filter(numero_par,numeros)))
print(list(filter(lambda numero_par: numero_par%2==0,numeros)))


class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "Nombre: {} - Cargo: {} - Salario: $ {}".format(self.nombre,self.cargo,self.salario)

listaEmpleado=[
    Empleado("Nicolas","Director",120000),
    Empleado("Ana","Supervisor",100000),
    Empleado("Mauro","Administrativo",17000),
    Empleado("Mario","Operario",10000),
    Empleado("Johanna","Supervisor",90000),
]

print("-----------------OTRO EJEMPLO--------------------\n")

salariosAltos=filter(lambda empleado:empleado.salario>50000,listaEmpleado)
for empleadosSalario in salariosAltos:
    print(empleadosSalario)
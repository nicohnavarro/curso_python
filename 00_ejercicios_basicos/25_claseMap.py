#La Funcion Map nos permite aplicar una funcion a cada elemento
#de una lista iterable (lista, tuplas, etc) devolviendo una lista con los resultados

class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "Nombre: {} - Cargo: {} - Salario: $ {}".format(self.nombre,self.cargo,self.salario)

listaEmpleados=[
    Empleado("Nicolas","Director",120000),
    Empleado("Ana","Supervisor",100000),
    Empleado("Mauro","Administrativo",90000),
]

def calculo_comision(empleado):
    if empleado.salario>=100000:
        empleado.salario=empleado.salario*1.03 #Un 3% incrementado
    return empleado

for empleado in listaEmpleados:
    print(empleado)

print("---------------------MAP---------------------------")

#La funcion map utiliza otra funcion como para parametro y se la aplica a cada elemento
listaEmpleadosComision=map(calculo_comision,listaEmpleados)
for empleado in listaEmpleadosComision:
    print(empleado)

class Persona():

    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    
    def descripcion(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Lugar de residencia: ",self.lugar_residencia)

class Empleado(Persona):

    def __init__(self,salario,antiguedad,nombre,edad,residencia):
        super().__init__(nombre,edad,residencia)
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario)
        print("Antiguedad: ",self.antiguedad)

#Principio de sustitucion "Es Siempre un/a" es decir un empleado es siempre una persona.
#Pero no siempre una persona no es un empleado.
#Funcion isinstance() ->True o False
persona1=Persona("Antonio",55,"España")
persona2=Empleado(15000,6,"Nicolas",26,"Argentina")
persona1.descripcion()
print("")
persona2.descripcion()

print(isinstance(persona2,Empleado))
print(isinstance(persona1,Empleado))
print(isinstance(persona2,Persona))
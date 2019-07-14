class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculo(vehiculo): #Magia del polimorfismo
    vehiculo.desplazamiento()

print("\n--------------------Polimorfismo----------------")
miVehiculo1=Moto()
miVehiculo1.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()

miVehiculo3=Camion()
desplazamientoVehiculo(miVehiculo3)
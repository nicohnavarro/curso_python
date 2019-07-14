class Vehiculos():

    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo)
        print("En Marcha:",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)

class Moto(Vehiculos): #Entre parentesis le pasamos la clase padre
    hacecaballito=" "
    def caballito(self):
        self.hacecaballito="Voy haciendo caballito!"
    
    def estado(self): #Siempre se sobreescribe el metodo de la clase padre nunca va a llamar al otro metodo
        print("Marca: ",self.marca,"\nModelo: ",self.modelo)
        print("En Marcha:",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)
        print(self.hacecaballito)
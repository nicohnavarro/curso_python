#Paquetes ->Directorios donde se almacenan modulos relacionados entre si
#Sirven para organizar y reutilizar modulos
#La carpeta donde creamos los modulos debe tener el archivo __init__.py
#Se pueden agregar los modulos que queramos
#Se pueden incluso agregar paquetes a tu paquete
#Utilizaremos el paquete calculos->calculos_generales

from paquete_calculos.calculos_generales import dividir,potenciar,redondear
dividir(4,6)
potenciar(2,8)
redondear(4.23)


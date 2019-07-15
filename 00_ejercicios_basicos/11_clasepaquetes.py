#Paquetes ->Directorios donde se almacenan modulos relacionados entre si
#Sirven para organizar y reutilizar modulos
#La carpeta donde creamos los modulos debe tener el archivo __init__.py
#Se pueden agregar los modulos que queramos
#Se pueden incluso agregar paquetes a tu paquete
#Utilizaremos el paquete calculos->calculos_generales

#Ahora funciona desde cualquier lugar porque el paquete 
#ya esta instalado en la version de python
from paquetes.paquete_calculos.calculos_generales import dividir
dividir(4,6)


#Paquetes Distribuibles 
#Crear paquetes -> Instalar Paquetes
#Este donde este lo puedo ejecutar 


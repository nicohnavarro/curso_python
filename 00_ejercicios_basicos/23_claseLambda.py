#LAMBDA Simplificar la funciones
"""def area_triangulo(base,altura):
    return (base*altura)/2

triangulo1=area_triangulo(5,7)
triangulo2=area_triangulo(9,6)
print(triangulo1)
print(triangulo2)"""

#Simplificar la sintaxis
area_triangulo=lambda base,altura:(base*altura)/2
print(area_triangulo(7,5))
print(area_triangulo(9,6))

#-----------------OTRO EJEMPLO--------------------
destacar_valor=lambda comision:"¡{}! $".format(comision)
comision_Nico=15230
print(destacar_valor(comision_Nico))

#Son para funciones simples que no ocuparian mas de un par de lineas de codigo!
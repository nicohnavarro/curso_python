#Bucles for (variable) in (elemento a recorrer)->Lista, Tupla, String, Array
#Ejemplo Simple
print("\n-------------------------FOR-------------------------\n")
for i in ["Enero","Febrero","Marzo","Abril"]:
    #print(i) Salto de linea
    print(i,end =" ")#Espacio sin salto de linea
print("\n")
for i in "nicolas":
    print(i)
    #print(i,end="")
print("")
contador=0
email=False
for i in "nicohnavarro@gmail.com":
    if i=="@" or i==".":
        contador=contador+1
        email=True

if email and contador==2:
    print("Mail Correcto")
else:
    print("Incorrecto")
print("")

#Range numerico
for i in range(contador):
    print(i)
#Range numerico entre valores
for i in range(contador,5):
    print(i)
#Range numerico entre valores con crecimiento
for i in range(contador,10,2):
    print(i)

#WHILE
print("\n-------------------While-------------------\n")
i=1
while i <=10:
    print("While "+str(i))
    i=i+1

#Generadores
print("\n-------------------Generadores-------------------\n")
#yield

def genera_pares_I(limite):
    num=1
    milista=[]
    while num<limite:
        milista.append(num*2)
        num+=1
    return milista

#Objeto Generador
def genera_pares_II(limite):
    num=1
    while num<limite:
        yield num*2 #yield imporante
        num+=1

print(genera_pares_I(10))

devuelve_pares=genera_pares_II(10)
#for i in devuelve_pares:
#    print(i) #Aqui los genera todos esta completo
#NO se genera el resto de los valores del objeto 
#NO reserva espacio en memoria
print(next(devuelve_pares))
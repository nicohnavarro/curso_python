#Bases de datos
#Archivos extrernos
    #Texto plano
        #Creaccion -> Apertura -> Manipulacion -> Cierre
        #Steam flujo de datos
from io import open
print("----------------Archivos-----------------")
archivo_texto=open("archivo.txt","w") #->Creamos el archivo de texto!
frase="Linea 1: Estamos escribiendo en un archivo\nLinea 2: Seguimos..."
archivo_texto.write(frase)
archivo_texto.close()


archivo_texto=open("archivo.txt","r")
#texto_leido=archivo_texto.read()
#print(texto_leido)

linea_texto=archivo_texto.readlines() #Se guarda en una lista []
archivo_texto.close()
print(linea_texto)
print(linea_texto[1])

archivo_texto=open("archivo.txt","a")
archivo_texto.write("\nLinea 3: Estamos agregando texto a nuestro archivo\nLinea 4.")
archivo_texto.close()
#Podemos modificar la posicion del puntero (cursor)
#por defecto se situa al final del archivo
#metodo seek()
#archivo_texto.seek(5)
#texto_leido=archivo_texto.read(11) se detiene en la posicion 11 
#readline() -> Lee linea por linea
#open("nombre_archivo","r+")->lectura y escritura

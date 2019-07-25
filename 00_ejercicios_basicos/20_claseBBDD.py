import sqlite3
miConexion=sqlite3.connect("PrimeraBase")#Creamos la base de datos
miCursor=miConexion.cursor()#Crear el cursor o puntero
#miCursor.execute("CREATE TABLE Productos (NOMBRE_ARTICULO VARCHAR(50)
#                           +", PRECIO INTEGER, SECCION VARCHAR(20))") Una Sola vez se Crea!
#miCursor.execute("INSERT INTO Productos VALUES('Pelota',750,'Deportes')")
#variosProductos=[
#    ("Camiseta",1599,"Deportes"),
#    ("Botines",2700,"Deportes"),
#    ("Campera",10000,"Ropa Moda"),
#    ("Buzo",1700,"Ropa Moda")
#]
#miCursor.executemany("INSERT INTO Productos VALUES (?,?,?)",variosProductos)
miCursor.execute("SELECT * FROM Productos")
variosProductos=miCursor.fetchall()
#print(variosProductos)
for producto in variosProductos:
    #print(producto)
    print("Nombre Articulo: ",producto[0])
miConexion.commit() #Confirmamos los cambios que queremos en la base de datos
miConexion.close()#Cerramos la conexion
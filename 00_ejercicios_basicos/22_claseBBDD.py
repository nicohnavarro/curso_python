import sqlite3
#Operaciones CRUD 
#Create Read Update Delete
miConexion=sqlite3.connect("GestionProductosII")
miCursor=miConexion.cursor()

#miCursor.execute('''
#    CREATE TABLE PRODUCTOS_II (
#        ID INTEGER PRIMARY KEY AUTOINCREMENT,
#        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#        PRECIO INTEGER,
#        SECCION VARCHAR(20)
#    )
#''')

#productos=[
#    ("Leche",55,"Lacteos"),
#    ("Pan",35,"Almacen"),
#    ("Mermelada",75,"Almacen"),
#    ("Coca-Cola",45,"Bebidas")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS_II VALUES (NULL,?,?,?)",productos)

#Read
miCursor.execute("SELECT * FROM PRODUCTOS_II WHERE SECCION='Almacen'")
productos=miCursor.fetchall()
for articulo in productos:
    print(articulo)

#Update
miCursor.execute("UPDATE PRODUCTOS_II SET PRECIO=99 WHERE ID=1")

#Delete
miCursor.execute("DELETE FROM PRODUCTOS_II WHERE ID=2")

miConexion.commit()
miConexion.close()
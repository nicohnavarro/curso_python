import sqlite3
miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

miCursor.execute(''' 
    CREATE TABLE PRODUCTOS (
        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY, 
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))
''')
#ID INTEGER PRIMARY KEY AUTOINCREMENT,
productos=[
    ("AR01","Leche",55,"Lacteos"),
    ("AR02","Pan",35,"Almacen"),
    ("AR03","Mermelada",75,"Almacen"),
    ("AR04","Coca-Cola",45,"Bebidas")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)",productos)
#? = NULL
miConexion.commit()
miConexion.close()
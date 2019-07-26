from tkinter import *
from tkinter import messagebox
import sqlite3
#------------------------Funciones-------------------------------
def conexionBBDD():
    miconexion=sqlite3.connect("Usuarios")
    micursor=miconexion.cursor()
    micursor.execute('''
        CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(20),
            APELLIDO VARCHAR(20),
            USUARIO VARCHAR(20),
            PASSWORD VARCHAR(20),
            DIRECCION VARCHAR(40),
            COMENTARIOS VARCHAR(100)
        )
    ''')



root=Tk()
#------------------------MENU-------------------------------
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos")

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Create")
crudMenu.add_command(label="Read")
crudMenu.add_command(label="Update")
crudMenu.add_command(label="Delete")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)

#--------------------FRAME---------------------------------
miFrame=Frame(root)
miFrame.pack()
#--------------------ENTRYS---------------------------------
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="left")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=10,pady=10)
cuadroApellido.config(fg="blue",justify="left")

cuadroUsuario=Entry(miFrame)
cuadroUsuario.grid(row=2,column=1,padx=10,pady=10)
cuadroUsuario.config(fg="yellow",justify="center",background="black")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1,padx=10,pady=10)
cuadroPass.config(show="%",background="black",fg="green")

cuadroAddress=Entry(miFrame)
cuadroAddress.grid(row=4,column=1,padx=10,pady=10)
cuadroAddress.config(background="blue",fg="white",justify="left")

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#--------------------LABELS---------------------------------
labelNombre=Label(miFrame,text="Nombre: ")
labelNombre.grid(row=0,column=0,sticky="e",padx=10,pady=10)

labelApellido=Label(miFrame,text="Apellido: ")
labelApellido.grid(row=1,column=0,sticky="e",padx=10,pady=10)

labelUsuario=Label(miFrame,text="Usuario: ")
labelUsuario.grid(row=2,column=0,sticky="e",padx=10,pady=10)

labelPass=Label(miFrame,text="Password: ")
labelPass.grid(row=3,column=0,sticky="e",padx=10,pady=10)

labelAddress=Label(miFrame,text="Direccion: ")
labelAddress.grid(row=4,column=0,sticky="e",padx=10,pady=10)

labelComentario=Label(miFrame,text="Comentarios: ")
labelComentario.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#--------------------BUTTONS---------------------------------
miFrameInferior=Frame(root)
miFrameInferior.pack()

btnCrear=Button(miFrameInferior,text="Create")
btnCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

btnLeer=Button(miFrameInferior,text="Read")
btnLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

btnActualizar=Button(miFrameInferior,text="Update")
btnActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

btnBorrar=Button(miFrameInferior,text="Delete")
btnBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)


root.mainloop()
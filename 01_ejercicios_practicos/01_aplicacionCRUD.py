from tkinter import *
from tkinter import messagebox
import sqlite3
#------------------------Funciones-------------------------------
def conexionBBDD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
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
        messagebox.showinfo("BBDD","Base de Datos Creada con exito!")
    except:
        messagebox.showwarning("Atencion!","La Base de Datos ya existe!")
    miConexion.close()

def salirAplicacion():
    valor=messagebox.askquestion("Salir","Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()

def limpiarCampos():
    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miUsuario.set("")
    miPassword.set("")
    miAddress.set("")
    textoComentario.delete(1.0, END)

def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '"+miNombre.get()+
        "','"+miApellido.get()+
        "','"+miUsuario.get()+
        "','"+miPassword.get()+
        "','"+miAddress.get()+
        "','"+textoComentario.get("1.0",END)+ "')")"""
    datos=miNombre.get(),miApellido.get(),miUsuario.get(),miPassword.get(),miAddress.get(),textoComentario.get("1.0",END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?,?)",(datos))
    miConexion.commit()
    miConexion.close()
    messagebox.showinfo("BBDD","Registro Insertado con exito!")

def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+miID.get())
        elUsuario=miCursor.fetchall()
        limpiarCampos()
        for usuario in elUsuario:
            miID.set(usuario[0])
            miNombre.set(usuario[1])
            miApellido.set(usuario[2])
            miUsuario.set(usuario[3])
            miPassword.set(usuario[4])
            miAddress.set(usuario[5])
            textoComentario.insert(1.0,usuario[6])
        miConexion.commit()
    except:
        messagebox.showerror("ID Error","El ID no ha sido encontrado en la Base de Datos...")
    miConexion.close()

def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    """miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE='"+miNombre.get()+
        "', APELLIDO='"+ miApellido.get()+
        "', USUARIO='"+ miUsuario.get()+
        "', PASSWORD='"+ miPassword.get()+
        "', DIRECCION='"+ miAddress.get()+
        "', COMENTARIOS='"+ textoComentario.get("1.0",END)+
        "' WHERE ID=" + miID.get())"""
    datos=miNombre.get(),miApellido.get(),miUsuario.get(),miPassword.get(),miAddress.get(),textoComentario.get("1.0",END)
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE=?, APELLIDO=?, USUARIO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=?"+
        "WHERE ID="+miID.get(),(datos))

    miConexion.commit()
    miConexion.close()
    messagebox.showinfo("BBDD","Registro Actualizado con exito!")

def eliminar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+miID.get())
    miConexion.commit()
    miConexion.close()
    messagebox.showinfo("BBDD","Registro Eliminado con exito!")

root=Tk()
#------------------------MENU-------------------------------
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos",command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Create",command=crear)
crudMenu.add_command(label="Read",command=leer)
crudMenu.add_command(label="Update",command=actualizar)
crudMenu.add_command(label="Delete",command=eliminar)

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)

#--------------------FRAME---------------------------------
miFrame=Frame(root)
miFrame.pack()
#--------------------ENTRYS---------------------------------
miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miUsuario=StringVar()
miPassword=StringVar()
miAddress=StringVar()


cuadroID=Entry(miFrame,textvariable=miID)
cuadroID.grid(row=0,column=1,padx=10,pady=10)
cuadroID.config(background="black",fg="white",justify="center")

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="left")

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)
cuadroApellido.config(fg="blue",justify="left")

cuadroUsuario=Entry(miFrame,textvariable=miUsuario)
cuadroUsuario.grid(row=3,column=1,padx=10,pady=10)
cuadroUsuario.config(fg="yellow",justify="center",background="black")

cuadroPass=Entry(miFrame,textvariable=miPassword)
cuadroPass.grid(row=4,column=1,padx=10,pady=10)
cuadroPass.config(show="%",background="black",fg="green")

cuadroAddress=Entry(miFrame,textvariable=miAddress)
cuadroAddress.grid(row=5,column=1,padx=10,pady=10)
cuadroAddress.config(background="blue",fg="white",justify="left")

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=6,column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=6,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#--------------------LABELS---------------------------------
labelID=Label(miFrame,text="ID: ")
labelID.grid(row=0,column=0,sticky="e",padx=10,pady=10)

labelNombre=Label(miFrame,text="Nombre: ")
labelNombre.grid(row=1,column=0,sticky="e",padx=10,pady=10)

labelApellido=Label(miFrame,text="Apellido: ")
labelApellido.grid(row=2,column=0,sticky="e",padx=10,pady=10)

labelUsuario=Label(miFrame,text="Usuario: ")
labelUsuario.grid(row=3,column=0,sticky="e",padx=10,pady=10)

labelPass=Label(miFrame,text="Password: ")
labelPass.grid(row=4,column=0,sticky="e",padx=10,pady=10)

labelAddress=Label(miFrame,text="Direccion: ")
labelAddress.grid(row=5,column=0,sticky="e",padx=10,pady=10)

labelComentario=Label(miFrame,text="Comentarios: ")
labelComentario.grid(row=6,column=0,sticky="e",padx=10,pady=10)

#--------------------BUTTONS---------------------------------
miFrameInferior=Frame(root)
miFrameInferior.pack()

btnCrear=Button(miFrameInferior,text="Create",command=crear)
btnCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

btnLeer=Button(miFrameInferior,text="Read",command=leer)
btnLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

btnActualizar=Button(miFrameInferior,text="Update",command=actualizar)
btnActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

btnBorrar=Button(miFrameInferior,text="Delete",command=eliminar)
btnBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)


root.mainloop()
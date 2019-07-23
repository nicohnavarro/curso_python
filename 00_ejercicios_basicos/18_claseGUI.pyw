from tkinter import *

root=Tk()
miFrame=Frame(root, width=1200,height=600)
miFrame.pack()

minombre=StringVar() #Se trata de una cadena de caracteres

labelNombre=Label(miFrame,text="Nombre:")
labelNombre.grid(row=0, column=0,sticky="w",pady=4,padx=4)
cuadroNombre=Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row=0, column=1,pady=4,padx=4)
cuadroNombre.config(fg="green",justify="center")

labelApellido=Label(miFrame,text="Apellido:")
labelApellido.grid(row=1,column=0,sticky="w",pady=4,padx=4)
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1,pady=4,padx=4)

labelEmail=Label(miFrame,text="Correo:")
labelEmail.grid(row=2,column=0,sticky="w",pady=4,padx=4)
cuadroEmail=Entry(miFrame)
cuadroEmail.grid(row=2,column=1,pady=4,padx=4)

labelPassword=Label(miFrame,text="Contraseña:")
labelPassword.grid(row=3,column=0,sticky="w",pady=4,padx=4)
cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3,column=1,pady=4,padx=4)
cuadroPassword.config(show="*")

labelComentario=Label(miFrame,text="Comentarios:")
labelComentario.grid(row=4,column=0,sticky="w",pady=4,padx=4)
textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4,column=1,pady=4,padx=4)
scroll=Scrollbar(miFrame, command=textoComentario.yview)
#Agregar de forma manual el scrolling
scroll.grid(row=4,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scroll.set)

def codigoBoton():
    minombre.set("Juan")


btnEnvio=Button(root, text="Enviar",command=codigoBoton)
btnEnvio.pack()

root.mainloop()
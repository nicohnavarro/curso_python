from tkinter import *
root=Tk()
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
#archivoMenu.add_command(Label="Nuevo")
#archivoMenu.add_command(Label="Guardar")
archivoEdicion=Menu(barraMenu)
archivoHerramientas=Menu(barraMenu)
archivoAyuda=Menu(barraMenu)

#barraMenu.add_cascade(Label="Archivo", menu=archivoMenu)
#barraMenu.add_cascade(Label="Edicion",menu=archivoEdicion)
#barraMenu.add_cascade(Label="Herramientas",menu=archivoHerramientas)
#barraMenu.add_cascade(Label="Ayuda",menu=archivoAyuda)

root.mainloop()

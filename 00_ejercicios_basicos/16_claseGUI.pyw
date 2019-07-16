#Paquete tkinter para interfaces graficas de usuario (GUI)
from tkinter import *
#Esta basado en principalmente de una Raiz...
raiz = Tk()
raiz.title("Ventana de Pruebas")
#raiz.resizable(False,True) #No se puede redimensionar ->Depende de que eje X o Y
raiz.iconbitmap("burn_folder.ico")
#raiz.geometry("650x350") ->La raiz se adapta de su contenedor interno!(Frame)
raiz.config(bg="black")
raiz.config(bd=30)
raiz.config(relief="groove")
raiz.config(cursor="hand2")
#El Frame...que contiene los widgets
miFrame=Frame()
miFrame.pack()
#miFrame.pack(side="right")
#miFrame.pack(fill="both",expand=True)
miFrame.config(bd=30)
miFrame.config(relief="sunken")
miFrame.config(bg="green")
miFrame.config(width="650",height="350")
#miFrame.config(cursor="hand2")
miFrame.config(cursor="pirate")
raiz.mainloop() #->Bucle infinito Siempre al final!!
from tkinter import * #Importamos la biblioteca necesaria para crear GUI
root=Tk()
miFrame=Frame(root)
miFrame.pack()
operador=""
resultado=0
#-----------------Pantalla---------------------------
numeroPantalla=StringVar()
pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=4,pady=4,columnspan=4)
pantalla.config(background="black",fg="white",justify="right")
#Colspan funcion web

#-----------------Pulsaciones Teclado----------------
def numeroPulsado(num):
    global operador
    if operador!= "":
        numeroPantalla.set(num)
        operador=""
    else:
        numeroPantalla.set(numeroPantalla.get()+ num)

#-----------------Operaciones---------------------------
def suma(num):
    global operador
    global resultado
    resultado+=int(num)
    operador="suma"
    numeroPantalla.set(resultado)

#-----------------Fila 1---------------------------
btnSiete=Button(miFrame,text="7",width=3,background="grey",command=lambda:numeroPulsado("7"))
btnSiete.grid(row=2,column=1)
btnOcho=Button(miFrame,text="8",width=3,background="grey",command=lambda:numeroPulsado("8"))
btnOcho.grid(row=2,column=2)
btnNueve=Button(miFrame,text="9",width=3,background="grey",command=lambda:numeroPulsado("9"))
btnNueve.grid(row=2,column=3)
btnDiv=Button(miFrame,text="/",width=3,background="black",fg="green")
btnDiv.grid(row=2,column=4)

#-----------------Fila 2---------------------------
btnCuatro=Button(miFrame,text="4",width=3,background="grey",command=lambda:numeroPulsado("4")) #Funciones lambda -> Simplificar funciones
btnCuatro.grid(row=3,column=1)
btnCinco=Button(miFrame,text="5",width=3,background="grey",command=lambda:numeroPulsado("5"))
btnCinco.grid(row=3,column=2)
btnSeis=Button(miFrame,text="6",width=3,background="grey",command=lambda:numeroPulsado("6"))
btnSeis.grid(row=3,column=3)
btnMulti=Button(miFrame,text="*",width=3,background="black",fg="green")
btnMulti.grid(row=3,column=4)

#-----------------Fila 3---------------------------
btnUno=Button(miFrame,text="1",width=3,background="grey",command=lambda:numeroPulsado("1"))
btnUno.grid(row=4,column=1)
btnDos=Button(miFrame,text="2",width=3,background="grey",command=lambda:numeroPulsado("2"))
btnDos.grid(row=4,column=2)
btnTres=Button(miFrame,text="3",width=3,background="grey",command=lambda:numeroPulsado("3"))
btnTres.grid(row=4,column=3)
btnRest=Button(miFrame,text="-",width=3,background="black",fg="green")
btnRest.grid(row=4,column=4)

#-----------------Fila 4---------------------------
btnComa=Button(miFrame,text=",",width=3,background="black",fg="white",command=lambda:numeroPulsado(","))
btnComa.grid(row=5,column=1)
btnCero=Button(miFrame,text="0",width=3,background="white",command=lambda:numeroPulsado("0"))
btnCero.grid(row=5,column=2)
btnIgual=Button(miFrame,text="=",width=3,background="black",fg="yellow")
btnIgual.grid(row=5,column=3)
btnSuma=Button(miFrame,text="+",width=3,background="black",fg="green",command=lambda:suma(numeroPantalla.get()))
btnSuma.grid(row=5,column=4)

root.mainloop()

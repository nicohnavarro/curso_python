from tkinter import *
root =Tk()
miFrame=Frame(root, width=500,height=400)
miFrame.pack()

#miLabel=Label(miFrame, text="Hola mundo!")
#miLabel.pack()#Se adapta el contenedor al label
#miLabel.place(x=100,y=200)
#tkinter imagenes solo formato png y gif
Label(miFrame, text="Hola mundo 1!", fg="red",font=("Comic Sans MS",10)).place(x=20,y=30)
Label(miFrame, text="Hola mundo 2!", fg="black",font=(12)).place(x=20,y=50)
Label(miFrame, text="Hola mundo 3!", fg="blue",font=("Comic Sans MS",10)).place(x=20,y=70)
Label(miFrame, text="Hola mundo 4!", fg="grey",font=(12)).place(x=20,y=90)
Label(miFrame, text="Hola mundo 5!", fg="green",font=("Comic Sans MS",10)).place(x=20,y=110)
Label(miFrame, text="Hola mundo 6!", fg="white",font=(12)).place(x=20,y=130)
root.mainloop()
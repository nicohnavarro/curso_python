#Necesitamos frameworks o bibliotecas
#Flask es mas facil
#Django mas preparado

from flask import Flask, render_template
#Flask 
#render_template para los archivos html
app=Flask(__name__)

@app.route('/') #Una ruta para mi pagina principal
def home():
    #return 'Home Page'
    #siempre tiene que estar escuchando peticiones
    #Se mantenga escuchando constatemente
    return render_template('home.html')

@app.route('/about')
def about():
    #return 'About Page'
    return render_template('about.html')
#Tenemos que ir actualizando el servidor 

if __name__=='__main__':
    app.run(debug=True)
    #Entra en estado debug para no tenes que cerrar el servidor

#Crear una carpeta
#que contenga las vistas los archivos Html (Templates)

#Heroku
#Servidor real compartirlo
#servicio que permite desplagar aplicaciones sin la necesidad de
#o de instalar tu programa 
#Version gratuita

#python virtualenv
#python -m venv vend
#Ejecutar el index.py desde el entorno virtual creado
#heroku cli

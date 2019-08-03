from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
#Usamos Xampp paquete
app = Flask(__name__)

#MySql Connection
#Coneccion a mi localhost
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
#app.config['MYSQL_PASSWORD']='password'
app.config['MYSQL_DB']='pythoncontacts'
mysql=MySQL(app)

#Settings
app.secret_key='mysecretkey'

@app.route('/') #Lo que hacemos es que cada vez que el usuario entre a la ruta vamos a responderle algo
def Index():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacts')
    data= cursor.fetchall()
    return render_template('index.html', contacts=data)

@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method =='POST':
        fullname=request.form['fullname']
        phone=request.form['phone']
        email=request.form['email']
        
        #Aqui usamos el cursor de mysql
        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname,phone,email))
        mysql.connection.commit() #Ejecutamos la consulta
        flash('Contact Added Successfully')
        return redirect(url_for('Index')) #nombre de la funcion principal

@app.route('/edit/<id>')
def get_contact(id):
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacts WHERE id=%s',(id))
    data=cursor.fetchall()

    return render_template('edit-contact.html',contact= data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname=request.form['fullname']
        phone=request.form['phone']
        email=request.form['email']
        cursor=mysql.connection.cursor()
        cursor.execute(""" 
            UPDATE contacts
            SET fullname=%s,
                phone=%s,
                email=%s
            WHERE id = %s
        """,(fullname, phone, email, id))
        mysql.connection.commit()
        flash('Contact Updated Successfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cursor=mysql.connection.cursor()
    cursor.execute('DELETE FROM contacts WHERE id= {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)

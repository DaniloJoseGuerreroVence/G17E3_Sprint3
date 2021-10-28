
from flask import Flask, render_template, request
from wtforms.validators import Email

import forms, os, DB, werkzeug.security as ws

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    formsearch = forms.FormSearch()
    return render_template('Home.html', formsearch = formsearch)

@app.route('/Loging')
def Login():
    form = forms.Formlogin()
    return render_template('Login.html', formlogin = form)

@app.route('/Signing', methods=['GET','POST'])
def Signin():
    formsignin = forms.FormSignin()
    return render_template('Signin.html', formsignin = formsignin)

@app.route('/tech')
def tech():
    return render_template('tech.html')
    
@app.route('/AddProduct')
def AddProduct():
    return render_template('add_product.html')

@app.route('/buscar')
def buscar():
    return "<H1>BUSCANDO...</H1>"

@app.route('/Buying')
def Buying():
    formbuying = forms.FormBuy()
    return render_template('Buy.html', formbuying = formbuying)

@app.route('/newuser', methods=['GET','POST'])
def CreateUser():
    form = forms.FormSignin()
    if request.method == 'GET':
        return render_template('Signin.html', formsignin = form)
    else:
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        DB.createUser(name, lastname, email, ws.generate_password_hash(password))
        return 'User created'

@app.route('/Loging', methods=['GET', 'POST'])
def Loging():
    form = forms.Formlogin()
    if request.method == 'GET':
        return render_template('Login.html', formlogin = form)
    else:
        user = request.form['username']
        existing_user = DB.getLogs('Users', "Email='{}'".format(user))
        bd_password = existing_user[0][4]
        if existing_user is not None:
            password = request.form['password']
            check_password = ws.check_password_hash(bd_password, password)
            if check_password:
                return 'Logged User'
        return render_template('Login.html', formlogin = form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 

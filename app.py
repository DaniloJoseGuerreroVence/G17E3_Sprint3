
import re
from flask import Flask, render_template, request, session
from werkzeug.utils import redirect 
from wtforms.validators import Email

import forms, os, DB, werkzeug.security as ws

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.before_request
def BeforeRequest():
    if 'user' not in session and request.endpoint in ['Profile']:
        return redirect('/')
    elif 'user' in session and request.endpoint in ['Login', 'Singin']:
        return redirect('/addproduct/{}'.format(session['user']))

@app.route('/')
def index():
    formsearch = forms.FormSearch()
    return render_template('Home.html', formsearch = formsearch)

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/buscar')
def buscar():
    return "<H1>BUSCANDO...</H1>"

@app.route('/Buying')
def Buying():
    formbuying = forms.FormBuy()
    return render_template('Buy.html', formbuying = formbuying)

@app.route('/Signing', methods=['GET','POST'])
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
        session['user'] = email
        return redirect('/addproduct/{}'.format(email))

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
                session['user'] = user
                return redirect('/addproduct/{}'.format(user))
        return render_template('Login.html', formlogin = form)

@app.route('/Logout')
def Logout():
    if 'user' in session:
        session.pop('user')
        return redirect('/')

@app.route('/addproduct')
@app.route('/addproduct/<user>')
def Profile(user=None):
    if user:
        user_data = DB.getLogs('Users', "Email='{}'".format(user))
        if user_data:
            name = user_data[0][0]
            add = False
            if user == session['user']:
                add = True
            return render_template('add_product.html', user=user_data, add=add)
        else:
            user = session['user']
            return redirect('/addproduct/{}'.format(user))
    else:
        return render_template('add_product.html')        
        

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 

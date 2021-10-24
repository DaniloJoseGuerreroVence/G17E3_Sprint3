
from flask import Flask, render_template
app = Flask(__name__)

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
@app.route('/Login')
def index():
    formsearch = forms.FormSearch()
    return render_template('Home.html', formsearch = formsearch)

@app.route('/Loging')
def Login():
    formlogin = forms.Formlogin()
    return render_template('Login.html', formlogin = formlogin)

@app.route('/Signing')
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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 

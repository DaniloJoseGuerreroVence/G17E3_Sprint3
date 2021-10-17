from flask import Flask, render_template
import forms, os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/Loging')
def Login():
    formlogin = forms.Formlogin()
    return render_template('Login.html', formlogin = formlogin)

@app.route('/Signing')
def Signin():
    formsignin = forms.FormSignin()
    return render_template('Signin.html', formsignin = formsignin)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
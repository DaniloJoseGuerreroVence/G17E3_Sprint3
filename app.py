from flask import Flask, render_template,url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Login.html')


@app.route('/buscar')
def buscar():
    return "<H1>BUSCANDO...</H1>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
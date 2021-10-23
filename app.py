
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Login.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
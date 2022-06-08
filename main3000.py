from flask import Flask,render_template
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def initServer(): 
    return {
        'response':'Servidor corriendo'
    }

@app.route('/resta', methods = ['POST'])
def resta():
    numero1 = int(request.json['numero1'])
    numero2 = int(request.json['numero2'])

    result = numero1-numero2

    return str(result)

@app.route('/alreves/palabra:<string:word>', methods=["GET"])
def multiplicacion(word):

    return str(word[::-1])

if (__name__ == '__main__'):
    app.run(port = 3000, debug = True)
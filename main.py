from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def initServer(): 
    return {
        'response':'Servidor corriendo'
    }

@app.route('/suma', methods = ['POST'])
def suma():
    numero1 = int(request.json['numero1'])
    numero2 = int(request.json['numero2'])

    result = numero1+numero2

    return str(result)

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port = 3000, debug = True)
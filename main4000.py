from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def initServer(): 
    return {
        'response':'Servidor corriendo'
    }

@app.route('/info', methods=["GET"])
def info():
    return "Nombre: Luis Felipe Delgado Benitez \n Carnet: 201900051"

if (__name__ == '__main__'):
    app.run(port = 4000, debug = True)
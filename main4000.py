from flask import Flask, send_from_directory
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def initServer(): 
    return {
        'message':"Servidor corriendo"
    }

@app.route('/alreves/palabra:<string:word>', methods=["GET"])
def alreves(word):

    return {'message' :word[::-1]}
    
if (__name__ == '__main__'):
    app.run(port = 4000, debug = True)
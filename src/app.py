import os

from flask import Flask, request

app = Flask(__name__)

nome = 'nada'

@app.route('/', methods=['GET'])
def getinfo():
    global nome
    return 'Hello '+ nome

@app.route('/', methods=['POST'])
def postinfo():
    global nome
    nome = request.form['nome']
    return 'hello' + nome

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
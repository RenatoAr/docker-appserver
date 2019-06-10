import os
import json
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

dados = 'Hello World\n'

@app.route('/GET_INFO', methods=['GET'])
def getinfo():
    global dados
    return dados

@app.route('/POST_INFO', methods=['POST'])
def postinfo():
    global dados
    dados = request.get_json(force=True)
    return jsonify(dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

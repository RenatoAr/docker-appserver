import os
import json
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

dados = 'vazio'
nomecontainer = 'vazio'
idcontainer = 'vazio'
idimage = 'vazio'
usocpu = 'vazio'
usomem = 'vazio'

@app.route('/GET_INFO', methods=['GET'])
def getinfo():
    global dados
    global nomecontainer
    global idcontainer
    global idimage
    global usocpu
    global usomem
    return jsonify({'timestamp':dados, 'nomecontainer':nomecontainer, 'idcontainer':idcontainer, 'idimage':idimage, 'usocpu':usocpu, 'usomem':usomem})

@app.route('/POST_INFO', methods=['POST'])
def postinfo():
    global dados
    global nomecontainer
    global idcontainer
    global idimage
    global usocpu
    global usomem
    dados = request.form['timestamp']
    nomecontainer = request.form['nomecontainer']
    idcontainer = request.form['idcontainer']
    idimage = request.form['idimage']
    usocpu = request.form['usocpu']
    usomem = request.form['usomem']
    return jsonify({'timestamp':dados, 'nomecontainer':nomecontainer, 'idcontainer':idcontainer, 'idimage':idimage, 'usocpu':usocpu, 'usomem':usomem})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

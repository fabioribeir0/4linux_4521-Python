#!/usr/bin/python
from flask import Flask, render_template, jsonify
from Modulos.Docker import Docker
import logging as log


log.basicConfig(filename = 'Flaskapp.log', level = log.INFO, format = '%(asctime)s %(levelname)s %(message)s',
                                                                        datefmt = '[%d/%m/%Y - %H:%M:%S]')

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Este e o metodo que renderiza a pagina index da nossa aplicacao.
    '''
    log.info('Pagina index acessada.')
    d = Docker()
    containers = d.listar_containers()
    return render_template('index.html', containers = containers)
                                            # DICIONARIOS. INDEX containers = LISTA DE CONTAINERS

@app.route('/start/<id>')
def start(id):
    '''
    Este e o metodo que inicializa os containers no Docker.
    Recebe um parametro obrigatorio com o ID do container.

    ====== ======
    Params Values
    ====== ======
      ID    123
    ====== ======

    * 1
    * 2
    * 3

    :Param: id
    :Returns: Json message
    '''
    d = Docker()
    d.iniciar_container(id)
    log.info('Container iniciado. ID: %s.' % id)
    return jsonify({'message':'Container ligado.'})


@app.route('/stop/<id>')
def stop(id):
    '''
    Este e o metodo que para os containers no Docker.
    Recebe um parametro obrigatorio com o ID do container.
    '''
    d = Docker()
    d.parar_container(id)
    log.warning('Container desligado. ID: %s.' % id)
    return jsonify({'message':'Container desligado.'})


if __name__ == '__main__':
    log.info('Aplicacao iniciada.')
    app.run(host='0.0.0.0', debug = True)

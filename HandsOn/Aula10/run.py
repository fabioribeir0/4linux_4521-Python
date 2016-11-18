#!/usr/bin/python
from flask import Flask, render_template
from Modulos.Docker import Docker


app = Flask(__name__)

@app.route('/')
def index():
    d = Docker()
    containers = d.listar_containers()
    return render_template('index.html', containers = containers)
                                            # DICIONARIOS. INDEX containers = LISTA DE CONTAINERS


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

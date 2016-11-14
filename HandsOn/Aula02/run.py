#!/usr/bin/python
from flask import Flask, jsonify
from Blueprints.usuarios import usuario_bp
from Blueprints.grupos import grupo_bp


app = Flask(__name__)
app.register_blueprint(usuario_bp)
app.register_blueprint(grupo_bp)


@app.route('/')
def index():
    retorno = {'message': 'Aplicacao em Flask.'}
    return jsonify(retorno)


if __name__ == '__main__':
    app.run(port=8000, debug=True)

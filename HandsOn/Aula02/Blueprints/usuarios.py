#!/usr/bin/python
from flask import Blueprint, jsonify, request
from flask_mongoengine import MongoEngine
from datetime import datetime
from Models.APIModel import Usuarios as UsuariosModel
import json


usuario_bp = Blueprint('usuarios', __name__)


@usuario_bp.route('/usuarios/', methods=['GET'])
# GET E DEFAULT, NAO PRECISA ESPECIFICAR
def listar_usuarios():
    todos = UsuariosModel.objects().to_json()
    retorno = {'usuarios': json.loads(todos)}
    return jsonify(retorno)



@usuario_bp.route('/usuarios/', methods=['POST'])
def cadastrar_usuario():
    novo = request.get_json()
    u = UsuariosModel()
    u.nome = novo.get('nome')
    u.email = novo.get('email')
    u.save()
    retorno = {'message': 'Usuario cadastrado com sucesso'}
    return jsonify(retorno)
    


@usuario_bp.route('/usuarios/<id>/', methods=['PUT'])
def atualizar_usuario(id):
    # O MESMO QUE {'id': 1} ==== {chave do dict : id passado como parametro}
    u = UsuariosModel.objects(id=id).first()
    dados = request.get_json()
    u.nome = dados.get('nome')
    u.email = dados.get('email')
    u.save()
    retorno = {'message': 'Usuario atualizado com sucesso.'}
    return jsonify(retorno)


@usuario_bp.route('/usuarios/<id>/', methods=['DELETE'])
def remover_usuario(id):
    u = UsuariosModel.objects(id=id).first()
    # O MESMO QUE {'id': 1} ==== {chave do dict : id passado como parametro}      
    u.delete()
    retorno = {'message': 'Usuario removido com sucesso.'}
    return jsonify(retorno)

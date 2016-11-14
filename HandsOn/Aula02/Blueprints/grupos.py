#!/usr/bin/python
from flask import Blueprint, jsonify, request
from flask_mongoengine import MongoEngine
from datetime import datetime
from Models.APIModel import Grupos as GruposModel
import json


grupo_bp = Blueprint('grupos', __name__)


@grupo_bp.route('/grupos/', methods=['GET'])
# GET E DEFAULT, NAO PRECISA ESPECIFICAR
def listar_grupos():
    g = GruposModel.objects().to_json()
    retorno = {'grupos': json.loads(g)}
    return jsonify(retorno)


@grupo_bp.route('/grupos/', methods=['POST'])
def cadastrar_grupo():
    dados = request.get_json()
    g = GruposModel()
    g.nome = dados.get('nome')
    g.save()
    retorno = {'message': 'Grupo cadastrado com sucesso'}
    return jsonify(retorno)


@grupo_bp.route('/grupos/<id>/', methods=['PUT'])
def atualizar_grupo(id):
    # O MESMO QUE {'id': 1} ==== {chave do dict : id passado como parametro}
    g = GruposModel.objects(id=id).first()
    dados = request.get_json()
    g.nome = dados.get('nome')
    g.save()
    retorno = {'message': 'Grupo atualizado com sucesso.'}
    return jsonify(retorno)


@grupo_bp.route('/grupos/<id>/', methods=['POST'])
def add_integrante_grupo(id):
    # O MESMO QUE {'id': 1} ==== {chave do dict : id passado como parametro}
    g = GruposModel.objects(id=id).first()
    novo = request.get_json()
    g.integrantes.append(novo.get('nome'))
    g.save()
    retorno = {'message': 'Usuario adicionado ao grupo.'}
    return jsonify(retorno)


@grupo_bp.route('/grupos/<id>/', methods=['DELETE'])
def remover_grupo(id):
    g = GruposModel.objects(id=id).first()
    # O MESMO QUE {'id': 1} ==== {chave do dict : id passado como parametro}      
    g.delete()
    retorno = {'message': 'Grupo removido com sucesso.'}
    return jsonify(retorno)

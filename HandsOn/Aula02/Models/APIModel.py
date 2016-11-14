#!/usr/bin/python
from flask_mongoengine import MongoEngine
from flask import Flask
from datetime import datetime


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'dexter_api'}   #{'db': 'dexter-api', 'host': '127.0.0.1'}

db = MongoEngine(app)


class Usuarios(db.Document):
    nome = db.StringField()
    email = db.StringField(unique=True)
    data_cadastro = db.DateTimeField(default = datetime.now())


class Grupos(db.Document):
    nome = db.StringField(unique = True)
    integrantes = db.ListField()


if __name__ == '__main__':
    pass
#    CRIAR NOVO USUARIO
#    novo = Usuarios()
#    novo.nome = 'Fabio'
#    novo.email = 'fabio@email.com'
#    novo.save()
#    -----------------------------------------------------------
#    LISTAR TODOS
#    usuarios = Usuarios.objects()
#    for u in usuarios:
#        print u.to_json()
#        print u.nome, u.email
#    -----------------------------------------------------------
#    LISTAR 1 SO
#    user = Usuarios.objects(nome='fabio@email.com').first()
#    print user.nome, user.email
#    print user.to_json()
#    -----------------------------------------------------------
#    DELETAR USUARIO
#    user.delete()

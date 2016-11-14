#!/usr/bin/python
import requests
import json


def listar():
    response = requests.get('http://localhost:5000/usuarios/')
    response = json.loads(response.content)
    for u in response.get('usuarios'):
        print u.get('id'), u.get('nome'), u.get('email')


def atualizar():
    print '\n==ATUALIZAR USUARIO==\n'
    uid = raw_input('Digite o ID do usuario:')
    novo = {}
    novo['nome'] = raw_input('Digite o nome do usuario:')
    novo['email'] = raw_input('Digite o email do usuario:')
    content_type = {'Content-Type':'application/json'}
    response = requests.put('http://localhost:5000/usuarios/{0}/'.format(uid),
                            headers = content_type, data = json.dumps(novo))
    print json.loads(response.content)['message']


def cadastrar(linha):
    novo = {}
    linha = linha.replace('\n','')
    novo['nome'] = linha
    novo['email'] = linha.replace(' ','.').lower() + '@dexter.com.br'
    content_type = {'Content-Type':'application/json'}
    response = requests.post('http://localhost:5000/usuarios/',
                            headers = content_type, data = json.dumps(novo))
    
    print json.loads(response.content)['message']


def deletar():
    listar()
    print '\n==DELETAR USUARIO==\n'
    uid = raw_input('Digite o ID do usuario:')
    response = requests.delete('http://localhost:5000/usuarios/{0}/'.format(uid))
    print json.loads(response.content)['message']


if __name__ == '__main__':
    with open('users.txt', 'r') as f:
        for l in f.readlines():
            cadastrar(l)

#!/usr/bin/python
import requests
import json
import ConfigParser
import os


class Gitlab:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(os.path.dirname(os.path.abspath(__file__))+'/../config.cfg')
        self.token = config.get('gitlab', 'token')
        self.servidor = config.get('gitlab', 'server')
        self.headers = {'Content-Type': 'application/json'}


    def _post(self, recurso, data):
        response = requests.post('http://{0}/api/v3/{1}?private_token={2}'
                                 .format(self.servidor, recurso, self.token), 
                                 data = json.dumps(data), headers = self.headers)
        return response


    def _get(self, recurso):
        response = requests.get('http://{0}/api/v3/{1}?private_token={2}'
                                .format(self.servidor, recurso, self.token),
                                headers = self.headers)
        return response


    def criar_usuario(self, email):
        recurso = 'users'
        unome = email.split('@')[0]
        nome = unome.replace('.', ' ')
        data = {'username': unome, 'email': email, 'name': nome, 'password': '4linux123'}
        response = self._post(recurso, data)
        if response.status_code == 201:
            print 'Usuario criado com sucesso.'
        else:
            print 'Falhou ao criar usuario.\n', response.content


    def listar_usuarios(self):
        recurso = 'users'
        response = self._get(recurso)
        usuarios = json.loads(response.content)
        return usuarios


    def criar_projeto(self, nome):
        recurso = 'projects'
        data = {'name': nome}
        response = self._post(recurso, data)
        if response.status_code == 201:
            print 'Projeto criado com sucesso.'
        else:
            print 'Falhou ao criar projeto.\n', response.content


    def listar_projetos(self):
        recurso = 'projects/all'
        response = self._get(recurso)
        projetos = json.loads(response.content)
        return projetos


    def add_web_hook(self, nome, url):
        projetos = self.listar_projetos()
        # RETORNA UMA LISTA (COM UM DICT DENTRO) COM O PROJETO Q ATENDE O if
        projeto = [p for p in projetos if p.get('name') == nome]

        if projeto:
            pid = projeto[0].get('id')
            data = {'name': nome, 'url': url}
            recurso = 'projects/%s/hooks' % pid
            response = self._post(recurso, data)

            if response.status_code == 201:
                print 'Webhook cadastrada com sucesso.'
            else:
                print 'Falhou ao cadastrar.', response.content

        else:
            print 'Projeto nao encontrado.'


    def add_dev(self, uname, pname):
        usuarios = self.listar_usuarios()
        projetos = self.listar_projetos()

        usuario = [u for u in usuarios if u.get('email') == uname]
        projeto = [p for p in projetos if p.get('name') == pname]

        if usuario and projeto:
            uid = usuario[0].get('id')
            pid = projeto[0].get('id')

            recurso = '/projects/%s/members' % pid
            data = {'id': pid, 'user_id': uid, 'access_level': 30}

            response = self._post(recurso, data)
            print response.content
        else:
            print 'Falhou ao adicionar dev ao projeto.'


    def projeto_url(self, nome):
        projetos = self.listar_projetos()
        projeto = [ p for p in projetos if p.get('name') == nome ]

        if projeto:
            projeto = projeto[0].get('ssh_url_to_repo')
            return projeto
        else:
            print 'Projeto nao encontrado.'
            return self


if __name__ == '__main__':
    g = Gitlab()
    g.add_dev('Teste05', 'Projeto01')

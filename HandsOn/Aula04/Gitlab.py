#!/usr/bin/python
import requests
import json


class Gitlab:
    def __init__(self):
        self.token = 'y5BAhu9Tdmi84XjSY2yR'
        self.servidor = '192.168.0.3'
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


    def criar_usuario(self):
        recurso = 'users'
        data = {'username': 'teste5', 'email': 'teste5@teste.com', 'name': 'Teste05', 'password': '4linux123'}
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


    def criar_projeto(self):
        recurso = 'projects'
        data = {'name': 'Projeto02'}
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

        usuario = [u for u in usuarios if u.get('name') == uname]
        projeto = [p for p in projetos if p.get('name') == pname]

        if usuario and projeto:
            uid = usuario[0].get('id')
            pid = projeto[0].get('id')

            recurso = '/projects/%s/members' % pid
            data = {'id': pid, 'user_id': uid, 'access_level': 30}

            response = self._post(recurso, data)
            print response.content
        else:
            print 'Falhou ao adicionar dev {0} ao projeto {1}.'.format(uid, pid), response.content


if __name__ == '__main__':
    g = Gitlab()
    g.add_dev('Teste05', 'Projeto01')

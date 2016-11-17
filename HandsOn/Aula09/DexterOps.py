#!/usr/bin/python
from Modulos.Docker import Docker
from Modulos.Gitlab import Gitlab
from Modulos.Jenkins import Jenkins
import yaml
import argparse


class DexterOps:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-i', help = 'Define o arquivo de deploy.')


    def read_yaml(self, arquivo):
        with open(arquivo, 'r') as f:
            self.arquivo = yaml.load(f.read())


    def get_args(self):
        return self.parser.parse_args()


    def main(self):

        g = Gitlab()
        print 'Criando repositorio:', self.arquivo.get('name')
        g.criar_projeto(self.arquivo.get('name'))

        print 'Adicionando desenvolvedores:'
        for d in self.arquivo.get('developers'):
            g.criar_usuario(d)

            g.add_dev(self.arquivo.get('name'), d)

            hook = 'http://192.168.0.4:8080/gitlab/build_now'
            g.add_web_hook(self.arquivo.get('name'), hook)
            print d

        repo = g.projeto_url(self.arquivo.get('name'))

        j = Jenkins()

        print 'Criando job no Jenkins.', self.arquivo.get('name')

        j.criar_job(self.arquivo.get('name'), repo)


if __name__ == '__main__':
    d = DexterOps()
    args = d.get_args()
    d.read_yaml(args.i)
    d.main()

#!/usr/bin/python

from docker import Client
import time
import ConfigParser
import os


class Docker:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(os.path.dirname(os.path.abspath(__file__))+'/../config.cfg')
        self.client = Client(base_url='tcp://%s:2376' % config.get('docker', 'server'))


    def listar_containers(self):
        for c in self.client.containers():
            print c


    def criar_container(self, nome='novo', imagem='ubuntu', comando='/bin/bash'):
        container = self.client.create_container(image=imagem, command=comando,
                                                 name=nome, stdin_open=True, tty=True,  detach=True,
                                                 ports=[80],
                                                 host_config=self.client.create_host_config(port_bindings={80:80}))
        return container


    def iniciar_container(self, id):
        self.client.start(container = id)
        print 'Container iniciado'


    def parar_container(self, id):
        self.client.stop(container = id)
        print 'Container parado.'


    def rem_container(self, id):
        self.client.stop(container=id)
        self.client.remove_container(container=id)
        print 'Container removido.'


    def exec_comando(self, id, comando):
        exec_id = self.client.exec_create(container=id, cmd=comando)
        resultado = self.client.exec_start(exec_id)
        return resultado


    def inspec_container(self, id):
        container = self.client.inspect_container(container=id)
        return container


if __name__ == '__main__':
    d = Docker()
    container = d.criar_container()
    d.iniciar_container(container)
    # d.listar_containers()
    ip = d.inspec_container(container)
    print 'IP:', ip.get('NetworkSettings').get('IPAddress')
    print d.exec_comando(container, 'apt-get update')
    time.sleep(10)
    d.rem_container(container)


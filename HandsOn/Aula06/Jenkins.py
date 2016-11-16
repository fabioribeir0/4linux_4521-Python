#!/usr/bin/python
import jenkins
from lxml import etree


class Jenkins:
    def __init__(self):
        self.server = jenkins.Jenkins('http://192.168.0.4:8080')
        print self.server.get_version()


    def criar_job(self, nome):
        xml = self._criar_job_steps()
        self.server.create_job(nome, xml)


    def _criar_job_steps(self):
        with open('template.xml', 'r') as f:
            xml = f.read()
        root = etree.XML(xml)

        for b in root.findall('builders'):
            builder = b

        with open('Deploy.txt', 'r') as f:            
            for l in f.readlines():
                elemento_shell = etree.Element('hudson.tasks.Shell')
                elemento_command = etree.Element('command')

                elemento_command.text = l
                elemento_shell.append(elemento_command)
                builder.append(elemento_shell)

        root = etree.tostring(root)
        return root


    def exec_job(self, nome, **kwargs):
        self.server.build_job(nome, kwargs)


if __name__ == '__main__':
    j = Jenkins()
    #j.exec_job('JobPython', APP_NAME='container_teste', PORTA=81)
    j.criar_job('JobPython_Steps')
    j.exec_job('JobPython_Steps')

#!/usr/bin/python
import jenkins
from lxml import etree
import ConfigParser
import os


class Jenkins:
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(os.path.dirname(os.path.abspath(__file__))+'/../config.cfg')
        self.server = jenkins.Jenkins('http://%s:8080' % config.get('jenkins', 'server'))
        print self.server.get_version()


    def criar_job(self, nome, repo):
        xml = self._criar_job_steps(repo)
        self.server.create_job(nome, xml)


    def _criar_job_steps(self, repo):
        with open('template.xml', 'r') as f:
            xml = f.read().replace('REPO', repo)
        root = etree.XML(xml)

        for b in root.findall('builders'):
            builder = b

        elemento_shell = etree.Element('hudson.tasks.Shell')
        elemento_command = etree.Element('command')

        elemento_command.text = 'DeployTool -i $WORKSPACE/deploy.yml'
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

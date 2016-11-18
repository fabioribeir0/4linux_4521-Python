#!/usr/bin/bash
import boto3


ec2 = boto3.resource('ec2')

# new_instance = ec2.create_instances(ImageId = 'ami-b2e3c6d8', MinCount = 1,
#                                     MaxCount = 1, SecurityGroupIds = ['sg-9f9e18e2'])

instance = ec2.instances.filter(InstanceIds = ['i-52d5f5c1'])
# print instance.__dict__
# instance.stop()
# instance.start()
instance.terminate()

# sg = ec2.create_security_group(GroupName = 'PythonSG', Description = 'SG do Python')
# print sg

sg = ec2.SecurityGroup('sg-9f9e18e2')
sg.delete()
# sg.authorize_ingress(FromPort = 80, ToPort = 80, CidrIp = '0.0.0.0/0', IpProtocol = 'tcp')
# sg.revoke_ingress(FromPort = 21, ToPort = 21, CidrIp = '0.0.0.0/0', IpProtocol = 'tcp')
# sg.authorize_ingress(FromPort = 443, ToPort = 443, CidrIp = '0.0.0.0/0', IpProtocol = 'tcp')
# sg.authorize_ingress(FromPort = 22, ToPort = 22, CidrIp = '0.0.0.0/0', IpProtocol = 'tcp')


instances = ec2.instances.all()
for i in instances:
    print i.id, i.state

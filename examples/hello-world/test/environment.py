""" Environment file for behave """
import os
import subprocess
import time

def before_all(context):
    """ function run before all the scenarios in a feature """
    print(os.getcwd()) 
    subprocess.call(['docker-compose', '-f', 'fixtures/docker-compose.yml',
                     'up', '-d', '--build'])

    subprocess.call(['docker','cp','resources', 'ansible-rm:/var/alm_ansible_rm/'])
    time.sleep(10)

def after_all(context):
    """ function run after all the scenarios in a feature """
    #subprocess.call(['docker-compose', '-f', 'fixtures/docker-compose.yml',
     #                'kill'])
   # subprocess.call(['docker-compose', '-f','fixtures/docker-compose.yml',
    #                 'rm', '-f'])

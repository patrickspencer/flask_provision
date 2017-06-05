from fabric.api import *
import configparser

config = configparser.RawConfigParser()
config.read('server_settings.ini')

env.hosts = [config.get('env', 'hosts')]
env.user  = config.get('env', 'user')

def gitpull():
    with cd("/home/ubuntu/okapi"):
        run('git pull')

def collectstatic():
    with cd("/home/ubuntu/okapi"):
        run('python manage.py collectstatic')

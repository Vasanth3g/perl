from fabric import tasks
from fabric.api import run
from fabric.api import env
from fabric.network import disconnect_all

env.hosts = [
    '192.168.1.21',
    '192.168.1.37',
]

def host_type():
    run('uname -s')

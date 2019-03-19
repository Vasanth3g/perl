from fabric import tasks
from fabric.api import run
from fabric.api import env
from fabric.network import disconnect_all

env.hosts = [
    'x.x.x.x',
    'x.x.x.x',
]

def host_type():
    run('uname -s')

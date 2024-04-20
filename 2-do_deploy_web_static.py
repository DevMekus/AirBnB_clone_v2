#!/usr/bin/python3
"""
This ia Fabric script that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.227.221.235', '100.26.57.130']


def do_deploy(archive_path):
    """function that distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        myFile_n = archive_path.split("/")[-1]
        noExt = myFile_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, noExt))
        run('tar -xzf /tmp/{} -C {}{}/'.format(myFile_n, path, noExt))
        run('rm /tmp/{}'.format(myFile_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, noExt))
        run('rm -rf {}{}/web_static'.format(path, noExt))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, noExt))
        return True
    except:
        return False

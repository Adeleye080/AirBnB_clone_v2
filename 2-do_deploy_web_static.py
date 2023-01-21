#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from fabric.api import run, env, put
import time
import os


env.hosts = ['44.200.178.81', '54.175.65.219']


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None


def do_deploy(archive_path):
    """ """
    arc_path = 'versions/web_static_20221214143240.tgz'
    filename = arc_path.split('/')[-1]
    no_ext = filename.split('.')[0]
    path = '/data/web_static/releases/'

    if os.exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, '/tmp/')
            run(f'sudo mkdir -p {path}{filename}')
            run(f'sudo tar -xzf /tmp/{arc_path} -C {path}{no_ext}')
            run(f'sudo rm /tmp/{filename}')
            run(f'sudo mv {path}{no_ext}/web_static/* {path}{no_ext}/')
            run(f'sudo rm -rf {path}{no_ext}/web_static')
            run(f'sudo rm -rf /data/web_static/current')
            run(f'sudo ln -s {path}{no_ext} /data/web_static/current')
            return True
        except Exception:
            return False

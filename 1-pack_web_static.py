#!/usr/bin/python3
from fabric.api import local
import time


def do_pack():
    try:
        d_time = time.strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        local(f'tar -czvf versions/web_static_{d_time}.tgz web_static/')
        return f"versions/web_static_{d_time}.tgz"
    except:
        return None

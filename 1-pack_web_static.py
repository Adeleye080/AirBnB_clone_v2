#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the
 web_static folder of your AirBnB Clone repo
"""
from fabric.api import local
import time


def do_pack():
    """Generate a tgz archive from web_static folder"""
    try:
        d_time = time.strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        local(f'tar -czvf versions/web_static_{d_time}.tgz web_static/')
        return f"versions/web_static_{d_time}.tgz"
    except:
        return None

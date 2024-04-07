#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import env, run, local, lcd, cd
from datetime import datetime
from os import listdir

env.hosts = ['100.25.190.180', '54.224.40.16']

def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    try:
        number = int(number)
    except ValueError:
        return False

    if number < 0:
        return False
    elif number == 0 or number == 1:
        number = 1

    with lcd("versions"):
        local("ls -1t | tail -n +{} | xargs rm -rf".format(number + 1))

    with cd("/data/web_static/releases"):
        run("ls -1t | tail -n +{} | xargs rm -rf".format(number + 1))


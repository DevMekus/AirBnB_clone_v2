
n Deletes out-of-date dArchives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['100.26.57.130', '54.227.221.235']


def do_clean(number=0):
    """function Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.    
    """
    number = 1 if int(number) == 0 else int(number)

    dArchives = sorted(os.listdir("versions"))
    [dArchives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in dArchives]

    with cd("/data/web_static/releases"):
        dArchives = run("ls -tr").split()
        dArchives = [a for a in dArchives if "web_static_" in a]
        [dArchives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in dArchives]#!/usr/bin/python3
"""
Function Deletes out-of-date dArchives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['100.26.57.130', '54.227.221.235']


def do_clean(number=0):
    """function Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.    
    """
    number = 1 if int(number) == 0 else int(number)

    dArchives = sorted(os.listdir("versions"))
    [dArchives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in dArchives]

    with cd("/data/web_static/releases"):
        dArchives = run("ls -tr").split()
        dArchives = [a for a in dArchives if "web_static_" in a]
        [dArchives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in dArchives]

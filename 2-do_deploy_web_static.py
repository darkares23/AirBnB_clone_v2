#!/urs/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:
"""
from fabric.api import run, put, env, sudo
from fabric.contrib.files import exists
from datetime import datetime

env.hosts = ['34.74.164.242', '3.87.108.35']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            fileName = archive_path.split("/")[1].split(".")[0]
            path = "/data/web_static/releases/{}".format(fileName)
            sudo("mkdir -p {}/".format(path))
            sudo("tar -zxf /tmp/{}.tgz -C {}/".format(fileName, path))
            sudo("rm /tmp/{}".format(archive_path.split("/")[1]))
            sudo("rm /data/web_static/current")
            sudo("ln -fs /data/web_static/releases/{} /data/web_static/current"
                 .format(fileName))
            sudo("service nginx restart")
        except Exception:
            return False
    return True

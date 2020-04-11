#!/urs/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:
"""
from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os.path import exists

env.hosts = ['34.74.164.242', '3.87.108.35']


def do_deploy(archive_path):
    """This function will deploy the web static to the servers"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        fileName = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(fileName)
        sudo("mkdir -p {}/".format(path))
        sudo("tar -zxf /tmp/{}.tgz -C {}/".format(fileName, path))
        sudo("rm /tmp/{}".format(archive_path.split("/")[1]))
        sudo("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(fileName, fileName))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(fileName))
        print("New version deployed!")
        return True
    except Exception:
        return False

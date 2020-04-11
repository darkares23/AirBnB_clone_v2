#!/urs/bin/python3
from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os.path import exists

env.hosts = ['34.74.164.242', '3.87.108.35']


def do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(filename)
        run("sudo mkdir -p {}/".format(path))
        run("sudo tar -zxf /tmp/{}.tgz -C {}/".format(filename, path))
        run("sudo rm /tmp/{}".format(archive_path.split("/")[1]))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(filename, filename))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(filename))
        print("New version deployed!")
        return True
    except Exception:
        return False

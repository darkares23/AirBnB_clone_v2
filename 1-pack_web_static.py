#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create web satic package"""
    try:
        current_date = datetime.now().strftime("%Y%m%d%H%M%S")
        zipper = "versions/web_static_{}.tgz".format(current_date)
        local("sudo mkdir -p versions | sudo tar -cvzf {} web_static".format(
            zipper))
        return zipper
    except Exception:
        return None

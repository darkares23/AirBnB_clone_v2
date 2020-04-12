#!/usr/bin/python3

from os.path import exists
from datetime import datetime
from fabric.api import local, run, env, put, sudo
env.hosts = ["3.84.104.13", "35.237.21.147"]


def do_clean(number=0):
    number = int(number)
    local("ls -d -1tr versions/* | tail -n +{} | \
          xargs -d '\n' rm -f --".format(2 if number < 1 else number + 1))
    run("ls -d -1tr /data/web_static/releases/* | tail -n +{} | \
          xargs -d '\n' rm -rf --".format(2 if number < 1 else number + 1))

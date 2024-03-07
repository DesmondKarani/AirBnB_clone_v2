#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy"""

from fabric.api import *
from os.path import exists

env.hosts = ['100.25.158.138', '35.168.3.127']  # My server IPs


def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not exists(archive_path):
        return False
    filename = archive_path.split('/')[-1]
    no_tgz = f'/data/web_static/releases/{filename.split(".")[0]}'
    tmp = f"/tmp/{filename}"

    try:
        put(archive_path, "/tmp/")
        run(f"mkdir -p {no_tgz}/")
        run(f"tar -xzf {tmp} -C {no_tgz}/")
        run(f"rm {tmp}")
        run(f"mv {no_tgz}/web_static/* {no_tgz}/")
        run(f"rm -rf {no_tgz}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {no_tgz} /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

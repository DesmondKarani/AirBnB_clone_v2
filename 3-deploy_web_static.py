#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from web_static contents and
distributes it to web servers.
"""
from fabric.api import *
from datetime import datetime
from os.path import isfile

env.hosts = ['100.25.158.138', '35.168.3.127']


def do_pack():
    """
    Generates a .tgz archive from the contents of the 'web_static' folder.
    """
    local("mkdir -p versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)
    local_cmd = local("tar -cvzf {} web_static".format(archive_path))
    if local_cmd.succeeded:
        return archive_path
    return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    if not isfile(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        tmp_path = "/tmp/{}".format(filename)
        release_path = "/data/web_static/releases/{}".format(no_ext)
        current_path = "/data/web_static/current"
        put(archive_path, tmp_path)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(tmp_path, release_path))
        run("rm {}".format(tmp_path))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf {}".format(current_path))
        run("ln -s {} {}".format(release_path, current_path))
        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False


def deploy():
    """
    Creates and distributes an archive to web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

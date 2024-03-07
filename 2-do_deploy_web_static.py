#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy"""

from fabric.api import env, put, run, local
from os.path import isfile

env.hosts = ['100.25.158.138', '35.168.3.127']
env.user = "ubuntu"
env.key_filename = "my_ssh_private_key"


def do_deploy(archive_path):
    if not isfile(archive_path):
        return False

    try:
        # Extract the file name from the archive_path
        file_name = archive_path.split("/")[-1]
        name_without_extension = file_name.split(".")[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(file_name))

        # Create directory where we will uncompress the archive
        run("mkdir -p /data/web_static/releases/{}/"
            .format(name_without_extension))

        # Uncompress the archive
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, name_without_extension))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Move the content out of the web_static folder
        run("mv /data/web_static/releases/{}/web_static/*"
            "/data/web_static/releases/{}/"
            .format(name_without_extension, name_without_extension))

        # Delete the now empty web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(name_without_extension))

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name_without_extension))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False

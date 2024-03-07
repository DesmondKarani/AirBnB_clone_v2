#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['IP_web-01', 'IP_web-02']  # Replace with your actual IP addresses
env.user = "ubuntu"  # Assuming 'ubuntu' is the user for SSH access


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        # Extract the file name from the archive_path
        file_name = archive_path.split("/")[-1]
        # Remove extension from the file_name to get to the root folder name
        name_no_ext = file_name.split(".")[0]

        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, "/tmp/{}".format(file_name))

        # Create the directory where we will uncompress the archive
        run("mkdir -p /data/web_static/releases/{}/".format(name_no_ext))

        # Uncompress the archive to the folder on the server
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, name_no_ext))

        # Delete the archive from the server
        run("rm /tmp/{}".format(file_name))

        # Move content out from archive folder to its parent
        # then delete the empty archive folder
        run("mv /data/web_static/releases/{}/web_static/*"
            "/data/web_static/releases/{}/".format(name_no_ext, name_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(name_no_ext))

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name_no_ext))

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

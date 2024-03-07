#!/usr/bin/python3
"""a Fabric script that generates a .tgz
archive from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack."""


from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the directory versions if it doesn't exist
    local("mkdir -p versions")

    # Format the current datetime to create the archive name
    now = datetime.now()
    archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Create the archive using tar command
    command = "tar -cvzf {} web_static".format(archive_name)
    result = local(command, capture=True)

    # Check if the archive was successfully created
    if result.failed:
        return None
    return archive_name

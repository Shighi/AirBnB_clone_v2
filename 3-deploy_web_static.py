#!/usr/bin/python3
"""A Fabric script that creates and distributes an archive to web servers.

This module provides functions to:
    - Create a compressed archive of the web_static directory
    - Deploy the archive to multiple web servers
    - Combine both operations in a single deployment command
"""
from fabric.api import env, local, put, run
from datetime import datetime
import os.path


env.hosts = ['34.207.212.172', '18.210.13.214']
env.user = 'ubuntu'
env.key_filename = os.path.expanduser('~/privatekey')


def do_pack():
    """Create a compressed archive of the web_static directory.

    Returns:
        str: Path to created archive if successful, None otherwise
    """
    try:
        local('mkdir -p versions')
        datetime_format = '%Y%m%d%H%M%S'
        archive_path = 'versions/web_static_{}.tgz'.format(
            datetime.now().strftime(datetime_format))
        local('tar -cvzf {} web_static'.format(archive_path))
        if os.path.exists(archive_path):
            return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploy web static content to servers.

    Args:
        archive_path (str): Path to the archive to deploy

    Returns:
        bool: True if deployment succeeded, False otherwise
    """
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = os.path.basename(archive_path)
        no_ext = file_name.split('.')[0]
        put(archive_path, '/tmp/')
        releases_path = '/data/web_static/releases/{}'.format(no_ext)
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, releases_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    """Execute full deployment: create archive and deploy to servers.

    Returns:
        bool: True if deployment succeeded, False otherwise
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

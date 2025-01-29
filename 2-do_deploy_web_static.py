#!/usr/bin/python3
"""Fabric script module for deploying web static content.

This script provides functionality to distribute archives to web servers,
automating the deployment process of static files. It handles file uploads,
extraction, and symbolic link management on remote servers.
"""
from fabric.api import env, put, run
import os


# Server configuration
env.hosts = ['34.207.212.172', '18.210.13.214']
env.user = 'ubuntu'
env.key_filename = os.path.expanduser('~/privatekey')


def do_deploy(archive_path):
    """Deploy web static content to servers.

    Args:
        archive_path (str): Path to the archive file to deploy.

    Returns:
        bool: True if deployment succeeds, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Get filename from archive path
        file_name = os.path.basename(archive_path)
        # Remove .tgz extension for directory name
        no_ext = file_name.split('.')[0]
        # Upload archive
        put(archive_path, '/tmp/')
        # Prepare release path
        releases_path = '/data/web_static/releases/{}'.format(no_ext)

        # Create directory and set permissions
        run('sudo mkdir -p {}'.format(releases_path))
        run('sudo chown -R ubuntu:ubuntu {}'.format(releases_path))

        # Extract archive
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, releases_path))

        # Remove archive
        run('rm /tmp/{}'.format(file_name))

        # Move contents - modified to handle existing directories
        run('cp -r {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))

        # Set permissions
        run('sudo chown -R ubuntu:ubuntu {}'.format(releases_path))
        run('sudo chmod -R 755 {}'.format(releases_path))

        # Update symbolic link
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(releases_path))

        print('New version deployed!')
        return True

    except Exception as e:
        print('Deployment failed:', str(e))
        return False

#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""
from fabric.api import env, put, run, local
from datetime import datetime
import os

# Server configuration
env.hosts = ['34.207.212.172', '18.210.13.214']
env.user = 'ubuntu'
env.key_filename = os.path.expanduser('~/privatekey')

def do_deploy(archive_path):
    """
    Deploys the static files to the host servers
    Args:
        archive_path: path to the archive file
    Returns:
        True if successful, False otherwise
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
        
        # Create directory
        run('mkdir -p {}'.format(releases_path))
        
        # Extract archive
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, releases_path))
        
        # Remove archive
        run('rm /tmp/{}'.format(file_name))
        
        # Move contents
        run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))
        
        # Update symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        
        return True

    except Exception:
        return False

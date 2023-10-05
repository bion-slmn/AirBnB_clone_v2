#!/usr/bin/python3
''' This Fabric script that generates a .tgz archive
from the contents of the web_static'''
from fabric.api import local, run, env, put
from datetime import date
from datetime import datetime
import os.path

env.hosts = ['54.89.179.242', '3.90.83.124']


def do_deploy(archive_path):
    '''deploys achivef file'''
    try:
        file_exists = os.path.isfile(archive_path)
        if not file_exists:
            return False

        # removing extension fromthe file name
        file_name = os.path.basename(archive_path)
        no_ext = file_name.split('.')[0]
        dest_dir = f'/data/web_static/releases/{no_ext}'

        # upload to remote
        put(archive_path, '/tmp/')
        run(f'sudo rm -rf {dest_dir}')
        run(f'sudo mkdir -p {dest_dir}')

        # unzip the acrchive
        run(f'sudo tar -C {dest_dir} -xzf /tmp/{file_name}')
        # remove the acrchive
        run(f'sudo rm /tmp/{file_name}')
        # move the content
        run(f'sudo mv {dest_dir}/web_static/* {dest_dir}')
        run(f'sudo rm -rf {dest_dir}/web_static')
        run(f'sudo rm -rf /data/web_static/current')
        # create a symblink
        run(f'sudo ln -s {dest_dir} /data/web_static/current')
        print("New version deployed!")
        return True
    except Exception as e:
        return False

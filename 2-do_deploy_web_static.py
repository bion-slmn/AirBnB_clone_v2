#!/usr/bin/python3
'''Fabric script (based on the file 1-pack_web_static.py) t
that distributes an archive to your web servers'''
import os.path
from fabric.api import run, put, env


env.hosts = ['54.89.179.242', '3.90.83.124']
env.user = 'ubuntu'


def do_pack():
    ''' the function to generate compressed file'''
    local('mkdir -p versions')
    today = date.today()
    now = datetime.now()

    print('here')

    file_name = "web_static_{}{}{}{}{}{}.tgz".format(today.year,
                                                     today.month,
                                                     today.day,
                                                     now.hour,
                                                     now.minute,
                                                     now.second)

    comp = local('tar -czvf versions/{} web_static'.format(file_name))

    if comp.failed:
        return None

    return 'versions/{}'.format(file_name)


def do_deploy(archive_path):
    '''deploys achivef file'''
    file_exists = os.path.isfile(archive_path)
    if not file_exists:
        return False

    # removing extension fromthe file name
    file_name = os.path.basename(archive_path)
    no_ext = file_name.split('.')[0]
    dest_folder = f'/data/web_static/releases/{no_ext}'

    put(archive_path, '/tmp/')
    run(f'mkdir -p {dest_folder}')

    # extracting
    run(f'sudo tar -C {dest_folder} -xvf /tmp/{file_name}')
    run(f'sudo rm /tmp/{file_name}')
    run('sudo rm /data/web_static/current')
    run(f'ln -s {dest_folder} /data/web_static/current')
    return True

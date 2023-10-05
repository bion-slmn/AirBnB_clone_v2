#!/usr/bin/python3
''' This Fabric script that generates a .tgz archive
from the contents of the web_static'''
from fabric.api import local, run, env, put, task, execute
from datetime import date
from datetime import datetime
import os.path


env.hosts = ['54.89.179.242', '3.90.83.124']


@task
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


@task
def do_deploy(archive_path):
    '''deploys achivef file'''
    try:
        if not os.path.exists(archive_path):
            return False
        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(dpath, fn_no_ext))
        run("mkdir -p {}{}/".format(dpath, fn_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(fn_with_ext, dpath, fn_no_ext))
        run("rm /tmp/{}".format(fn_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fn_no_ext))
        run("rm -rf {}{}/web_static".format(dpath, fn_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dpath, fn_no_ext))
        print("New version deployed!")
        return True
    except Exception as e:
        return False


@task
def deploy():
    '''creates and distributes an archive to your web servers'''
    archive_path = do_pack()
    if not archive_path:
        return false
    execute(do_deploy, archive_path)
    exit()

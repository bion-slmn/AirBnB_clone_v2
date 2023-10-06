#!/usr/bin/python3
'''defines a functioin hat deletes out-of-date archives'''
from fabric.api import run, env, task, local
import os

env.hosts = ['54.89.179.242', '3.90.83.124']


def do_clean(number=0):
    '''deletes out-of-date archives
    number (int)  is the number of the archivies to keep
            number is 0 or 1, keep only the most recent version
            number is 2, keep the most recent, and second most recent versions
            and son on
    '''
    no = int(number)
    # puting the content in list content of the directory
    dir_path = '/data/web_static/releases/'
    dir_path1 = 'versions'

    dir_list = run('ls -t {}'.format(dir_path)).split()
    dir_list1 = sorted(os.listdir(dir_path1), reverse=True)

    # delete accordingly
    if no == 0 or no == 1:
        no = 1

    for arch in dir_list[no:]:
        path = os.path.join(dir_path, arch)
        run('rm -rf {}'.format(path))
    for arch in dir_list1[no:]:
        path = os.path.join(dir_path1, arch)
        local('rm -rf {}'.format(path))

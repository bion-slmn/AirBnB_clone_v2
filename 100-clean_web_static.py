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
    # puting the content in list content of the directory
    dir_path = '/data/web_static/releases/'
    dir_path1 = 'versions'

    dir_list = run(f'ls {dir_path}').split()
    dir_list1 = local(f'ls {dir_path1}', capture=True).split()
    # sort them in desceding order
    sorted_list = sorted(dir_list, reverse=True)
    sorted_list1 = sorted(dir_list1, reverse=True)
    # delete accordingly
    if int(number) == 0 or int(number) == 1:
        number = 1
        print('HERE')
    else:
        number = int(number)

    for arch in sorted_list[number:]:
        path = os.path.join(dir_path, arch)
        print(f'{path} PAATJ')
        run(f'rm -rf {path}')
    for arch in sorted_list1[number:]:
        path = os.path.join(dir_path1, arch)
        local(f'rm -rf {path}')

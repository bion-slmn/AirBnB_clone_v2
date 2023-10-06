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
    remote_path = '/data/web_static/releases/'
    local_path = 'versions'

    no = int(number)

    # delete accordingly
    if no == 0 or no == 1:
        no = 1

    local('ls -t versions | tail +{} | xargs -I % rm -rf versions/%'.format(no + 1))
    run('ls -t {} | tail +{} | xargs -I % rm -rf versions/%'.format(remote_path, no + 1))

#!/usr/bin/python3
''' This Fabric script that generates a .tgz archive
from the contents of the web_static'''
from fabric.api import local
from datetime import date
from datetime import datetime


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

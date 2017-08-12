# -*- coding=utf-8 -*-
'''
create by :paddyguan
create time:2017-08-09
'''
import apps
from flask_script import Manager

app = apps.create_app()
manager = Manager(app)


if __name__ == '__main__':
    manager.run()

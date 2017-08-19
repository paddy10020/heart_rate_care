# -*- coding=utf-8 -*-
'''
create by :paddyguan
create time:2017-08-09
'''
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from wsgi import app      
from models.base import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

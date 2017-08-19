# -*- coding:utf-8 -*-
"""
Brief Desc: apps配置和初始化
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-10 23:40:17. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from flask import Flask
from models import base

def create_app(config=None):
    """app创建工厂方法"""
    app = Flask(__name__)
    config = config or 'config.Config'
    app.config.from_object(config)
    
    register_db(app)
    register_blueprints(app)
    
    return app

def register_db(app):
    base.db.init_app(app)


def create_db_app(config=None):
    ''' datebases initial '''
    app = Flask(__name__)
    register_db(app)
    
def register_blueprints(app):
    from apps import bp_index

    app.register_blueprint(bp_index.bp)

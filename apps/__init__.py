# -*- coding:utf-8 -*-
"""
Brief Desc: apps配置和初始化
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-10 23:40:17. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from flask import Flask
from apps import bp_index


def create_app():
    """app创建工厂方法"""
    app = Flask(__name__)
    app.register_blueprint(bp_index.bp)
    return app


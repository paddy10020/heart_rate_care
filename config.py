# -*- coding:utf-8 -*-
"""
Brief Desc: app的一些配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-12 16:08:15. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


class Config(object):
    '''配置文件类''' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = r'mysql://root:qwe8885845@127.0.0.1:3306/heart_rate?charset=utf-8'
    SQLALCHEMY_DATABASE_URI = r'sqlite:////tmp/test.db'


class DevConfig(Config):
    '''测试配置文件类'''
    DEBUG = True


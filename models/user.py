# -*- coding:utf-8 -*-
"""
Brief Desc: 填写你的注释
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-13 20:09:44. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import datetime
import traceback

import ujson as json
from sqlalchemy import text
#from sqlalchemy.dialects.mysql import \
#     DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, LONGBLOB, LONGTEXT, MEDIUMBLOB, \
#     MEDIUMINT, MEDIUMTEXT, NCHAR, NUMERIC, NVARCHAR, REAL, SET, SMALLINT, \
#     TEXT, TIME, TIMESTAMP, TINYBLOB, TINYINT, YEAR, BIGINT, BINARY, BIT, \
#     BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, TINYTEXT, VARBINARY, VARCHAR

from base import db

class User(db.Model):
    """ Model docstring """
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}

    # 模型常量定义
    # STATUS_OK = 1
    # STATUS_FAIL = 0

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(64), nullable=False, default='VALUE')
    # col2_name = db.Column(db.String(64), nullable=True)   # 如有必要请注释
    user_age = db.Column(db.Integer, nullable=True)
    user_sex = db.Column(db.Boolean, nullable=True)
    # 视具体情况开放以下字段：动态数据表应当开放attribute;后台相关表应当开放
    # create_by和update_by和update_time;视情况为create_time和update_time增加
    # 索引;     <# 生成代码后请删除不需要的注释#>
    create_time = db.Column(db.DateTime, server_default=text('NOW()'))
    update_time = db.Column(db.DateTime, nullable=False, \
                            server_default=text('NOW()'), onupdate=datetime.datetime.now)

# -*- coding:utf-8 -*-
"""
Brief Desc: 数据模型的基础类
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-13 20:10:37. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import random
import datetime
from functools import partial

import sqlalchemy.orm as orm
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy, get_state
from sqlalchemy import text
from sqlalchemy.dialects.mysql import INTEGER, TEXT, ENUM

db = SQLAlchemy()

class AutoRouteSession(orm.Session):
    def __init__(self):
        pass

    def get_bind(self):
        pass


class AutoRouteSQLAlchemy(SQLAlchemy):
    def create_scoped_session(self, options=None):
        pass







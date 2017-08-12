# -*- coding:utf-8 -*-
"""
Brief Desc: 填写你的注释
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-10 23:33:34. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import datetime
import traceback

import ujson as json
from flask import Blueprint, current_app
from flask_login import current_user, login_required

bp = Blueprint('bp_index', __name__)

@bp.route('/', methods=['GET'])
def index():
    return '<html><h1>Index Page!</h1></html>'

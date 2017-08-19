# -*- coding:utf-8 -*-
"""
Brief Desc: index page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-10 23:33:34. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import datetime
import traceback

import ujson as json
from flask import Blueprint, current_app
from flask_login import current_user, login_required
from flask import request

bp = Blueprint('bp_index', __name__)

@bp.route('/', methods=['GET'])
def index():
    return '<html><h1>Index Page!</h1></html>'

@bp.route('/send_heart_rate', methods=['GET', 'POST'])
def get_heart_rate_from_client():
    print 'get_heart_from_client'
    heart_rate = str(request.form.get('heart_rate'))
    print 'heart_rate is ' + heart_rate
    return '<html><h1>heart_rate is %s </h1></html>' % heart_rate

@bp.route('/get_heart_rate', methods=['GET'])
def send_heart_rate():
    return '<html><h1>get_heart_from_client</h1> </html>'

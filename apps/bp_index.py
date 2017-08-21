# -*- coding:utf-8 -*-
"""
Brief Desc: index page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-10 23:33:34. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import datetime
import traceback
from lib.deal_source_data import filter_date

import ujson as json
from flask import Blueprint, current_app, request
from flask_login import current_user, login_required
from flask import request


bp = Blueprint('bp_index', __name__)

@bp.route('/', methods=['GET'])
def index():
    return '<html><h1>Index Page!</h1></html>'

@bp.route('/send_heart_rate', methods=['GET', 'POST'])
def get_heart_rate_from_client():
    print 'get_heart_from_client'
    try:
        origin_data = request.get_json()
    except Exception, e:
        print e
    else:
        print type(origin_data['heart_rate_data'])
        print len(origin_data['heart_rate_data'])
        result = filter_date(origin_data['heart_rate_data'])
        print result
    return json.dumps({'code':0,
                       'msg': 'success',
                       'data': result,
                       })


@bp.route('/get_heart_rate', methods=['GET'])
def send_heart_rate():
    return '<html><h1>get_heart_from_client</h1> </html>'

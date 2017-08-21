# -*- coding:utf-8 -*-
"""
Brief Desc:test bp_index.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-12 15:55:15. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import unittest
import ujson as json
import datetime
import requests
from wsgi import app

class TestIndexCase(unittest.TestCase):
    '''xxx'''
    def setUp(self):
        self.app = app
        self.client = app.test_client()
    
    def test_index(self):
        print 'test_index'
        with self.app.app_context():
            r = self.client.get('/')
            print r.data
        print '-'*20

    def test_send_heart_rate(self):
        print 'test_send_heart_rate'
        test_url = 'send_heart_rate'
        with self.app.app_context():
            with open('/Users/paddyguan/python_project/heart_rate_care/tests/lib/heart_rate_data.txt') as f:
                heart_rate_data = [int(i.strip()) for i in f.readlines()]
            r = self.client.post(test_url, data=json.dumps({'heart_rate_data': heart_rate_data, 'time': str(datetime.datetime.now())[0:19]}), headers={'Content-type': 'application/json;charset=utf-8'})
            print r.data
        print '-'*20

    def test_get_heart_rate(self):
        print 'test_get_heart_rate'
        test_url = 'get_heart_rate'
        with self.app.app_context():
            r = self.client.get(test_url)
            print r.data
        print '-'*20

    def tearDown(self):
        pass
        
if __name__ == '__main__':
    unittest.main()

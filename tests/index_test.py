# -*- coding:utf-8 -*-
"""
Brief Desc:test bp_index.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-12 15:55:15. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import unittest
import ujson as json
import requests
# import os
# import sys
# from .  import wsgi
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
        #a = requests.post('http://127.0.0.1:5000', json=json.dumps({'heart_rate': 123}), headers={'Content-type': 'application/json;charset=utf-8'})
        with self.app.app_context():
            print dir(self.client.post)
            r = self.client.post(test_url, data=json.dumps({'heart_rate': '123'}), headers={'Content-type': 'application/json;charset=utf-8'})
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

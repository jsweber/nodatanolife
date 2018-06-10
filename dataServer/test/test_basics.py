import unittest
from flask import current_app
import os, sys

parentDir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, parentDir)
from app import create_app, db

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        #在测试前运行
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        #在测试后运行
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
        

# if __name__ == '__main__':

    print(os.environ.get('MAIL_USERNAME'))
    print(os.environ.get('MAIL_PASSWORD'))
    print('[test message]: no var? try source <filename>')

from flask import render_template

import os, sys

parentDir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, parentDir)
from auth import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')



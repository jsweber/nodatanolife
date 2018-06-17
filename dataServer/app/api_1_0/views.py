import os, sys
from datetime import datetime
from flask_login import login_required
from flask import Flask, make_response, url_for, request, json, jsonify, session, redirect, render_template

parentDir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, parentDir)
from api_1_0 import api
from __init__ import db
from models import Job
import json

@api.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # print('form===================', request.form) #都是可以的
        # print('values================', request.values)
        # data = request.values.get('data')
        # print(request.get_data())
        reqData = json.loads(request.get_data().decode('utf-8'))
        return jsonify(code=200, data=reqData.get('data'), message='ok')
    elif request.method == 'GET':
        data = request.args.get('data', None)
        return jsonify(code=200, data=data, message='ok')


import os, sys
from datetime import datetime
from flask_login import login_required
from flask import Flask, make_response, url_for, request, json, jsonify, session, redirect, render_template
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

parentDir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, parentDir)
from api_1_0 import api
from __init__ import es
from models import Job
import json
#https://github.com/chiangf/Flask-Elasticsearch
#https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html
#https://elasticsearch-py.readthedocs.io/en/master/

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

@api.route('/s', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        postData = json.loads(request.get_data().decode('utf8'))
        query = postData.get('q')
    elif request.method == 'GET':
        query = request.args.get('q')
    print(query)
    
    # resp = es.search(index='job_data', doc_type='job', body={
    #     'query': {
    #         'match': {
    #             'job_name': query
    #         }
    #     }
    # })
    resp = es.get('job_data', doc_type='job', id=1)

    print(resp)

    return jsonify({"code":200, "data":{"list": "", "length": 12}, "message":'ok'})





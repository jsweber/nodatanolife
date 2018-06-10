import os, sys
from datetime import datetime
from flask import Flask, make_response, url_for, request, json, jsonify, session, redirect, render_template

parentDir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, parentDir)
from main import main
from __init__ import db
from models import Job

@main.route('/', methods=['GET', 'POST'])
def index():
    
    return redirect(url_for('.index'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    print(request.args.get('name', 'none'))
    if request.method == 'POST':
        return 'post'
    elif request.method == 'GET':
        return jsonify(username=request.args.get('name', 'nobody'), age=30, location='shanghai')

@main.route('/api/count/<name>')
def count(name):
    c = db.session.query(Job.salary).filter(Job.job_name.op('regexp')(name)).all()
    resp = make_response('<p>'+ str(c) +'</p>')
    return resp

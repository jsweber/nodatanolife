import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response, render_template
from flask_script import Manager
from flask_wtf import Form
from hello import Job, db

app = Flask(__name__)
#csrf cross site request forgery
app.config['SECRET_KEY'] = 'secret key'
manager = Manager(app)

def conncet_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def index():
    resp = make_response('<p>welcome</p>')
    resp.set_cookie('test','99999')
    return resp

@app.route('/r')
def redirectUrl():
    return redirect('http://tradeww.com')

@app.route('/html/<name>')
def html(name):
    return render_template('index.html', name=name)

@app.route('/api/count/<name>', methods=['GET', 'POST'])
def count(name):
    # c = db.session.query(Job.job_id).filter(Job.job_name.op('regexp')('java')).count()
    c = db.session.query(Job.job_name, Job.welfare_list).filter(Job.job_name.op('regexp')('土建工程师')).count()
    return c

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interval(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    print(__name__)
    manager.run()

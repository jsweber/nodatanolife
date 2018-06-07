import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response, render_template
from flask_script import Manager
from flask_wtf import Form
from hello import Job, User, db
from flask_mail import Mail, Message

app = Flask(__name__)
#csrf cross site request forgery
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'nodatanolife@qq.com'
app.config['MAIL_PASSWORD'] = 'ghhxublhjmyldhad'

manager = Manager(app)
mail = Mail(app)
message = Message('test subject', recipients=['951092973@qq.com'])
message.body = 'test content'
mail.send(message)
# message.html = '<p style="color:red">html</p>'
# with app.app_context():
    

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
    print('name：'+name)
    c = db.session.query(Job.salary).filter(Job.job_name.op('regexp')(name)).all()
    # c = db.session.query(User.username).all()
    resp = make_response('<p>'+ str(c) +'</p>')
    return resp

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interval(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    print(__name__)
    manager.run()

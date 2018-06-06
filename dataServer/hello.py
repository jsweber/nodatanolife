#!/usr/bin/env python
#encoding:utf8

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
import os
from datetime import datetime
import re

basedir = os.path.abspath(os.path.dirname(__file__))
SQL_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ecust2014@localhost:3306/renting_data'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ecust2014@localhost:3306/trade_home'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand) #python hello.py db init

class Job(db.Model):
    __tablename__= 'liepin_2018_4'
    job_id = db.Column(db.String(32), primary_key=True)
    job_name = db.Column(db.String(50), nullable=False, index=True)
    job_url = db.Column(db.String(300))
    company = db.Column(db.String(50))
    salary = db.Column(db.String(30))
    work_location = db.Column(db.String(100))
    publish_time = db.Column(db.DateTime, default=datetime.now().strftime(SQL_DATETIME_FORMAT))
    required_list = db.Column(db.String(200), nullable=False)
    welfare_list = db.Column(db.String(300), nullable=False)
    job_describe = db.Column(db.Text, nullable=False)
    crawl_time = db.Column(db.DateTime, default=datetime.now().strftime(SQL_DATETIME_FORMAT))

    def __repr__(self):
        return '<Job %s>' % (self.job_name,)

class User(db.Model):
    __tablename__='user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45))
    telephone = db.Column(db.String(45))
    email = db.Column(db.String(45))
    gender = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<User %s>' % self.username

def make_shell_context():
    return dict(app=app, db=db, User=User, Job=Job)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    # print(db.session.query(Job.job_name, Job.welfare_list).filter(Job.job_name == '土建工程师').count()) #14 没有all或者count返回原始sql
    # print(db.session.query(Job.job_name, Job.welfare_list).filter(Job.job_name.like('%土建工程师%')).count()) #19
    # print(db.session.query(Job.job_name, Job.welfare_list).filter(Job.job_name.op('regexp')('土建工程师')).count()) #19
    # print(db.session.query(User.username).all())
    newJob = Job(
        job_id='123456',
        job_name='web前端工程师',
        job_url="http://www.tradeww.com",
        company='腾讯',
        salary="30w",
        required_list='细讲',
        welfare_list='无线一斤',
        job_describe='no way'
    )
    db.session.add(newJob)
    db.session.commit()

    manager.run()

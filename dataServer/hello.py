from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
import datetime
import re

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ecust2014@localhost:3306/renting_data'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Job(db.Model):
    __tablename__= 'liepin_2018_4'
    job_id = db.Column(db.String(32), primary_key=True)
    job_name = db.Column(db.String(50), nullable=False, index=True)
    company = db.Column(db.String(50))
    salary = db.Column(db.String(30))
    work_location = db.Column(db.String(100))
    publish_time = db.Column(db.DateTime, default=datetime.datetime.now().time())
    required_list = db.Column(db.String(200), nullable=False)
    welfare_list = db.Column(db.String(300), nullable=False)
    job_describe = db.Column(db.Text, nullable=False)
    crawl_time = db.Column(db.DateTime, default=datetime.datetime.now().time())

    def __repr__(self):
        return '<User %s>' % (self.job_name,)
if __name__ == '__main__':
    # print(db.session.query(Job.job_name, Job.welfare_list).filter(Job.job_name == '土建工程师').count()) #14 没有all或者count返回原始sql
    # print(db.session.query(Job.job_name, Job.welfare_list).filter(Job.job_name.like('%土建工程师%')).count()) #19
    print(db.session.query(Job.job_name, Job.welfare_list).filter(Job.job_name.op('regexp')('土建工程师')).count()) #19


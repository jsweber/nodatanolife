from datetime import datetime
import os
import sys
SQL_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
basedir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, basedir)
from __init__ import db

class Job(db.Model):
    __tablename__= 'liepin_2018_4'
    __table_args__ = {"useexisting": True}
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

if __name__ == '__main__':
    pass

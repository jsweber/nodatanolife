import os
import sys
basedir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, basedir)
from __init__ import db

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

if __name__ == '__main__':
    pass
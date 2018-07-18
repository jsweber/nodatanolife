import os, sys
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, basedir)
from __init__ import db, login_manager

class User(UserMixin, db.Model):
    __tablename__='user'
    __table_args__ = {"useexisting": True}
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    password_hash = db.Column(db.String(128))
      # password = db.Column(db.String(45))
    telephone = db.Column(db.String(45))
    email = db.Column(db.String(45), unique=True, index=True)
    gender = db.Column(db.Integer, nullable=False)

    @property
    def password(self):
        raise AttributeError('passwd is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.user_id
    
    def __repr__(self):
        return '<User %s>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    pass
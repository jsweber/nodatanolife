import os
import sys
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response, render_template
from flask_script import Manager
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from elasticsearch import Elasticsearch

basedir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
moment = Moment()
db = SQLAlchemy()
es = Elasticsearch()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    sys.path.insert(0,basedir)
    from config import config

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    moment.init_app(app)
    # db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from main import main as main_blueprint
    from auth import auth as auth_blueprint
    from api_1_0 import api as api_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

if __name__ == '__main__':
    print(create_app('development'))
    print(basedir)

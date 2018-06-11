import os
import sys
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response, render_template
from flask_script import Manager
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

basedir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    sys.path.insert(0,basedir)
    from config import config

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from main import main as main_blueprint
    from auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

if __name__ == '__main__':
    print(create_app('development'))
    print(basedir)

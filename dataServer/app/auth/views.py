from flask import render_template

import os, sys
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('what is your name?', validators=[Required()])
    submit = SubmitField('submit')

parentDir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, parentDir)
from auth import auth

@auth.route('/login', methods=['GET'])
def login():
    form = NameForm()
    return render_template('auth/login.html', form=form)


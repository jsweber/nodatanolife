from flask import render_template, session, redirect, flash, url_for, request

import os, sys
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email
from flask_login import login_user

class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[Required()])
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')

parentDir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, parentDir)
from auth import auth
from models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            #equest.args.get('next'): 当用户访问受保护的页面时会跳转到登陆页，当登陆完成后自动跳转回刚才跳转的页面，next就是表示这个页面
            print('login success:')
            print(user)
            print(user.verify_password(form.password.data))
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('invalid username or passwd')

    return render_template('auth/login.html', form=form)


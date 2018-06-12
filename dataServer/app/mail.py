#!/usr/bin/env python
#encoding:utf8

import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response, render_template
# from flask_script import Manager
# from flask_wtf import Form
# from hello import Job, User, db
from flask_mail import Mail, Message
from threading import Thread

app = Flask(__name__)
#csrf cross site request forgery
# app.config['SECRET_KEY'] = 'secret key'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'nodatanolife@qq.com'
app.config['MAIL_PASSWORD'] = 'deyqqpsuocwfdcgh'

def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(subject, recipients=[to])
    # msg.body = render_template(template + '.txt', **kwargs)
    # msg.html = render_template(template + '.html', **kwargs)
    msg.body = '测试内容'
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
    return thr


if __name__ == '__main__':
    send_email('951092973@qq.com', 'test', 'template随便啦' )
    app.run()
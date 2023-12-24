# -*- coding:utf-8 -*-
# @FileName: main.py
# @Time:2023/12/24 22:39
# @Author    :dengzz
import os

from flask import Flask, abort, render_template
from sqlalchemy import MetaData

from common.database import db
import pymysql

pymysql.install_as_MySQLdb()  # 解决python2(MySQLdb中使用的) 的问题 ModuleNotFoundError: No module named 'MySQLd
app = Flask(__name__, template_folder='template', static_url_path='/', static_folder='resource')
app.config['SECRET_KEY'] = os.urandom(24)  # 24位 生成随机数种子  用于产生sessionID

# 使用集成方式处理SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:000000@hadoop102:3306/woniunote?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:000000@hadoop102:3306/woniunote?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 跟踪数据库的修改 及时发送信号给Flask
app.config['SQLALCHEMY_ECHO'] = True  # 跟踪数据库的修改 及时发送信号给Flask
app.config['JSON_AS_ASCII'] = False
# 初始化数据库
db.init_app(app)  # Flask环境跟db绑定了


# 定义404 错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-404.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('error-500.html')


if __name__ == '__main__':
    app.run(debug=True)

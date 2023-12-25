# -*- coding:utf-8 -*-
# @FileName  :users.py
# @Time      :2023/12/25 9:22
# @Author    :dzz
# @Function  :
from main import db
class Users(db.Model):
    __tablename__ = "users"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(32))
    nickname = db.Column(db.String(32))
    avatar = db.Column(db.String(32))
    qq = db.Column(db.String(32))
    role = db.Column(db.String(32))
    credit = db.Column(db.String(32))

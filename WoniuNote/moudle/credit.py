# -*- coding:utf-8 -*-
# @FileName: credit.py.py
# @Time:2024/1/27 7:55
# @Author    :dengzz
import time, random

from flask import session

from main import db


class Credit(db.Model):
    __tablename__ = "credit"
    creditid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    category = db.Column(db.String(32))
    target = db.Column(db.String(32))
    credit = db.Column(db.Integer)
    createtime = db.Column(db.DateTime)
    updatetime = db.Column(db.DateTime)

    # 插入积分明细数据
    def insert_detail(self, type, target, credit):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        credit = Credit(userid=session.get('userid'), category=type, target=target,
                        credit=credit, createtime=now, updatetime=now)
        db.session.add(credit)
        db.session.commit()

    # 判断用户是否已经消耗积分
    def check_payed_article(self, articleid):
        result = db.session.query(Credit).filter_by(userid=session.get('userid'), target=articleid).all()
        if len(result) > 0:
            return True
        else:
            return False

# -*- coding:utf-8 -*-
# @FileName  :article.py
# @Time      :2023/12/25 9:24
# @Author    :dzz
# @Function  :
from main import db
from moudle.users import Users


class Article(db.Model):
    __tablename__ = 'article'
    articleid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    type = db.Column(db.Integer)
    headline = db.Column(db.String(64))
    content = db.Column(db.String(1024))
    thumbnail = db.Column(db.String(64))
    credit = db.Column(db.Integer)
    readcount = db.Column(db.Integer)
    replycount = db.Column(db.Integer)
    recommended = db.Column(db.String(64))
    hidden = db.Column(db.String(64))
    drafted = db.Column(db.String(64))
    checked = db.Column(db.String(64))
    createtime = db.Column(db.DateTime)
    updatetime = db.Column(db.DateTime)

    def find_all(self):
        result = db.session.query(Article).all()

    def find_by_id(self, articleid):
        row = db.session.query(Article).filter_by(articleid=articleid).first()
        return row

    # 指定分页的limit和offset的参数 同时与users表关联查询
    def find_limit_with_user(self, start, count):
        result = db.session.query(Article, Users.nickname)\
            .join(Users, Users.userid == Article.userid)\
            .order_by(Article.articleid.desc())\
            .limit(count)\
            .offset(start)\
            .all()
        return result

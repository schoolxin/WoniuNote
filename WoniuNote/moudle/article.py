# -*- coding:utf-8 -*-
# @FileName  :article.py
# @Time      :2023/12/25 9:24
# @Author    :dzz
# @Function  :
from sqlalchemy import func

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
        result = db.session.query(Article, Users.nickname) \
            .join(Users, Users.userid == Article.userid) \
            .order_by(Article.articleid.desc()) \
            .limit(count) \
            .offset(start) \
            .all()
        return result

    # 统计当前文章的总数量
    def get_total_count(self):
        count = db.session.query(Article).count()
        return count

    # 根据文章类型获取文章
    def find_by_type(self, article_type, start, count):
        result = db.session.query(Article, Users.nickname) \
            .join(Users, Users.userid == Article.userid) \
            .filter(Article.type == article_type) \
            .order_by(Article.articleid.desc()) \
            .limit(count) \
            .offset(start) \
            .all()
        return result

    # 根据文章类型获取总条数
    def get_total_count_by_type(self, article_type):
        count = db.session.query(Article).filter(Article.type == article_type).count()
        return count

    # 根据文章标题进行模糊搜索
    def find_by_headline(self, headline, start, count):
        result = db.session.query(Article, Users.nickname) \
            .join(Users, Users.userid == Article.userid) \
            .filter(Article.headline.like('%' + headline + '%')) \
            .order_by(Article.articleid.desc()) \
            .limit(count) \
            .offset(start) \
            .all()
        return result

    # 统计分页数量
    def get_total_count_by_headline(self, headline):
        count = db.session.query(Article).filter(Article.headline.like('%' + headline + '%')).count()
        return count

    # 获取最新文章
    def find_last_9(self):
        result = db.session.query(Article.headline, Article.articleid) \
            .order_by(Article.articleid.desc()) \
            .limit(9).all()
        return result

    # 获取最多阅读的
    def find_most_9(self):
        result = db.session.query(Article.headline, Article.articleid) \
            .order_by(Article.readcount.desc()) \
            .limit(9).all()
        return result

    # 特别推荐
    def find_recommand_9(self):
        result = db.session.query(Article.headline, Article.articleid) \
            .filter(Article.recommended==1) \
            .order_by(func.rand()) \
            .limit(9).all()
        return result
    # 一次性返回三个推荐
    def find_last_most_recommend(self):
        last = self.find_last_9()
        most = self.find_most_9()
        recommend = self.find_recommand_9()
        return (last,most,recommend)


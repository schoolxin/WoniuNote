# -*- coding:utf-8 -*-
# @FileName  :users.py
# @Time      :2023/12/25 9:22
# @Author    :dzz
# @Function  :
from main import db
from flask import session
import time, random
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
    createtime = db.Column(db.DateTime)
    updatetime = db.Column(db.DateTime)

    # 查询用户名，可用于注册时判断用户名是否已注册，也可用于登录校验
    def find_by_username(self, username):
        result = db.session.query(Users).filter_by(username=username).all()
        return result

    # 实现注册，首次注册时用户只需要输入用户名和密码，所以只需要两个参数
    # 注册时，在模型类中为其他字段尽力生成一些可用的值，虽不全面，但可用
    # 通常用户注册时不建议填写太多资料，影响体验，可待用户后续逐步完善
    def do_register(self, username, password):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        nickname = username.split('@')[0]  # 默认将邮箱账号前缀作为昵称
        avatar = str(random.randint(1, 15))  # 从15张头像图片中随机选择一张
        user = Users(username=username, password=password, role='user', credit=50,
                     nickname=nickname, avatar=avatar + '.png', createtime=now, updatetime=now)
        db.session.add(user)
        db.session.commit()
        return user

    # 修改用户剩余积分，积分为正数表示增加积分，为负数表示减少积分
    def update_credit(self, credit):
        user = db.session.query(Users).filter_by(userid=session.get('userid')).one()
        user.credit = int(user.credit) + credit
        db.session.commit()

    def find_by_userid(self, userid):
        user = db.session.query(Users).filter_by(userid=userid).one()
        return user

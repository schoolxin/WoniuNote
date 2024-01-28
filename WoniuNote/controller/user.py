# -*- coding:utf-8 -*-
# @FileName: user.py
# @Time:2024/1/21 8:11
# @Author    :dengzz
import hashlib

from flask import Blueprint, make_response, session, request
from common.utility import ImageCode, gen_email_code, send_email
import re

from moudle.credit import Credit
from moudle.users import Users

user = Blueprint('user', __name__)


@user.route("/vscode")
def vscode():
    code, bstring = ImageCode().get_code()
    resp = make_response(bstring)
    resp.headers['Content-type'] = 'image/jpeg'
    session['vscode'] = code.lower()
    return resp


@user.route("/ecode", methods=['POST'])
def ecode():
    email = request.form.get('email')
    print(email)
    if not re.match('.+@.+\..+', email):
        return 'email-invalid'
    code = gen_email_code()

    try:
        send_email(email, code)
        session['ecode'] = code  # 将邮箱验证码保存在session中
        return 'send-pass'
    except:
        return 'send-fail'


@user.route("/user", methods=['POST'])
def register():
    user = Users()
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()
    ecode = request.form.get('ecode').strip()
    if ecode != session.get('ecode'):
        return 'ecode-error'
        # 验证邮箱地址的正确性和密码的有效性
    elif not re.match('.+@.+\..+', username) or len(password) < 5:
        return 'up-invalid'

    # 验证用户是否已经注册
    elif len(user.find_by_username(username)) > 0:
        return 'user-repeated'

    else:
        # 实现注册功能
        password = hashlib.md5(password.encode()).hexdigest()
        result = user.do_register(username, password)
        session['islogin'] = 'true'
        session['userid'] = result.userid
        session['username'] = username
        session['nickname'] = result.nickname
        session['role'] = result.role
        # 更新积分详情表
        Credit().insert_detail(type='用户注册',target='0',credit=50)
        return 'reg-pass'
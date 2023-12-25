# -*- coding:utf-8 -*-
# @FileName: index.py
# @Time:2023/12/24 22:48
# @Author    :dengzz
from flask import Blueprint, render_template
from moudle.article import Article

index = Blueprint("index", __name__)


@index.route("/")
def home():
    artile = Article()
    result = artile.find_limit_with_user(0, 10)

    return render_template('index.html', result=result)

# -*- coding:utf-8 -*-
# @FileName: index.py
# @Time:2023/12/24 22:48
# @Author    :dengzz
import math

from flask import Blueprint, render_template
from moudle.article import Article

index = Blueprint("index", __name__)


@index.route("/")
def home():
    artile = Article()
    result = artile.find_limit_with_user(0, 10)
    total = math.ceil(artile.get_total_count() / 10)  # 总页数
    last,most,recommended = artile.find_last_most_recommend()
    return render_template('index.html', result=result, total=total, current_page=1,last=last,most=most,recommended=recommended)


@index.route("/page/<int:page>")
def paginate(page):
    start = (page - 1) * 10
    artile = Article()
    result = artile.find_limit_with_user(start, 10)
    total = math.ceil(artile.get_total_count() / 10)  # 总页数
    return render_template('index.html', result=result, total=total, current_page=page)


@index.route("/type/<int:article_type>-<int:page>")
def classify(article_type, page):
    start = (page - 1) * 10
    artile = Article()
    result = artile.find_by_type(article_type, start, 10)
    total = math.ceil(artile.get_total_count_by_type(article_type) / 10)
    return render_template('type.html', result=result, current_page=page, total=total,type = article_type)


@index.route("/search/<int:page>-<keyword>")
def search(page, keyword):
    start = (page - 1) * 10
    artile = Article()
    result = artile.find_by_headline(keyword,start, 10)
    total = math.ceil(artile.get_total_count_by_headline(keyword) / 10)  # 总页数
    return render_template('search.html', result=result, current_page=page, total=total, headline=keyword)

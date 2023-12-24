# -*- coding:utf-8 -*-
# @FileName: index.py
# @Time:2023/12/24 22:48
# @Author    :dengzz
from flask import Blueprint, render_template

index = Blueprint("index", __name__)


@index.route("/")
def home():
    pass

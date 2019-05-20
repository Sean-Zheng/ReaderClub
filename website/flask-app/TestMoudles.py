# 测试模块

from app import app, auth
from flask import request, jsonify
from Models import *


# 接口测试
@app.route('/test/api')
def test_api():
    return jsonify(message='这个是来自flask的接口测试')


# 登陆测试
@app.route('/test/login', methods=['GET', 'POST'])
@auth.login_required
def test_login():
    return jsonify(message="测试登录成功")


# 初始化数据库
@app.route('/test/init')
def initdatabase():
    db.create_all()
    return 'success'


@app.route('/test/dict')
def dict_test():
    mydict = {}
    mydict['12'] = 12
    mydict['ss'] = 'aa'
    return jsonify(dict=mydict)

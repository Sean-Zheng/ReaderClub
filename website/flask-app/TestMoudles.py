#测试模块

from app import app,auth
from flask import request,jsonify



#登陆测试
@app.route('/test/login',methods=['GET','POST'])
@auth.login_required
def test_login():
    return jsonify(message="测试登录成功")


#初始化数据库
@app.route('/test/init')
def initdatabase():
    db.create_all()
    return 'success'
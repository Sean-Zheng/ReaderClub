#用户模块

from app import app
from flask import request,jsonify
from Models import *

#注册功能
@app.route('/user/register',methods=['POST'])
def register():
    email=request.get_json(force=True).get('email')
    password=request.get_json(force=True).get('password')
    nickname=request.get_json(force=True).get('nickname')
    if email is None or password is None or nickname is None:
        return jsonify(status=111)
    elif User.query.filter_by(Email=email).first() is not None:
        return jsonify(status=113)
    else:
        user=User(Email=email)
        user.encrypt_password(password)
        user.NickName=nickname
        db.session.add(user)
        try:
            db.session.commit()
        except Exception:
            return jsonify(status=114)
        return jsonify(status=112)


#登录功能
@app.route('/user/login',methods=['POST'])
def login():
    account=request.get_json(force=True).get('account')
    password=request.get_json(force=True).get('password')
    if account is None or password is None:
        return jsonify(status=121)
    if '@' in account:#判断是否为邮箱
        user=User.query.filter_by(Email=account).first()
    else:
        user=User.query.filter_by(NickName=account).first()
    if not user:
        return jsonify(status=123)
    if user.verify_password(password):
        token=user.generate_auth_token()
        return jsonify(status=122,token=token,type='Bearer')
    else:
        return jsonify(status=123)

@app.route('/user/nickname')
def nickname_check():
    nick_name=request.get_json(force=True).get('nickname')
    if nick_name is None:
        return jsonify(status=131)
    user=User.query.filter_by(NickName=nick_name).first()
    if user:
        return jsonify(status=132,exist=True)
    else:
        return jsonify(status=132,exist=False)
#用户模块

from app import app
from flask import request,jsonify

#注册功能
@app.route('/user/register',methods=['POST'])
def register():
    email=request.get_json(force=True).get('email')
    password=request.get_json(force=True).get('password')
    if email is None or password is None:
        return jsonify(status=111)
    elif User.query.filter_by(Email=email).first() is not None:
        return jsonify(status=113)
    else:
        user=User(Email=email)
        user.encrypt_password(password)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception:
            return jsonify(status=114)
        return jsonify(status=112)


#登录功能
@app.route('/user/login',methods=['POST'])
def login():
    email=request.get_json(force=True).get('email')
    password=request.get_json(force=True).get('password')
    if email is None or password is None:
        return jsonify(status=121)
    user=User.query.filter_by(Email=email).first()
    if not user:
        return jsonify(status=123)
    if user.verify_password(password):
        token=user.generate_auth_token()
        return jsonify(status=122,token=token,type='Bearer')
    else:
        return jsonify(status=123)
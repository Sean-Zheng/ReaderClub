from Recommend import *
from TestMoudles import *
from CommentMoudles import *
from MarkMoudles import *
from BookShelfMoudles import *
from UserMoudles import *
from flask import Flask, render_template, g
from flask_httpauth import HTTPTokenAuth
from flask_cors import CORS
from Models import *
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

CORS(app, supports_credentials=True)

auth = HTTPTokenAuth()


# 令牌验证
@auth.verify_token
def verify_token(token):
    user = User.verify_auth_token(token)
    # 暂时关闭用户验证令牌
    # user=User.query.filter_by(Email="sean").first()
    if user is None:
        return False
    else:
        g.user = user
        return True


# 令牌验证失败
@auth.error_handler
def error_handler():
    return jsonify(status=0)


# 首页
@app.route('/')
def index():
    # return 'index'
    return render_template('index.html')


@app.route('/index')
def testindex():
    return render_template('test.html')


# 引入视图映射


if __name__ == '__main__':
    app.run(debug=True)

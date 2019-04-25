from flask import Flask,render_template,jsonify,request,g
from flask_httpauth import HTTPTokenAuth
from Models import *
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

auth=HTTPTokenAuth()


#令牌验证
@auth.verify_token
def verify_token(token):
    return User.verify_auth_token(token)


#令牌验证失败
@auth.error_handler
def error_handler():
    return jsonify(status=0)


#跳转到首页index.html
@app.route('/')
def index():
    return 'index'
    # return render_template('index.html')


#注册功能
@app.route('/register',methods=['POST'])
def register():
    email=request.get_json(force=True).get('email')
    password=request.get_json(force=True).get('password')
    if email is None or password is None:
        return jsonify(status=11)
    elif User.query.filter_by(Email=email).first() is not None:
        return jsonify(status=12)
    else:
        user=User(Email=email)
        user.encrypt_password(password)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception:
            return jsonify(status=14)
        return jsonify(status=13)


#登录功能
@app.route('/login',methods=['POST'])
def login():
    email=request.get_json(force=True).get('email')
    password=request.get_json(force=True).get('password')
    if email is None or password is None:
        return jsonify(status=21)
    user=User.query.filter_by(Email=email).first()
    if not user:
        return jsonify(status=22)
    if user.verify_password(password):
        token=user.generate_auth_token()
        return jsonify(status=23,token=token,type='Bearer')
    else:
        return jsonify(status=22)


@app.route('/test/login',methods=['GET','POST'])
@auth.login_required
def test_login():
    return jsonify(status=3)


@app.route('/initdatabase')
def initdatabase():
    db.create_all()
    return 'success'


@app.route('/init')
def init():
    #创建表关联
    db.create_all()
    #添加小说类型表
    # book_type = BookType(TypeName='小说')
    # db.session.add(book_type)
    # # db.session.commit()
    # #添加用户
    # user1 = User(NickName='user1', Email='user1', Password='user1')
    # user2 = User(NickName='user2', Email='user2', Password='user2')
    # user3 = User(NickName='user3', Email='user3', Password='user3')
    # db.session.add(user1)
    # db.session.add(user2)
    # db.session.add(user3)
    # #添加书籍
    # book1 = BookMessage(BookName='book1', BookAuthor='author', BookURL='test')
    # book2 = BookMessage(BookName='book2', BookAuthor='author', BookURL='test')
    # book3 = BookMessage(BookName='book3', BookAuthor='author', BookURL='test')
    # #设置书籍类型
    # book1.type=book_type
    # book2.type=book_type
    # book3.type=book_type
    # #添加用户书架
    # user1.books.append(book1)
    # user1.books.append(book2)
    # user2.books.append(book2)
    # user2.books.append(book3)
    # user3.books.append(book1)
    # user3.books.append(book3)
    # db.session.add(book1)
    # db.session.add(book2)
    # db.session.add(book3)
    # # db.session.commit()

    # mark1=Bookmark(CatalogNumber=1)
    # mark2=Bookmark(CatalogNumber=2)
    # mark3=Bookmark(CatalogNumber=3)
    
    # mark1.book=book1
    # mark2.book=book1
    # mark3.book=book1

    # mark1.user=user1
    # mark2.user=user1
    # mark3.user=user1
    # db.session.add(mark1)
    # db.session.add(mark2)
    # db.session.add(mark3)

    # #提交更改
    # db.session.commit()

    return 'index html'


#测试数据库
@app.route('/test')
def test():
    user=User.query.filter_by(NickName='user1').first()
    books=user.books
    for item in books:
        print('{}:{}'.format(item.BookID,item.BookName))
        pass
    marks=user.marks
    for item in marks:
        print('{}:{}:{}'.format(item.UserID,item.BookID,item.CatalogNumber))
        pass
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
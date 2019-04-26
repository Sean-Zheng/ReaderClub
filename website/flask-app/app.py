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
    user=User.verify_auth_token(token)
    if user is None:
        return False
    else:
        g.user=user
        return True


#令牌验证失败
@auth.error_handler
def error_handler():
    return jsonify(status=0)



#跳转到首页index.html
@app.route('/')
def index():
    return 'index'
    # return render_template('index.html')


#用户模块


#注册功能
@app.route('/register',methods=['POST'])
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
@app.route('/login',methods=['POST'])
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


#用户书架模块

#添加到书架
@app.route('/book/add',methods=['POST'])
@auth.login_required
def book_add():
    book_name=request.get_json(force=True).get('name')
    book_author=request.get_json(force=True).get('author')
    book_description=request.get_json(force=True).get('description')
    book_url=request.get_json(force=True).get('source_url')
    type_name=request.get_json(force=True).get('book_type')
    if book_name is None or book_author is None or book_description is None or book_url is None or  type_name is None:
        return jsonify(status=211)
    #判断书籍是否存在
    book_message=BookMessage.get_book(book_name,book_author)
    if book_message is None:#如果不存在
        #检查书籍类型是否存在
        book_type=BookType.get_type(type_name)
        if book_type is None:#该类型不存在
            book_type=BookType(TypeName=type_name)
            db.session.add(book_type)
        book_message=BookMessage(book_name,book_author,book_description,book_url)
        book_message.type=book_type
        db.session.add(book_message)
        pass
    g.user.books.append(book_message)
    db.session.commit()
    return jsonify(status=212)



@app.route('/book/remove',methods=['POST'])
@auth.login_required
def book_remove():
    book_name=request.get_json(force=True).get('name')
    book_author=request.get_json(force=True).get('author')
    if book_name is None or book_author is None:
        return jsonify(status=221)
    book_message=BookMessage.get_book(book_name,book_author)
    if book_message is None:
        return jsonify(status=223)
    g.user.books.remove(book_message)
    db.session.commit()
    return jsonify(status=222)
    

@app.route('/book/list')
@auth.login_required
def book_list():
    books=g.user.books
    book_list=[]
    for book_item in books:
        result_item={}
        result_item['name']=book_item.BookName
        result_item['author']=book_item.BookAuthor
        result_item['description']=book_item.BookDescription
        result_item['source_url']=book_item.BookURL
        result_item['book_type']=book_item.type.TypeName
        book_list.append(result_item)
        pass
    return jsonify(status=232,list=book_list)
#测试模块


@app.route('/test/login',methods=['GET','POST'])
@auth.login_required
def test_login():
    return jsonify(status=3)


@app.route('/type/test')
def type_test():
    type_list=BookType.query.all()
    for item in type_list:
        print("{} : {}".format(item.TypeID,item.TypeName))
        pass
    return 'ok'

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

@app.route('/api/json')
def json_test():
    return ''

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
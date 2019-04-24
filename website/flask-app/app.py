from flask import Flask
from Models import *
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    #创建表关联
    db.create_all()
    #添加小说类型表
    book_type = BookType(TypeName='小说')
    db.session.add(book_type)
    # db.session.commit()
    #添加用户
    user1 = User(NickName='user1', Email='user1', Password='user1')
    user2 = User(NickName='user2', Email='user2', Password='user2')
    user3 = User(NickName='user3', Email='user3', Password='user3')
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    #添加书籍
    book1 = BookMessage(BookName='book1', BookAuthor='author', BookURL='test')
    book2 = BookMessage(BookName='book2', BookAuthor='author', BookURL='test')
    book3 = BookMessage(BookName='book3', BookAuthor='author', BookURL='test')
    #设置书籍类型
    book1.type=book_type
    book2.type=book_type
    book3.type=book_type
    #添加用户书架
    user1.books.append(book1)
    user1.books.append(book2)
    user2.books.append(book2)
    user2.books.append(book3)
    user3.books.append(book1)
    user3.books.append(book3)
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    # db.session.commit()

    mark1=Bookmark(CatalogNumber=1)
    mark2=Bookmark(CatalogNumber=2)
    mark3=Bookmark(CatalogNumber=3)
    
    mark1.book=book1
    mark2.book=book1
    mark3.book=book1

    mark1.user=user1
    mark2.user=user1
    mark3.user=user1
    db.session.add(mark1)
    db.session.add(mark2)
    db.session.add(mark3)

    #提交更改
    db.session.commit()

    return 'index html'

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
    app.run()
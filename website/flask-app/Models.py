from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from passlib.apps import custom_app_context
from config import SECRET_KEY
from itsdangerous import TimedJSONWebSignatureSerializer,BadSignature,SignatureExpired
from datetime import datetime
db = SQLAlchemy()


#书籍-用户关联表
Bookshelf = db.Table('Bookshelves',
                     db.Column('UserID', db.Integer, db.ForeignKey('Users.UserID'), primary_key=True),
                     db.Column('BookID', db.Integer, db.ForeignKey('BookMessages.BookID'), primary_key=True)
                     )


#书籍类型表
class BookType(db.Model):
    __tablename__ = 'BookTypes'
    TypeID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    TypeName = db.Column(db.String(20), nullable=False)
    # 一对多关系定义
    type_of_books=db.relationship("BookMessage",backref='type')

    '''
    如果不存在则返回None
    如果存在则返回类型
    '''
    @staticmethod
    def get_type(type_name):
        return BookType.query.filter_by(TypeName=type_name).first()
    pass


#书签表
class Bookmark(db.Model):
    __tablename__='Bookmarks'
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), primary_key=True)
    BookID = db.Column(db.Integer, db.ForeignKey('BookMessages.BookID'), primary_key=True)
    CatalogNumber = db.Column(db.Integer, primary_key=True)
    BookmarkDescription = db.Column(db.String(100), nullable=True)
    pass


#评论表
class BookComment(db.Model):
    __tablename__='BookComments'
    CommentID=db.Column(db.Integer, autoincrement=True, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), nullable=False)
    BookID = db.Column(db.Integer, db.ForeignKey('BookMessages.BookID'), nullable=False)
    CommentTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    Comment = db.Column(db.String(500), nullable=False)
    Score = db.Column(db.Integer, nullable=False)
    pass


#用户表
class User(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    NickName = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(128), nullable=False)
    Avatar = db.Column(db.String(100), nullable=True)
    Signature = db.Column(db.String(200), nullable=True)
    # 多对多关系定义
    books = db.relationship('BookMessage', secondary=Bookshelf, backref=db.backref('users'))
    #一对多关系定义
    marks=db.relationship("Bookmark",backref='user')
    comments=db.relationship("BookComment",backref='user')

    #密码加密
    def encrypt_password(self, password):
        self.Password=custom_app_context.encrypt(password)

    #密码验证
    def verify_password(self, password):
        return custom_app_context.verify(password,self.Password)
    
    #生成令牌，默认令牌有效时间5个小时
    def generate_auth_token(self, expiration=18000):
        ts=TimedJSONWebSignatureSerializer(SECRET_KEY,expires_in=expiration)
        return ts.dumps({'email':self.Email,'password':self.Password}).decode('ascii')
    
    #验证令牌
    @staticmethod
    def verify_auth_token(token):
        ts=TimedJSONWebSignatureSerializer(SECRET_KEY)
        try:
            data=ts.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user=User.query.filter_by(Email=data['email']).first()
        if user is None:#未找到该用户
            return None
        elif data['password']==user.Password:
            return user
        else:
            return None


#书籍表
class BookMessage(db.Model):
    __tablename__ = 'BookMessages'
    BookID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    BookName = db.Column(db.String(50), nullable=False)
    BookAuthor = db.Column(db.String(50), nullable=False)
    BookDescription = db.Column(db.String(500), nullable=True)
    TypeID = db.Column(db.Integer, db.ForeignKey('BookTypes.TypeID'), nullable=False)
    BookURL = db.Column(db.String(100), nullable=False)
    #一对多关系定义
    marks=db.relationship("Bookmark",backref='book')
    comments=db.relationship("BookComment",backref='book')

    def __init__(self,book_name,book_author,book_description,book_url):
        self.BookName=book_name
        self.BookAuthor=book_author
        self.BookDescription=book_description
        self.BookURL=book_url
        

    #判断书籍是否存在
    @staticmethod
    def get_book(book_name,book_author):
        return BookMessage.query.filter_by(BookName=book_name,BookAuthor=book_author).first()
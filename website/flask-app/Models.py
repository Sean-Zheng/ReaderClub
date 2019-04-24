from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


Bookshelf = db.Table('Bookshelves',
                     db.Column('UserID', db.Integer, db.ForeignKey('Users.UserID'), primary_key=True),
                     db.Column('BookID', db.Integer, db.ForeignKey('BookMessages.BookID'), primary_key=True)
                     )


class BookType(db.Model):
    __tablename__ = 'BookTypes'
    TypeID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    TypeName = db.Column(db.String(20), nullable=False)
    # 一对多关系定义
    type_of_books=db.relationship("BookMessage",backref='type')
    pass


class Bookmark(db.Model):
    __tablename__='Bookmarks'
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), primary_key=True)
    BookID = db.Column(db.Integer, db.ForeignKey('BookMessages.BookID'), primary_key=True)
    CatalogNumber = db.Column(db.Integer, primary_key=True)
    BookmarkDescription = db.Column(db.String(100), nullable=True)
    pass


class BookComment(db.Model):
    __tablename__='BookComments'
    CommentID=db.Column(db.Integer, autoincrement=True, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), nullable=False)
    BookID = db.Column(db.Integer, db.ForeignKey('BookMessages.BookID'), nullable=False)
    CommentTime = db.Column(db.DateTime, nullable=False)
    Comment = db.Column(db.String(500), nullable=False)
    Score = db.Column(db.Integer, nullable=False)
    pass


class User(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    NickName = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)
    Avatar = db.Column(db.String(100), nullable=True)
    Signature = db.Column(db.String(200), nullable=True)
    # 多对多关系定义
    books = db.relationship('BookMessage', secondary=Bookshelf, backref=db.backref('users'))
    #一对多关系定义
    marks=db.relationship("Bookmark",backref='user')
    comments=db.relationship("BookComment",backref='user')
    pass


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
    pass

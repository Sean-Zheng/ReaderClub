#用户评论模块

from app import app,auth
from flask import request,jsonify,g
from Models import *

@app.route('/comment/add',methods=['POST'])
@auth.login_required
def comment_add():
    book_name=request.get_json(force=True).get('book_name')
    book_author=request.get_json(force=True).get('book_author')
    comment_text=request.get_json(force=True).get('comment_text')
    score=request.get_json(force=True).get('score')
    if book_id is None or comment_text is None or score is None:
        return jsonify(status=411)
    book_message=BookMessage.get_book(book_name,book_author)
    if book_message is None:
        return jsonify(status=413)
    comment=BookComment()
    comment.Comment=comment_text
    comment.Score=int(score)
    comment.book=book_message
    comment.user=g.user
    db.session.add(comment)
    db.session.commit()
    return jsonify(status=412)

    

@app.route('/comment/remove')
@auth.login_required
def comment_remove():
    id=request.get_json(force=True).get('comment_id')
    if id is None:
        return jsonify(status=421)
    comment=BookComment.query.get(id)
    if comment is None:
        return jsonify(status=423)
    db.session.delete(comment)
    db.session.commit()
    return jsonify(status=422)

#获取该用户的评论
@app.route('/comment/user/list')
@auth.login_required
def comment_user_list():
    comments=g.user.comments
    comment_list=[]
    for comment in comments:
        comment_item={}
        comment_item['comment_id']=comment.CommentID
        comment_item['comment_time']=comment.CommentTime
        comment_item['comment_text']=comment.Comment
        comment_item['comment_score']=comment.Score
        comment_item['book_id']=comment.BookID
        comment_item['book_name']=comment.book.BookName
        comment_item['book_author']=comment.book.BookAuthor
        comment_list.append(comment_item)
    return jsonify(status=422,list=comment_list)





#获取该书的评论
@app.route('/comment/book/list')
@auth.login_required
def comment_book_list():
    book_name=request.get_json(force=True).get('name')
    book_author=request.get_json(force=True).get('author')
    if book_name is None or book_author is None:
        return jsonify(status=431)
    book_message=BookMessage.get_book(book_name,book_author)
    if book_message is None:
        return jsonify(status=433)
    comments=book_message.comments
    comment_list=[]
    for comment in comments:
        comment_item={}
        comment_item['comment_id']=comment.CommentID
        comment_item['comment_time']=comment.CommentTime.strftime('%Y-%m-%d %H:%M:%S')
        comment_item['comment_text']=comment.Comment
        comment_item['comment_score']=comment.Score
        comment_item['user_id']=comment.UserID
        comment_item['user_name']=comment.user.NickName
        comment_item['user_email']=comment.user.Email
        comment_list.append(comment_item)
    return jsonify(status=432,list=comment_list)
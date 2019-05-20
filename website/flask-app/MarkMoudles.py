# 用户书签模块

from app import app, auth
from flask import request, jsonify, g
from Models import *


@app.route('/mark/add')
@auth.login_required
def mark_add():
    catalog_number = request.get_json(force=True).get('catalog_number')
    book_id = request.get_json(force=True).get('book_id')
    description = request.get_json(force=True).get('description')
    if catalog_number is None or book_id is None or description is None:
        return jsonify(status=311)
    book_message = BookMessage.query.get(book_id)
    if book_message is None:
        return jsonify(status=313)
    mark = Bookmark(CatalogNumber=int(catalog_number),
                    BookmarkDescription=description)
    mark.user = g.user
    mark.book = book_message
    db.session.add(mark)
    db.session.commit()
    return jsonify(status=312)

# 删除书签
@app.route('/mark/remove')
@auth.login_required
def mark_remove():
    catalog_number = request.get_json(force=True).get('catalog_number')
    book_id = request.get_json(force=True).get('book_id')
    if catalog_number is None or book_id is None:
        return jsonify(status=321)
    mark = Bookmark.query.filter_by(UserID=int(g.user.UserID), BookID=int(
        book_id), CatalogNumber=int(catalog_number)).first()
    if mark is None:
        return jsonify(status=323)
    db.session.delete(mark)
    db.session.commit()
    return jsonify(status=322)

# 获取书签列表
@app.route('/mark/list')
@auth.login_required
def mark_list():
    marks = g.user.marks
    mark_list = []
    for mark in marks:
        mark_item = {}
        mark_item['user_id'] = mark.UserID
        mark_item['book_id'] = mark.BookID
        mark_item['catalog'] = mark.CatalogNumber
        bs = mark.book
        mark_item['book_name'] = bs.BookName
        mark_list.append(mark_item)
    return jsonify(status=332, list=mark_list)

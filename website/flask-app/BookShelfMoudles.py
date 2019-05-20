# 用户书架模块

from app import app, auth
from flask import request, jsonify, g
from Models import *


# 添加到书架
@app.route('/book/add', methods=['POST'])
@auth.login_required
def book_add():
    book_name = request.get_json(force=True).get('name')
    book_author = request.get_json(force=True).get('author')
    book_description = request.get_json(force=True).get('description')
    book_url = request.get_json(force=True).get('source_url')
    type_name = request.get_json(force=True).get('book_type')
    if book_name is None or book_author is None or book_description is None or book_url is None or type_name is None:
        return jsonify(status=211)
    # 判断书籍是否存在
    book_message = BookMessage.get_book(book_name, book_author)
    if book_message is None:  # 如果不存在
        # 检查书籍类型是否存在
        book_type = BookType.get_type(type_name)
        if book_type is None:  # 该类型不存在
            book_type = BookType(TypeName=type_name)
            db.session.add(book_type)
        book_message = BookMessage(
            book_name, book_author, book_description, book_url)
        book_message.type = book_type
        db.session.add(book_message)
        pass
    g.user.books.append(book_message)
    db.session.commit()
    return jsonify(status=212)


# 从书架移除图书
@app.route('/book/remove', methods=['POST'])
@auth.login_required
def book_remove():
    book_name = request.get_json(force=True).get('name')
    book_author = request.get_json(force=True).get('author')
    if book_name is None or book_author is None:
        return jsonify(status=221)
    book_message = BookMessage.get_book(book_name, book_author)
    if book_message is None:
        return jsonify(status=223)
    g.user.books.remove(book_message)
    db.session.commit()
    return jsonify(status=222)


# 获取用户书架所有书籍
@app.route('/book/list')
@auth.login_required
def book_list():
    books = g.user.books
    book_list = []
    for book_item in books:
        result_item = {}
        result_item['book_id'] = book_item.BookID
        result_item['name'] = book_item.BookName
        result_item['author'] = book_item.BookAuthor
        result_item['description'] = book_item.BookDescription
        result_item['source_url'] = book_item.BookURL
        result_item['book_type'] = book_item.type.TypeName
        book_list.append(result_item)
        pass
    return jsonify(status=232, list=book_list)

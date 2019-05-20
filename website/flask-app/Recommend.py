
from app import app, auth
from flask import request, jsonify, g
from Models import *
from math import sqrt


@app.route('/recommend')
@auth.login_required
def recommend():
    user = g.user
    # 出现的书籍集合
    book_set = set()
    # 用户集合
    user_list = []
    # 用户书籍集合
    g_user_book_set = getUSerBookSet(user)
    # 用户书籍数量
    g_user_len = len(g_user_book_set)
    # 与该用户相关联的用户集合
    user_set = getUserSet(user)
    for user_item_id in user_set:
        user_item = User.query.get(user_item_id)
        # 关联用户书籍集合
        user_item_book_set = getUSerBookSet(user_item)
        # 并集
        book_set = book_set | user_item_book_set
        # 集合数量
        user_item_len = len(user_item_book_set)
        # 交集数量
        intersection_len = len(g_user_book_set & user_item_book_set)
        # 相似度分母
        length = sqrt(g_user_len*user_item_len)
        # 相似度
        similarity_degree = intersection_len/length
        user_item_book_set = user_item_book_set-g_user_book_set
        user_message = UserMessage(
            user_item, user_item_book_set, similarity_degree)
        user_list.append(user_message)
        pass
    # 除去已经存在的书籍
    book_set = book_set-g_user_book_set
    # 初始化结果合集
    book_dict = {}
    for book_item in book_set:
        book_dict[book_item] = 0

    for item in user_list:
        for book_item in item.book_set:
            book_dict[book_item] += item.similarity_degree

    sort_list = sorted(book_dict.items(),
                       key=lambda item: item[1], reverse=True)
    result_list = []
    for index in range(len(sort_list)):
        if index >= 5 or sort_list[index][1] < 0.5:
            break
        result_dict = {}
        result_dict['book_id'] = sort_list[index][0]
        result_dict['similarity_degree'] = sort_list[index][1]
        book_message = BookMessage.get_book_by_id(sort_list[index][0])
        result_dict['book_name'] = book_message.BookName
        result_dict['book_author'] = book_message.BookAuthor
        result_dict['book_description'] = book_message.BookDescription
        result_dict['book_url'] = book_message.BookURL
        result_list.append(result_dict)
    return jsonify(booklist=result_list)


# 返回user集合
def getUserSet(user):
    books = user.books
    user_set = set()
    for book_item in books:
        users = book_item.users
        for user_item in users:
            user_set.add(user_item.UserID)
    user_set.remove(user.UserID)
    return user_set


def getUSerBookSet(user):
    books = user.books
    book_set = set()
    for book_item in books:
        book_set.add(book_item.BookID)
    return book_set


class UserMessage(object):
    # #用户模型类
    # user
    # 用户书籍集合
    book_set = None
    # 相似度
    similarity_degree = 0
    user_id = ''
    user_name = ''

    def __init__(self, user, book_set, similarity_degree):
        self.book_set = book_set
        self.similarity_degree = similarity_degree
        self.user_id = user.UserID
        self.user_name = user.NickName

    def printMessage(self):
        print("{}-{}:{}".format(self.user_id,
                                self.user_name, self.similarity_degree))
        pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchItem(scrapy.Item):
    #封面图片地址
    image_url=scrapy.Field()
    #书籍地址
    source_url=scrapy.Field()
    #书名
    name = scrapy.Field()
    #作者
    author=scrapy.Field()
    #描述
    description=scrapy.Field()
    #书籍类型
    book_type=scrapy.Field()
    #更新时间
    update_time=scrapy.Field()
    #最新章节
    latest_chapters=scrapy.Field()
    pass

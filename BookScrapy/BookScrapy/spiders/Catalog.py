# -*- coding: utf-8 -*-
import scrapy


class CatalogSpider(scrapy.Spider):
    name = 'Catalog'
    allowed_domains = ['www.biquge.com.cn']
    start_urls = ['http://www.biquge.com.cn/']

    def parse(self, response):
        pass

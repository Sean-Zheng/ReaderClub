# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookDetail,CatalogItem

class CatalogSpider(scrapy.Spider):
    name = 'Catalog'
    allowed_domains = ['www.biquge.com.cn']
    start_urls = ['https://www.biquge.com.cn/book/30458/']

    def parse(self, response):
        le=LinkExtractor(restrict_xpaths='//div[@id="list"]/dl/dd')
        catalog_links=le.extract_links(response)
        catalogs=[]
        for link_item in catalog_links:
            item=CatalogItem()
            item['text']=link_item.text
            item['link']=link_item.url
            catalogs.append(item)
            pass
        bd=BookDetail()
        bd['catalogs']=catalogs
        print(bd)
        pass

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
        book_detail=BookDetail()
        book_detail['name']=response.xpath("//div[@id='info']/h1/text()").extract_first()
        book_detail['author']=response.xpath("//div[@id='info']/p[1]/text()").re_first('作    者：(.+)')
        book_detail['status']=response.xpath("//div[@id='info']/p[2]/text()").re_first('状    态：(.+),')
        book_detail['book_type']=response.xpath("//div[@class='con_top']/a[2]/text()").extract_first()
        book_detail['update_time']=response.xpath("//div[@id='info']/p[3]/text()").re_first('最后更新：(.+)')
        book_detail['latest_chapters']=response.xpath("//div[@id='info']/p[4]/a/text()").extract_first()
        book_detail['latest_chapter_url']=response.urljoin(response.xpath("//div[@id='info']/p[4]/a/@href").extract_first())
        book_detail['image_url']=response.xpath("//div[@id='fmimg']/img/@src").extract_first()
        book_detail['description']=response.xpath("string(//div[@id='intro'])").extract_first().strip()
        book_detail['catalogs']=catalogs
        yield book_detail
        pass

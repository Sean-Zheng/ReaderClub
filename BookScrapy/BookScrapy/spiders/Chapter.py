# -*- coding: utf-8 -*-
import scrapy
from ..items import ChapterItem


class ChapterSpider(scrapy.Spider):
    name = 'Chapter'
    allowed_domains = ['www.biquge.com.cn']
    start_urls = ['https://www.biquge.com.cn/book/30458/53580.html']

    def parse(self, response):
        chapter=ChapterItem()
        chapter['title']=response.xpath("//div[@class='bookname']/h1/text()").extract_first()
        previous_link=response.xpath("//div[@class='bookname']/div[1]/a[1]/@href").extract_first()
        next_link=response.xpath("//div[@class='bookname']/div[1]/a[3]/@href").extract_first()
        catalog_link=response.xpath("//div[@class='bookname']/div[2]/a[1]/@href").extract_first()
        chapter['previous_chapter']=response.urljoin(previous_link)
        chapter['next_chapter']=response.urljoin(next_link)
        chapter['catalog_url']=catalog_link
        chapter['content']=response.xpath("//div[@id='content']").extract_first().replace('</div>','').replace('<div id="content">','')
        return chapter

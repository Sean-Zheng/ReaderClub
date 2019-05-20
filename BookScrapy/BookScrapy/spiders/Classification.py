# -*- coding: utf-8 -*-
import scrapy
from ..items import RecommendList, RecommendDetail


class ClassificationSpider(scrapy.Spider):
    name = 'Classification'
    allowed_domains = ['www.biduo.cc']
    start_urls = ['https://www.biduo.cc/book_1_1/']

    def parse(self, response):
        detail = response.xpath('//*[@id="hotcontent"]/div/div')
        result = {}
        detail_list = []
        simple_list = []
        for item in detail:
            rd = RecommendDetail()
            rd['name'] = item.xpath('./dl/dt/a/text()').extract_first()
            rd['link'] = response.urljoin(
                item.xpath('./dl/dt/a/@href').extract_first())
            rd['author'] = item.xpath('./dl/dt/span/text()').extract_first()
            rd['description'] = item.xpath('string(./dl/dd)').extract_first()
            rd['image_url'] = item.xpath('./div[1]/a/img/@src').extract_first()
            detail_list.append(rd)
        simple = response.xpath('//*[@id="newscontent"]/div[2]/ul/li')
        for item in simple:
            rl = RecommendList()
            rl['name'] = item.xpath('./span[1]/a/text()').extract_first()
            rl['author'] = item.xpath('./span[2]/text()').extract_first()
            rl['link'] = response.urljoin(item.xpath(
                './span[1]/a/@href').extract_first())
            simple_list.append(rl)
        result['detail_list'] = detail_list
        result['simple_list'] = simple_list
        yield result
        pass

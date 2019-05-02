# -*- coding: utf-8 -*-
import scrapy
from ..items import RecommendDetail,RecommendList,HomeRecommend

class HomeSpider(scrapy.Spider):
    name = 'Home'
    allowed_domains = ['www.biduo.cc']
    start_urls = ['https://www.biduo.cc/']

    def parse(self, response):
        home=response.xpath('//*[@id="hotcontent"]/div[1]/div')
        result={}
        home_list=[]
        classification_list=[]
        #四个首页推荐
        for item in home:
            rd=RecommendDetail()
            rd['name']=item.xpath('./dl/dt/a/text()').extract_first()
            rd['author']=item.xpath('./dl/dt/span/text()').extract_first()
            rd['link']=response.urljoin(item.xpath('./dl/dt/a/@href').extract_first())
            rd['image_url']=item.xpath('./div[1]/a/img/@src').extract_first()
            rd['description']=item.xpath('./dl/dd/text()').extract_first()
            home_list.append(rd)
        result['home_list']=home_list
        #分类推荐
        classification=response.xpath('//div[@class="content border"]')
        for item in classification:
            hr=HomeRecommend()
            #分类名
            hr['type_name']=item.xpath('./h2/text()').extract_first()
            #第一推荐
            img_url=item.xpath('./div/div[1]/a/img/@src').extract_first()
            name=item.xpath('./div/dl/dt/a/text()').extract_first()
            link=item.xpath('./div/dl/dt/a/@href').extract_first()
            description=item.xpath('./div/dl/dd/text()').extract_first()
            recommend_first={}
            recommend_first['name']=name
            recommend_first['link']=response.urljoin(link)
            recommend_first['image_url']=img_url
            recommend_first['description']=description
            hr['recommend_first']=recommend_first
            #余下推荐
            recommend_list=[]
            for list_item in item.xpath('./ul/li'):
                rl=RecommendList()
                rl['link']=response.urljoin(list_item.xpath('./a/@href').extract_first())
                rl['name']=list_item.xpath('./a/text()').extract_first()
                rl['author']=list_item.xpath('./text()').extract_first().replace('/','')
                recommend_list.append(rl)
            hr['recommend_list']=recommend_list
            classification_list.append(hr)
        result['classification_list']=classification_list
        yield result
        pass

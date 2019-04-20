# -*- coding: utf-8 -*-
import scrapy
from ..items import SearchItem


class SearchSpider(scrapy.Spider):
    name = 'Search'
    allowed_domains = ['www.biquge.com.cn']
    start_urls = ['https://www.biquge.com.cn/search.php?keyword={keyword}'.format(keyword='大道朝天')]
    #当前页数
    current_page=1
    #结果页总数
    page_count=0

    def parse(self, response):
        result_list=response.xpath("//div[@class='result-list']/div")
        if not result_list:
            return
        for item in result_list:
            book_info=SearchItem()
            #封面图片地址
            book_info['image_url']=item.xpath('./div[1]/a/img/@src').extract_first()
            #书籍地址
            book_info['source_url']=item.xpath('./div[1]/a/@href').extract_first()
            #书名
            book_info['name']=item.xpath('./div[2]/h3/a/span/text()').extract_first()
            #描述
            book_info['description']=item.xpath('./div[2]/p/text()').extract_first()
            #作者
            book_info['author']=item.xpath('./div[2]/div/p[1]/span[2]/text()').extract_first().strip()
            #书籍类型
            book_info['book_type']=item.xpath('./div[2]/div/p[2]/span[2]/text()').extract_first().strip()
            #更新时间
            book_info['update_time']=item.xpath('./div[2]/div/p[3]/span[2]/text()').extract_first().strip()
            #最新章节
            book_info['latest_chapters']=item.xpath('./div[2]/div/p[4]/a/text()').extract_first().strip()
            yield book_info
        #获取下一页地址
        next_page=response.xpath("//div[@class='search-result-page']/div/a[@title='下一页']/@href").extract_first()
        #获取结果页数
        self.page_count=int(response.xpath("//div[@class='search-result-page']/div/a[@title='末页']/@href").re_first(r"/search.php\?keyword=.+&page=(\d+)"))
        #判断是否有下一页和末页
        if next_page and self.page_count:
            #判断下一页是否是末页
            if self.current_page<self.page_count:
                self.current_page+=1
                next_url=response.urljoin(next_page)
                yield scrapy.Request(next_url,callback=self.next_page_parse)
        pass


    def next_page_parse(self, response):
        for item in response.xpath("//div[@class='result-list']/div"):
            book_info=SearchItem()
            #封面图片地址
            book_info['image_url']=item.xpath('./div[1]/a/img/@src').extract_first()
            #书籍地址
            book_info['source_url']=item.xpath('./div[1]/a/@href').extract_first()
            #书名
            book_info['name']=item.xpath('./div[2]/h3/a/span/text()').extract_first()
            #描述
            book_info['description']=item.xpath('./div[2]/p/text()').extract_first()
            #作者
            book_info['author']=item.xpath('./div[2]/div/p[1]/span[2]/text()').extract_first().strip()
            #书籍类型
            book_info['book_type']=item.xpath('./div[2]/div/p[2]/span[2]/text()').extract_first().strip()
            #更新时间
            book_info['update_time']=item.xpath('./div[2]/div/p[3]/span[2]/text()').extract_first().strip()
            #最新章节
            book_info['latest_chapters']=item.xpath('./div[2]/div/p[4]/a/text()').extract_first().strip()
            yield book_info
        #获取下一页地址
        next_page=response.xpath("//div[@class='search-result-page']/div/a[@title='下一页']/@href").extract_first()
        if next_page and self.page_count:
            #判断下一页是否是末页
            if self.current_page<self.page_count:
                self.current_page+=1
                next_url=response.urljoin(next_page)
                yield scrapy.Request(next_url,callback=self.next_page_parse)
        pass
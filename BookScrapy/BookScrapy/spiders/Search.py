# -*- coding: utf-8 -*-
import scrapy
from ..items import SearchItem

# https://www.biduo.cc/search.php?keyword=


class SearchSpider(scrapy.Spider):
    name = 'Search'
    allowed_domains = ['www.biduo.cc']
    start_urls = [
        'https://www.biduo.cc/search.php?keyword={keyword}&page=8'.format(keyword='大道')]
    # 当前页数
    current_page = 1
    # 结果页总数
    page_count = 0

    def parse(self, response):
        result_list = response.xpath("//div[@class='result-list']/div")
        if not result_list:
            return
        pages = response.xpath(
            "//div[@class='search-result-page']/div/a[@title='末页']/@href").re_first(r"/search.php\?keyword=.+&page=(\d+)")
        if pages:
            self.page_count = int(pages)
        for item in result_list:
            book_info = SearchItem()
            # 封面图片地址
            book_info['image_url'] = item.xpath(
                './div[1]/a/img/@src').extract_first()
            # 书籍地址
            book_info['source_url'] = item.xpath(
                './div[1]/a/@href').extract_first()
            # 书名
            book_info['name'] = item.xpath(
                './div[2]/h3/a/span/text()').extract_first()
            # 描述
            book_info['description'] = item.xpath(
                './div[2]/p/text()').extract_first()
            # 作者
            book_info['author'] = item.xpath(
                './div[2]/div/p[1]/span[2]/text()').extract_first().strip()
            # 书籍类型
            book_info['book_type'] = item.xpath(
                './div[2]/div/p[2]/span[2]/text()').extract_first().strip()
            # 更新时间
            book_info['update_time'] = item.xpath(
                './div[2]/div/p[3]/span[2]/text()').extract_first().strip()
            # 最新章节
            book_info['latest_chapters'] = item.xpath(
                './div[2]/div/p[4]/a/text()').extract_first().strip()
            book_info['latest_chapter_url'] = item.xpath(
                './div[2]/div/p[4]/a/@href').extract_first().strip()
            book_info['page_count'] = self.page_count
            yield book_info

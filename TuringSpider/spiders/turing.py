# -*- coding: utf-8 -*-
import scrapy


class TuringSpider(scrapy.Spider):
    name = 'turing'
    allowed_domains = ['http://biz.turingos.cn/log/1217']
    start_urls = ['http://http://biz.turingos.cn/log/1217/']

    def parse(self, response):
        pass

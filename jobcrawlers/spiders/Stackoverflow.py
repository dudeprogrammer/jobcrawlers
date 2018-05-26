# -*- coding: utf-8 -*-
import scrapy


class StackoverflowSpider(scrapy.Spider):
    name = 'Stackoverflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/']

    def parse(self, response):
        pass

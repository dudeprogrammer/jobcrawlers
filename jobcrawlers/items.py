# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobcrawlersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    details = scrapy.Field()
    tags = scrapy.Field()

    job_type = scrapy.Field()
    experience = scrapy.Field()
    industry = scrapy.Field()
    role = scrapy.Field()
    company_size = scrapy.Field()
    company_type = scrapy.Field()

    date_scraped = scrapy.Field()

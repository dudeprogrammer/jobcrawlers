# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from jobcrawlers.items import JobcrawlersItem


class StackoverflowSpider(scrapy.Spider):
    """Crawl http://stackoverflow.com for job ads."""

    name = 'stackoverflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/jobs']

    def parse(self, response):
        """Parse http://stackoverflow.com/jobs page extracting job links."""

        job_link_xpath = '//div[contains(@class, "-job") and contains(@class, "-item")]//h2/a/@href'
        job_links = response.xpath(job_link_xpath)
        for link in job_links:
            yield response.follow(link, callback=self.parse_job_page)

        follow_links = response.xpath(
            '//div[contains(@class, "pagination")]//a[contains(@class, "job-link")]/@href')
        for follow_link in follow_links:
            yield response.follow(follow_link, callback=self.parse)

    def parse_job_page(self, response):
        """Parse a specific job page extracting job details.
            :return an item of type JobcrawlersItem
        """
        job_item_loader = ItemLoader(item=JobcrawlersItem(), response=response)
        job_item_loader.add_xpath('link', '//header//h1/a/@href')
        job_item_loader.add_xpath('title', '//header//h1/a/@title')

        about_data_xpath = '//div/span[contains(.,"%s")]/../span[2]/text()'
        job_item_loader.add_xpath('job_type', about_data_xpath % "Job type:")
        job_item_loader.add_xpath('experience', about_data_xpath % "Experience level:")
        job_item_loader.add_xpath('industry', about_data_xpath % "Industry:")
        job_item_loader.add_xpath('role', about_data_xpath % "Role")
        job_item_loader.add_xpath('company_size', about_data_xpath % "Company size:")
        job_item_loader.add_xpath('company_type', about_data_xpath % "Company type:")

        job_item_loader.add_xpath('tags', '//section/h2[contains(., "Technologies")]/../div/a/text()')
        job_item_loader.add_xpath('details', '//h2[contains(., "Job description")]/..//text()')
        job_item_loader.add_value('date_scraped', 'today')

        yield job_item_loader.load_item()

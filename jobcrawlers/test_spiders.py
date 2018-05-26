import json
import unittest
from scrapy.http import Request, TextResponse
from jobcrawlers.spiders.Stackoverflow import StackoverflowSpider


class StackoverflowSpiderTest(unittest.TestCase):
    """Test Stackoverflow spider"""

    def setUp(self):
        self.spider = StackoverflowSpider()

    def test_stackoverflow_job_list_page(self):
        """Test Stackoverflow.parse

            Note that it depends on sample_pages/stackoverflow_job_list.html sample file and
            sample_pages/job_list_res.txt.
        """

        with open('sample_pages/stackoverflow_job_list.html', 'r') as file:
            http_body = file.read()
        url = 'https://stackoverflow.com/jobs'
        request = Request(url=url)
        response = TextResponse(url, body=http_body, request=request, encoding='utf-8')
        items = self.spider.parse(response)
        items = str(list(items))

        with open('sample_pages/job_list_res.txt') as file:
            result = file.read()
        self.assertEqual(items, result)

    def test_stackoverflow_job_page(self):
        """Test Stackoverflow.parse_job_page

            Note that it depends on sample_pages/stackoverflow_job_list.html sample file and
            sample_pages/job_page_res.json.
        """

        with open('sample_pages/stackoverflow_job_page.html', 'r') as file:
            http_body = file.read()
        url = 'https://stackoverflow.com/jobs/172695/mobile-qa-engineer-to-guard-the-quality-of-our-app-annie'
        request = Request(url=url)
        response = TextResponse(url, body=http_body, request=request, encoding='utf-8')
        items = self.spider.parse_job_page(response)
        item = list(items)[0]

        with open('sample_pages/job_page_res.json', 'r') as file:
            data = json.load(file)
        self.assertEqual(data['company_size'], item['company_size'])
        self.assertEqual(data['company_type'], item['company_type'])
        self.assertEqual(data['date_scraped'], item['date_scraped'])
        self.assertEqual(data['experience'], item['experience'])
        self.assertEqual(data['industry'], item['industry'])
        self.assertEqual(data['job_type'], item['job_type'])
        self.assertEqual(data['link'], item['link'])
        self.assertEqual(data['role'], item['role'])
        self.assertEqual(data['tags'], item['tags'])
        self.assertEqual(data['title'], item['title'])

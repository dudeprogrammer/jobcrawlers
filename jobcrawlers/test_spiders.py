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

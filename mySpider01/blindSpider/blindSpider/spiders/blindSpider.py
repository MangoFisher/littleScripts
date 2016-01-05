'''
Created on 2016-1-5

@author: MangoFisher
'''
# -*- coding: utf-8 -*-


import scrapy.spiders.Spider


class BlindSpider(scrapy.spiders.Spider):
    name = "zgd"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
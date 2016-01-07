# -*- coding: utf-8 -*-
'''
Created on 2016-1-5

@author: MangoFisher
'''



import scrapy
from blindSpider.items import *
import logging

class BlindSpider(scrapy.spiders.Spider):
    name = "zgd"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        logging.warning("parse function begined")
        for sel in response.xpath('//ul/li'):
            item = BlindSpiderItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
            
#             print "title:",title
#             print "\n"
#             print "link:",link
#             print "\n"
#             print "desc:",desc
#             print "\n"
        
            
#第二次提交
#第三次提交
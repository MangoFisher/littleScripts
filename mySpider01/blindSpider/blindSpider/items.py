'''
Created on 2016-1-5

@author: MangoFisher
'''
# -*- coding: utf-8 -*-


import scrapy


class BlindSpiderItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    
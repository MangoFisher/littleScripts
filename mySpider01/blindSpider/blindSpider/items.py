# -*- coding: utf-8 -*-
'''
Created on 2016-1-5

@author: MangoFisher
'''



import scrapy


class BlindSpiderItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    
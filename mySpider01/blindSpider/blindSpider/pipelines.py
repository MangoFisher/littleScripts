# -*- coding: utf-8 -*-
'''
Created on 2016-1-5

@author: MangoFisher
'''
import json

class BlindspiderPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
    
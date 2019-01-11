# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaPipeline(object):
    def process_item(self, item, spider):
        sonUrl = item['sonUrl']
        filename = sonUrl[7:-6].replace('/','_')
        filename += ".txt"

        fp = open(item['subFilename']+'/'+filename,'w')
        fp.write(item['content'])
        fp.close()
        return item

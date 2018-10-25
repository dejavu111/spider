# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import os
import scrapy
from scrapy.utils.project import get_project_settings

class DouyuPipeline(ImagesPipeline):
    images_store = get_project_settings().get("IMAGES_STORE")
    def get_media_requests(self,item,info):
        image_link = item['imagelink']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok,x in results if ok]

        os.rename(self.images_store+image_path[0],self.images_store+item['nickname']+".jpg")

        return item



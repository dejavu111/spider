# -*- coding: utf-8 -*-

from items import SinaItem
import scrapy
import os

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domain = ["sina.com.cn"]
    start_urls = ["http://news.sina.com.cn/guide/"]

    def parse(self, response):
        items = []
        parentUrls = response.xpath('//h3[@class="tit02"]//a/@href').extract()
        parentTitles = response.xpath('''//h3[@class="tit02"]//a/text()''').extract()

        subUrls = response.xpath('''//ul[@class="list01"]//li//a/@href''').extract()
        subTitles = response.xpath('''//ul[@class="list01"]//li//a/text()''').extract()

        for i in range(0, len(parentTitles)):
            parentFilename = "./Data/" + parentTitles[i]


            if (not os.path.exists(parentFilename)):
                os.makedirs(parentFilename)

            for j in range(0, len(subUrls)):
                item = SinaItem()

                item['parentTitle'] = parentTitles[i]
                item['parentUrl'] = parentUrls[i]

                if_belong = subUrls[j].startswith(parentUrls[i])

                if if_belong:
                    subFilename = parentFilename + "/" + subTitles[j]

                    if (not os.path.exists(subFilename)):
                        os.makedirs(subFilename)
                    item['subTitle'] = subTitles[j]
                    item['subUrl'] = subUrls[j]
                    item['subFilename'] = subFilename

                    items.append(item)

        for item in items:
            yield scrapy.Request(url = item['subUrl'],meta={'meta_1':item},callback=self.second_parse)

    def second_parse(self,response):
        meta_1 = response.meta['meta_1']

        sonUrls = response.xpath('''//a/@href''').extract()

        items = []

        for i in range(len(sonUrls)):
            if_belong = sonUrls[i].startswith(meta_1['parentUrl']) and sonUrls[i].endswith(".shtml")

            if if_belong:
                item = SinaItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrl'] = meta_1['parentUrl']
                item['subTitle'] = meta_1['subTitle']
                item['subUrl'] = meta_1['subUrl']
                item['subFilename'] = meta_1['subFilename']
                item['sonUrl'] = sonUrls[i]
                items.append(item)


        for item in items:
            yield scrapy.Request(url=item['sonUrl'],meta={'meta_2':item},callback=self.detail_parse)

    def detail_parse(self,response):
        item = response.meta['meta_2']
        content = ''
        head = response.xpath('''//h1/text()''').extract()
        content_list = response.xpath('''//p/text()''').extract()

        for content_item in content_list:
            content += content_item

        item['head'] = head
        item['content'] = content

        yield item

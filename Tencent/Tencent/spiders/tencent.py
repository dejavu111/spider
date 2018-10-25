# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    baseURL = "https://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [baseURL+str(offset)]

    def parse(self, response):
        node_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        for node in node_list:
            # 构建item对象，用来保存数据
            item = TencentItem()
            # 提取每个职位的信息
            item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0]

            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]

            if len(node.xpath("./td[2]/text()")):
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0]
            else:
                item['positionType'] = "NULL"

            item['peopleNumber'] = node.xpath("./td[3]/text()").extract()[0]

            item['workLocation'] = node.xpath("./td[4]/text()").extract()[0]

            item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]

            # yield 的重要性，是返回数据后还能回来接着执行代码
            yield item

        if self.offset < int(response.xpath('//div[@class="pagenav"]/a[last()-1]/text()').extract()[0])*10-10:
        #if self.offset < 2980:
            self.offset += 10
            url = self.baseURL + str(self.offset)
            # 返回给调度器
            yield scrapy.Request(url,callback=self.parse) # 如果响应不一样，写一个新的callback()函数

        # # 第二种写法：直接从response获取需要爬取的连接，并发送请求处理，直到链接全部提取完
        # if len(response.xpath("//a[@class='noactive' and @id='next']")) == 0:
        #     url = response.xpath("//a[@id='next']/@href").extract()[0]
        #     yield scrapy.Request("http://hr.tencent.com/" + url, callback=self.parse)

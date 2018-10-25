# -*- coding: utf-8 -*-
import scrapy

from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬虫名称
    allowed_domains = ['www.itcast.cn'] #爬虫允许的域的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] # 发送的第一个url地址请求 列表 可迭代对象 多个参数的话并发

    # 处理响应文件的方法
    # 下载器下载的每个响应文件都会调用该方法来处理
    # response参数是start_urls拿下来的参数
    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")

        # 用来存储所有的item字段的
        # items = []
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = ItcastItem()
            # .extract() 将xpath对象转换为Unicode字符串
            name = node.xpath('./h3/text()').extract() # 返回一个数组 .表示从当前节点
            title = node.xpath('./h4/text()').extract()
            info = node.xpath('./p/text()').extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # items.append(item)
            # 返回提取到的每个item数据，给管道文件处理，同时还会回来继续执行后面的代码
            yield item
        # return items # 给引擎


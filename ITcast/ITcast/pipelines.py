 # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook # 读取xlsx的库
import json
class ItcastPipeline(object):
    def __init__(self):
        self.f = open("itcast_pipelines.json","wb")
        # 存入Excel
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['name','title','info'])

    def process_item(self, item, spider):
        # item(Item对象)-被爬取的对象
        # spider-爬取该item的spider
        # 这个方法必须实现，每个item pipeline组件都需要调用该方法
        # 这个方法必须返回一个Item对象，被丢弃的item将不会被之后的pipeline组件所处理
        content = json.dumps(dict(item), ensure_ascii=False) + ", \n"
        self.f.write(content.encode("utf-8"))
        line = [item['name'],item['title'],item['info']]
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('.teachers.xlsx')  # 保存xlsx文件
        return item
        #返回给引擎

    def close_spider(self,spider):
        # spider (Spider 对象) – 被关闭的spider
        # 可选实现，当spider被关闭时，这个方法被调用
        # 还有open_sider()方法
        self.f.close()

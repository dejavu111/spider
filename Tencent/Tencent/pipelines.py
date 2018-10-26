# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook # 读取xlsx的库
import json
class TencentPipeline(object):
    def __init__(self):
        self.f = open("tencent.json", "wb")
        # 存入Excel
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['职位名', '职位详情地址', '职位类型','招聘人数','工作地点','发布时间'])

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content.encode("utf-8"))

        line = [item['positionName'], item['positionLink'], item['positionType'],item['peopleNumber'],item['workLocation'],item['publishTime']]
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('.tencent.xlsx')  # 保存xlsx文件
        return item

    def close_spider(self, spider):
        self.f.close()

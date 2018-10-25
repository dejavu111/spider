from lxml import etree

html = etree.parse('hello.html')

print(type(html))

result = html.xpath('//li')

print(result)
print(len(result))
print(type(result))
print(result[0])
print(type(result[0]))
print('--------------------------')
result = html.xpath('//li/@class')
print(result)
print('--------------------------')
result = html.xpath('//li/a[@href="link1.html"]')
print(result)
print('--------------------------')
result = html.xpath('//li/a/span') # 相当于html.xpath('//li//span')
print(result)
print('--------------------------')
result = html.xpath('//li/a//@class')
print(result)
print('--------------------------')
result = html.xpath('//li[last()]/a/@href')
print(result)
print('--------------------------')
result = html.xpath('//li[last()-1]/a')
# text 方法可以获取元素内容
print(result[0].text)
print('--------------------------')
result = html.xpath('//*[@class="bold"]')
# tag方法可以获取标签名
print(result[0].tag)

from lxml import etree
# 读取外部文件hello.html
html = etree.parse('./hello.html')
result = etree.tostring(html,pretty_print=True)
print(result)
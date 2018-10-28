# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html,features="html.parser")

#soup = BeautifulSoup(open('index.html'))

print(soup.prettify())

# 此类用法返回第一个对应标签
print(soup.title) # <title>The Dormouse's story</title>
print(type(soup.title)) # <class 'bs4.element.Tag'>
print(soup.head) # <head><title>The Dormouse's story</title></head>
print(soup.a)

# Tag的两大属性 name   attrs
print(soup.name) # [document]
print(soup.head.name) # head
# 指定标签所有属性
print(soup.p.attrs) # {'class': ['title'], 'name': 'dromouse'}
print(soup.p['class']) # ['title']
print(soup.p.get('class'))

soup.p['class'] = "newClass" # 对属性进行修改

del soup.p['class'] #对属性删除

# 获取标签内部文字
print(soup.p.string) # he Dormouse's story
print(type(soup.p.string)) # <class 'bs4.element.NavigableString'>

# BeautifulSoup 对象表示的是一个文档的内容。
# 大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，
# 我们可以分别获取它的类型，名称，以及属性
print(type(soup.name))
print(soup.attrs)
print(soup.name)

# tag 的 .content 属性可以将tag的子节点以列表的方式输出
print(soup.head.contents) # [<title>The Dormouse's story</title>]
print(soup.head.contents[0])

print(soup.head.children) # <list_iterator object at 0x00000029DEB8D668>
for child in  soup.body.children:
    print(child)

print(soup.find_all('b')) # [<b>The Dormouse's story</b>]

import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b

soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.find_all(text="Elsie")
# [u'Elsie']

soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']

soup.find_all(text=re.compile("Dormouse"))
# [u"The Dormouse's story", u"The Dormouse's story"]

print(soup.select('title'))
#[<title>The Dormouse's story</title>]

print(soup.select('a'))
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.select('b'))
#[<b>The Dormouse's story</b>]

# 通过类名查找 .xxx
print(soup.select('.sister'))
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# 通过id名查找 #xxx
print(soup.select('#link1'))
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

# 组合
print(soup.select('p #link1'))
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

# 子标签
print(soup.select("head > title"))
#[<title>The Dormouse's story</title>]

# 属性查找
print(soup.select('a[class="sister"]'))
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# 获取内容
soup = BeautifulSoup(html, 'lxml')
print(type(soup.select('title')))
print(soup.select('title')[0].get_text())

for title in soup.select('title'):
    print(title.get_text())

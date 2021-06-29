# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/2/12'


from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# 1.返回文档内该标签第一个内容及其内容,type=bs4.element.Tag
# print(bs.p)

# print(bs.p.attrs)  # 2.标签里的所有属性,键值对
# print(bs.p.string)
# print(type(bs.p.string))  # 3.标签的内容,type=bs4.element.NavigableString

# 3.返回整个文档,ypet=bs4.BeautifulSoup
# print(type(bs))
# print(bs.name) # [document]
# print(bs)

# 4.注释,是一个特殊的bs4.element.NavigableString,输出的内容不包含注释符号,type=bs4.element.Comment
# 如果标签内嵌套其他标签,会输出None

# print(bs.a.string)
# print(type(bs.a.string))


# 文档遍历
# print(bs.head.contents)


# 文档的收索
# find_all = bs.find_all("a") # 字符串过滤,获取所有的匹配的标签的内容

# 正则表达式收索
import re

# find_all = bs.find_all(re.compile("a")) # 字符串过滤,根据正则匹配标签,获取内容


# def name_is_exists(tag):
#     return tag.has_attr("name");
# find_all = bs.find_all(name_is_exists) # 根据方法搜索

# find_all = bs.find_all(id="story") # id标签=story的
# find_all = bs.find_all(class_=True)  # 包含class标签的
# find_all = bs.find_all(text=['Lacie', 'Tillie', 'and'])  # 文本筛选
# find_all = bs.find_all(text=re.compile("\d")) # 包含正则表达式的
find_all = bs.find_all(text=re.compile("\d"), limit=1)  # limit

print(find_all)

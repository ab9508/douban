# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/2/12'

import urllib.request
import urllib.parse


# 获取get请求
def httpGet():
    response = urllib.request.urlopen("http://www.baidu.com")
    print(response.read().decode("utf-8"))


# 获取post请求
def httpPost():
    try:
        data = bytes(urllib.parse.urlencode({"hello": "word"}), encoding="utf-8")
        response = urllib.request.urlopen("http://httpbin.org/post", data=data, timeout=3)
        print(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        # 超时处理
        print("time out")


# 处理418:伪装成浏览器
def handler():
    baseurl = "https://movie.douban.com/top250?start=1"
    headers = {
        # 伪装成浏览器
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    data = bytes(urllib.parse.urlencode({"name": "eric"}), encoding="utf-8")
    req = urllib.request.Request(baseurl, data=data, headers=headers, method="GET")
    response = urllib.request.urlopen(req)
    print(response.read().decode("utf-8"))


handler()

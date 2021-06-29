# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/2/12'
# 爬虫，获取豆瓣排行前50的电影

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行sqlite数据库操作


def saveDataDB(dataList):
    print("准备建表")
    connect = sqlite3.connect("movie.db")
    # createtable(connect)
    print("准备插入数据")
    for item in dataList:
        cursor = connect.cursor()
        insert = '''
        insert into movie250 (info_link,pic_link,cname,ename,score,rated,instroduction,info)
        values (?,?,?,?,?,?,?,?)
        '''
        param = (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        cursor.execute(insert, param)
        connect.commit()
        cursor.close()
    connect.close()
    print("插入数据成功")
    pass


def createtable(connect):
    cursor = connect.cursor()
    creatTable = '''
    create table movie250 (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated varchar,
        instroduction text,
        info text
    )
    '''
    cursor.execute(creatTable)
    connect.commit()
    cursor.close()


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    print("准备爬取网页")
    dataList = getData(baseurl)
    # 2.解析数据
    # 3.保存数据
    # savepath = '.\\豆瓣电影Top250.xls'
    # saveData(dataList, savepath)  # 保存数据到excel
    # 保存到sqlite数据库
    saveDataDB(dataList)


# 创建正则表达式对象，表示规则（字符创的模式）,r:忽略所有的特殊符号
findLink = re.compile(r'<a href="(.*?)">')  # 筛选详情
findimg = re.compile(r'<img.*?src="(.*?)"', re.S)  # 筛选图片,re.S:忽略换行符
findTitle = re.compile(r'<span class="title">(.*?)</span>')  # 筛选片名
findRating = re.compile(r'<span class="rating_num".*>(.*)</span>')  # 影片的评分
findJudge = re.compile(r'<span>(\d*人评价)</span>')  # 评价人数
findInq = re.compile(r'<span class="inq">(.*)</span>')  # 概况
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 影片的相关内容


# 爬取网页
def getData(baseurl):
    dataList = []
    # 获取10次,共250条
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        # 获取源码
        html = askUrl(url)
        # 逐一解析
        bs = BeautifulSoup(html, "html.parser")
        soup = bs.find_all("div", class_="item")  # 匹配满足条件的
        for item in soup:
            # print(item)  # 电影的全部信息
            data = []  # 保存一部电影的全部信息
            item = str(item)
            link = re.findall(findLink, item)[0]  # 进一步筛选影片详情的链接
            data.append(link)
            # print("详情: " + link)
            img = re.findall(findimg, item)[0]
            data.append(img)
            # print("图片: " + img)
            titles = re.findall(findTitle, item)
            if titles:
                # for title in titles:
                # print(type(title))
                data.append(titles[0].replace('/', ''))
                data.append(titles[1].replace('/', '') if len(titles) > 1 else '')
            else:
                data.append(" ")
                data.append(" ")
            # print("片名: " + title)
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            # print("评分: " + rating)
            hudge = re.findall(findJudge, item)[0]
            data.append((hudge))
            # print("评价人数: " + num)
            inq = re.findall(findInq, item)
            if inq:
                data.append(inq[0])
            else:
                data.append(" ")
            # print("概况： " + inq)
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', ' ', bd)  # 替换换行符
            bd = re.sub('/', ' ', bd)
            data.append(bd)
            # print("相关内容： " + bd.strip())
            # print("data= " + str(data))
            # print("= 单一结束 =")
            dataList.append(data)
            # break
    # dataList = dataList + [html] # 源码拼接
    return dataList


# 保存数据到excel
def saveData(dataList, savepath):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('豆瓣Top250', cell_overwrite_ok=True)
    col = ('链接', '图片链接', '中文名', '英文名', '评分', '评分数', '概况', '相关信息')
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])
    for i in range(0, len(dataList)):
        # print("第%d条" % (i))
        data = dataList[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    workbook.save(savepath)
    pass


# 保存到数据库

# 得到指定一个url的网页内容
def askUrl(baseurl):
    headers = {
        # 伪装成浏览器
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    request = urllib.request.Request(baseurl, headers=headers, method="GET")
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
        return html
    except urllib.error.URLError as e:
        if headers(e, "code"):
            print(e.code)
        if headers(e, "reason"):
            print(e.reason)


if __name__ == '__main__':
    # main()
    askUrl("https://movie.douban.com/top250?start=")
    print("ok")




    # list = []
    # list.append("/ The Shawshank".replace("/", ""))
    # for item in list:
    # print(list)
# list.append(2)
# list.append(1)
# list.insert(2)
# list.insert(1)
# print(list)

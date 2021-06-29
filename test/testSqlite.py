# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/2/13'

import sqlite3


conn = sqlite3.connect("test.db")  # 打开或创建数据库
print("open ok")
# 获取游标
cursor = conn.cursor()

# sql = '''
# create table company(
# id int primary key not null,
# name test not null,
# age int not null,
# address text not null,
# salary real
# );
# '''
# 执行sql语句
# cursor.execute(sql)
# 提交
# conn.commit()
print("建表成功")

# # 插入数据
# sql = '''
# insert into company (id,address,age,name,salary)
#     values (2,'上海','25','ab',800)
# '''
# cursor.execute(sql)
# conn.commit()

# 查找
sel = 'select * from company'
cursor.execute(sel)
fetchall = cursor.fetchall()
for item in fetchall:
    print(item)

print("ok")



# 关流
cursor.close()
conn.close()
# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/2/13'

import xlwt

workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook
sheet = workbook.add_sheet('1')  # 创建sheetl
# sheet.write(0, 0, 'hello')  # 写入数据
# for i, j in zip(range(0, 10), range(0, 10)):

#     print("i= " + str(i) + ' j= ' + str(j))
for i in range(1, 10):
    for j in range(1, i + 1):
        # sheet.write(i - 1, j - 1, (str(i) + ' * ' + str(j) + " = " + str(1 * j)))
        sheet.write(i - 1, j - 1, '%d * %d = %d' % (i, j, i * j))
workbook.save('test.xls')  # 保存

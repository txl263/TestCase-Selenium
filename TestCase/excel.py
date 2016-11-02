# -*- coding: utf-8 -*-
# 读取excel数据
# 
import xlrd
import xlwt
import xlsxwriter
data = xlrd.open_workbook('growing.xlsx') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
for i in range(nrows): # 循环逐行打印
	print table.row_values(i)[0:2] # 取前十三列

workbook = xlsxwriter.Workbook("new.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Hello world')
worksheet.insert_image('C3', 'capture/verify.png',{'x_scale':0.2, 'y_scale':0.2})
worksheet.set_row(2, 40)
worksheet.set_column('C:D', 20)
workbook.close()
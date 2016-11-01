# -*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import unicode_literals
import xlsxwriter as wx
import xlrd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os, sys
from sys import stdin, stdout
import password

xlsx1 = xlrd.open_workbook('growing.xlsx')		# 打开xls文件
table = xlsx1.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
workbook = wx.Workbook('growing_new.xlsx')				# 创建名为filename.xlsx的.xlsx文件，注意，这个库每次打开的文件都会被清空内容

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.baseUrl = "http://m.wukonglicai.com/"
driver.get(driver.baseUrl + "weixin/specialSale/index.html")
driver.set_window_size(450, 800)
driver.find_element_by_id("bt").click()
driver.find_element_by_xpath("//div[a/div/p/span/b[text()='21']]/div/a/p").click()   #点击马上加入
driver.find_element_by_id("mobile").send_keys(password.mobile)
driver.find_element_by_class_name("login_btn").click()
driver.find_element_by_id("password").send_keys(password.password)
driver.find_element_by_class_name("login_btn").click()

worksheet1 = workbook.add_worksheet()				# 创建worksheet，括号里可传worksheet的名字，如workbook.add_worksheet('abc')
for i in range(nrows): # 循环逐行打印
	# if i == 0: # 跳过第一行
	# 	continue
	print table.row_values(i)[0:2] # 取前十三列
	col1value = table.row_values(i)[0]
	col2value = table.row_values(i)[1]
	col3value = table.row_values(i)[2]
	coloum1 = "A" + str(i)	# 在excel文件的$A$1位置写入数字123
	worksheet1.write(coloum1, col1value)
	coloum2 = "B" + str(i)
	worksheet1.write(coloum2,col2value)
	coloum3 = "C" + str(i)
	worksheet1.write(coloum3,col3value)
	driver.get(driver.baseUrl + col2value)
	picname = "capture/" + str(i) + ".jpeg"
	driver.get_screenshot_as_file(picname)
	coloum4 = "D" + str(i)
	worksheet1.insert_image(coloum4, picname, {'x_offset':0.1, 'y_offset':0.1})
	worksheet1.set_row(i, 40)    #设置第1行单元格高度为40像素，且引用加粗
workbook.close()

def read_excel():
# 打开文件
	workbook = xlrd.open_workbook(r'TestCase_Login.xlsx')
	# 获取所有sheet
	print workbook.sheet_names() # [u'sheet1', u'sheet2']
	sheet1_name = workbook.sheet_names()[1]
	# 根据sheet索引或者名称获取sheet内容
	sheet1 = workbook.sheet_by_index(1) # sheet索引从0开始
	sheet1 = workbook.sheet_by_name('Test Case 1')
	 
	# sheet的名称，行数，列数
	print sheet1.name,sheet1.nrows,sheet1.ncols
	
	# 获取整行和整列的值（数组）
	rows = sheet1.row_values(3) # 获取第四行内容
	cols = sheet1.col_values(2) # 获取第三列内容
	print rows
	print cols
	 
	# 获取单元格内容
	print sheet1.cell(1,0).value.encode('utf-8')
	print sheet1.cell_value(1,0).encode('utf-8')
	print sheet1.row(1)[0].value.encode('utf-8')
		 
	# 获取单元格内容的数据类型
	print sheet1.cell(1,0).ctype
 

if __name__=="__main__":
    read_excel() #执行用例#
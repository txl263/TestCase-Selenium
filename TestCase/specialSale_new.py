#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by Sublime.
# User: Eric
# Date：2016年10月10日10:56:39
# Module：新手专享·限1笔
#coding=utf-8
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import xml.etree.ElementTree as ET
import password
tree = ET.parse('specialSale_1.xml')
root = tree.getroot()
#for child_of_root in root:
    #print child_of_root.tag, child_of_root.attrib
#setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL的访问放到初始化部分。#
class Wukong(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.baseUrl = "http://m.wukonglicai.com"
        self.verificationErrors=[]  #脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert=True  #是否继续接受下一个警告#

    def test_specialSale_new(self):
        driver = self.driver
        driver.get(self.baseUrl + "/weixin/specialSale/index.html")
        driver.set_window_size(450, 800)  #调整窗口大小
        driver.get_screenshot_as_file("capture/1_1.png")   #截图
        driver.find_element_by_id("bt").click()    #点击马上
        time.sleep(1)
        driver.get_screenshot_as_file("capture/1_2.png")   #截图
        tree = ET.parse('New_TFB-20160823.XML')
        root = tree.getroot()
        
        driver.execute_script("window.scrollTo(0, 500);")      #滚动到底部
        time.sleep(1)    
        driver.get_screenshot_as_file("capture/1_3.png")   #截图
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")      #滚动到底部
        time.sleep(1)    
        driver.get_screenshot_as_file("capture/1_4.png")   #截图


        list = driver.find_elements_by_xpath("//div[a/div/p/span/b[text()='21']]")
        product_Name = (driver.find_element_by_xpath("//div[a/div/p/span/b[text()='21']]/a/div[1]/p/span[1]").text)
        product_Number = (driver.find_element_by_xpath("//div[a/div/p/span/b[text()='21']]/a/div[1]/p/span[2]").text)
        product_Profit = (driver.find_element_by_xpath("//div[a/div/p/span/b[text()='21']]/a/div[3]/p").text)
        product_Hold_day = (driver.find_element_by_xpath("//div[a/div/p/span/b[text()='21']]/a/div[4]/p[1]/span").text)
        product_Min_invest = (driver.find_element_by_xpath("//div[a/div/p/span/b[text()='21']]/a/div[4]/p[2]/span").text)
        product_Max_invest = (driver.find_element_by_xpath("//div[a/div/p/span/b[text()='21']]/a/div[4]/p[3]/span").text)
        # product_Jion

        self.assertEqual (product_Name, "新手专享·限1笔")
        self.assertEqual (product_Profit, "15.0%")
        self.assertEqual (product_Hold_day, "封闭期21天")
        self.assertEqual (product_Min_invest, "100元起投")
        self.assertEqual (product_Max_invest, "限购5万元")
        driver.find_element_by_xpath("//div[a/div/p/span/b[text()='21']]/div/a/p").click()   #点击马上加入
        time.sleep(1)
        driver.get_screenshot_as_file("capture/2_1.png")   #截图
        # driver.find_element_by_link_text("马上加入").click()
        print  driver.current_url
        driver.find_element_by_id("mobile").send_keys(password.mobile)
        driver.get_screenshot_as_file("capture/2_2.png")   #截图
        driver.find_element_by_class_name("login_btn").click()
        time.sleep(1)
        driver.get_screenshot_as_file("capture/3_1.png")   #截图
        time.sleep(1)
        driver.find_element_by_id("password").send_keys(password.password)
        driver.get_screenshot_as_file("capture/3_2.png")   #截图
        driver.find_element_by_class_name("login_btn").click()
        driver.get_screenshot_as_file("capture/4_1.png")



        # print product_Name
        # print product_Profit
        # print product_Hold_day
        # print product_Min_invest
        # # print product_Max_invest
        # for lists in list:
        #     print lists.text

        #parent = driver.find_element_by_xpath("//span[text()='封闭期21天']parent::section")
        #print (parent)
        #print (driver.find_element_by_xpath("//span[text()='封闭期21天']/parent::section/parent::section/parent::section)").text)
        time.sleep(2)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([],self.verificationErrors)
        '''
        tearDown 方法在每个测试方法执行后调用，这个地方做所有清理工作，如退出浏览器等。 
        self.assertEqual([], self.verificationErrors) 是个难点，
        对前面verificationErrors方法获得的列表进行比较；如查verificationErrors的列表不为空，输出列表中的报错信息。'''
if __name__=="__main__":
    unittest.main() #执行用例#
#suite = unittest.TestLoader().loadTestsFromTestCase(Wukong)
#unittest.TextTestRunner(verbosity=2).run(suite)
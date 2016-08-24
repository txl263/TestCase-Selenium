#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys     
#from selenium.webdriver.common.keys import Keys#
from selenium.webdriver.support import select
#from selenium.webdriver.support.ui import Select#
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re
#setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL的访问放到初始化部分。#
class Wukong(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.implicitly_wait(30)
        self.baseUrl = "http://test3.wukonglicai.com/"
        self.verificationErrors=[]  #脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert=True  #是否继续接受下一个警告#
    def specialSale_obj_pro():
        driver = self.driver
        driver.get(self.base_url + "/weixin/specialSale/index.html")
        driver.find_element_by_xpath("html/body/div[1]/div[1]/a/div[1]/p/span[1]").send_keys("13011898794")
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
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
    unittest.main() #执行用例#
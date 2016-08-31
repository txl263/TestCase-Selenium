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
import xml.etree.ElementTree as ET
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

    def test_specialSale_obj_pro(self):
        driver = self.driver
        driver.get(self.baseUrl + "/weixin/specialSale/index.html")
        driver.set_window_size(450, 800)
        driver.find_element_by_id("bt").click()
        print (driver.find_element_by_xpath("html/body/div[1]/div[1]/a/div[4]/p[2]/span").text)
        for i in range(0,len(root)):
        	if root[i][0].text == "XPath":
        		self.assertEqual(driver.find_element_by_xpath(root[i][1].text).text , root[i][2].text)
        		#self.assertTrue(driver.find_element_by_xpath(root[i][1].text).text == root[i][2].text)
        #driver.get_screenshot_as_file("test.png")
        #driver.save_screenshot("shot.png")
        driver.find_element_by_xpath("html/body/div[1]/div[1]").click() #第一个产品
        
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
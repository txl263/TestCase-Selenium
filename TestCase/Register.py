#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by Sublime.
# User: Eric
# Date：2016年10月11日23:53:36
# Module：Login
from __future__ import unicode_literals
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import password
import pytesseract
from PIL import Image
class WukongRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.baseUrl = "http://m.wukonglicai.com"
        self.verificationErrors=[]  #脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert=True  #是否继续接受下一个警告#

    def test_login(self):
        driver = self.driver
        driver.get(self.baseUrl + "/weixin/specialSale/index.html")
        driver.set_window_size(450, 800)
        driver.find_element_by_id("bt").click()
        driver.find_element_by_link_text("马上加入").click()
        time.sleep(1)
        # cookie = driver.get_cookie('utoken')
        # print cookie
        time.sleep(1)
        driver.find_element_by_id("mobile").send_keys("13711111114")
        driver.find_element_by_class_name("login_btn").click()
        #跳转到验证码输入页
        time.sleep(2)
        driver.get_screenshot_as_file("capture/verify.png")   #截图
        im =Image.open('capture/verify.png')
        box = (330,25,429,80)
        region = im.crop(box)
        region.save("capture/verify_1.png")
        image = Image.open("capture/verify_1.png")
        vcode = pytesseract.image_to_string(image)
        #验证码识别
        print (vcode)
        # time.sleep(2)
        vcode = re.sub("\D","",vcode)
        if not vcode.strip():
            print ("vcode为空")
            driver.find_element_by_class_name("login_btn").click()
        else:
            print (vcode)
            driver.find_element_by_id("captcha").send_keys(vcode)
            driver.find_element_by_class_name("login_btn").click()
        # time.sleep(1)
        i = 1
        try:
            while driver.find_element_by_xpath(".//*[@id='bto']"):
                i = i+1
                vcode = ""
                print ("进入循环")
                driver.find_element_by_xpath(".//*[@id='bto']").click()
                print ("点击确定")
                driver.find_element_by_xpath(".//*[@id='login_do']/img").click()
                print ("点击图片刷新验证码")
                time.sleep(0.1)
                driver.get_screenshot_as_file("capture/verify.png")   #截图
                im =Image.open('capture/verify.png')
                box = (330,25,429,80) 
                region = im.crop(box)
                region.save("capture/verify_1.png")
                image = Image.open("capture/verify_1.png")
                vcode = pytesseract.image_to_string(image)
                print (vcode)
                vcode = re.sub("\D","",vcode)
                print (vcode)
                # time.sleep(2)
                driver.find_element_by_id("captcha").clear()
                driver.find_element_by_id("captcha").send_keys(vcode)
                time.sleep(0.5)
                driver.find_element_by_class_name("login_btn").click()
                time.sleep(0.5)
        except Exception, e:
            errMessage = str(i) + "次通过验证码" 
            print errMessage
        else:
            pass

        time.sleep(2)
        print ("还能继续吗")

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
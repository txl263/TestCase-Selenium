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
import os, sys
from sys import stdin, stdout
from SSDB import SSDB
try:
    pass
    ssdb = SSDB('192.168.45.35', 8888)
except Exception , e:
    pass
    print e
    sys.exit(0)
from PIL import Image
mobile = 13520692413
class WukongRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.baseUrl = "http://test3.wukonglicai.com"
        self.verificationErrors=[]  #脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert=True  #是否继续接受下一个警告#

    def test_login(self):
        driver = self.driver
        driver.get(self.baseUrl + "/weixin/specialSale/index.html")
        # driver.set_window_size(450, 800)
        driver.set_window_size(400, 650)    #针对
        driver.find_element_by_id("bt").click()
        driver.find_element_by_link_text("马上加入").click()
        time.sleep(1)
        # cookie = driver.get_cookie('utoken')
        # print cookie
        time.sleep(1)
        driver.find_element_by_id("mobile").send_keys(str(mobile))
        driver.find_element_by_class_name("login_btn").click()
        #跳转到验证码输入页
        time.sleep(2)
        driver.get_screenshot_as_file("capture/verify.png")   #截图
        im =Image.open('capture/verify.png')
        # box = (330,25,429,80)
        box = (264,25,360,74)
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
                print "第" + str(i) + "次"
                print ("进入循环")
                driver.find_element_by_xpath(".//*[@id='bto']").click()
                print ("点击确定")
                driver.find_element_by_xpath(".//*[@id='login_do']/img").click()
                print ("点击图片刷新验证码")
                time.sleep(0.1)
                driver.get_screenshot_as_file("capture/verify.png")   #截图
                im =Image.open('capture/verify.png')
                region = im.crop(box)
                region.save("capture/verify_1.png")
                image = Image.open("capture/verify_1.png")
                vcode = pytesseract.image_to_string(image,config='-psm 40')  #图形转化为文字
                print (vcode)
                vcode = re.sub("\D","",vcode)   #去除数字意外的其它字符
                print (vcode)
                # time.sleep(2)
                driver.find_element_by_id("captcha").clear()    #清空验证码
                driver.find_element_by_id("captcha").send_keys(vcode)   #填写验证码
                time.sleep(0.5)
                driver.find_element_by_class_name("login_btn").click()  #提交验证码
                time.sleep(0.5)
        except Exception, e:
            errMessage = str(i) + "次通过验证码" 
            print errMessage
        else:
            pass

        time.sleep(2)
        print ("还能继续吗")
        vmobile = "V" + str(mobile)
        time.sleep(3)
        vcaptcha = str(ssdb.request('get', [vmobile]))[-4:]   #从SSDB获取验证码
        print (str(vcaptcha))
        driver.find_element_by_id("captcha").send_keys(vcaptcha)    #填写验证码
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("passwordCheck").send_keys("111111")
        driver.find_element_by_id("inviteCode").send_keys("666666") #填写邀请码
        driver.find_element_by_id("regButton").click()


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
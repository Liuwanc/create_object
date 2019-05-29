# coding=utf8

import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import os
from time import sleep

class AddStudent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/admin.php')


    def tearDown(self):
        sleep(2)
        self.driver.quit()


    def test1_add_student(self):
        '''添加学生测试'''
        # 输入账号
        driver = self.driver
        driver.find_element_by_id("username").send_keys("admin")
        # 输入密码
        driver.find_element_by_name("password").send_keys("admin")
        # 点击登录按钮
        driver.find_element_by_xpath("//*[@id='loginFrm']/input").click()
        # 点击会员标题
        driver.find_element_by_link_text('会员中心').click()
        # 内嵌框架表单切换
        driver.switch_to.frame('mainframe')
        # 点击添加学生
        driver.find_element_by_xpath("//span[.='添加学生']").click()
        sleep(2)
        # 输入用户账号
        driver.find_element_by_name("username").send_keys("13000000000")
        # 输入昵称
        driver.find_element_by_id("realname").send_keys("添加学生自动化测试")
        #输入密码
        driver.find_element_by_xpath("//*[@id='password']").send_keys("22222222")
        sleep(3)
        # 勾选性别：
        driver.find_element_by_xpath("//*[@id='form']/div/div[4]/div/label[1]/input").click()
        #选择角色
        a1 =driver.find_element_by_css_selector("select[name='roleid']")
        Select(a1).select_by_visible_text('大众会员')
        sleep(3)
        #上传头像
        driver.find_element_by_xpath("//span[text()='上传头像']").click()
        driver.find_element_by_xpath("//li[text()='本地上传']").click()
        driver.find_element_by_css_selector("input[name='imgFile']").send_keys('D:/AutoItV3/123.jpg')
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/span[1]/input").click()
        sleep(2)
        #选择机构
        b1 = driver.find_element_by_id("oneCategory")
        Select(b1).select_by_visible_text('郑州大学')
        sleep(2)
        #填写邮箱
        driver.find_element_by_name("email").send_keys("12345@qq.com")
        #填写手机号码
        driver.find_element_by_name("phone").send_keys("13000000000")
        #地址选择
        c1 = driver.find_element_by_name("location_p")
        Select(c1).select_by_visible_text('四川省')
        sleep(3)
        d1 = driver.find_element_by_name("location_c")
        Select(d1).select_by_visible_text('南充市')
        e1 = driver.find_element_by_name("location_a")
        Select(e1).select_by_visible_text('顺庆区')

        sleep(3)
        #点击确认保存
        driver.find_element_by_link_text("确认保存").click()

        sleep(5)
        # 点击确认/消息提示框
        driver.switch_to_alert().accept()
        # 点击取消
        # self.driver.switch_to.alert().dismiss()
        sleep(5)

        driver.find_element_by_link_text("返回列表").click()
        qw=driver.find_element_by_xpath('//*[@id="recordList"]/tr[1]/td[2]/div/a').text
        if qw == '13000000000':
            print(qw)
            print("添加学生成功")

        # ele = driver.find_element_by_xpath("//*[@id='header']/p/a[3]")
        # driver.execute_script('arguments[0].click()', ele)

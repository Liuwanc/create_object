from selenium import webdriver
from selenium.webdriver.support.select import Select
import os
from time import sleep
import  time

# 创建driver对象
def create_driver():
    driver = webdriver.Chrome()
    return driver

def open_url(driver):
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://127.0.0.1/admin.php')

def login(driver):
    driver.find_element_by_id("username").send_keys("admin")
    # 输入密码
    driver.find_element_by_name("password").send_keys("admin")
    # 点击登录按钮
    driver.find_element_by_xpath("//*[@id='loginFrm']/input").click()
    time.sleep(3)
    # 判断是否登录成功
    result =driver.find_element_by_xpath("//*[@id='header']/p/span[1]/strong").text
    return result

def click_mem(driver):
    # 点击会员标题
    driver.find_element_by_link_text('会员中心').click()

def click_teacher(driver):
    # 点击教师列表
    ele = driver.find_element_by_xpath("//*[@id='side-menu']/div[3]/ul/li[2]/a")
    driver.execute_script('arguments[0].click()', ele)

def iframe_swith(driver):
    # 内嵌框架切换
    driver.switch_to.frame("mainframe")

def clic_teacher(driver):
    # 点击添加教师
    driver.find_element_by_link_text('添加教师').click()

def add_teacher(driver):
    # 输入用户账号
    driver.find_element_by_id("username").send_keys("13222222222")
    # 输入昵称
    driver.find_element_by_id("realname").send_keys("自动化测试")
    # 输入密码
    driver.find_element_by_name("password").send_keys("1234567")
    # 勾选性别：
    driver.find_element_by_xpath("//*[@id='form']/div/div[4]/div/label[1]/input").click()
    #选择角色
    a1 =driver.find_element_by_css_selector("select[name='roleid']")
    Select(a1).select_by_visible_text('大众会员')
    # 选择机构
    b1 = driver.find_element_by_id("oneCategory")
    Select(b1).select_by_visible_text('郑州大学')
    # 填写邮箱
    driver.find_element_by_name("email").send_keys("12345@qq.com")
    # 填写手机号码
    driver.find_element_by_name("phone").send_keys("13000000000")

    # 选择地址
    c1 = driver.find_element_by_name("location_p")
    Select(c1).select_by_visible_text('四川省')
    sleep(3)
    d1 = driver.find_element_by_name("location_c")
    Select(d1).select_by_visible_text('南充市')
    e1 = driver.find_element_by_name("location_a")
    Select(e1).select_by_visible_text('顺庆区')
    # 填写详细地址
    driver.find_element_by_name("address").send_keys("幸福小乡村")
    # 填写个人简介
    driver.find_element_by_name("introduce").send_keys("个人简介")
    # 点击确认按钮
    driver.find_element_by_link_text("确认保存").click()
    time.sleep(5)
    # 警告框处理：点击“确认”
    driver.switch_to_alert().accept()
    time.sleep(3)
    # 点击返回按钮
    driver.find_element_by_link_text("返回列表").click()

def check_add(driver):
    Add =driver.find_element_by_xpath('//*[@id="recordList"]/tr[1]/td[2]/div/a').text
    print(Add)
    if Add =="13222222222":
        print("教师添加成功")




def add_teachers():
    driver = create_driver()
    open_url(driver)
    login(driver)
    click_mem(driver)
    click_teacher(driver)
    iframe_swith(driver)
    clic_teacher(driver)
    add_teacher(driver)
    check_add(driver)


if __name__ == '__main__':
    add_teachers()
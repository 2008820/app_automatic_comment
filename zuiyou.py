# -*- coding:utf-8 -*-
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
desired_caps = {
    #设备系统
    'platformName': 'Android',
    #设备名称
    'deviceName': '127.0.0.1:7555',
    #安卓版本
    'platformVersion': '4.4.4',
    # apk包名
    'appPackage': 'cn.xiaochuankeji.tieba',
    # apk的launcherActivity
    'appActivity': 'cn.xiaochuankeji.tieba.ui.base.SplashActivity',
    'unicodeKeyboard': True,  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
     'resetKeyboard':True,# 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来
    "noReset": True,

}



driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
y = driver.get_window_size()['height']
x = driver.get_window_size()['width']

WebDriverWait(driver, 12, 4).until(lambda driver:driver.find_element_by_id("cn.xiaochuankeji.tieba:id/middle_view"))
driver.swipe(0.5*x, 800, 0.5*x, 200, 80)
time.sleep(1)
def send_image():
    driver.find_element_by_id('cn.xiaochuankeji.tieba:id/add_image').click()
    driver.find_element_by_id('cn.xiaochuankeji.tieba:id/check_view').click()
    driver.find_element_by_id('cn.xiaochuankeji.tieba:id/button_confirm').click()
    driver.find_element_by_id('cn.xiaochuankeji.tieba:id/send').click()

for i in xrange(200):
    driver.find_element_by_id('cn.xiaochuankeji.tieba:id/middle_view').click()
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('cn.xiaochuankeji.tieba:id/etInput').send_keys(u"哈哈我屎都笑出来了")
        driver.find_element_by_id('cn.xiaochuankeji.tieba:id/send').click()
    except:
        pass
    driver.find_element_by_id('cn.xiaochuankeji.tieba:id/ivBack').click()
    time.sleep(3)
    driver.swipe(0.5*x, 600, 0.5*x, 10, 1000)
    try:
        driver.find_element_by_id('cn.xiaochuankeji.tieba:id/middle_view')
    except:
        driver.swipe(0.5 * x, 800, 0.5 * x, 200, 1000)

driver.quit()

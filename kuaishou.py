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
    'appPackage': 'com.smile.gifmaker',
    # apk的launcherActivity
    'appActivity': 'com.yxcorp.gifshow.HomeActivity',
    'unicodeKeyboard': True,  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
     'resetKeyboard':True, # 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来
    "noReset": True,

}



driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(10)
y = driver.get_window_size()['height']
x = driver.get_window_size()['width']

WebDriverWait(driver, 12, 4).until(lambda driver:driver.find_element_by_id("com.smile.gifmaker:id/player_gif_cover"))

class_list = driver.find_element_by_class_name('android.widget.ImageView')
for i in xrange(50):
    for item in driver.find_elements_by_xpath("//*[@resource-id='com.smile.gifmaker:id/container']"):
        item.click()
        driver.swipe(0.5 * x, 800, 0.5 * x, 100, 80)
        time.sleep(2)
        driver.tap([(68, 920), (529, 943)])
        try:
            driver.find_element_by_id("com.smile.gifmaker:id/editor").send_keys(u"哈哈哈 我屎都笑出来了".format(i))
            driver.find_element_by_id("com.smile.gifmaker:id/finish_button").click()
        except:
            pass
        time.sleep(1)
        driver.swipe(0.5 * x, 200, 0.5 * x, 800, 80)
        time.sleep(2)
        time.sleep(50)
        try:
            driver.find_element_by_id("com.smile.gifmaker:id/back_btn").click()
        except:
            pass

    driver.swipe(0.5 * x, 800, 0.5 * x, 100, 400)

driver.quit()

# -*- coding: utf-8 -*-
# @Author: yanchao
# @Date:   2017-07-06 14:10:47
# @Last Modified by:   yanchao
# @Last Modified time: 2017-07-24 16:59:09
import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe')
driver.get("http://192.168.1.39:8089/")
driver.maximize_window()  # 将浏览器最大化显示
usernameInput = driver.find_element_by_id("userName")
passwordInput = driver.find_element_by_id("password")
usernameInput.clear()
passwordInput.clear()
# 输入用户名
usernameInput.send_keys("admin")
# 输入密码
passwordInput.send_keys("123456")
# 获取登录Button并点击进行登录
submitButton = driver.find_element_by_css_selector(".ant-btn.ant-btn-primary.ant-btn-lg.button")
submitButton.click()
# 等待页面元素加载完成
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-btn.ant-btn-default.ant-dropdown-trigger"))
)
# 导航下拉与选定定位
menu = driver.find_element_by_css_selector(".ant-btn.ant-btn-default.ant-dropdown-trigger")
bkbjElement = driver.find_element_by_xpath(
    "//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical "
    "ant-dropdown-menu-light ant-dropdown-menu-root']/li[text()='布控报警']")
# 鼠标悬浮导航下拉按钮，然后点击“布控报警”
ActionChains(driver).move_to_element(menu).perform()
try:
    time.sleep(5)
finally:
    driver.close()

# -*- coding: utf-8 -*-
# @Author: yanchao
# @Date:   2017-07-05 10:06:16
# @Last Modified by:   yanchao
# @Last Modified time: 2017-07-05 11:24:21
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe')
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
try:
	title = WebDriverWait(driver, 10).until(
		EC.title_contains("python")
	)
	time.sleep(5)
finally:
	driver.close()
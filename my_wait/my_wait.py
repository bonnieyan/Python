from selenium import webdriver
driver = webdriver.Chrome("/home/yanjun/Downloads/chromedriver")
driver.get("https://passport.jd.com/new/login.aspx")
'''
1.强制等待　time.sleep
2.隐性等待　driver.implicitly_wait(10)　最长等待10s
'''

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

locator = (By.CSS_SELECTOR, ".login-tab.login-tab-r")
element = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(locator))
element.click()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 这个路径要写你自己的chromedriver所在路径
path = "/home/yanjun/Downloads/chromedriver"
driver = webdriver.Chrome(path)
time.sleep(1)
driver.get("http://www.python.org")
time.sleep(1)

assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
time.sleep(1)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

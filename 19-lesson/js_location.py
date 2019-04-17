from selenium import webdriver
import time


def search_12306():
    try:
        driver = webdriver.Chrome("/workspace/greedy_ai/python_and_ai/chromedriver")
        driver.get("https://www.12306.cn/index/")
        from_element = driver.find_element_by_id("fromStationText")
        time.sleep(2)
        from_element.click()
        from_element.send_keys("北京")
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='北京北']").click()

        to_element = driver.find_element_by_id("toStationText")
        to_element.click()
        to_element.send_keys("长春")
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='长春南']").click()
        js = "$('input[id=train_date]').removeAttr('readonly')"
        driver.execute_script(js)
        date_element = driver.find_element_by_id("train_date")
        date_element.click()
        date_element.clear()
        date_element.send_keys("2019-03-10")
        driver.find_element_by_class_name("form-label").click()
        driver.find_element_by_id("search_one").click()

    finally:
        time.sleep(3)
        driver.quit()


search_12306()



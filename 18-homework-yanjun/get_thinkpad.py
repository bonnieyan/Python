from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import json

driver = webdriver.Chrome("/home/yanjun/Downloads/chromedriver")
driver.maximize_window()


def login():
    driver.get("https://www.jd.com/")
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("17380409735")
    driver.find_element_by_id("nloginpwd").send_keys("988105yskyj+_")
    driver.find_element_by_id("loginsubmit").click()

    save_cookies(driver)


def save_cookies(driver):
    # 获取本地路径
    file_path = os.getcwd()+ "/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    # 保存cookies到文件中
    cookies = driver.get_cookies()
    with open(file_path + "jd.cookies", "w") as c:
        # 这里必须用dump方式写入文件
        # 不然你loads的时候会有问题，
        # 格式会不匹配
        json.dump(cookies, c)
    print(cookies)


def check_cookies():

    # 初始化login_status
    login_status = False

    # 将本地cookies装载到driver中
    driver = load_local_cookies_to_driver()

    # 校验cookies是否过期，未过期则能访问到订单中心
    driver.get("https://order.jd.com/center/list.action")
    current_url = driver.current_url
    if current_url == "https://order.jd.com/center/list.action":
        login_status = True
        print("cookies校验通过，登录成功")
        return login_status
    else:
        print("登录失败")
        return login_status


def load_local_cookies_to_driver():
    file_path = os.getcwd() + "/cookies/"
    # 读取cookies信息
    jd_cookies_str = open(file_path + "jd.cookies", "r").readline()
    # 加载cookies信息
    jd_cookies_dict = json.loads(jd_cookies_str)

    # 这个地方必须先访问一下网站，然后把旧的cookies 删除掉，再把我们保存的cookies添加进去
    driver.get("https://www.jd.com/")
    driver.delete_all_cookies()

    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)
    return driver

def to_thinkpad(driver):
    driver.get("https://www.jd.com")
    elem = driver.find_element_by_link_text("电脑")
    # 鼠标悬停
    ActionChains(driver).move_to_element(elem).perform()
    time.sleep(3)
    driver.find_element_by_link_text("笔记本").click()
    # 新开页了，需要切换句柄，否则定位不到
    handles = driver.window_handles
    index_handle = driver.current_window_handle
    for handle in handles:
        if handle != index_handle:
            driver.switch_to_window(handle)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"brand-11518\"]/a").click()
    # 7000以上
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"J_selectorPrice\"]/div/div[2]/div/ul/li[7]/a").click()
    # 评论
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"J_filter\"]/div[1]/div[1]/a[3]").click()
    driver.find_element_by_xpath("//*[@id=\"plist\"]/ul/li[1]/div/div[1]/a/img").click()
    # 新开页
    handles = driver.window_handles
    notebook_handle = driver.current_window_handle
    for handle in handles:
        if handle != index_handle and handle != notebook_handle:
            driver.switch_to_window(handle)
    time.sleep(2)
    # 滑动滚轮
    js = "window.scrollTo(0,1500)"
    driver.execute_script(js)
    time.sleep(2)
    # 点击规格与包装
    driver.find_element_by_xpath("//*[@id=\"detail\"]/div[1]/ul/li[2]").click()
    # 解析标签
    result_list = []
    # 拿取所有的信息Ptable-item
    info_elements = driver.find_elements_by_class_name("Ptable-item")
    for info_element in info_elements:
        # 获取到每一行的笔记本的配置信息
        info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)

    # 保存信息到文件
    save_goods_info(result_list)


def get_info_element_dict(info_element):

    # 主体等
    computer_part = info_element.find_element_by_tag_name("h3")

    # 系列等
    computer_info_keys = info_element.find_elements_by_tag_name("dt")

    # 配置信息等
    computer_info_values = info_element.find_elements_by_xpath("dl//dd[not(contains(@class,'Ptable-tips'))]")

    # 存储计算机中的key,value
    key_and_value_dict = {}

    # 用来存储所有的计算机组成信息的字典
    parts_dict = {}

    for i in range(len(computer_info_keys)):
        key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text
    parts_dict[computer_part.text] = key_and_value_dict

    return parts_dict


def save_goods_info(result_list):
    file_path = os.getcwd() + "/goods_info/"

    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with open(file_path + "computer.infos", "a", encoding="utf-8") as c:
        c.write(str(result_list))
        print(str(result_list))


if __name__ == "__main__":
    # login()
    try:
        #用循环控制校验的登录态
        loop_status = True
        while loop_status:
            #校验cookies是否过期
            login_status = check_cookies()
            if login_status:
                loop_status = False
            else:
                login()
        to_thinkpad(driver)
    finally:
        time.sleep(2)
        driver.quit()




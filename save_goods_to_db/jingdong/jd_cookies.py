
import os
import json

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


def check_cookies(driver):

    # 初始化login_status
    login_status = False

    # 将本地cookies装载到driver中
    driver = load_local_cookies_to_driver(driver)

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


def load_local_cookies_to_driver(driver):
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

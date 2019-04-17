from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

# 用来写我的业务逻辑


def to_baidu(name,server_address):
    print(name + "启动")
    driver = webdriver.Remote(
        command_executor=server_address,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.get("https://www.baidu.com")

# 这个变量用来存储我所有的远程服务地址


data = {
    "linux": "http://192.168.0.105:4444/wd/hub",
    # "windows": "http://192.168.1.38:4444/wd/hub"
}

threads = []
for name, url in data.items():
    t = Thread(target=to_baidu, args=(name, url))
    threads.append(t)

for t in threads:
    t.start()

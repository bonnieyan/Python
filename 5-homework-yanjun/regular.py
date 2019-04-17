# 类初始化时接受一个字符串的参数，下面的方法将不会接受参数。
import re


class Regular:
    def __init__(self, s):
        self.s = s

    # 方法能够匹配出所有的数字
    def get_numbers(self):
        print(re.findall("\d{3,11}", s))

    # 方法能够匹配出所有的邮箱
    def get_emails(self):
        print(re.findall("\d*@[a-z0-9]*.com", s))

    # 方法可以匹配出所有的ip
    def get_ips(self):
        print(re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s))

    # 方法能够匹配出所有的电话号码,电话包含座机和移动电话，座机要考虑区号3位或4位，号码要考虑7位或8位
    def get_phone_numbers(self):
        print(re.findall("0\d{2,3}-\d{7,8}|13[0-9]\d{8}|17[0-9]\d{8}", s))

    # 方法能够匹配出所有的url，url可以以http开头、https开头、ftp开头
    def get_urls(self):
        print(re.findall("http://w{3}.[a-z]*.com|https://w{3}.[a-z]*.com|ftp://w{3}.[a-z]*.com", s))


s = "给的一串数字1231，是不是哦1778881；" \
    "我的邮箱是：525663314@qq.com,她的邮箱是：1738022131@126.com；" \
    "ip地址是：1132.1112.312.1,123.124.121.122，10.112.123.122；" \
    "我的电话号码是：010-12341213,0832-3821251,17380409735,12345678901" \
    "以下url为：http://www.baidu.com,https://www.tmall.com,ftp://www.taobao.com"
p = Regular(s)
p.get_numbers()
p.get_emails()
p.get_ips()
p.get_phone_numbers()
p.get_urls()
#ok
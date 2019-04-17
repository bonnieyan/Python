# for i in range(5):
#     print(i)
#
# for j in range(0, 5):
#     print(j)
import re
s = "phone number : 010-8877665  0431-98989498 0832-3821251"
reg = "0\d{2}-d{7}|0\d{3}-\d{7}|0\d{3}-\d{8}"
print(re.findall(reg,s))

#捕捉与不捕捉7665
ip = "1234.543.123.12  255.255.133.255  0.0.144.0  192.168.11.1"
reg1 = "(?:\d{1,3}\.){3}\d{1,3})"
print(re.findall(reg1, ip))
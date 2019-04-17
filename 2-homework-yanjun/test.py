import re

s = "下边的号码中，哪些是手机号呢:18475309876,18719462345,17665148777,13332839908,12398028761"
# s1 = re.findall("\d{11}",s)
# print(s1)
# for i in range(len(s1)):
#     result = re.findall("((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\d{8}$",s1[i])
#     if result:
#         continue
#     else:
#         del s1[i]
# print(s1)

r = re.findall("13[0-9]\d{8}|14[5,7]\d{8}|15[0-3,5-9]\d{8}|17[0,3,5-8]\d{8}|18[0-9]\d{8}|166\d{8}|198\d{8}|199\d{8}|147\d{8}",s)
print(r)
#
text ="1324.231.432.12934,192.168.1.6,10.25.11.8 这些信息中，哪些是ip呢？"
text1 = re.findall(("\d+.\d+.\d+.\d*"), text)
print(text1)
for i in range(len(text1)-1):
    result = re.findall("^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$",text1[i])
    if result:
        continue
    else:
        del text1[i]
print(text1)

sd ="525663314里包含几个数字啊？"
r = re.search("\d*", sd).group(0)
print(str(len(r))+"个")



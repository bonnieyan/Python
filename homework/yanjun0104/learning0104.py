#数据类型 int，float，bool，str
name = '小花'
age = 18
high = 160.5
girl = True

print(type(name))
print(type(age))
print(type(high))
print(type(girl))


#条件控制

# names = input()
# if names == '小花':
#     print("Hello" + names)
# elif names == '小狗':
#     print("Hello" + names)
# else:
#     print("我不认识你！")

#循环while, for

'''
break:跳出当前循环，continue:继续当前循环
'''


# while True:
#     print("死循环")
#     break
#
# while True:
#     print("死循环2")
#     continue
#     print("永远无法执行这条语句")

count = 0
for i in range(1,101):
    count += i
    i+1
print(count)


for s in 'python':
    print("当前字母: " + s)



#文件读取
'''
read:读取全部，readline:读取第一行,readlines:读取所以数据病放到一个list中
模式:a，追加；w，清空写文件
open("data.txt", "w",encoding = "utf8")
'''
file = open("data.txt", encoding="utf8")
data = file.readlines()
# data = file.read()
# file.write("今天天气真好呀")
print(data)

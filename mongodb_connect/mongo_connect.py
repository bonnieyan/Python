import pymongo
# 链接mongdb数据库
client = pymongo.MongoClient(host="localhost", port=27017,
                             username="admin", password="123456"
                             )
# 链接数据库
db = client.python_ui
# 制定操作的集合（表）
collection = db.my_test_collection
# collection = db['my_test_collection']
# 插入数据
info_dict = {
    "id": 1,
    "name": "张三",
    "age": 20
    }

# re = collection.insert(info_dict)
# print(re)

info_dict1 = {
    "id": 2,
    "name": "张三2",
    "age": 20
    }

info_dict2 = {
    "id": 3,
    "name": "张三3",
    "age": 20
    }

# re = collection.insert_many([info_dict1, info_dict2])
# print(re)

info_dict3 = {
    "my_list": [
        {
            "id": 10,
            "name": "小化",
            "age": 21
        },
        {
            "id": 11,
            "name": "小化1",
            "age": 22,
            "test": "yyy"
        },
    ],
    "comment": "这是我的练习数据"
}
# re = collection.insert_one(info_dict3)
# print(re)

# re = collection.find_one({"id": 2})＃ 返回的是具体结果
# re = collection.find({"id": 2}) # 返回的是对象
# print(re)
# 返回的是对象
re = collection.find({"id": 2}, {"name"})
# print(re)
# for r in re:
#     print(r)
# 同个list算一条数据
# re = collection.find_one({"my_list.id":11})
# print(re)

# 更新操作
'''
1.查询到想要更新的数据
２．更新结果 set
３．执行更新
'''
filter_data = {"my_list": 10}
filter_re = collection.find_one(filter_data)
filter_re["school"] = "MIT"
re = collection.update(filter_data, {"$set": filter_re})
print(re)
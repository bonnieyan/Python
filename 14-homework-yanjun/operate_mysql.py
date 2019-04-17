# TODO：连接数据库
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     db='test_db',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
# 查询apply表
apply_sql = 'select applicant, status from apply'
apply_detail = pd.read_sql(sql=apply_sql, con=db)

def get_od_apply(person_id):
# 通过apply_detail拿到'applicant','status'两列的值
    #将dataFrame转换为numpy.ndarray
    apply_list_1 = apply_detail.values
    # print(type(apply_list_1))
    #将numpy.ndarrayz转换为list
    apply_list = apply_list_1.tolist()
    # print(apply_list)
    for i in apply_list:
        # print(i)
        # print(i[0])
        # print(i[1])
        # print(type(i[1]))
        if i[0] == person_id:
            if i[1] == 'OVERDUE':
                return True
            else:
                continue
        if i[0] > person_id:
            return False

    # print(apply_list)
    # print(type(apply_list))
    # for p in apply_list:
    #     print(p)
    #     if p == person_id:
    #         print(p)
    # return p
# 遍历apply_list,找到person_id，如果有OVERDUE状态进件则返回True，否则返回False

# print(get_od_apply(20000004))
if __name__ =="__main__":
    print(get_od_apply(20000004))
    print(get_od_apply(20000035))



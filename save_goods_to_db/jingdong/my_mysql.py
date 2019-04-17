import pymysql


def save_goods_tomysql(result_list):
    # 获取链接
    try:
        db_conn = get_connection()

        # 获取游标
        cur = db_conn.cursor()
        # 书写sql
        for info in result_list:
            for key, value in info.items():
                # 避免有坑，第一数据必须为元祖，第二数据为string，用引号
                sql = "insert into goods(computer_part_name,computer_info) values (\"%s\",\"%s\")" % (key, value)
                print(sql)
                cur.execute(sql)
                db_conn.commit()
        # 执行sql
        # 提交sql
    # 关闭链接
    finally:
        close_db(db_conn, cur)


def get_connection():
    db_conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='test_db',
        charset='utf8')

    return db_conn


def close_db(db_conn, cur):
    cur.close()
    db_conn.close()
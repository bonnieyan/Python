import xlwt
import time
import xlrd
from xlutils.copy import copy
import logging
logger =logging.getLogger()
logger.setLevel("DEBUG")
#流处理，控制输出到控制台
stream_handle = logging.StreamHandler()
#设置文件handler
file_handler = logging.FileHandler("my.log", mode='a', encoding="utf8")
logger.addHandler(file_handler)
logger.addHandler(stream_handle)
#格式化
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s  - %(message)s')
file_handler.setFormatter(formatter)
stream_handle.setFormatter(formatter)

class Worker():
    def __init__(self, worker_num, worker_name, worker_message, position_salary, start_time, end_time):
        self.worker_num = worker_num
        self.worker_name = worker_name
        self.worker_message = worker_message
        self.position_salary = position_salary
        self.start_time = start_time
        self.end_time = end_time


class Finace():
    def write_excel(list_all):
        book = xlwt.Workbook()
        sheet = book.add_sheet('员工工资计算')
        row0 = ['员工编号', '工资结算时间', '员工姓名', '员工基本信息', '岗位', '工资', '说明', '工资总计']
        #写表头
        for i in range(len(row0)):
            sheet.write(0, i, row0[i])
        row_num = 1
        for c in list_all:
            col_num = 0
            for s in c:
                sheet.write(row_num, col_num, s)
                col_num += 1
            row_num += 1

        book.save('员工工资计算.xls')

    def write_excel_append(path, listall):
        index = len(listall)  # 获取需要写入数据的行数
        workbook = xlrd.open_workbook(path)  # 打开工作簿
        worksheet = workbook.sheet_by_name('员工工资计算')
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
        for i in range(0, index):
            for j in range(0, len(listall[i])):
                new_worksheet.write(i + rows_old, j, listall[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
        new_workbook.save(path)  # 保存工作簿
        logger.info("xls格式表格【追加】写入数据成功！")

    def calc_salary(worker):
        list_all = []
        list_posi = []
        list_sa_base =[]
        start_sec = time.mktime(time.strptime(worker.start_time, '%Y-%m-%d'))
        end_sec = time.mktime(time.strptime(worker.end_time, '%Y-%m-%d'))
        worker_time = (int((end_sec - start_sec)/(24*60*60))) // 7
        logger.info(worker_time)
        for l in worker.position_salary:
            for key in l.keys():
                posi = key
            list_posi.append(posi)
            for value in l.values():
                sa_base = int(value) * worker_time
            list_sa_base.append(sa_base)
        logger.info(list_posi)
        logger.info(list_sa_base)
        s_total = 0
        for i in range(len(list_posi)):
            list_content = []
            list_content.append(worker.worker_num)
            list_content.append('2019-1')
            list_content.append(worker.worker_name)
            list_content.append(worker.worker_message)
            list_content.append(list_posi[i])
            list_content.append(list_sa_base[i])
            list_content.append('工资结算4周')
            s_total += list_sa_base[i]
            list_content.append(s_total)
            list_all.append(list_content)
        logger.info(list_all)
        return list_all


worker = Worker(1, '小A', '住在回龙观', [{"程序员": 2000}, {"扫地": 1000}], '2019-01-01', '2019-01-31')
re = Finace.calc_salary(worker)
print(re)
Finace.write_excel(re)
worker = Worker(1, '小B', '居住在天通苑', [{"程序员": 2000}], '2019-01-01', '2019-01-31')
re = Finace.calc_salary(worker)
Finace.write_excel_append('/home/yanjun/1-homework-yanjun/9-homework-yanjun/员工工资计算.xls', re)
worker = Worker(1, '小c', '居住在西二旗', [{"程序员": 2000}], '2019-01-01', '2019-01-31')
re = Finace.calc_salary(worker)
Finace.write_excel_append('/home/yanjun/1-homework-yanjun/9-homework-yanjun/员工工资计算.xls', re)
worker = Worker(1, '小D', '居住在天通苑', [{"程序员": 2000}], '2019-01-01', '2019-01-31')
re = Finace.calc_salary(worker)
Finace.write_excel_append('/home/yanjun/1-homework-yanjun/9-homework-yanjun/员工工资计算.xls', re)







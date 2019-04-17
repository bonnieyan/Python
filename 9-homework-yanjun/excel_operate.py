#excel 的读写
import xlwt
import xlrd
import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='my.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s  - %(message)s')


def write_excel(excel_file: str, sheet_name: str):
    book = xlwt.Workbook()
    sheet = book.add_sheet(sheet_name)
    content = [['姓名', '年龄', '性别', '分数'], ['mary', 20, '女', 89.9], ['mary', 20, '女', 89.9], ['mary', 20, '女', 89.9], ['mary', 20, '女', 89.9]]
    row_num = 0
    for c in content:
        col_num = 0
        for s in c:
            sheet.write(row_num, col_num, s)
            col_num += 1
        row_num += 1
    try:
        book.save(excel_file)
    except:
        raise Exception("文件不存在")
        return False
    else:
        return True


def read_excel(excel_file: str, sheet_name: str, row_num: int = 0, col_num: int = 0):
    book = xlrd.open_workbook(excel_file)
    sheet = book.sheet_by_name(sheet_name)
    cell = sheet.cell(row_num, col_num)
    logging.info("获取制定单元格的内容:"+str(cell.value))


if __name__ == "__main__":
    write_excel("w.xls", "成绩单")
    read_excel("w.xls", "成绩单", 3, 3)
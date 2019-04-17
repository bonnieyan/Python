import shutil
import os
import logging
# 实现图片文件的复制
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='my.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s  - %(message)s')

def copy_image(source_file, target_path):

    shutil.copy(os.path.join(source_file, "mao.jpeg"), os.path.join(target_path))
    logging.info("copy_image:复制图片成功")

def get_files(file_path):
    list_dirs = os.listdir(file_path)
    for file in list_dirs:
        path = os.path.join(file_path, file)
        if os.path.isdir(path):
            get_files(path)
        else:
            logging.info(path+":"+file)




if __name__ == "__main__":
    # copy_image("./old_image", "./new_image")
    get_files("/home/yanjun/1-homework-yanjun/9-homework-yanjun")
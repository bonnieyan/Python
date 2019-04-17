import logging
logger =logging.getLogger()
logger.setLevel("DEBUG")
#设置文件handler
file_handler = logging.FileHandler("all.log", mode='a', encoding="utf8")
#流处理，控制输出到控制台

stream_handle = logging.StreamHandler()
error_handle = logging.FileHandler("error.log", mode='a', encoding="utf-8")
error_handle.setLevel(logging.ERROR)
logger.addHandler(file_handler)
logger.addHandler(stream_handle)
logger.addHandler(error_handle)

#格式化
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s  - %(message)s')
file_handler.setFormatter(formatter)
error_handle.setFormatter(formatter)
stream_handle.setFormatter(formatter)

logger.debug("这是debug日志")
logger.info("这是info日志")
logger.error("这是error日志")
'''
 1.需求：1.要求所有级别的所有日志都写入磁盘文件中
 2）all.log文件中计入所有日志文件
 3）error.log单独计入error及以上错误信息
 4）要求all.log在每天凌晨进行切割
 2.分析
 1）设置日志最低级别为DEBUG
 2）日志需要被发送到两个目的地，因此需要设置两个handler，两个目的地都是磁盘文件，因此两个handler都必须与FilterHandler相关
 3）all.log要求按时间进行日志切割，因此使用logging.handlers.TimedRotatingFileHandler
 4)两个要设置不同的格式
'''
import logging
import  logging.handlers
import  datetime
logger=logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)
rf_handler=logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1,backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s--%(levelname)s--%(message)s"))

f_handler=logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s--%(levelname)s--%(filename)s[:%(lineno)]-%(message)s"))

logger.addHandler(f_handler)
logger.addHandler(rf_handler)

logging.info("This is an info")
logging.warning("this is a warning")
logging.debug("this is a debug")
logging.error("this is an error")
logging.critical("This is a critical")
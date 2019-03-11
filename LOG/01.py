import logging
Log_format="%(asctime)s=====%(levelname)s++++(message)"
logging.basicConfig(filename="tulingxueyuan.log",level=logging.DEBUG,format=Log_format)#设置最低级别,在本地生成一个tulingxueyuan.log的文件，并且输出到这个文件中
logging.info("This is a info log")
logging.log(logging.INFO,"This is a info log")#低于warning级别的日志不显示
logging.warning("This is a warning log")
logging.log(logging.WARNING,"This is a warning log")



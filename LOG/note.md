#LOG
-logging模块提供模块级别的函数记录日志
-包括四大组件
##1:日志相关的概念
-日志的级别
    -不同用户关注不同的程序信息
-IO操作=》不要太频繁操作
LOG的作用
    -调试
    -了解软件的运行情况
    -分析定位问题
-日志信息
    -time
    -地点
    -level
    -内容
 ##2.Logging模块
 -日志级别
    -级别可定义
    -DEBUG
    -INFO
    -WARNING
    -ERROR
    -CRITICAL
-初始化/写日志实例需要指定级别，只有当级别等于或高于制定级别才被记录
-使用方式
    -直接使用logging(封装了其他组件)模块
    -logging四大组件直接定制
#2.1 logging模块级别的日志
-使用以下几个函数
    -logging.dubug(msg,*args,**kwargs) 创建一个严重级别为DEBUG的日志记录
    -logging.info(msg,*args,**kwargs) 创建一个严重级别为INFO的日志记录
    -logging.warning(msg,*args,**kwargs) 创建一个严重级别为WARNING的日志记录
    -logging.error(msg,*args,**kwargs) 创建一个严重级别为ERROR的日志记录
    -logging.critical(msg,*args,**kwargs) 创建一个严重级别为CRITICAL的日志记录
    -logging.log(level,*args,**kwargs) 创建一条严重级别为level的日志记录
    -logging.basicConfig(**Kwargs) 对root logger进行一次性配置
#2.2logging模块处理流程
-四大组件
    -日志器(logger)产生日志的一个接口
    -处理器（Handler）：把产生的日志发送到相应的目的地
    -过滤器（Filter）：更精确的控制哪些日志的输出
    -格式器（Formatter）:对输出的信息进行格式化
    Logger
    -产生一个日志
    -操作
    logger.setLevel()-设置日志的最低级别
    logger.addHandler() 和 logger.removeHandler()为该logger添加和移除一个handler
    logger.addFilter() 和logger.removeFilter为该日志添加或者移除一个filter
    logger.debug 产生一个debug级别的日志
    logger.log获取一个明确的日志level参数创建一个日志记录
    -如何得到一个logger对象
        -实例化
        -logging.getlogger()
   -Handler
   https://blog.csdn.net/lilong117194/article/details/82852054 logging详述
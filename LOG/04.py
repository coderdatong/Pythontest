import logging
import logging.handlers
import datetime
logger=logging.getLogger('myLoger')
logger.setLevel(logging.DEBUG)
rf_handler=logging.handlers.TimedRotatingFileHandler("All.log",when='midnight',interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s--%(levelname)s--%(message)s"))
f_handler=logging.FileHandler('errors.log')
f_handler.setFormatter(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s--%(levelname)s--%(filename)s[:%(lineno)d]--%(message)s"))
logger.addHandler(rf_handler)
logger.addHandler(f_handler)
logger.info('info message')
logger.debug('debug message')
logger.warning('warningmessage')
logger.error('error message')
logger.critical('critical message')
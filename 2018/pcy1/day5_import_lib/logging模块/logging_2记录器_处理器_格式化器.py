#_*_coding:utf-8_*_

import logging
# 记录器
logger_name='logger_1'
logger=logging.getLogger(logger_name) #实例化logger记录器
# 级别
logger.setLevel(logging.DEBUG)#设定记录器级别

#处理器
ch = logging.StreamHandler() #实例化处理器：使用标准输出处理器(屏幕)，并实例化给ch
ch.setLevel(logging.ERROR)#屏幕只显示ERROR和以上CRITICAL的两条信息，
filename='logfile/logger_1.log'#logfile文件夹必须存在
fh=logging.FileHandler(filename)#实例化处理器：使用文件输出处理器，并实例化给fh
# fh没有设定level，会采用记录器的level，这里记录debug以上的5条信息。


# 格式化
fmt='%(asctime)s -%(filename)s[line:%(lineno)d]—— %(name)s - %(levelname)s - %(message)s'#格式化定义
datefmt='%a, %d %b %Y %H:%M:%S'#时间格式
formatter = logging.Formatter(fmt,datefmt)

# 把处理器和格式化器相关联
ch.setFormatter(formatter)#设定输出的格式为已经定义好的格式
fh.setFormatter(formatter)

#把记录器和处理器关联
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message') #默认是warn级别
logger.error('error message')
logger.critical('critical message')


#_*_coding:utf-8_*_
'''
先简单介绍一下，logging库提供了多个组件：Logger、Handler、Filter、Formatter。
Logger对象提供应用程序可直接使用的接口，
Handler发送日志到适当的目的地，
Filter提供了过滤日志信息的方法，
Formatter指定日志显示格式。

Logger
Logger是一个树形层级结构，输出信息之前都要获得一个Logger（如果没有显示的获取则自动创建并使用root Logger，如第一个例子所示）。
logger = logging.getLogger()返回一个默认的Logger也即root Logger，并应用默认的日志级别、Handler和Formatter设置。
当然也可以通过Logger.setLevel(lel)指定最低的日志级别，可用的日志级别有
logging.DEBUG、logging.INFO、logging.WARNING、logging.ERROR、logging.CRITICAL。
Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()输出不同级别的日志，
只有日志等级大于或等于设置的日志级别的日志才会被输出。
'''
import logging

# 创建一个logger
logger = logging.getLogger()

logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('mylogger')
logger2.setLevel(logging.INFO)

logger3 = logging.getLogger('mylogger.child1')
logger3.setLevel(logging.WARNING)

logger4 = logging.getLogger('mylogger.child1.child2')
logger4.setLevel(logging.DEBUG)

logger5 = logging.getLogger('mylogger.child1.child2.child3')
logger5.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('logfile/test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

# 定义handler的输出格式formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 定义一个filter过滤器
# filter = logging.Filter('mylogger.child1.child2')
# fh.addFilter(filter)

# 给logger添加filter
# logger.addFilter(filter)
logger.addHandler(fh)
logger.addHandler(ch)

# logger1.addFilter(filter)
logger1.addHandler(fh)
logger1.addHandler(ch)
#
# logger2.addHandler(fh)
# logger2.addHandler(ch)
#
# logger3.addFilter(filter)
# logger3.addHandler(fh)
# logger3.addHandler(ch)
#
# logger4.addFilter(filter)
# logger4.addHandler(fh)
# logger4.addHandler(ch)
#
# logger5.addHandler(fh)
# logger5.addHandler(ch)

# 记录一条日志
# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')
#
# logger2.debug('logger2 debug message')
# logger2.info('logger2 info message')
# logger2.warning('logger2 warning message')
# logger2.error('logger2 error message')
# logger2.critical('logger2 critical message')
#
# logger3.debug('logger3 debug message')
# logger3.info('logger3 info message')
# logger3.warning('logger3 warning message')
# logger3.error('logger3 error message')
# logger3.critical('logger3 critical message')
#
# logger4.debug('logger4 debug message')
# logger4.info('logger4 info message')
# logger4.warning('logger4 warning message')
# logger4.error('logger4 error message')
# logger4.critical('logger4 critical message')
#
# logger5.debug('logger5 debug message')
# logger5.info('logger5 info message')
# logger5.warning('logger5 warning message')
# logger5.error('logger5 error message')
# logger5.critical('logger5 critical message')
# import logging
# logging.basicConfig(
# filename='access.log',
# format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
# datefmt='%Y-%m-%d %H:%M:%S %p',
# level=40,
# )
#
# logging.debug('debug...') # 10
# logging.info('info....') #20
# logging.warning('可能着火...') #30
# logging.error('着火啦快跑') # 40
# logging.critical('火越烧越大') #50

#===========================================logging模块的四种对象========================================
# #logger:负责产生日志
# logger1=logging.getLogger('xxx')
#
# #filter：过滤日志（不常用）
#
# #handler：控制日志打印到文件or终端
# fh1=logging.FileHandler(filename='a1.log',encoding='utf-8')
# fh2=logging.FileHandler(filename='a2.log',encoding='utf-8')
# sh=logging.StreamHandler()
#
# #formatter：控制日志的格式
# formatter1=logging.Formatter(
# fmt='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
# datefmt='%Y-%m-%d %H:%M:%S %p',
# )
#
# formatter2=logging.Formatter(fmt='%(asctime)s - %(message)s',)
#
#
# # 为logger1对象绑定handler
# logger1.addHandler(fh1)
# logger1.addHandler(fh2)
# logger1.addHandler(sh)
#
# # 为handler对象绑定日志格式
# fh1.setFormatter(formatter1)
# fh2.setFormatter(formatter1)
# sh.setFormatter(formatter2)
#
#
# #日志级别: 两层关卡，必须都通过，日志才能正常记录
# logger1.setLevel(10)
# fh1.setLevel(10)
# fh2.setLevel(10)
# sh.setLevel(10)
#
# #调用logger1对象下的方法，产生日志，然后交给不同的handler，控制日志记录到不同的地方
# logger1.debug('调试信息')
#





# 瞅一眼：日志的继承
import logging
logger1=logging.getLogger('father')
logger2=logging.getLogger('father.son')
logger3=logging.getLogger('father.son.grandson')


sh=logging.StreamHandler()
formatter2=logging.Formatter(fmt='%(asctime)s - %(message)s',)
sh.setFormatter(formatter2)

logger1.addHandler(sh)
logger2.addHandler(sh)
logger3.addHandler(sh)




logger1.setLevel(10)
logger2.setLevel(10)
logger3.setLevel(10)
sh.setLevel(10)



# logger1.debug('测试。。。。')
# logger2.debug('测试。。。。')
logger3.debug('测试。。。。')













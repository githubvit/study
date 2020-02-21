#_*_coding:utf-8_*_

import logging
# logging.basicConfig(filename='logger.log', level=logging.INFO)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',)
                    # filename='logger.log',
                    # filemode='w')
'''
在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有
filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。 
datefmt：指定日期时间格式。 
level：设置rootlogger（后边会讲解具体概念）的日志级别 
stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。
若同时列出了filename和stream两个参数，则stream参数会被忽略。
例：
logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='/tmp/test.log',  
                    filemode='w') 
输出：Mon, 05 May 2014 16:29:53 test_logging.py[line:9] DEBUG debug message
'''
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message') #默认是warn级别
logging.error('error message')
logging.critical('critical message')
#项目的配置文件
import os
# 从当前文件settings.py找到项目根目录atm
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 用户数据库模拟文件路径
USER_PATH=r'%s\db\user.json'%BASE_DIR 

#日志文件路径
LOGON_PATH=r'%s\log\logon.log'%BASE_DIR #登录日志
REGIST_PATH=r'%s\log\register.log'%BASE_DIR #注册日志

# 定义三种日志输出格式
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[task_id:%(name)s][%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[task_id:%(name)s][%(levelname)s][%(asctime)s] %(message)s'

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,

    #1、定义日志的格式
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'id_simple':{
            'format':id_simple_format
        }
    },
    'filters': {},

    #2、定义日志输出的目标：文件或者终端
    'handlers': {
        #打印到终端的日志
        'stream': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'logon_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': LOGON_PATH,  # 日志文件
            # 'maxBytes': 1024*1024*5,  # 日志大小 5M
            'maxBytes': 300,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        #打印到文件的日志,收集error及以上的日志
        'register_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'id_simple',
            'filename': REGIST_PATH,  # 日志文件
            # 'maxBytes': 1024*1024*5,  # 日志大小 5M
            'maxBytes': 300,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },

    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['stream','logon_log','register_log'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
        'logon': {
            'handlers': ['stream','logon_log'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'ERROR',
            'propagate': False,  # 向上（更高level的logger）传递
        },
        'register': {
            'handlers': ['stream','register_log'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
    },
}



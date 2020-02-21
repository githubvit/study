# from conf import settings
#
# def logger(msg):
#     with open(settings.LOG_PATH,'a',encoding='utf-8') as f:
#         f.write('%s\n' %msg)



import logging.config
import logging
from conf import settings

def get_logger(name): #name='atm'
    logging.config.dictConfig(settings.LOGGING_DIC)  # 导入上面定义的logging配置
    l1=logging.getLogger(name)
    return l1

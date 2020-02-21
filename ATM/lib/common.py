# 工具
import logging
import logging.config
from conf import settings

def get_logger(name):
    # # 导入settings定义的logging配置
    logging.config.dictConfig(settings.LOGGING_DIC)
    #取得logger对象
    logger1=logging.getLogger(name)
    return logger1
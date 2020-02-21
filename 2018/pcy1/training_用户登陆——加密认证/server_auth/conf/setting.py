#!_*_coding:utf-8_*_

import os,logging
# import sys
# import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASE = {
    'engine': 'file_storage', #只是定义了数据库的类型为file_srorage。
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'access': 'access.log',
}
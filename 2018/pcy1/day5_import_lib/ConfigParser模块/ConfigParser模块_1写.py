#-*- coding:utf8 -*-

import configparser

config = configparser.ConfigParser()
# 写入 就是用字典

config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here

config['DEFAULT']['ForwardX11'] = 'yes'

with open('example3.ini', 'w') as configfile:
    config.write(configfile)



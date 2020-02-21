#-*- coding:utf8 -*-

import configparser

conf = configparser.ConfigParser()
conf.read('example.ini')
print conf.sections()#因为文件里有["DEFAULT"]节点，所以读不出该节点，如果不是，就可以读出。
# print conf.defaults()#可用defaults方法读出该节点全部内容
for key in conf['topsecret.server.com']: print(key) #打印该节点下的key
print conf['bitbucket.org']['user']
s='DEFULT'
for i in conf[s]:#打印该节点下的key和value
    print '%s  %s'%(i,conf[s][i])

#-*- coding:utf8 -*-


import ConfigParser

config = ConfigParser.ConfigParser()
config.read('example.ini')#读出要修改的对象
#
########## 读2 ##########
# secs = config.sections()
# print secs #读出所有节点列表
# options = config.options('DEFULT')
# print options #读出某节点下的选项列表
#
# item_list = config.items('DEFULT')
# print item_list #读出某节点下的key\value二元元组列表



# ########## 改写 ##########

# # 增加节点alex
# sec = config.add_section('alex')
#
# # 增加节点alex下的子项k1=11111
# config.set('alex','k1',11111)
# config.set('alex','k2',22222)
# config.write(open('example2.ini', "w"))


# ########## 删除 ##########
# 删除bitbucket.org节点下的子项k1
# config.read('example2.ini')
# sec=config.remove_option('alex','k1')
# 删除bitbucket.org节点
# sec=config.remove_section('alex')
# config.write(open('example2.ini','w'))
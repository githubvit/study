#_*_coding:utf-8_*_
'''
发布订阅 收音机模式
'''

import redis

class RedisHelper:

    def __init__(self):
        # 建立redis实例 连接redis服务器
        self.__conn = redis.Redis(host='192.168.2.240', port=6379,password='foobared')
        self.chan_sub = 'fm104.5' #收 订阅
        self.chan_pub = 'fm104.5' #发 发布

    def public(self, msg): #发 发布
        self.__conn.publish(self.chan_pub, msg)#调用redis实例的publish方法发布
        return True

    def subscribe(self):#收 订阅
        pub = self.__conn.pubsub()#打开收音机 调用redis实例的pubsub方法订阅
        pub.subscribe(self.chan_sub)#调频道
        pub.parse_response()#准备接收
        return pub
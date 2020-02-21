#_*_coding:utf-8_*_
'''
发布订阅的订阅
直接在rehl7的redis客户端上用publish命令进行发布
127.0.0.1:6379> publish fm104.5 'from publish 1'
(integer) 1
127.0.0.1:6379> 
用本程序实现订阅
'''
import redis


from redis3_radio import RedisHelper

obj = RedisHelper()#实例化RedisHelper

redis_sub = obj.subscribe()#准备接收

while True:
    msg = redis_sub.parse_response()#开始接收
    print msg
'''
运行结果：收到发布方在rehl7上用redis的publish命令发布的消息
 ['message', 'fm104.5', 'from publish 1']
'''

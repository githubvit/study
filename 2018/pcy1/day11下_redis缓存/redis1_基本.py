#_*_coding:utf-8_*_
'''
redis
Redis优点
单线程异步io

异常快速 : Redis是非常快的，每秒可以执行大约110000设置操作，81000个/每秒的读取操作。

支持丰富的数据类型 : Redis支持最大多数开发人员已经知道如列表，集合，可排序集合，哈希等数据类型。

这使得在应用中很容易解决的各种问题，因为我们知道哪些问题处理使用哪种数据类型更好解决。
操作都是原子的 : 所有 Redis 的操作都是原子，从而确保当两个客户同时访问 Redis 服务器得到的是更新后的值（最新值）。

MultiUtility工具：Redis是一个多功能实用工具，可以在很多如：缓存，消息传递队列中使用（Redis原生支持发布/订阅）
，在应用程序中，如：Web应用程序会话，网站页面点击数等任何短暂的数据；
'''

import redis
# 先启动redis服务，在运行
# 连接redis服务器
#普通方式
# r = redis.Redis(host='192.168.2.240', port=6379,password='foobared')
#连接池方式
pool= redis.ConnectionPool(host='192.168.2.240', port=6379,password='foobared')
r = redis.Redis(connection_pool=pool)

#设定key和value

for i in range(10):
    r.rpush('names', i)#r.set(key,value)

#查看r对象 原来的print r 会报错（KeyError: 'db'），这样用type包起来就可以了。
print type(r)
#Redis<ConnectionPool<Connection<host=localhost,port=6379,db=0>>>,redis共有16张表（0-15），当前在0表。select index.html 切换

# 获取'foo'key的value

print r.lrange('names',0,-1) #Bar
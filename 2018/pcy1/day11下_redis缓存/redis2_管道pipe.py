#_*_coding:utf-8_*_
'''
redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，
并且默认情况下一次pipline 是原子性操作。
原子操作的意思就是要么都做，要么都不做。
'''
import redis
import time
pool = redis.ConnectionPool(host='192.168.2.240', port=6379,password='foobared')

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)


pipe = r.pipeline(transaction=True)

pipe.set('name', 'alex2')
time.sleep(10)#可以在等候的时候断电，如果是原子操作，则name alex2也不会执行。
pipe.set('role', 'sb2')

pipe.execute()

# r.set('name','alex3')
# time.sleep(10)#不是原子操作，在等候的时候断电，上面执行，下面不执行
# r.set('role','sb3')
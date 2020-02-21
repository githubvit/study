#_*_coding:utf-8_*_


import pika

# 1，建立socket，连接rabbitmq服务器
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))#Parameters参数
# 2，在socket上建立管道
channel=connection.channel()#channel管道、渠道
#3，在管道里，声明queue队列
channel.queue_declare(queue='hello',durable=True)#declare声明，持久化也要写上，不然会连不了。
# 4，定义回调函数
def callback(ch,method,properties,body):#properties属性、特征
    print 'ch:', ch                 #接收的管道
    print 'method:', method         #接收的方法
    print 'properties:', properties #接收的属性
    print 'body:', body             #接收的消息
    '''
    ch: 管道对象<BlockingChannel impl协议名称=<Channel number管道数量=1 OPEN conn连接实例=<SelectConnection OPEN socket=('::1', 54924, 0, 0)->('::1', 5672, 0, 0) params连接参数=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>>> 
    method: 投递方法<Basic.Deliver(['consumer_tag=ctag1.150ceab0a15940829dda02d4d3b13804门牌号', 'delivery_tag=1投递数量', 'exchange=邮局名称现在为空', 'redelivered=False不重复投递', 'routing_key=hello投递员就是队列名称'])> 
    properties: 基本属性<BasicProperties> 现在为空
    body: 消息Hello World!
    '''
    print(" [x] Received %r" % body)#用%r 收到的body加单引号 [x] Received 'Hello World!'
   # 用%s收到的body没单引号 [x] Received Hello World!
    ch.basic_ack(delivery_tag=method.delivery_tag)#通过管道channel向服务器确认手动确认消息处理已完成，可以删除消息了。ch就是channel对象。

# 5，定义接收消息或叫消费消息的语法
# 回调函数callback（意思是如果收到消息就调用callback），管道名=hello、noack=True无须确认。
channel.basic_qos(prefetch_count=1)#如果还剩1条消息没处理，就不收。
channel.basic_consume(callback,
                     queue='hello',
                     # no_ack=True#当把这句注释，就没有对服务器的确认了，在回调函数中必须手动确认消息处理完成的结果，这样消息才会被删除。
                     )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 6，开始收消息。一旦启动，就一直收，没有就阻塞-等待。
# 收到的消息是bytes类型的。
channel.start_consuming()
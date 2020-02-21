#_*_coding:utf-8_*_


import pika,time

# 1，建立socket，连接rabbitmq服务器
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))#Parameters参数
# 2，在socket上建立管道
channel=connection.channel()#channel管道、渠道
#3，在管道里，声明queuq队列
channel.queue_declare(queue='hello',durable=True)#declare声明
# 4，定义回调函数
def callback(ch,method,properties,body):#properties属性、特征
    print 'ch:', ch
    print 'method:', method
    print 'properties:', properties
    print 'body:', body
    '''
    ch: 管道对象<BlockingChannel impl协议名称=<Channel number管道数量=1 OPEN conn连接实例=<SelectConnection OPEN socket=('::1', 54924, 0, 0)->('::1', 5672, 0, 0) params连接参数=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>>> 
    method: 投递方法<Basic.Deliver(['consumer_tag=ctag1.150ceab0a15940829dda02d4d3b13804',门牌号 'delivery_tag=1',投递数量 'exchange=', 邮局名称，现在为空'redelivered=False',不是重复投递 'routing_key=hello'投递员签名])> 
    properties: 基本属性<BasicProperties> 现在为空
    body: 消息Hello World!
    '''
    time.sleep(5)#模拟断电
    print(" [x] Received %r" % body)#用%r 收到的body加单引号 [x] Received 'Hello World!'
   # 用%s收到的body没单引号 [x] Received Hello World!
    channel.basic_ack(delivery_tag=method.delivery_tag)#向服务器确认手动确认消息处理已完成，可以删除消息了。

# 5，定义接收消息或叫消费消息的语法
# 回调函数callback（意思是如果收到消息就调用callback，像事件驱动），管道名=hello、no_ack=True如果我done了，无须确认，丢弃。
channel.basic_qos(prefetch_count=1)#如果还剩1条消息没处理，就不收。
channel.basic_consume(callback,
                     queue='hello',
                     # no_ack=True#如果我done了，无须确认，丢弃。如果注释掉，那么没收完done了，消息就会存在消息队列中，下次连接时，就会‘全部’重新接收（不是从上次断开的地方开始收）。因为接收操作是原子操作，done了，消息完整保存在消息队列中。
                      # 如果注释了，我done了，别人连接了这个队列，这个消息就会发给别人，并且在别人的method字段：redelivered=False就会变成redelivered=True，表示这是重复收到的消息。
                     #  一般在应用中是注释掉，因为如果done了，消息会保存，还有就是消息处理完了，rabbitmq会把消息从队列中删除。
                     )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 6，开始收消息。一旦启动，就一直收，没有就阻塞-等待。
# 收到的消息是bytes类型的。
channel.start_consuming()
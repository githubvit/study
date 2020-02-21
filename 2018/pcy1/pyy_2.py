#_*_coding:utf-8_*_

# -----------------------进程间通信：消息队列RabbitMQ recv、c端：-----------
# 1，建立socket
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
# 2. 声明管道
channel = connection.channel()
# 3，在管道里，声明queue队列，必须和服务端queue名字一样。#确保声明了管道，有可能是消费端先启动，这样保证管道被声明。否则可能报错。
channel.queue_declare(queue='hello')
# 4，回调函数callback：ch（管道内存对象）、method（）、properties（）、body（消息）
def callback(ch, method, properties, body):
    print 'args1:',ch,'args2:',method,'args3:',properties,'args4:',body
    '''
    args1: 管道对象<BlockingChannel impl=<Channel number=1 OPEN conn=<SelectConnection OPEN socket=('::1', 54924, 0, 0)->('::1', 5672, 0, 0) params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>>> 
    args2: 投递方法<Basic.Deliver(['consumer_tag=ctag1.150ceab0a15940829dda02d4d3b13804门牌号', 'delivery_tag=1投递数量', 'exchange=邮局名称', 'redelivered=False重复投递', 'routing_key=hello投递员就是队列名称'])> 
    args3: <BasicProperties> 
    args4: 消息Hello World!
    '''
    print(" [x] Received %r" % body)
# 5，声明语法：通过管道消费消息（就是收消息），回调函数callback（意思是如果收到消息就调用callback），管道名、noack=True无须确认。
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
# 6，开始收消息。一旦启动，就一直收，没有就阻塞-等待。
channel.start_consuming()
# 7，收到的消息是bytes类型的。

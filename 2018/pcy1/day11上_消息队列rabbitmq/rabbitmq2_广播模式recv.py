# _*_coding:utf-8_*_
'''
广播模式接收端：实时接收，发的时候没有收，就收不到了，因为服务器不存广播消息。
必须声明queue，因为接收端是通过queue绑定exchange收消息
'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
# 声明exchang
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
# 声明随机队列
result = channel.queue_declare(exclusive=True)  # 不指定queue名字,rabbit会随机分配一个名字,
# exclusive=True会在使用此queue的消费者断开后,自动将queue删除

# 获取随机队列的名字
queue_name = result.method.queue
# 管道队列绑定exchange
channel.queue_bind(exchange='logs',
                   queue=queue_name,
                   routing_key=''
                   )

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print 'ch:', ch
    print 'method:', method
    print 'properties:', properties
    print 'body:', body
    print type(body)
    print " [x] %s" %body.decode('utf8')
#管道接收语法
channel.basic_consume(callback,
                      queue=queue_name,#队列名
                      # no_ack=True
                      )
#开始接收
channel.start_consuming()
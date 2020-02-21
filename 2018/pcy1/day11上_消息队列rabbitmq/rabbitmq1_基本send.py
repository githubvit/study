#_*_coding:utf-8_*_

'''
基本模式
'''
import pika

# 生产P-消费C
# send-recv
'''
发送端就是寄信人，往邮筒投信，投完就走了，关闭了。
在基本的情况下，服务器一对多连接是公平-依次分发，轮询机制，负载均衡。
'''
# send、p端：
# 1，建立socket，连接rabbitmq服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
# 2，在socket上建立管道 在管道里发消息
channel = connection.channel()
# 3，在管道里，声明queuq队列名称hello，durable=True表示队列持久化，如果不持久化，服务器done了，再启动，队列就没了。
channel.queue_declare(queue='hello',durable=True)
# 4，通过管道发消息： routing_key=queue名字，body=消息。
for i in range(10):
    msg='Hello World!%s'%i
    channel.basic_publish(
                        exchange='',#交换器名字为空，必须写
                        routing_key='hello',#把routing_key设为管道名,routing线路选择，这是个动作。
                        properties=pika.BasicProperties(
                            delivery_mode=2 #投递模式=2表示消息持久化
                        ),
                        body=msg.decode('utf-8').encode('utf-8'))#消息必须是bytes类型,在py2.7上str和bytes是没有区别的。py3.x必须是bytes，因为是用socket在收发。
print(" [x] Sent 'Hello World!'")
# 5，关闭socket
connection.close()
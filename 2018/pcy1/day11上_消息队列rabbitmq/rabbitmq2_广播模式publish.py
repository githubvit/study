#_*_coding:utf-8_*_

'''
消息广播模式publish发端
没有必要声明queue
因为发端是直接发到exchange
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
# 声明exchange exchange_type='fanout'
channel.exchange_declare(exchange='logs',exchange_type='fanout')#fanout: 所有bind到此exchange的queue都可以接收消息，这就是广播模式。

message = ' '.join(sys.argv[1:]) or "info: Hello World 中文!"
#通过命令行调用sys.argv[1:]参数1，作为消息。如果没有就发or后面的消息
# 定义发送消息的语法及发送消息
channel.basic_publish(exchange='logs',
                      routing_key='',#不进行路线选择，也要写为空。
                      body=message.decode('utf-8').encode('utf-8'))
print(" [x] Sent %r" % message)
connection.close()
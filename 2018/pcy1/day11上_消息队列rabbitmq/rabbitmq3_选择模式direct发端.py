#_*_coding:utf-8_*_

'''
消息选择模式publish发端
没有必要声明queue
因为发端是直接发到exchange
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
# 声明exchange，设定类型为direct
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')
# 用三元表达式来定义一个变量，从命令参数位置1获取变量，没有参数就定义变量为info
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'#severity重要程度
# 从命令参数位置2获取消息，如果没有该参数就设定消息为hello world。
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',#交换器名
                      routing_key=severity,#定义routing_key为三元表达式的变量
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
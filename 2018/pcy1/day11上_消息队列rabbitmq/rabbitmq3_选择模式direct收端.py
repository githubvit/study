# _*_coding:utf-8_*_
'''
选择模式接收端：根据routing_key，绑定queue，实时接收，发的时候没有收，就收不到了，因为服务器不存选择消息。
必须声明queue，因为接收端是通过queue绑定exchange收消息
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
# 声明exchange，定义类型为direct
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')
#声明queue为随机queue，用完就删除该queue。
result = channel.queue_declare(exclusive=True)
# 获取随机queue的名字
queue_name = result.method.queue
# 从命令参数位置1开始一直到最后，获取变量severities的值，是一个参数列表。
severities = sys.argv[1:]
if not severities:#如果命令参数位置没输入,就通过 标准错误 报错提示必须输入的内容，然后退出。
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)
# 循环命令参数列表，获取routing_key的值，管道绑定exchange、queue、routing_key实现选择接收。
for severity in severities:
    channel.queue_bind(exchange='direct_logs',#从哪个exchange接收
                       queue=queue_name,#用哪个queue接收
                       routing_key=severity#选择哪个routing_key接收
                       )

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

#声明接收的语法
channel.basic_consume(callback,
                      queue=queue_name,
                      # no_ack=True
                      )
#开始接收
channel.start_consuming()
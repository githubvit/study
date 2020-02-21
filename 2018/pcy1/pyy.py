#_*_coding:utf-8_*_
# print 'hello word!'
# def sayhai():
#     print 'this in sayhai funcoint'
# def test1():
#     print 'in the test1'
# def test2():
#     print 'in the test2'
#
# sayhai()
# test1()
# test2()
# print (__file__)
# def test1(name,age):
#     name=name
#     age=age

# r1=('Foo', ('typ', 'obje'), {'modul': 'mai', 'metacla':  'MyType'})#元组内的列表和字典都可以增删改查。
# # r1=['typ', 'obje']
# print type(r1)
# print r1
# r1[2]['z']='123'
# print '改后',r1
#-------------------文件状态：os.stat----------
# import os
# print os.path.isfile('水质参数意义.txt'.decode('utf-8'))
# print os.stat('水质参数意义.txt'.decode('utf-8'))

# --------------事件：红绿灯------------

# import time
# import threading
#
#
# event = threading.Event()
#
# def lighter():
#     count = 0
#     event.set() #先设置绿灯
#     while True:
#         if count >5 and count < 10: #改成红灯
#             event.clear() #把标志位清了
#             print("\033[41;1mred light is on....\033[0m")
#         elif count >10:
#             event.set() #变绿灯
#             count = 0
#         else:
#             print("\033[42;1mgreen light is on....\033[0m")
#         time.sleep(1)
#         count +=1
#
# def car(name):
#     while True:
#         if event.is_set(): #代表绿灯
#             print("[%s] running..."% name )
#             time.sleep(1)
#         else:
#             print("[%s] sees red light , waiting...." %name)
#             event.wait()
#             print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)
#
#
# light = threading.Thread(target=lighter,)
# light.start()
#
# car1 = threading.Thread(target=car,args=("Tesla",))
# car1.start()
#-----------------------队列取出顺序：优先级-----------
# import Queue
# q=Queue.PriorityQueue()
# q.put((10,'d1'))
# q.put((1,'d2'))
# q.put((5,'d3'))
#
# print q.get()
# print q.get()
# print q.get()
#
# '''
# (1, 'd2')
# (5, 'd3')
# (10, 'd1')
# '''
# --------------------------------------------------
# import threading,time
#
# import Queue
#
# q = Queue.Queue(maxsize=10)
#
# def Producer(name):
#     count = 1
#     while True:
#         q.put("骨头%s" % count)
#         print"生产了骨头",count
#         count +=1
#         time.sleep(0.2)
#
#
#
# def  Consumer(name):
#     # while q.qsize()>0:
#     while True:
#         print("[%s] 取到[%s] 并且吃了它..." %(name, q.get()))
#         time.sleep(1)
#
#

# p = threading.Thread(target=Producer,args=("Alex",))
# c = threading.Thread(target=Consumer,args=("ChengRonghua",))
# c1 = threading.Thread(target=Consumer,args=("王森",))
#
#
# p.start()
# c.start()
# c1.start()
#------------------------------------------------------socks代理
# import socket
# import socks
# import requests
#
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
# socket.socket = socks.socksocket
# print(requests.get('http://ifconfig.me/ip').text)
# ---------------------进程间通信：消息队列RabbitMQ------------
import pika

# 生产P-消费C
# send-recv
'''
发送端就是寄信人，往邮筒投信，投完就走了，
'''
# send、p端：
# 1，建立socket
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
# 2，声明管道 在管道里发消息
channel = connection.channel()
# 3，在管道里，声明queuq队列
channel.queue_declare(queue='hello')
# 4，通过管道发消息： routing_key=queue名字，body=消息。
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
# 5，关闭socket
connection.close()

'''
# recv、c端：
# 1，建立socket
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
# 2. 声明管道
channel = connection.channel()
# 3，在管道里，声明queue队列，必须和服务端queue名字一样。#确保声明了管道，有可能是消费端先启动，这样保证管道被声明。否则可能报错。
channel.queue_declare(queue='hello')
# 4，回调函数callback：ch（管道内存对象）、method（）、properties（）、body（消息），回调函数处理完了就代表确认收到了消息。
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
# 5，声明语法：通过管道消费消息（就是收消息），回调函数callback（意思是如果收到消息就调用callback），管道名、noack=True无须确认。
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')                      
# 6，开始收消息。一旦启动，就一直收，没有就阻塞-等待。
channel.start_consuming()
# 7，收到的消息是bytes类型的。

'''


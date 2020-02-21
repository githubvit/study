# _*_coding:utf-8_*_
'''
io多路复用之select
'''
'''
Python的select()方法直接调用操作系统的IO接口，
它监控sockets,open files, and pipes(所有带fileno()方法的文件句柄)何时变成readable 和writeable, 或者通信错误，
select()使得同时监控多个连接变的简单，并且这比写一个长循环来等待和监控多客户端连接要高效，
因为select直接通过操作系统提供的C的网络接口进行操作，而不是通过Python的解释器。

注意：Using Python’s file objects with select() works for Unix, but is not supported under Windows.

接下来通过echo server例子要以了解select 是如何通过单进程实现同时处理多个非阻塞的socket连接的
'''

import select
import socket
import Queue

server=socket.socket()


server.bind(('localhost',9998))
server.listen(5)
# 因为select是阻塞（blcok）的，是操作系统内核态完成的，帮socket完成等待，一有消息(fd就绪)就通知socket。
# 所以把socket设置成非阻塞的，就不用等了，这就比单纯的socket高效
server.setblocking(False)
'''
把socket实例添加到要select管理的列表inputs里，达成select多路复用，
先把server这个服务端做为第一个socket实例放进去,
让select开始监控server的文件描述符。
'''

inputs=[server,]
'''
outputs是select监控writeable的对象
'''
outputs=[]
'''
select需要三个列表参数输入，分别对应：要监控哪些io的输入、要监控哪些io的输出、要监控哪些io的异常。
输出三个列表readable列表、writeable列表、exception列表。

一旦这些监控的对象文件描述符产生变化，就会输出相应的变化对象列表readable,writeable,exceptional。
那么用户进程可以遍历，拿到这些对象去做相应的操作。

我们这个例子里，要对所有socket连接实例进行输入监控和异常监控，所以第1个和第3个参数是一样的。

readable,writeable,exceptional=select.select(inputs,outputs,inputs)
'''

msg_direct={}#为每个连接建立消息队列字典

while True:
    readable,writeable,exceptional=select.select(inputs,outputs,inputs)#阻塞，监控每个过来的连接，
    print readable,writeable,exceptional

    for r in readable:#当输入信号变化，这里就是你告诉了socket对象有连接过来，
        if r is server:#如果信号是server时，代表是有新连接建立，就要等待接收。
            print r
            conn,addr=server.accept()#把过来的新连接实例化成新连接对象
            inputs.append(conn)#把新连接对象加入监控对象列表
            print '有新连接过来conn:',conn
            msg_direct[conn] = Queue.Queue() # 建立每个新连接对象的队列
        else:#如果不是新连接，就代表是已建立的连接发过来了消息
            print '有消息过来'
            data=r.recv(1024)#收消息
            if not data:#如果收不到data代表什么呢? 代表客户端断开了呀
                print '断开连接',r
                #清理，从所有列表删除
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                #清理消息字典，删除该连接的消息队列
                del msg_direct[r]
            else:
                print data
                msg_direct[r].put(data)#把收到的该对象的消息放进自己的队列
                outputs.append(r)#把该连接对象放进输出监控列表what

    for w in writeable:#当输出信号变化，就是告诉要进行输出
        print '要发送消息给客户端',w
        data_to_client=msg_direct[w].get()#从消息队列字典里取出该连接的消息
        w.send(data_to_client)#发送给相应客户端
        outputs.remove(w)#从输出列表删除，不然会越来越多

    for e in exceptional:#当有异常发生，就删除。
        print '处理异常',e
        # 开始清理
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        e.close()
        #删除该连接队列，清理消息队列字典
        del msg_direct[e]

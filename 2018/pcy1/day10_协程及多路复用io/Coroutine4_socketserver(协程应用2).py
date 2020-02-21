# _*_coding:utf-8_*_
'''
单线程多并发的socketserver
协程实现的socketserver并发
在windows不能超过1024个socket连接
IOError: cannot watch more than 1024 sockets

给客户端的响应非常快，比select和epoll做的socket server快，快很多。
'''

import sys
import socket
import time
import gevent

from gevent import socket, monkey

monkey.patch_all()


def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)
        #协程：把每个客户端连接过来的实例cli交给handle_request处理,启动一个协程（py自带socketserver模块是启动一个线程）
        #这种逻辑和py自带socketserver模块要求的写法一致。


def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print"recv:", data.decode('utf-8')
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)#这是关闭客户端，发个wr信号什么的，直接在这里break也可以

    except Exception as  ex:
        print(ex)
    finally:
        # pass
        conn.close()
if __name__ == '__main__':
    server(8001)
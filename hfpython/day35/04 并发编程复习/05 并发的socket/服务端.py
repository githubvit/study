from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import socket


def talk(conn):
    while True:
        try:
            data = conn.recv(1024)  # 1024 接收数据的最大限制
            if not data: break  # 针对linux系统
            conn.send(data.upper())  # 注意：收发都是以bytes为单位
        except ConnectionResetError:
            break
    conn.close()

def serve_forever(ip,port,func):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # print(server)

    #服务端和客户端都需要有ip和port，但 只有服务端才绑定ip和port
    server.bind((ip,port))
    server.listen(5) # 半连接池：限制的是请求数，而不是连接数
    tpool=ThreadPoolExecutor(3)
    while True:
        conn,client_addr=server.accept() # 等待客户端发来连接请求
        print(conn)
        # t=Thread(target=talk,args=(conn,))
        # t.start()
        tpool.submit(func,conn)
    server.close()


if __name__ == '__main__':
    serve_forever('127.0.0.1',8080,talk)
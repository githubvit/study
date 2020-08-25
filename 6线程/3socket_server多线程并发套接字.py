# import socket

# server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind(('127.0.0.1',8081))
# server.listen(5)

# while True:
#     conn,cli_addr=server.accept()
#     print('%s连接,来自%s'%(conn,cli_addr))

#     while True:
#         try:
#             data=conn.recv(1024)
#             if not data:break
#             conn.send(data.upper())
#         except ConnectionResetError:
#             break
#     # print('关闭来自[%s]的连接'%(cli_addr))  # 报错，元组作为一个元素要加‘，’
#     # typeError: not all arguments converted during string formatting
#     print('关闭来自[%s]的连接'%(cli_addr,))  # 加','，表示该元组作为一个元素，就解决了。  
#     conn.close()
# server.close()

# socket多线程改造
# 1 客户端不用改.
# 2 服务端把通信循环和链接循环两个功能独立出来。

from threading import Thread
import socket

# 收发 通信循环
def communication(conn,cli_addr):
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    # print('关闭来自[%s]的连接'%(cli_addr))  # 报错，元组作为一个元素要加‘，’
    # ypeError: not all arguments converted during string formatting
    print('关闭来自[%s]的连接'%(cli_addr,))  # 加','，表示该元组作为一个元素，就解决了。  
    conn.close()
    
# 服务 链接循环
def server(ip,port):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)

    while True:
        conn,cli_addr=server.accept()
        print('%s连接,来自%s'%(conn,cli_addr))
        # 建立新线程 开启收发
        t=Thread(target=communication,args=(conn,cli_addr))
        t.start()
    server.close()

if __name__ == "__main__":
    server('127.0.0.1',8081)
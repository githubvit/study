# 协程socket
from gevent import spawn,monkey; monkey.patch_all() # 标记IO
import socket,time,os

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
    # typeError: not all arguments converted during string formatting
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
        # 建立连接协程 这里就不用join
        spawn(communication,conn,cli_addr)
        # 这样当阻塞时，server任务和communitcation任务两者之间就会不停的来回切换
        # 由于切换的非常快，当有链接就立即连上了，当有通信就立即收发了，
        # 因此每个客户端感觉都是在独占服务端。
        # 这就实现了单线程下的并发。
        # 用一个线程的协程方式高效率应对500个独立的客户端线程。
    server.close()

if __name__ == "__main__":
    #建立服务协程对象
    # g=spawn(server,'127.0.0.1',8081) 
    # g.join()#这一行保证协程永远执行，没有就直接结束了
    server('127.0.0.1',8081)
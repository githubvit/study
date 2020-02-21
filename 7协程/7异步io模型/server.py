# 在io模型中是效率最高的，
# 就是线程池 异步+回调机制


from concurrent.futures import ThreadPoolExecutor
import socket,time,os

# 收发 通信循环
def communication(obj):
    res=obj.result()
    conn=res[0]
    cli_addr=res[1]
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
def server_forever(server):
    conn,cli_addr=server.accept()
    print('%s连接,来自%s'%(conn,cli_addr))
    return (conn,cli_addr)
   
    

if __name__ == "__main__":
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',8081))
    server.listen(5)
    pool=ThreadPoolExecutor(3)
    while True:
        pool.submit(server_forever,server).add_done_callback(communication)



# 模拟500个线程
from threading import Thread,current_thread
import socket

def client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('127.0.0.1',8081))

    while True:
        msg='%s say hello'%current_thread().getName()
        print(msg)
        client.send(msg.encode('utf-8'))
        res=client.recv(1024)
        print(res)
    client.close()

if __name__ == "__main__":
    for i in range(500):
        t=Thread(target=client)
        t.start()
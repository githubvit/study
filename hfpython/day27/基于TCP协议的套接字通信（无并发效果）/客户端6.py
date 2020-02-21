import socket
import time

while True:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.connect(('127.0.0.1',8080))
        break
    except ConnectionRefusedError:
        time.sleep(3)
        print('等待3秒。。。')

while True:
    msg=input('>>>: ').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    data=client.recv(1024)
    print(data.decode('utf-8'))

client.close()
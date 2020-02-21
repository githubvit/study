import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8081))

while True:
    msg=input('>>')
    if not msg:
        continue
    if msg=='n':
        break
    client.send(msg.encode('utf-8'))
    res=client.recv(1024)
    print(res)
client.close()
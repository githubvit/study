from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
# print(client)

while True:
    cmd=input('>>>: ').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))
    # print('has send')
    res=client.recv(14744)
    # print('has recv')
    print(len(res))
    print(res.decode('gbk'))

client.close()
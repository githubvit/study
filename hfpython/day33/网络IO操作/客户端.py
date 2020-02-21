from socket import *

client = socket()
client.connect(('127.0.0.1', 8080))

while True:

    data = input('>>: ').strip()
    if not data:continue
    client.send(data.encode('utf-8'))
    print('has send')


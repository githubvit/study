from socket import *
import time

s = socket()
s.bind(('127.0.0.1',8080))
s.listen(5)
s.setblocking(False)

r_list=[]
while True:
    try:
        conn, addr = s.accept()
        r_list.append(conn)

    except BlockingIOError:
        # time.sleep(3)
        print('可以去干其他的活了')
        print('rlist: ',len(r_list))
        for conn in r_list:
            try:
                data=conn.recv(1024)
                conn.send(data.upper())
            except BlockingIOError:
                continue

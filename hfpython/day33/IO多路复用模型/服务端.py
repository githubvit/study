from socket import *
import select

s = socket()
s.bind(('127.0.0.1',8080))
s.listen(5)
s.setblocking(False)
# print(s)

r_list=[s,]
w_list=[]
w_data={}
while True:
    print('被检测r_list： ',len(r_list))
    print('被检测w_l ist： ',len(w_list))
    rl,wl,xl=select.select(r_list,w_list,[],) #r_list=[server,conn]

    # print('rl: ',len(rl)) #rl=[conn,]
    # print('wl: ',len(wl))

    # 收消息
    for r in rl: #r=conn
        if r == s:
            conn,addr=r.accept()
            r_list.append(conn)
        else:
            try:
                data=r.recv(1024)
                if not data:
                    r.close()
                    r_list.remove(r)
                    continue
                # r.send(data.upper())
                w_list.append(r)
                w_data[r]=data.upper()
            except ConnectionResetError:
                r.close()
                r_list.remove(r)
                continue

    # 发消息
    for w in wl:
        w.send(w_data[w])
        w_list.remove(w)
        w_data.pop(w)

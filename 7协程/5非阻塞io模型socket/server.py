# 非阻塞IO模型 server

import socket,time

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8081))
server.listen(5)

# 设置为非阻塞，这样所有的阻塞都会报错 accept、recv、send
# 后面的程序要try except捕捉错误
# 也可以理解为不是报错是提示，那后面跟着提示处理就可以了。
server.setblocking(False)

# 定义两个列表，便于收发和捕捉阻塞
# 1 收消息的列表叫读列表
r_list=[]
# 2 发消息的列表叫写列表
w_list=[]

while True:
    try: 
        conn,cli_addr=server.accept()
        # 不阻塞 有链接来了 把链接对象加入链接列表 读列表
        r_list.append(conn)
    except BlockingIOError: # 处理accept阻塞 即没链接过来
        # 由于是非阻塞模型，因此资源占用非常高，解决该问题，就人为添加阻塞
        # time.sleep(0.5)
        # accept阻塞 就处理recv
        print('accept阻塞处理recv')
        print('链接对象r_list:',len(r_list))
        print('发送对象w_list:',len(w_list))
        # 收消息 recv
        # 设置删除对象列表，便于清理断开连接的客户端连接对象
        del_rlist=[]
        for conn in r_list:
            try:
                data=conn.recv(1024)
                if not data: # linux 处理客户端断开连接 抛空
                    conn.close()
                    # 把该链接加入要删除的链接对象列表
                    del_rlist.append(conn)
                    # 处理下一个链接对象
                    continue
                # 不阻塞 就把链接和要发送的数据放入发送列表 写列表
                w_list.append((conn,data.upper()))
            except BlockingIOError: # 处理recv阻塞
                continue #这个链接对象recv阻塞 就看下个链接对象的recv
            except ConnectionResetError: #windows 处理客户端断开链接 抛异常
                conn.close()
                # 把该链接加入要删除的链接对象列表
                del_rlist.append(conn)
        # 回收收空连接
        for conn in del_rlist:
            r_list.remove(conn)


        # 发消息
        # 设置发消息删除对象列表
        del_wlist=[]    
        for item in w_list:
            try:
                conn=item[0]
                res=item[1]
                conn.send(res)
                # 发成功后 删除该item 把item 放入发消息删除对象列表
                del_wlist.append(item)
            except BlockingIOError:
                continue
            except ConnectionResetError: 
                conn.close()
                del_wlist.append(item)
        # 回收发成功的连接
        for item in del_wlist:
            w_list.remove(item)
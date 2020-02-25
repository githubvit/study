# io多路复用select模型

# select 就是在 非阻塞模型的基础上，给每个任务增加了超时时间。
# 这样就不会独占cpu了。

# select参数 （r_list,w_list,x_list,timeout）三个列表 一个超时时间
# 三个套接字对象列表 收消息列表 发消息列表 异常列表
# 主要就用 收和发列表
# 输出三个有链接套接字对象列表rl\wl\xl。

# select工作过程 代理套接字对象和系统打交道，自动处理阻塞错误。
# 代收：从收列表中取出socket套接字对象进行接收，一旦接收成功，就不停通知套接字对象，直到取走。
#   1. 先要把server这个套接字对象放入收列表，一旦客户端有连接，select就会在输出的rl中添加该对象。
#   2. 通过循环rl使用该对象，如果对象是server,就可以accept接收。如果对象是conn，既可以recv接收。    
# 代发：从发列表中取出socket套接字对象进行发送，一旦发送成功，就通知套接字对象。

# 由于非阻塞模型独占cpu，对系统不太友好。
# 所以，有了io多路复用select模型，
# 该模型单任务（服务端只有1个套接字对象）效率甚至不如阻塞io，
# 其应用场景主要针对多任务

import socket,select,time

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8081))
server.listen(5)

# 设置为非阻塞，这样所有的阻塞都会报错 accept、recv、send
# 后面的程序要try except捕捉错误
# 也可以理解为不是报错是提示，那后面跟着提示处理就可以了。
# select会自动处理这些错误。send的阻塞要自己处理
# server.setblocking(False)

# 定义两个列表，便于收发和捕捉阻塞
# 1 收消息的套接字对象列表叫读列表，要先把server放入列表，这样一旦客户端连接过来，就可以accept;
r_list=[server,]
# 2 发消息的套接字对象列表叫写列表
w_list=[]
# 3 发消息的数据字典,以套接字对象为key.
w_data={}

while True:
    # 用select和系统打交道，如果都没有收发，则轮询3秒，再往下运行。
    # 一旦某个套接字有收发（即rl\wl中的len不是零，有套接字对象了），
    # 则立即不停催动下面的代码执行。
    rl,wl,xl=select.select(r_list,w_list,[],3)
    print('收',len(rl))
    print('发',len(wl))
    # 收消息
    for r in rl:
        if r is server:
            conn,cli_addr=r.accept()
            # 把客户端套接字对象放入收列表r_list中
            r_list.append(conn)
        else:
            try:
                data=r.recv(1024)
                if not data:
                    r.close()
                    r_list.remove(r)
                    continue
                # 收到数据，把该对象加入发消息列表
                w_list.append(r)
                # 添加要发送给该对象的数据
                w_data[r]=data.upper()   
            except ConnectionResetError:#处理客户端连接断开
                # 回收该连接
                r.close()
                # 在收列表r_list中删除该套接字对象
                r_list.remove(r)

    # 发消息
    for w in wl:
        try:
            w.send(w_data[w])
            # 发送成功后要删除
            # 在发列表w_list中删除该套接字对象
            w_list.remove(w)
            # 删除该对象的数据
            del w_data[w]
        except BlockingIOError:
            continue    
        except ConnectionResetError:
            # 回收该连接
            w.close()
            # 在发列表w_list中删除该套接字对象
            w_list.remove(w)
            # 删除该对象的数据
            del w_data[w]
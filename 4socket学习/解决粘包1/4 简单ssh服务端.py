import socket,subprocess,struct

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8090))
server.listen(5)
print('starting....')
#链接循环
while True:
    conn,addr=server.accept()
    print(conn,addr)
    # 通信循环
    while True:
        try:
            cmd=conn.recv(1024)
            if not cmd:break #解决Linux线路故障，连续抛空
            cmd=cmd.decode()
            print('执行命令cmd：',cmd)
            # 把命令的结果装入管道
            res=subprocess.Popen(cmd,shell=True,
            stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            #取出结果（正确和错误）
            stdout=res.stdout.read()
            stderr=res.stderr.read()
            #封装报头
             # 解决 粘包 关键在于 保证每次 收发 都干净
            # 发：
            # 1 先把要发送字节的大小算出来
            size=len(stdout)+len(stderr)
            print('server端发送的文件大小为：',size)
            # 2 用struct模块按‘i’格式，把每次算出的大小统一封装成固定字节位数，就是4个bytes。
            header=struct.pack('i',size)#对于数字用格式‘i’封    
            # 3 把上面的固定字节位数命名成报头heard
            # 4 发送报头
            conn.send(header)
            # 5 发送数据
            conn.send(stdout)
            conn.send(stderr)
            # 总结：上面实际定义了报文格式，根据tcp传输层nagle算法，
            # 因为报头数据足够小（4个bytes），报头和数据发送的时间间隔也足够小（ 连续发送），
            # 所以tcp传输层会把报头和数据一起发送。

            # 收
            # 接收方实际就收到了一次发送过来的，报头和数据在一起的打包数据。     
            # 那么接收方只要先取出4个bytes即报头，就可以知

        except ConnectionResetError: #处理windows线路异常抛错
            break
    # 回收该conn的实例,进入下一个链接循环，等待获取新的conn
    print('回收的conn实例为：',conn) 
    conn.close()
server.close()
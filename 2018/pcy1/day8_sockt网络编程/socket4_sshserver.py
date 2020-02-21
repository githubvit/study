#_*_coding:utf-8_*_
'''
socket ssh服务器
'''
import socket,os
server=socket.socket()
server.bind(('localhost',9999))#只能有一个参数,用元组。
server.listen(5)
while True:
    conn,addr=server.accept()
    print '新连接建立：',addr
    while True:
        print '等待新指令'
        data=conn.recv(1024)#python 3.x必须decode，否则报错。而python2.7不能decode，否则报错。
        if not data:
            print ('客户端已断开')
            break
        print('执行命令-->>%s' % data)
        cmd_res=os.popen(data).read()#执行命令，取得结果
        '''
        同样的一段字符串，特别是中文的存在，其str大小、Unicode大小、bytes大小完全不同，
        发送的大小到底用哪种？
        '''
        print '发送的str大小', len(cmd_res)
        print '发送的unicode大小', len(cmd_res.decode('gbk'))
        print '发送的bytes大小',len(cmd_res.decode('gbk').encode('utf8'))#用这个比大小，因为发送的都是bytes。
        if len(cmd_res)==0:
            cmd_res='%s命令没有输出结果。。。'%data
            cmd_res=cmd_res.decode('utf8').encode('gbk')
        # 因为send的时候为了匹配windows命令结果，要用gbk字符集decode成Unicode，所以这里编码成gbk，就可以一致了。
        # 当然在linux做为服务器时就不必了，因为执行的是linux命令，所有的gbk都要改成utf8。
        conn.send(str(len(cmd_res.decode('gbk').encode('utf8'))).encode('utf8'))#为保持同步，先把大小发送给客户端
        # python 2.7是既可以发送bytes，也可以发送str的：conn.send(str(len(cmd_res.decode('gbk').encode('utf8'))))
        # python3.x是不可以的，只能发送bytes类型。
        # len()是数字类型，数字类型是没有encode的，必须转成str后才能encode。
        client_ack=conn.recv(1024)#克服粘包
        print '克服粘包',client_ack
        conn.send(cmd_res.decode('gbk').encode('utf8'))
        print '发送完毕'
server.close()

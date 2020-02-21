# _*_coding:utf-8_*_
'''
io多路复用之epoll
'''
'''
Python的epoll模块是selectors
该模块是python3.4之后才有的，因此在虚拟机win7上才可以试出来。当然在linux上才可以使用epoll。
它具有根据平台选出最佳的IO多路机制，比如在win的系统上他默认的是select模式，而在linux上它默认的是epoll。
在Windows下和select没有什么差别，最多到500个socket，但代码要少很多。
在linux下跑到了8000个socket，没敢往上加了。
'''
import selectors
import socket
# 建立epoll对象sel
sel = selectors.DefaultSelector()#根据平台选择最佳的IO多路机制，比如linux就会选择epoll

#建立新连接的回调函数
def accept(sock, mask):
    conn, addr = sock.accept()  # 将新连接实例化为新连接对象
    print('accepted', conn, 'from', addr)
    # 将新连接对象设置为非阻塞
    conn.setblocking(False)
    # epoll对象将新连接对象注册到可读事件selectors.EVENT_READ中，回调函数定义为read。
    sel.register(conn, selectors.EVENT_READ, read)

# 建立连接消息的回调函数
def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:#如果收不到
        print('closing', conn)
        # 就从epoll对象注销该socket对象
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 9996))
sock.listen(100)
# 设置sock为非阻塞
sock.setblocking(False)
'''
事件驱动模型
# 调用sel的register方法，将种子sock添加到sel的可读事件selectors.EVENT_READ中
# 一旦种子sock有变化就调用accept方法。就是新连接过来，accept就是新连接的回调函数。
'''
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()#启动epoll对象开始阻塞
    print ('看', events)
    for key, mask in events:
        print (key, mask)
        callback = key.data#这个就是回调函数的地址，新连接是accept，消息发送就是read
        print (callback)
        callback(key.fileobj, mask)#回调函数加上括号和参数

'''
1,刚连接，还未发数据
看 [(SelectorKey(fileobj=<socket.socket fd=228, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 9999)>, fd=228, events=1, data=<function accept at 0x0000000000A4F7B8>), 1)]
SelectorKey(fileobj=<socket.socket fd=228, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 9999)>, fd=228, events=1, data=<function accept at 0x0000000000A4F7B8>) 1
<function accept at 0x0000000000A4F7B8>
accepted <socket.socket fd=224, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.2.208', 9999), raddr=('192.168.2.191', 62245)> from ('192.168.2.191', 62245) 1

2，发数据后
看 [(SelectorKey(fileobj=<socket.socket fd=224, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.2.208', 9999), raddr=('192.168.2.191', 62245)>, fd=224, events=1, data=<function read at 0x0000000000A4FA60>), 1)]
SelectorKey(fileobj=<socket.socket fd=224, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.2.208', 9999), raddr=('192.168.2.191', 62245)>, fd=224, events=1, data=<function read at 0x0000000000A4FA60>) 1
<function read at 0x0000000000A4FA60>
echoing b'123456' to <socket.socket fd=224, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.2.208', 9999), raddr=('192.168.2.191', 62245)>



'''
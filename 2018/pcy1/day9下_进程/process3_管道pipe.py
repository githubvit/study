#_*_coding:utf-8_*_
'''
多进程之间数据传递方式2-采用管道收发数据
进程1为一端send和recv
进程2为一端send和recv
看起来像socket
'''
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child3'])
    print("child recv",conn.recv())
    conn.close()


if __name__ == '__main__':
    #1，定义管道，一个管道有两端
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))#起一个进程，把管道一端做为参数
    p.start()
    print("parent recv1",parent_conn.recv())
    print("parent recv2",parent_conn.recv())
    parent_conn.send(" from parent")
    p.join()
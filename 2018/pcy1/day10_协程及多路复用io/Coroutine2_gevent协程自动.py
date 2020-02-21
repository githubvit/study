#_*_coding:utf-8_*_
'''
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，
在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。 
Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。
gevent.sleep()模仿io操作，因为Gevent就是碰到io就切换，实现协程的自动切换
'''

import gevent
'''
gevent就是碰到io就切换，实现协程的自动切换
io操作在计算机中属于比较慢的操作，比如网络io、硬盘读写序列化等。
gevent碰到io就切换——就屏蔽了io较慢的操作，集中精力于CPU计算。
'''

def foo():
    print('1Running in foo')
    gevent.sleep(2)#模仿io操作，因为Gevent就是碰到io就切换，实现协程的自动切换
    print('6Explicit context switch to foo again')
def bar():
    print('2Explicit精确的 context内容 to bar')
    gevent.sleep(1)
    print('5Implicit context switch back to bar')
def func3():
    print("3running func3 ")
    gevent.sleep(0)
    print("4running func3  again ")


gevent.joinall([#像多进程的pool，列表方式添加
    gevent.spawn(foo), #生成一个协程
    gevent.spawn(bar),
    gevent.spawn(func3),
])
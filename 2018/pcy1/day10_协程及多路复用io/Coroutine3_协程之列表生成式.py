#_*_coding:utf-8_*_
'''
同步与异步的性能区别
'''
import gevent


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(0.5)#模拟io操作
    print('Task %s done' % pid)


def synchronous():#这里是同步io操作，会生成10个任务，是串行。
    for i in range(1, 10):
        task(i)


def asynchronous():#这里是异步io操作，会生成10个协程，是并行，类似时分复用，这里是碰到io操作就分，io分复用。
    '''
    注意下面的这段写法
    1，用threads 列表生成式生成了10个协程gevent.spawn(task, i)，
    2，把列表统一放入协程池gevent.joinall(threads)
    :return: 
    '''
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
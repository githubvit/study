#_*_coding:utf-8_*_
'''
协程，又称微线程，纤程。英文名Coroutine。单线程下实现多并发的效果。
协程是用户自己定义的，与硬件无关，cpu根本不知道协程的存在。
也就是说协程是软件实现。
一句话说明什么是协程：协程是一种用户态的轻量级线程。

协程拥有自己的寄存器上下文和栈。
注意了：线程的上下文和栈会保存在CPU的寄存器中，因为线程是CPU的最小调度单位。
而CPU是不知道协程的存在的，因此，协程的寄存器也是用户自己实现的。

协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈。
因此：
协程能保留上一次调用时的状态（即所有局部状态的一个特定组合），每次过程重入时，就相当于进入上一次调用的状态，
换种说法：进入上一次离开时所处逻辑流的位置。



协程的好处：

无需线程上下文切换的开销——因为是单线程，不涉及cpu寄存器开销。
无需原子操作锁定及同步的开销
　　"原子操作(atomic operation)是不需要synchronized"，所谓原子操作是指不会被线程调度机制打断的操作；
    这种操作一旦开始，就一直运行到结束，中间不会有任何 context switch （切换到另一个线程）。
    原子操作可以是一个步骤，也可以是多个操作步骤，但是其顺序是不可以被打乱，或者切割掉只执行部分。
    视作整体是原子性的核心。方便切换控制流，简化编程模型
高并发+高扩展性+低成本：一个CPU支持上万的协程都不是问题。所以很适合用于高并发处理。
 

缺点：

无法利用多核资源：协程的本质是个单线程,它不能同时将单个CPU 的多个核用上,协程需要和进程配合才能运行在多CPU上.
当然我们日常所编写的绝大部分应用都没有这个必要，除非是cpu密集型应用。

进行阻塞（Blocking）操作（如IO时）会阻塞掉整个程序
'''

'''
符合什么条件就能称之为协程：

必须在只有一个单线程里实现并发
修改共享数据不需加锁
用户程序里自己保存多个控制流的上下文栈
一个协程遇到IO操作自动切换到其它协程
'''


# 原来用生成器yeid实现过生产-消费模型，就是很接近协程了
# 这个就是在单线程下实现了两个函数直接的切换，就好像执行了两个任务。
#
# def consumer(name):
#     print("--->starting eating baozi...")
#     while True:
#         new_baozi = yield
#         print("[%s] is eating baozi %s" % (name, new_baozi))
#         # time.sleep(1)
#
#
# def producer():
#     con.next()
#     con2.next()
#     n = 0
#     while n < 5:
#         n += 1
#         print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
#         con.send(n)
#         con2.send(n)
#
#
#
# if __name__ == '__main__':
#     con = consumer("c1")
#     con2 = consumer("c2")
#     p = producer()


#实际上python有协程包greenlet，用这个可以实现协程
# 在单线程下，实现多个任务之间的切换。

#
from greenlet import greenlet
def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()
def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1) #启动一个携程
gr2 = greenlet(test2)
gr1.switch()
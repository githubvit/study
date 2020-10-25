from threading import Timer
import threading
cnt=0
   
def one():
    global cnt
    cnt+=1
    print(cnt)
    timer = Timer(5, one)
    timer.start()
    print("threading active = {} \n   \n".format(threading.enumerate())) 
    #打印线程后发现，每次都会创建一个新的子线程，虽然活跃的线程只有一个，但是也是种资源浪费：

# one()

# threading active = [<_MainThread(MainThread, stopped 7948)>, <Timer(Thread-24, started 3612)>, <Timer(Thread-25, started 9804)>] t
# threading active = [<_MainThread(MainThread, stopped 7948)>, <Timer(Thread-25, started 9804)>, <Timer(Thread-26, started 1760)>] t
# threading active = [<_MainThread(MainThread, stopped 7948)>, <Timer(Thread-26, started 1760)>, <Timer(Thread-27, started 9908)>] t
# threading active = [<_MainThread(MainThread, stopped 7948)>, <Timer(Thread-27, started 9908)>, <Timer(Thread-28, started 9808)>] t
# threading active = [<_MainThread(MainThread, stopped 7948)>, <Timer(Thread-28, started 9808)>, <Timer(Thread-29, started 8432)>]t
# threading active = [<_MainThread(MainThread, stopped 7948)>, <Timer(Thread-29, started 8432)>, <Timer(Thread-30, started 9596)>]
'''
阅读源码和文档

class Timer(Thread):
    """Call a function after a specified number of seconds:

            t = Timer(30.0, f, args=None, kwargs=None)
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting

    """

    def __init__(self, interval, function, args=None, kwargs=None):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.finished = Event()

    def cancel(self):
        """Stop the timer if it hasn't finished yet."""
        self.finished.set()

    def run(self):
        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()

# Special thread class to represent the main thread
# This is garbage collected through an exit handler

'''

# 发现，其实Timer是threading的子类，用wait实现了定时效果，绑定了入参function，于是修改代码如下


def startTimer():
    global timer
    if timer != None:
        timer.finished.wait(5)
        
        # timer.function()
        if timer.finished.is_set:
            timer.function()
        else:
            timer.finished.clear()
    # else:
    #     timer = threading.Timer(3, countup)
    #     timer.start()
def kill_timer():
    print('输入q，退出定时器')
    inp=input('>>: ').strip()
    if inp=='q':
        timer.finished.clear()
        # timer.cancel()

def countup():
    global cnt
    cnt+=1
    print(cnt)
    print("threading active = {} \n   \n".format(threading.enumerate())) 
    timer = Timer(5, countup)
    kill_timer()
    startTimer()
    # timer.start()
    
 

# countup() # 报错 NameError: name 'timer' is not defined
timer = Timer(3, countup)    
timer.start()

# 始终只有一个线程且重复调用函数方法~End~
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 
# threading active = [<_MainThread(MainThread, stopped 10448)>, <Timer(Thread-1, started 5424)>] 
# 


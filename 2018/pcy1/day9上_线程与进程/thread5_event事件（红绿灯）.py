#_*_coding:utf-8_*_
'''
事件event
多线程间协调用的，保持同步，
    1,set 2,clear 3,wait 4,is_set
    红绿灯案例
        红绿灯是全局变量-事件对象，
        变灯：调节红绿灯是一个线程 set绿灯 clear红灯
        开车：车的跑和等是一个线程 用is_set检查灯是不是绿灯，如果是就跑，否则用wait卡住
'''
import threading,time
# 建立事件为全局变量
event = threading.Event()

def lighter():
    count = 0
    event.set() #先设置绿灯
    while True:
        if count >5 and count < 10: #改成红灯
            event.clear() #把标志位清了
            print("\033[41;1mred light is on....\033[0m")
        elif count >10:
            event.set() #变绿灯
            count = 0
        else:
            print("\033[42;1mgreen light is on....\033[0m")
        time.sleep(1)
        count +=1

def car(name):
    while True:
        if event.is_set(): #代表绿灯
            print("[%s] running..."% name )
            time.sleep(1)
        else:
            print("[%s] sees red light , waiting...." %name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)

# 变灯
light = threading.Thread(target=lighter,)
light.start()
# 开车
car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()


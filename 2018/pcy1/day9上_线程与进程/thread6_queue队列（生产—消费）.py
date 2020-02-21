#_*_coding:utf-8_*_
'''
队列queue 有顺序，取走一个就少一个。

    py2.7格式是大写
        import Queue
        q=Queue.Queue()
    py3.x格式是小写
        import queue
        q=queue.Queue()

    1，put放进去 get取出来 qsize查看数量
    2，q=Queue.Queue()先入先出
    3，get()取不到的时候会卡住，等着放进去;这时候用get_nowait()(或者get(block=False))就不会卡住,会出queue.Empty异常。
    4,设q=Queue.Queue(maxsize=3) maxsize最多数量，put到4的时候，还put会卡住。
        用put（timeout=1）放不进会等一秒，就不卡了。
    5，q=Queue.LifoQueue()后入先出
    6，q=Queue.PriorityQueue()优先级，put设置优先级用元组，按元组[0]位置排序，按ASCII码。
            import Queue
            q=Queue.PriorityQueue()
            q.put((10,'d1'))
            q.put((1,'d2'))
            q.put((5,'d3'))

            print q.get()
            print q.get()
            print q.get()

            
            运行结果
            (1, 'd2')
            (5, 'd3')
            (10, 'd1')
            
    队列经典应用
        生产-消费模型 put-get，注意put的时间和get的时间，不要造成get不到卡住的问题。
'''
import threading,time
import Queue
q=Queue.Queue(maxsize=10)

def Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print "生产了骨头",count
        count +=1
        # time.sleep(0.1)



def  Consumer(name):
    #while q.qsize()>0:
    while True:
        print("[%s] 取到[%s] 并且吃了它..." %(name, q.get()))
        time.sleep(0.1)



p = threading.Thread(target=Producer,args=("Alex",))
c = threading.Thread(target=Consumer,args=("ChengRonghua",))
c1 = threading.Thread(target=Consumer,args=("王森",))


p.start()
time.sleep(1)#让生产先干，毕竟有两个消费，如果get不到就会卡死
c.start()
c1.start()

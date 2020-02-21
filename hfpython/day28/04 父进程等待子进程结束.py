# from multiprocessing import Process
# import time
#
# x=1000
#
# def task():
#     time.sleep(3)
#     global x
#     x=0
#     print('儿子死啦',x)
#
#
# if __name__ == '__main__':
#     p=Process(target=task)
#     p.start()
#
#     p.join() # 让父亲在原地等
#     print(x)






# from multiprocessing import Process
# import time,random
#
# x=1000
#
# def task(n):
#     print('%s is runing' %n)
#     time.sleep(n)
#
# if __name__ == '__main__':
#     start_time=time.time()
#
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#     p1.start()
#     p2.start()
#     p3.start()
#
#     p3.join() #3s
#     p1.join()
#     p2.join(    )
#
#     print('主',(time.time() - start_time))


    # start_time=time.time()
    # p_l=[]
    # for i in range(1,4):
    #     p=Process(target=task,args=(i,))
    #     p_l.append(p)
    #     p.start()
    #
    # for p in p_l:
    #     p.join()
    #
    # print('主',(time.time() - start_time))




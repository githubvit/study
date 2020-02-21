4月24日作业
	1、改写下列程序，分别别实现下述打印效果

	from multiprocessing import Process
	import time
	import random

	def task(n):
	    time.sleep(random.randint(1,3))
	    print('-------->%s' %n)

	if __name__ == '__main__':
	    p1=Process(target=task,args=(1,))
	    p2=Process(target=task,args=(2,))
	    p3=Process(target=task,args=(3,))

	    p1.start()
	    p2.start()
	    p3.start()

	    print('-------->4')
	效果一：保证最先输出-------->4

	-------->4
	-------->1
	-------->3
	-------->2
	效果二：保证最后输出-------->4

	-------->2
	-------->3
	-------->1
	-------->4
	效果三：保证按顺序输出

	-------->1
	-------->2
	-------->3
	-------->4
	2、判断上述三种效果，哪种属于并发，哪种属于串行？


	3、基于多进程实现并发的套接字通信
		提示：需要在server.bind(('127.0.0.1',8080))之前添加一行
			server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

		思考每来一个客户端，服务端就开启一个新的进程来服务它，这种实现方式有无问题？



	4、预习互斥锁，编写模拟抢票程序：http://www.cnblogs.com/linhaifeng/articles/7428874.html#_label5






















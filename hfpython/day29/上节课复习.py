上节课复习
    1、创建进程的两种方式
        方式一：
        from multiprocessing import Process

        def task(name):
            print('%s is running' %name)

        if __name__ == '__main__':
            obj=Process(taget=task,args=('egon',))
            obj.start() # 发送信号给操作系统
            print('主')
            task('xxx')

        方式二：
        from multiprocessing import Process

        class MyTask(Process):
            def run(self):
                print('%s is running' %self.name)

        if __name__ == '__main__':
            obj=MyTask()
            obj.start() # 发送信号给操作系统

    2、进程之间地址空间隔离
    3、进程对象的其他方法
        obj.join(1)

        obj.terminate()
        obj.is_alive()

        obj.pid
        obj.name

    4、僵尸进程与孤儿进程







今日内容：
    守护进程（了解）
    互斥锁
    IPC机制（队列、管道）
    生产者消费者模型（重点）
    进程池（重点）
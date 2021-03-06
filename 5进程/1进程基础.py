
进程
    进程就是一个正在执行的过程，或者说一个软件的运行过程

    进程是一个抽象的概念

一 操作系统的作用：
    1：隐藏复杂的硬件接口，提供良好的抽象接口
    2：管理、调度进程，并且将多个进程对硬件的竞争变得有序

二 多道技术
    背景：在单核下实现并发

    两大核心点：
        1、空间上的复用
            多道程序同时读入内存中，等待被cpu执行，即产生了多个进程
            强调：进程之间的内存空间是相互隔离的，而且这种隔离是物理级别实现的

        2、时间上的复用
            一个进程有三种状态：运行态、就绪态、阻塞态。 
            复用cpu的时间片
            切：
                1、正在执行的进程遇到IO操作（提升效率）。由运行态 → 阻塞态。
                2、正在执行的进程占用cpu时间过长，或者有一个优先级更高的进程
                抢走cpu的执行权限 （降低效率）。由 运行态 → 就绪态。
                3、就绪态可以随时 → 运行态。
                4、阻塞态 不能直接转换为 运行态， 必须先  →  就绪态  →  执行态。
               
    ps：
        现在的主机一般是多核，那么每个核都会利用多道技术
        有4个cpu，运行于cpu1的某个程序遇到io阻塞，会等到io结束再重新调度，会被调度到4个
        cpu中的任意一个，具体由操作系统调度算法决定。

三  进程并发的实现
    进程并发的实现在于：
        硬件中断一个正在运行的进程，把此时进程运行的所有状态保存下来，
        为此，操作系统维护一张表格，即进程表（process table），
        每个进程占用一个进程表项（这些表项也称为进程控制块）

    该表存放了进程状态的重要信息：
        程序计数器、堆栈指针、内存分配状况、所有打开文件的状态、帐号和调度信息，
        以及其他在进程由运行态转为就绪态或阻塞态时，必须保存的信息，
        从而保证该进程在再次启动时，就像从未被中断过一样。
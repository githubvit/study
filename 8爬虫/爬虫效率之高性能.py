# 爬虫性能相关 - linhaifeng - 博客园
# https://www.cnblogs.com/linhaifeng/articles/7806303.html

# 什么是同步？何谓异步？回调是怎么回事？
    # 同步和异步是指任务提交方式，区别是任务提交完后，是否等待任务执行，等任务执行的就是同步方式。不等的就是异步方式。
    # 那么同步的应用程序，就必然是提交任务，等任务执行完成；再提交下一个任务，等。。。；再。。。；任务是串行的。
    # 而异步应用程序，则是连续提交任务，不等任务执行，就忙别的去了，
    # 哪如果需要根据任务执行的结果来干其他一些事请，怎么办呢？
    # 这就用到回调了，等任务完成了，通过回调这些事请会自动执行。
    # 一个任务完成后会自动触发的绑定的函数，就是回调函数。
    # 所以异步程序经常和回调联系在一起。

# 单进程下的多线程由于全局解释器锁GIL不能被多个cpu同时执行。
# 即单进程下的多个线程同一时刻只有一个在运行

# 什么叫协程？
    # 单线程下实现并发，就是协程。

# 什么是并发？
    # 切换+保存状态就叫并发。


# 1 同步
def sync():
    import requests
    import time

    urls=[
        'https://www.baidu.com/',
        'https://www.python.org/',
        'https://www.bilibili.com/'
    ]
    start=time.time()

    def parse(res):
        print(f'parth:{len(res)}')

    def get_page(url):
        respose=requests.get(url)
        print(f'get:{url}')
        return respose.text

    for url in urls:
        res=get_page(url)
        parse(res)

    done=time.time()
    print(f'sync_time:{done-start}')

# sync()
# 同步结果：
    # get:https://www.baidu.com/
    # parth:2443
    # get:https://www.python.org/
    # parth:48827
    # get:https://www.bilibili.com/
    # parth:141344
    # sync_time:49.81897163391113
                                                                                                                                                          


# 2 异步——多线程
def asycn_thread():
    import requests
    import time 
    from concurrent.futures import ThreadPoolExecutor
    from threading import current_thread

    urls=[
        'https://www.baidu.com/',
        'https://www.python.org/',
        'https://www.bilibili.com/'
    ]
    start=time.time()

    def parse_pool(obj):
        res=obj.result()
        print(f'{current_thread().getName()} parse：{len(res)}')

    def get_page(url):
        respose=requests.get(url)
        print(f'get:{url}')
        return respose.text

    # 建池 3线程
    pool=ThreadPoolExecutor(3)
    for url in urls:
        pool.submit(get_page,url).add_done_callback(parse_pool)
    # 关池 卡住 等子线程执行完毕
    pool.shutdown()

    done=time.time()
    print(f'asycn_thread_time:{done-start}')

# asycn_thread()
# 异步结果：
    # get:https://www.baidu.com/
    # ThreadPoolExecutor-0_0 parse：2443
    # get:https://www.bilibili.com/
    # ThreadPoolExecutor-0_2 parse：139061
    # get:https://www.python.org/
    # ThreadPoolExecutor-0_1 parse：48827
    # asycn_thread_time:90.59066534042358


# 复利交易系统
    # 为什么要建立：
        # 原因
            # 挖水井  图
            # 从众思维 逆向思维 

        # 建立一套系统方法 复制成功 避免 挖水井现象 克服 从众思维

        # 形成时间的持续优势


    # 基本原则 孔子和老子论羊 禅
        # 整体 
        # 确切
        # 稳定 即 相对一致
    # 认清价格波动
        # 多小（多数是小波动）、少大（少数是大波动，一年里没几次）
        # 市场不是只有牛熊之分，把市场按照四季来分 即春夏秋冬，更科学，春夏适宜入市操作，秋冬不宜。
            # 市场的春夏秋冬与自然有不同，首先时间不固定，冬季有可能3-5年。
            # 还有就是顺序不固定。

    # 市场操作
        # 胜率
        # 认清机会 
            # 长剑图形   盈亏比（剑身剑把比）为3:1
                # 止损点（剑尾）到买入点（剑卡）即剑的手柄-剑把
                # 买入点（剑卡）到目标掉（剑锋）即剑身

        # 经常性兑现利润，不要怕卖飞了，复利方式，就是积小胜成大胜。 
            # a:做短线获利了，兑现利润后，股票继续涨，后悔！
            # b:做短线浮盈了，舍不得卖，期望更高，但价格回落了，浮盈没了，甚至被套，后悔！
            # 反正都是后悔，前者是赚钱后悔，后者是空手的后悔，所以应该选a，经常性兑现利润。
        # 把市场资金分成多份，1只股票只用一个资金份额。就是分散风险。 
    # 卡位：高胜率的本质就是卡位
        # 四种日常基本图形（多小）：
            # 冲击价格河床上沿。
            # 冲击价格河床下沿。
            # 即冲击价格河床上沿，又冲击价格河床下沿。
            # 交易清淡，即不冲击价格河床上沿，又不冲击价格河床下沿。
        
        # 两种剧烈变动图形（少大）：
            # 突破价格河床上沿，找到新的河床，大幅上升。
            # 突破价格河床下沿，找到新的河床，大幅下跌。

        # 分析计算价格流动河床的定位值区间，就可以知道在什么位置卡位，在什么位置准备做多，在什么位置准备做空，
        # 这个卡的位置，就是前面讲的胜率高的位置，和长剑机会的位置。

# 3 用自己的async + requesta 没有做到异步
def async_diy():
    import requests
    import async_scher
    import time
    scher=async_scher.scher

    urls=[
        'https://www.baidu.com/',
        'https://www.python.org/',
        'https://www.bilibili.com/'
    ]

    async def get_page(url):
        print(f'get:{url}')
        respose=requests.get(url) # 这个阻塞 无法 await 切换 await requests.get(url) 导致 提交 无法异步,
        # 发回调信号 表明有回调
        scher.callback_able()
        return respose.text

    # 作为 回调
    def parse(url,task):
        res=str(task.result)
        print(f'parse:{url}：{len(res)}')

    start=time.time()
    for url in urls:
        scr_obj=scher.new_task(get_page(url))
        # 回调
        scr_obj.add_done_callback(url,callback=parse)

        # 发结果信号 表明要结果
        scr_obj.get_result()
        
    scher.run()
    done=time.time()
    print(f'asycn_diy_time:{done-start}')

# async_diy() #不是异步

    # get:https://www.baidu.com/
    # parse:('https://www.baidu.com/',)：2443
    # get:https://www.python.org/
    # parse:('https://www.python.org/',)：49058
    # get:https://www.bilibili.com/
    # parse:('https://www.bilibili.com/',)：147402
    # asycn_diy_time:22.806864738464355

# 4 asyncio + aiohttp
import asyncio 
import aiohttp
import time
def async_aiohttp():
    
    urls=[
        'https://www.baidu.com/',
        'https://www.python.org/',
        'https://www.bilibili.com/'
    ]


    async def get_page(url):
        print(f"get page：{url}")
        # session 要加协程锁
        async with aiohttp.ClientSession() as s:
            # .get(url)也要加锁
            async with s.get(url) as response:
                html=await response.text()
                return (url,html)
    
    # 回调
    def parse(res):
        print(f"parse: {res[0]} count: {len(res[1])}")     

    
    # 即时取得协程结果 使用asyncio.as_completed(tasks)
    async def main():
        tasks=[asyncio.ensure_future(get_page(url)) for url in urls]
        # -------------------------------------*****-------------------------------------
        for task in asyncio.as_completed(tasks):
            parse(await task) # 回调直接取得了协程的结果   
        # -------------------------------------*****-------------------------------------
            
    start=time.time()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    done=time.time()
    print(f'asycn_aiohttp time:{done-start}')

# async_aiohttp() # 异步 取决于最难连的www.python.org的连接时间 慢的时候66秒都有

    # get page：https://www.baidu.com/
    # get page：https://www.python.org/
    # get page：https://www.bilibili.com/
    # parse: https://www.baidu.com/ count: 227
    # parse: https://www.bilibili.com/ count: 147255
    # parse: https://www.python.org/ count: 48913
    # asycn_aiohttp time:8.274399518966675


# 5 asyncio + requests 来自linhaifengblog callback与requests没有解耦
# 把原来不能await 的func 变成可以 await func，因为可以集成func的阻塞io。
# 解决了await requests.get(url) 挂起切换的问题 await loop.run_in_executor(executor, requests.get, url) 
# 与线程池配合，使用多线程，在协程中集成阻塞io，使得 原来不能 await 的，就可以await 挂起和切换了，变成了Awaitable 可等待。
import requests
def async_loop():
    urls=[
        'https://www.baidu.com/',
        'https://www.python.org/',
        'https://www.bilibili.com/'
    ]

    async def get_page(func,*args):
        

        print('GET:%s' %args[0])
        response=await loop.run_in_executor(None,func,*args) # 运行并解压 普通函数  碰到io阻塞就自动切换
        # 原来的回调写在这里，就和请求耦合了，不好
        print(response.url,len(response.text))
        
        return 1

    # 作为 回调
    def parse(task):
        res=task.result
        print(f'parse:{len(res)}')
        

    start=time.time()
    loop=asyncio.get_event_loop()
    
    coros=[get_page(requests.get,url) for url in urls] #  loop.run_in_executor(None,func,*args) 
    
    # 增加回调就报错
    # tasks=[asyncio.ensure_future(coro).add_done_callback(parse) for coro in urls]

    tasks=asyncio.gather(*coros)

    results=loop.run_until_complete(tasks)
    loop.close()

    print('=====>',results) #[1, 1, 1]
    done=time.time()
    print(f'async_loop time:{done-start}')

# async_loop()

    # GET:https://www.baidu.com/
    # GET:https://www.python.org/
    # GET:https://www.bilibili.com/
    # https://www.baidu.com/ 2443
    # https://www.bilibili.com/?rt=V%2FymTlOu4ow%2Fy4xxNWPUZxvWSug8otBk15HheaNFPWs%3D 143651
    # https://www.python.org/ 49058
    # =====> [1, 1, 1]
    # async_loop time:8.962564468383789

# 6 asyncio+requests
# 这个比上面林海峰博客的好  实现了callback和requests解耦操作。

def async_callback():
    urls=[
        'https://www.baidu.com/',
        'https://www.python.org/',
        'https://www.bilibili.com/'
    ]

    async def get_page(func,*args):
        print(f'GET:{args[0]}' )

        # -------------------------------------*****-------------------------------------
        response=await loop.run_in_executor(None,func,*args) # 运行并解压 普通函数  碰到io阻塞就自动切换
        # -------------------------------------*****-------------------------------------
        
        return (args[0],response.text)

    # 作为 回调
    def parse(res):
        print(f'parse:{res[0]} : counts：{len(res[1])}')

    # 即时取得协程结果 使用asyncio.as_completed(tasks)
    async def main():

        # coros=[get_page(requests.get,url) for url in urls]

        # tasks=asyncio.gather(*coros) #不能使用gather对象，必须是 Iterable 比如列表
        # tasks=[]
        # for coro in coros:
        #     tasks.append(asyncio.ensure_future(coro))
        # for url in urls:
        #     tasks.append(asyncio.ensure_future(get_page(requests.get,url)))

        tasks=[asyncio.ensure_future(get_page(requests.get,url)) for url in urls]


        # -------------------------------------*****-------------------------------------
        # for task in asyncio.as_completed(coros):#协程不按顺序输出
        for task in asyncio.as_completed(tasks):
            parse(await task) # 回调直接取得了协程的结果   
        # -------------------------------------*****-------------------------------------
    start=time.time()
    loop=asyncio.get_event_loop() # 创建事件循环
    loop.run_until_complete(main())
    loop.close()
    done=time.time()
    print(f'async_callback time:{done-start}')

# async_callback()

    # GET:https://www.baidu.com/
    # GET:https://www.python.org/
    # GET:https://www.bilibili.com/
    # parse:https://www.baidu.com/ : counts：2443
    # parse:https://www.bilibili.com/ : counts：145886
    # parse:https://www.python.org/ : counts：48995
    # async_callback time:19.0075261592865


# 7 twisted+request
# twisted: 是用Python实现的基于事件驱动的网络引擎框架。

# Twisted是一个基于Reactor模式的异步IO网络框架
    
    # Reactor模式：
        # Reactor模式就是利用 循环体 来 等待事件 发生，然后处理发生的事件的模式。
            # 当有一个事件开始驱动的时候，就会陆续驱动多个事件，
            # 最后就像核反应堆一样链式反应，产生巨大的能量，
            # 在网络里就是高效地处理并发。

    # Reactor主要有如下两个功能：
        # 1 监视一系列与你I/O操作相关的文件描述符（description)。
            # 监视文件描述符的过程是异步的，也就是说整个循环体是非阻塞的；

        # 2 不停地向你汇报那些准备好的I/O操作的文件描述符。

    # Twisted就是基于Reactor模式帮我们抽象出了异步编程模型以及各种非阻塞的io模块（tcp、http、ftp等），
    # 使我们很方便地进行异步编程。

    # 异步版本的io操作是非阻塞式的，遇到io等待时会先去处理其他任务。

    # Twisted的Reactor只有通过调用reactor.run()才启动；
    # reactor循环是在其开始的线程中运行，也就是运行在主线程中；
    # 一旦启动，reactor就会在程序的控制下（或者具体在一个启动它的线程的控制下）一直运行下去；
    # reactor空转时并不会消耗任何CPU的资源；
    # 并不需要显式的创建reactor，只需要引入就OK了。

# Twisted支持许多常见的传输及应用层协议，包括TCP、UDP、SSL/TLS、HTTP、IMAP、SSH、IRC以及FTP。

# 总结：

    # 编写Twisted程序时，脑海中一定要有一个循环体，且将循环体分成两部分：我们的代码和Twisted代码；
    # Twisted代码：有各种写好的非阻塞网络模块，循环监听返回内容，一旦收到返回内容则调用回调函数，执行我们的业务逻辑；
    # 我们的代码：各种回调函数，处理socket数据流；
        # 我们的代码与Twisted代码运行在同一个线程中；
        # 当我们的代码运行时，Twisted代码是处于暂停状态的；
        # 同样，当Twisted代码处于运行状态时，我们的代码处于暂停状态；
        # Reactor事件循环会在我们的回调函数返回后恢复运行。
    # 整个循环体是单线程的，所以我们写的回调一定要是非阻塞的，否则就失去了异步的优势了。如果回调函数有io操作，那么需要将此回调异步化。

# Python Twisted介绍 https://blog.csdn.net/hanhuili/article/details/9389433
# Twisted基础介绍（一） - 知乎 https://zhuanlan.zhihu.com/p/84036822
# 安装：翻墙 
    # pip3 install twisted
    # pip3 install pyopenssl
    # pip install service_identity

def tw1():
    from twisted.web.client import getPage,Agent,defer
    from twisted.internet import reactor #引入 即创建了 reactor loop  就是asyncio 的 loop=asyncio.get_event_loop() # 创建事件循环

    def all_done(arg):
        # arg参数是接收任务列表里每个任务的回调执行的状态(True表示成功，False表示异常)和结果，用列表套元组
        # [(任务1回调执行状态，任务1回调执行结果)，
        # (任务2回调执行状态，任务2回调执行结果)，
        # (任务3回调执行状态，任务3回调执行结果)，
        # ...
        # ]
        # 如果元组的第一个值是True，表示该元组第二个值是成功的结果，即正常结果。

        print(arg)
        # 正常执行结果： [(True, 1), (True, 1), (True, 1)]
        # 异常执行结果：
        # [(False, <twisted.python.failure.Failure builtins.TypeError: >), (False, <twisted.python.failure.Failure builtins.TypeError: >), (False, <twisted.python.failure.Failure builtins.TypeError: >)]

        reactor.stop()

    def callback_sucess(res):
        print(len(res))
        # raise TypeError #抛异常
        return 1

    def callback_error(e):
        print(e)

    tasks=[]
    urls=[
        'http://www.baidu.com',
        'http://www.bing.com',
        'https://www.python.org',
    ]
    for url in urls:
        # 建立任务 集成任务内的io
        task=getPage(url.encode('utf-8'))
        # task=Agent(reactor).request('GET'.encode('utf-8'),uri=url.encode('utf-8'))
        # 绑定回调
        task.addCallback(callback_sucess)
        # 放入任务列表
        tasks.append(task)

    # 集成 任务列表 的 io  用事件循环去监测 io 执行的情况
    defer.DeferredList(tasks).addBoth(all_done)

    # 启动 就像asyncio loop.run_forever() 
    # 是while True 死循环 ， 结束循环是reactor.stop() ，不能在run后写，run是死循环，永远到不了stop
    # 通过 任务列表的addBoth回调 写一个all_done来结束循环
    # 之所以叫addBoth，是因为twisted跟js的promise一样既有成功的回调也有失败的回调，
    # 所以不管是成功的回调还是失败的回调，最后都增加addBoth里面的回调，在这个回调里执行reactor.stop() ，结束循环。
    reactor.run()
tw1()
# d:/pyj/st/study/8爬虫/爬虫效率之高性能.py:441: DeprecationWarning: twisted.web.client.getPage was deprecated in Twisted 16.7.0; plea
# se use https://pypi.org/project/treq/ or twisted.web.client.Agent instead
#   obj=getPage(url.encode('utf-8'))
# 253157
# 112780
# 48827
# [(True, 1), (True, 1), (True, 1)]

# 让你用Agent替代getPage 不要理这个警告。





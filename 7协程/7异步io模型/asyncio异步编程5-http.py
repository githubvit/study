#  asyncio http 网络连接

import asyncio

#  1. 处理网络连接的示例代码
#  连接三个网站，发送消息流，接收数据流。三个协程由一个线程并发完成：
def one():
    async def wget(host):
        print('wget {}'.format(host))

        # 1. 建立连接
        # 创建 TCP 客户端
        # 或者说创建一个 TCP 连接对象
        # open_connection 接收两个参数：主机和端口号
        # connect 是协程，这步仅是创建协程对象，立即返回，不阻塞
        connect = asyncio.open_connection(host, 80) # 协程Tcp 连接对象

        # await 运行协程连接服务器，这步是阻塞操作，释放 CPU
        # 连接创建成功后，asyncio.open_connection 方法的返回值就是读写对象
        # 读写对象分别为 StreamReader 和 StreamWriter 实例
        # 它们也是协程对象，底层调用 socket 模块的 send 和 recv 方法实现读写
        reader, writer = await connect

        # 2. 发送
        # header 是发送给服务器的消息，意为获取页面的 header 信息
        # 这个格式是固定的：
        # [ 请求方法'GET' 空格 url'/' 空格 协议版本'HTTP/1.0' 回车符'\r' 换行符'\n' ] → 请求行 
        # [ 头部字段名1'Host' ： 值'host' 回车符 换行符 头部字段名2 ： 值 回车符 换行符 ... 头部字段名n ： 值  ] → 请求头部
        # [ 回车符 换行符 回车符 换行符 '\r\n\r\n' ] → header结束
        header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)

        # 给服务器发消息，注意消息是二进制的
        writer.write(header.encode())

        # 这是一个与底层 IO 输入缓冲区交互的流量控制方法
        # 当缓冲区达到上限时，drain() 阻塞，待到缓冲区回落到下限时，写操作恢复
        # 当不需要等待时，drain() 会立即返回，例如上面的消息内容较少，不会阻塞
        # 这就是一个控制消息的数据量的控制阀 缓冲区满了就阻塞  有空就不阻塞
        await writer.drain()

        # 3. 接收
        # 给服务器发送消息后，就等着读取服务器返回来的消息
        while True:
            # 读取数据是阻塞操作，释放 CPU
            # reader 相当于一个水盆，服务器发来的数据是水流
            # readline 表示读取一行，以 \n 作为换行符
            # 如果在出现 \n 之前，数据流中出现 EOF（End Of File 文件结束符）也会返回
            # 相当于出现 \n 或 EOF 时，拧上水龙头，line 就是这盆水
            line = await reader.readline()

            # 数据接收完毕，会返回空字符串 \r\n ，退出 while 循环，结束数据接收
            if line.decode() == '\r\n':
                break

            # 接收的数据是二进制数据，转换为 UTF-8 格式并打印
            # rstrip 方法删掉字符串的结尾处的空白字符，也就是 \n
            print('{} header > {}'.format(host, line.decode().rstrip()))

        writer.close()   # 关闭数据流，可以省略

    host_list = ['www.shiyanlou.com', 'www.sohu.com', 't.tt']       # 主机列表
    loop = asyncio.get_event_loop()                                 # 事件循环
    
     # gather的使用

    # gather的作用和wait不同的是。
    # 1.采用wait收集输出的结果不是futuer，
    #   没有add_done_callback回调，
    #   而gather做收集器，输出futuer，有回调功能。
    # 2.可以按照传入参数的顺序，顺序输出。
    tasks = asyncio.gather(*[wget(host) for host in host_list])     # 任务收集器
    # tasks = asyncio.wait([wget(host) for host in host_list])        # 任务收集器 同上
    loop.run_until_complete(tasks)                                  # 阻塞运行任务
    loop.close()                                                    # 关闭事件循环

# one()

# wget www.shiyanlou.com
# wget www.sohu.com
# wget t.tt
# www.shiyanlou.com header > HTTP/1.1 308 Permanent Redirect
# www.shiyanlou.com header > Date: Thu, 13 Feb 2020 15:13:42 GMT
# www.shiyanlou.com header > Content-Type: text/html
# ...
# www.sohu.com header > HTTP/1.1 200 OK
# www.sohu.com header > Content-Type: text/html;charset=UTF-8
# www.sohu.com header > Connection: close
# ...
# t.tt header > HTTP/1.1 301 Moved Permanently
# t.tt header > Date: Thu, 13 Feb 2020 15:13:42 GMT
# t.tt header > Content-Type: text/html
# ...

# 2. 使用 async for 优化读取信息的代码

def two():
    async def wget(host):
        print('wget {}'.format(host))
        
        # 1 建立Tcp连接
        connect=asyncio.open_connection(host,80)
        reader,writer=await connect 

        # 2 发送
        header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
        writer.write(header.encode())
        await writer.drain()

        # 3 接收  优化
        # 给服务器发送消息后，就等着读取服务器返回来的消息
        # reader 对象较为特殊，它有 __aiter__ 和 __anext__ 方法
        # 这种对象不是 Iterable 对象（但仍然是可迭代对象），只能使用 async for 循环
        # __anext__ 方法的返回值会赋值给 line 变量
        # 整个循环其实是阻塞的，因为 __anext__ 方法里有 yield from 语句
        async for line in reader:
            print('{} header > {}'.format(host, line.decode('unicode_escape').rstrip()))

    host_list = ['www.shiyanlou.com', 'www.zhihu.com', 't.tt']  # 主机列表
    loop = asyncio.get_event_loop()                             # 事件循环
    tasks = asyncio.wait([wget(host) for host in host_list])    # 任务收集器
    loop.run_until_complete(tasks) 
    loop.close

# two()


# 3. asyncio.as_completed 方法即时获取任务结果

def three():
    async def wget(host):
        print('wget {}'.format(host))
        connect = asyncio.open_connection(host, 80)
        reader, writer = await connect
        header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
        writer.write(header.encode())
        await writer.drain()
        async for line in reader:
            print('{} header > {}'.format(host,
                line.decode('unicode_escape').rstrip()))
        return 'Host: {}'.format(host)


    '''
    host_list = ['www.shiyanlou.com', 'www.zhihu.com', 't.tt']  # 主机列表
    loop = asyncio.get_event_loop()                             # 事件循环
    coroutines = [wget(host) for host in host_list]             # 协程列表
    tasks = asyncio.wait(coroutines)                            # 任务收集器
    # 之前的文档中讲到过 asyncio.Task.all_tasks 方法可以获得事件循环中的任务集合
    # 事件循环的 run_until_complete 方法的返回值是二元元组
    # 元组的第一个元素也是任务集合
    # 任务本身是一个协程函数，函数的 return 值可以通过任务的 result 方法获得
    result = loop.run_until_complete(tasks)
    print(result)
    for task in result[0]:
        print(task.result())
    '''
    # 任务在结束时才会产生 result 值
    # 上面的写法只能等事件循环停止后一并获取全部任务的 result 值
    # 如果要随时获得任务的 result 值，可以使用 asyncio.as_completed 方法
    # 这样的话需要创建一个主任务并加入到事件循环，事件循环首先运行主任务
    # 在主任务中使用 asyncio.ensure_future 方法创建新的子任务
    # 这些子任务会自动加入到事件循环
    # 随后在主任务中使用 asyncio.as_completed 方法获取已经完成的任务
    async def main_task():
        tasks = []
        host_list = ['www.shiyanlou.com', 'www.zhihu.com', 't.tt']
        for host in host_list:
            tasks.append(asyncio.ensure_future(wget(host)))

        # 这里为什么不使用 asyncio.Task.all_tasks 方法获取任务集合呢？
        # 像这样：asyncio.as_completed(asyncio.Task.all_tasks())
        # 因为任务集合中包含主任务和子任务，虽然二者在事件循环中是并列关系
        # 但是 for 循环会阻塞在这里，主任务永远完不成
        for task in asyncio.as_completed(tasks):
            print(await task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_task())
    loop.close()

three()

# wget www.shiyanlou.com
# wget www.zhihu.com
# wget t.tt
# www.zhihu.com header > HTTP/1.1 301 Moved Permanently
# www.zhihu.com header > Server: Tengine
# www.zhihu.com header > Date: Thu, 13 Feb 2020 15:56:02 GMT
# www.zhihu.com header > Content-Type: text/html
# www.zhihu.com header > Content-Length: 278
# www.zhihu.com header > Connection: close
# www.zhihu.com header > Location: https://www.zhihu.com/
# www.zhihu.com header > x-cdn-provider: alibaba
# www.zhihu.com header > x-edge-timing: 0.000
# www.zhihu.com header > Via: cache11.cn1245[,0]
# www.zhihu.com header > Timing-Allow-Origin: *
# www.zhihu.com header > EagleId: b66a9b9f15816093625111647e
# www.zhihu.com header >
# www.zhihu.com header > <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
# www.zhihu.com header > <html>
# www.zhihu.com header > <head><title>301 Moved Permanently</title></head>
# www.zhihu.com header > <body bgcolor="white">
# www.zhihu.com header > <h1>301 Moved Permanently</h1>
# www.zhihu.com header > <p>The requested resource has been assigned a new permanent URI.</p>
# www.zhihu.com header > <hr/>Powered by Tengine</body>
# www.zhihu.com header > </html>
# Host: www.zhihu.com
# www.shiyanlou.com header > HTTP/1.1 308 Permanent Redirect
# www.shiyanlou.com header > Date: Thu, 13 Feb 2020 15:56:02 GMT
# www.shiyanlou.com header > Content-Type: text/html
# www.shiyanlou.com header > Content-Length: 164
# www.shiyanlou.com header > Connection: close
# www.shiyanlou.com header > Location: https://www.shiyanlou.com/
# www.shiyanlou.com header >
# www.shiyanlou.com header > <html>
# www.shiyanlou.com header > <head><title>308 Permanent Redirect</title></head>
# www.shiyanlou.com header > <body>
# www.shiyanlou.com header > <center><h1>308 Permanent Redirect</h1></center>
# www.shiyanlou.com header > <hr><center>nginx</center>
# www.shiyanlou.com header > </body>
# www.shiyanlou.com header > </html>
# Host: www.shiyanlou.com
# t.tt header > HTTP/1.1 301 Moved Permanently
# t.tt header > Date: Thu, 13 Feb 2020 15:56:02 GMT
# t.tt header > Content-Type: text/html
# t.tt header > Content-Length: 166
# t.tt header > Connection: close
# t.tt header > Location: https://www.smartisan.com
# t.tt header > Server: ARTWS/1.0
# t.tt header >
# t.tt header > <html>
# t.tt header > <head><title>301 Moved Permanently</title></head>
# t.tt header > <body>
# t.tt header > <center><h1>301 Moved Permanently</h1></center>
# t.tt header > <hr><center>openresty</center>
# t.tt header > </body>
# t.tt header > </html>
# Host: t.tt
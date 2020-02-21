
import socket,time,os
import asyncio
import functools

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8081))
server.listen(5)
server.setblocking(False)
async def server_start():
    n=0
    while True:
        n+=1
        print('连接',n)
        # 向 事件循环 注册 link 协程
        task=asyncio.create_task(linker())
        await asyncio.sleep(1) #交出控制权 控制速度

# 服务 链接循环
async def linker(): 
    try:
        conn,cli_addr=server.accept()
        print('%s连接,来自%s'%(conn,cli_addr))
        # 向 事件循环 注册 收发 communication 协程
        task=asyncio.create_task(communication(conn,cli_addr))
    except BlockingIOError: # 捕捉 阻塞io 异常
        await asyncio.sleep(0.1) #交出控制权
    

# 收发 通信循环
async def communication(conn,cli_addr):
    print('收发')
    c=0
    while True:
        c+=1
        print('收发',c)
        try:
            data = conn.recv(1024)
            if not data:break
            conn.send(data.upper())
            await asyncio.sleep(0.1) #交出控制权
        except BlockingIOError:
            continue    
        except ConnectionResetError:
            break
    # print('关闭来自[%s]的连接'%(cli_addr))  # 报错，元组作为一个元素要加‘，’
    # typeError: not all arguments converted during string formatting
    print('关闭来自[%s]的连接'%(cli_addr,))  # 加','，表示该元组作为一个元素，就解决了。  
    conn.close()    
    

# server.setblocking(False)
print('开始....') 

# 创建 事件循环
loop=asyncio.get_event_loop()
# 创建任务及回调
task1 = asyncio.ensure_future(server_start())

try:
    # 启动事件循环
    loop.run_until_complete(task1)
except KeyboardInterrupt:
    # 取消 ctrl+c 后事件循环中的任务
    # 获取任务列表
    tasks=asyncio.Task.all_tasks()
    for i in tasks:
        i.cancel()
finally:        
    print('game over') 
server.close()


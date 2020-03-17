import asyncio

async def handle_echo(reader, writer):
    print('[reader]',reader)
    print('[writer]',writer)
    data = await reader.read(100)
    print('data',data)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)

    
    # 这是一个与底层 IO 输入缓冲区交互的流量控制方法 await writer.drain()
        # 当缓冲区达到上限时，drain() 阻塞，待到缓冲区回落到下限时，写操作恢复
        # 当不需要等待时，drain() 会立即返回，例如上面的消息内容较少，不会阻塞
        # 这就是一个控制消息的数据量的控制阀 缓冲区满了就阻塞  有空就不阻塞
    await writer.drain()


    print("Close the connection")
    writer.close()

async def main(): 
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8081) # 协程方式 启动 套接字 服务
    print('[server]',server)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
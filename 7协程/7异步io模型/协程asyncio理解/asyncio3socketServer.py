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
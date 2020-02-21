#_*_coding:utf-8_*_

'''
RPC模式server：是响应client端要求的、并返回结果给client的一端，要定义处理函数。要先启动。
'''
import pika

# 建立soket，连接rabbitmq服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
# 建立管道
channel = connection.channel()
# 声明队列
channel.queue_declare(queue='rpc_queue')

#斐波那契处理函数，计算斐波那契数列第n项的值
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)#用递归计算斐波那契数列n项的值

#服务器端回调函数
def on_request(ch, method, props, body):
    print 'ch:', ch
    print 'method:', method
    print 'properties:', props
    print 'body:', body
    n = int(body)#把客户端发过来的消息转为int

    print(" [.] fib(%s)" % n)
    response = fib(n)#调用斐波那契处理函数，获得结果
    # 在回调函数中发送消息给客户端
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,#从客户端的properties获得queue名
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),#从客户端的properties获得UUID
                     body=str(response))#把斐波那契处理函数的结果作为消息，必须转为str字符串。
    ch.basic_ack(delivery_tag=method.delivery_tag)#向rabbitmq服务器确认完成结果

# 向rabbitmq服务器说明我没处理完不要给我任务，我不接收
channel.basic_qos(prefetch_count=1)
# 定义接收客户端消息的语法（回调函数，接收队列名）
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
# 接收客户端消息
channel.start_consuming()
#_*_coding:utf-8_*_

'''
RPC模式client：是提要求，要结果的一端。也是实时的，要server端（处理client提出的要求的一端）先启动。
'''
import pika
import uuid
import time


class FibonacciRpcClient(object):#远程调用斐波那契计算的结果
    # 在初始化时，就定义好socket、管道channel、queue、接收服务端返回的语法
    def __init__(self):
        #定义好socket、
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        #声明管道
        self.channel = self.connection.channel()
        #声明随机queue
        result = self.channel.queue_declare(exclusive=True)
        #获得随机queue名字
        self.callback_queue = result.method.queue
        # 接收服务端返回的语法
        self.channel.basic_consume(self.on_response, #回调函数
                                   queue=self.callback_queue,#通过queue接收的名字
                                   no_ack=True

                                   )

    def on_response(self, ch, method, props, body):#回调函数
        if self.corr_id == props.correlation_id:#如果本机的UUID等于接收服务端发过来的UUID，就获取服务端发过来的消息。
            self.response = body
        print 'ch:', ch
        print 'method:', method
        print 'properties:', props
        print 'body:', body

    def call(self, n):#发送给服务端，求斐波那契的n项是多少
        self.response = None
        self.corr_id = str(uuid.uuid4())#把UUID的结果转为str字符串。每次调用call都不一样，而实例化之后的queue名是一样的。
        #
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,#向服务端发送返回时的queue名
                                       correlation_id=self.corr_id,#向服务端发送本次发送的uuid字符串
                                   ),
                                   body=str(n)#发给服务端的必须是字符串，把n发给服务端，服务端会用斐波那契处理函数进行处理。
                                   )
        #当没有收到服务端的返回时，接收为非阻塞的方式，也就是循环接收
        while self.response is None:
            self.connection.process_data_events()#非阻塞接收，channel.start_consuming()是阻塞式接收。
            time.sleep(0.5)
            print self.response
        #当收到服务端的返回时，就返回服务端的计算结果。
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()#实例化斐波那契远程调用类

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)#求斐波那契第30项是多少。
response2 = fibonacci_rpc.call(6)#求斐波那契第30项是多少。
print(" [.] Got %r" % response)
print(" [.] Got %r" % response2)

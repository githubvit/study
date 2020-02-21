# 粘包1中用strcut封包了文件大小为固定字节长度，将其命名为报头。和数据一起发送，
# 接收端只要先按报头固定长度接收一次，就取出了文件大小，然后按文件大小循环接收，

# 粘包1中遗留的问题

# 1 struct封包数字是有限制的
# i格式封包的数字大小（封包结果为4个字节）
# <
# q格式封包的数字大小（封包结果为8个字节），
# 不管是i格式还是q格式都是有数字大小限制的。

# 2 报头内容问题
# 既然定义为报头，报头中的内容太少，想想http的报头内容多丰富。
# 希望报头是一个字典，可以写各种与报文数据有关的信息。


# 解决方案
# 发送方：
# 1 用字典定义报头，解决报头内容问题，
#  把报文数据大小total_size放入，解决数字限制问题。
# headers={
# 'filepath':'d:/xxx/x.txt',
# 'md5':'afasdfafsfa',
# 'total_size':464654613213,
# }
# 2 把报头字典转为字符串，再把字符串encoding成bytes。
# 3 用headers_size=struct.pack('i',len(报头bytes文件))
# 由于报头bytes文件数据都比较小，
# 此时用struct封装报头文件长度就没问题了。
#  4 发送：
#  先发 报头长度headers_size
#  再发 报头bytes文件
#  最后发 数据

#  接收方：
#  1 用4字节先接收报头大小
#   headers_size=client.recv(4)
#  2 根据headers_size一把接收报头bytes文件，
# 转换成报头字典，从报头取出数据大小
#   headers_bytes=client.recv(headers_size)
#  3 按数据大小循环取数据。
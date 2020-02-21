#1、把整型数字转成bytes类型
#2、转成的bytes是固定长度的

import struct

res=struct.pack('i',20332)
print(res,len(res))

# res2=struct.unpack('i',res)
# print(res2[0])
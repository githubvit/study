import struct

#封包
size=123464564912 # 超出struct范围 struct.error: argument out of range
size=12346456491  # 还是超出
size=1234645649   # 4 结果正常
header=struct.pack('i',size)
print(len(header))

#解包
print(struct.unpack('i',header))#(1234645649,)
print(struct.unpack('i',header)[0])#1234645649
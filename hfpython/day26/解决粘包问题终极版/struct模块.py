#1、把整型数字转成bytes类型
#2、转成的bytes是固定长度的

import struct
import json

header_dic = {
    'total_size': 3122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121,
    'md5': '123svsaef123sdfasdf',
    'filename': 'a.txt'
}

header_json=json.dumps(header_dic)
# print(header_json,type(header_json))
header_bytes=header_json.encode('utf-8')
header_size=len(header_bytes)

print(header_size)
obj=struct.pack('i',header_size)
print(obj,len(obj))
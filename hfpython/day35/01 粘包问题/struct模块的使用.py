import struct
import json

header_dic = {
    'filename': 'a.txt',
    'md5': 'asdf1231xcv123',
    'total_size': 122222222222222222222222222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222232222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222223
}
header_json = json.dumps(header_dic)
# print(header_json,type(header_json))
header_bytes = header_json.encode('utf-8')



res=struct.pack('i',len(header_bytes))
# print(res,len(res))

print(struct.unpack('i',res))
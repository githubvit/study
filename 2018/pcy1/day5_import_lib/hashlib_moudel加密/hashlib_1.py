#-*- coding:utf8 -*-

import hashlib

m = hashlib.md5()#生成一个加密的对象
m.update(b"Hello")#对谁加密
m.update(b"It's me")
print(m.hexdigest())
m2=hashlib.md5()#生成一个加密的对象
m2.update(b"HelloIt's me")
print (m2.hexdigest())#m2的md5和上面m的md5是一样的
m.update(b"It's me")
m.update(b"It's been a long time since last time we ...")

print(m.hexdigest())
print(len(m.hexdigest()))  # 16进制格式hash
# '''
# def digest(self, *args, **kwargs): # real signature unknown
#     """ Return the digest value as a string of binary data. """
#     pass
#
# def hexdigest(self, *args, **kwargs): # real signature unknown
#     """ Return the digest value as a string of hexadecimal digits. """
#     pass
#
# '''
# import hashlib
#
# # ######## md5 ########
#
# hash = hashlib.md5()
# hash.update('admin')
# print(hash.hexdigest())
#
# # ######## sha1 ########
#
# hash = hashlib.sha1()
# hash.update('admin')
# print(hash.hexdigest())
#
# # ######## sha256 ########
#
hash = hashlib.sha256()
hash.update('admin')
print(hash.hexdigest())
print(len(hash.hexdigest()))
#
# # ######## sha384 ########
#
# hash = hashlib.sha384()
# hash.update('admin')
# print(hash.hexdigest())
#
# # ######## sha512 ########
#
# hash = hashlib.sha512()
# hash.update('admin')
# print(hash.hexdigest())
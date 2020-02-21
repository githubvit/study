# 1、什么叫hash:hash是一种算法，该算法接受传入的内容，经过运算得到一串hash值
# 2、hash值的特点是：
#2.1 只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
#2.2 不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码
#2.3 只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的


# import hashlib
#
# m=hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# m.update('egon'.encode('utf-8'))
# print(m.hexdigest()) #3801fab9b8c8d9fcb481017969843ed5



# import hashlib
#
# m=hashlib.md5()
# m.update('h'.encode('utf-8'))
# m.update('e'.encode('utf-8'))
# m.update('lloworld'.encode('utf-8'))
# m.update('egon'.encode('utf-8'))
# print(m.hexdigest()) #3801fab9b8c8d9fcb481017969843ed5

# import hashlib
# m=hashlib.md5()
# with open(r'D:\code\SH_fullstack_s1\day18\上节课复习','rb') as f:
#     for line in f:
#         m.update(line)
#     hv=m.hexdigest()
# print(hv) #f2a3a94efd0809e8a9c5ac8794c4bb2d
          #953cd74a08f4fbb7e69a4bda8dfad056



# 密码加盐
# import hashlib
# pwd='alex3714'
#
# m=hashlib.md5()
# m.update('一行白鹭上青天')
# m.update(pwd.encode('utf-8'))
# m.update('天'.encode('utf-8'))
#
# m.update('小雨一米五'.encode('utf-8'))
# print(m.hexdigest())



# import hashlib
#
# # m=hashlib.md5()
# # m.update('helloworld'.encode('utf-8'))
# # print(m.hexdigest()) #fc5e038d38a57032085441e7fe7010b0
#
# m=hashlib.sha256()
# m.update('helloworld'.encode('utf-8'))
# print(m.hexdigest()) #936a185caaa266bb9cbe981e9e05cb78cd732b0b3280eb944412bb6f8f8f07af
#
#
# m=hashlib.sha512()
# m.update('helloworld'.encode('utf-8'))
# print(m.hexdigest()) #1594244d52f2d8c12b142bb61f47bc2eaf503d6d9ca8480cae9fcf112f66e4967dc5e8fa98285e36db8af1b8ffa8b84cb15e0fbcf836c3deb803c13f37659a60



import hmac
m=hmac.new('天王盖地虎，小鸡炖模块'.encode('utf-8'))
m.update('alex3814'.encode('utf-8'))
print(m.hexdigest())
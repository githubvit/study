# x='你好'
# res=x.encode('utf-8')
# print(res,type(res))
#
# print(res.decode('gbk'))
#
# with open('a.txt', encoding='utf-8') as f1,\
#         open('b.txt', encoding='utf-8') as f2,\
#         open('c.txt', encoding='utf-8') as f3:
#     pass

#
# with open('上节课复习',encoding='utf-8') as f:
#     data=f.read()
#     print(type(data))


with open(r'a\a.txt','a',encoding='utf-8') as f:
    f.writelines(['{"x":1}\n','{"y":1}\n'])
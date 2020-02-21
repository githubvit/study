#1、打开文件
# f=open(r'文件的路径',mode='打开文件的模式',encoding='操作文件的字符编码')
# f=open(r'a.txt',mode='r')
# print(f)
# #2、读/写
# data=f.read()
# print(data)
#
# # del f
#
# #3、关闭文件
# f.close() #回收操作系统的资源
# # print(f)
# # f.read()
# # del f
# # x=1


# with open(r'a.txt',mode='r') as f:
#     print('===>')
#     print(f.read())
#

# f1=open(r'a1.txt',mode='r')
# f2=open(r'a2.txt',mode='r')

# with open(r'a1.txt',mode='r') as f1,open('a2.txt',mode='r') as f2:
#     print('===>')
    # print(f1.read())
    # print(f2.read())


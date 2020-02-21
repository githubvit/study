#文件的打开模式b模式
#强调：
#1、与t模式类似不能单独使用，必须是rb，wb，ab
#2、b模式下读写都是以bytes单位的
#3、b模式下一定不能指定encoding参数


#rb模式
# with open('1.jpg',mode='rb',) as f:
#     data=f.read()
#     print(data,)
#     print(type(data))

# with open('db.txt',mode='rb',) as f:
#     data=f.read() #
#     print(data.decode('utf-8')) #bytes-----unicode
#     print(type(data))


#wb模式
# with open('b.txt',mode='wb') as f:
#     msg='你好啊，吴三炮'
#     f.write(msg.encode('gbk'))
# with open('b.txt',mode='wb') as f:
#     msg='你好啊，吴三炮'
#     f.write(msg.encode('utf-8'))

# with open('b.txt',mode='rb') as f:
#     data=f.read()
#     # print(type(data))
#     print(data.decode('utf-8'))
# with open('1.jpg',mode='rb') as f:
#     data=f.read()
#     print(type(data))
#     print(data.decode('utf-8'))


#ab模式
# with open('b.txt',mode='ab') as f:
#     f.write('你好'.encode('utf-8'))


# with open('1.jpg','rb') as f:
#     for line in f:
#         print(line)




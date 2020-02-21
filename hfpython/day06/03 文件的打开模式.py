#文件默认的打开模式是t模式：文本模式

#操作文件的模式有三种：r，w，a

#r：默认的打开模式,只读模式
#注意：当文件不存在时，报错


# f=open('a.txt',mode='r',encoding='utf-8') #mode='rt'
# # f.write('哈哈啊哈哈啊啊 啊啊123213213123\n') #抛出异常，不能写
# # print(f.readable())
# print('=============>1')
# print(f.read())
#
# print('=============>2')
# print(f.read())
#
# f.close()



# f=open('a.txt',mode='r',encoding='utf-8') #mode='rt'
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')
# f.close()


# f=open('a.txt',mode='r',encoding='utf-8') #mode='rt'
# print(f.readlines())
# f.close()

# with open('a.txt',encoding='utf-8') as f:
    # for line in f:
    #     print(line,end='')


    # print(f.readlines())
    # print(f.readlines())
    # print(f.readlines())
    # print(f.readlines())
    # print(f.readlines())
    # print(f.readlines())
    # for line in f.readlines(): #循环文件不要使用该方式，因为在文件过大的情况下有可能会撑爆内存
    #     print(line,end='')





#w：只写模式
#注意
# 1、当文件存在时，清空
# 2、当文件不存在时，创建空文档

# f=open(r'a1.txt',mode='w',encoding='utf-8') #默认是wt
# # f.write('第一行\n')
# # f.write('第二行\n')
#
# # f.writelines(['111111\n','222222\n','333333\n'])
# f.write('aaaaaaaaaaaaaaaaaaaa\nbbbbbbbbbbbbbbb\nccccccccccccccc\n')
#
#
# f.close()




#a：只追加写模式
#注意：
#在文件不存在时，创建空文件
#在文件存在时，光标直接跑到文件末尾

f=open('access.log',mode='a',encoding='utf-8')
# print(f.writable())
# f.readlines() #报错

f.write('5555555555555\n')

f.close()




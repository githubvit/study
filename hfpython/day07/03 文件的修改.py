# with open('user.txt','r+',encoding='utf-8') as f:
#     f.seek(9) #偏移量的单位是字节
#     # print(f.tell())
#     print(f.read())



# with open('user.txt','r+',encoding='utf-8') as f:
#     f.seek(9) #偏移量的单位是字节
#     # print(f.tell())
#     f.write('[老男孩第二帅的人]')


#修改文件方式一：
#1、先把文件内容全部读入内存
#2、然后在内存中完成修改
#3、再把修改后的结果覆盖写入原文件
#缺点：会在文件内容过大的情况下，占用过多的内存


# with open('user.txt',mode='r',encoding='utf-8') as f:
#     data=f.read()
#     data=data.replace('吴佩其','吴佩其[老男孩第二帅的人]')
#
# with open('user.txt',mode='w',encoding='utf-8') as f:
#     f.write(data)


#修改文件方式二：
#1、以读的方式打开原文件，以写的方式打开一个新文件
import os

with open('user.txt',mode='rt',encoding='utf-8') as read_f,\
        open('user.txt.swap',mode='wt',encoding='utf-8') as write_f:

    for line in read_f:
        if '吴佩其' in line:
            line=line.replace('吴佩其','吴佩其[老男汉特别特别的老]')

        write_f.write(line)

os.remove('user.txt')
os.rename('user.txt.swap','user.txt')
#-*- coding:utf8 -*-

'''
输入要修改的文件名 想修改的内容 新的内容
就会在文件的同级目录下 产生修改后的以源文件名+'.bak'结尾的新的文件。
'''


import sys
print sys.argv   #sys.argv 读取程序运行参数列表，打印一下参数列表，以便确定参数的下标是否正确
filename=sys.argv[1]
f1=open(filename,'r')
f2=open(filename+'.bak','w')  #这里尤其要注意，要用+'.bak'，才能创建filename.bak文件。
a=sys.argv[2]#.decode('gbk').encode('utf8')   #如果原文是utf8，而comd命令行是gbk，只有转成utf8才能找到相应字符，否则找不到。
b=sys.argv[3]#.decode('gbk').encode('utf8')   #替换的内容如果是中文，不转码，就会乱码
for line in f1:
    if a in line:
        line=line.replace(a,b)
    f2.write(line)
f1.close()
f2.close()
'''运行的命令：
python D:\wksp1\pcy1\day5_import_lib\sys_moudel\sys_2修改文件.py 要修改的文件 想修改的内容 新内容
格式 python 程序名 要修改的文件 想修改的内容 新内容'''
import os

# res=os.getcwd()
# print(res)

# res=os.listdir('.')
# print(res)

# print(os.sep)
# print([os.linesep,])
# print(os.pathsep)

# res=os.system('ipconfig')
# print('返回值',res)

#os.path系列

# file_path=r'a\b\c\d.txt'
# print(os.path.abspath(file_path))

# res=os.path.split(r'C:\a\b\c\d.txt')
# print(res[-1])
# print(res[0])

# print(os.path.isabs(r'b/c/d.txt'))



# print(os.path.normcase('c:/windows\\system32\\') )
# import os
# BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# DB_PATH=r'%s\db\db.txt' %BASE_DIR
# print(os.path.normcase(DB_PATH))

# print(os.path.normpath('c://windows\\System32\\../Temp/'))


# BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)


res=os.path.normpath(os.path.join(__file__,'..','..'))
print(res)


# 优先掌握
# print(os.path.dirname(r'C:\a\b\c\d.txt'))
# print(os.path.basename(r'C:\a\b\c\d.txt'))

#  os.path.exists只管路径是否存在，不区分文件还是文件夹
# print(os.path.exists(r'D:\code\SH_fullstack_s1\day15\下午\json.py'))
# print(os.path.exists(r'D:\code\SH_fullstack_s1\day15'))

#os.path.isfile如果path是一个存在的文件，返回True。否则返回False
# print(os.path.isfile(r'D:\code\SH_fullstack_s1\day15\下午'))

# os.path.isdir


# print(os.path.join('C:\\','a','b','a.txt'))
# print(os.path.join('C:\\','a','D:\\','b','a.txt'))

# print(os.path.join('a','b','a.txt'))

# res=os.path.getsize(r'D:\code\SH_fullstack_s1\day15\上午\settings.py') # 单位是字节
# print(res)






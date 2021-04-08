import os,shutil

os.makedirs(r'D:/a/b/c')

# shutil.rmtree(r'D:/a/b') #删除b 文件夹 不删除 a

# os.listdir(path)
# 返回path指定的文件夹包含的文件或文件夹的名字的列表。
print(os.listdir(r'D:/a')) # 不返回路径 只返回名字列表
#  ['b']

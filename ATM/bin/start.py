#整个项目的执行文件 触发整个项目的执行
import sys,os
# print (sys.path) #环境变量 列表

print(__file__)#当前文件的路径 d:/pyj/st/ATM/bin/start.py
print (os.path.dirname(__file__)) #取得当前文件的目录 d:/pyj/st/ATM/bin
#找到项目根目录
BASE_DIR=os.path.dirname(os.path.dirname(__file__)) # 取得父目录，即项目根目录
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)
# print(sys.path)
from core import src

if __name__ == "__main__":
    src.run()
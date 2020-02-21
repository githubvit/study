import sys,os

# 应该把项目的根目录添加到环境变量中
# sys.path.append(r'D:\code\SH_fullstack_s1\day15\ATM')
# 拿到ATM所在的文件夹
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# BASE_DIR=os.path.normpath(os.path.join(
#     __file__,
#     '..',
#     '..'
# ))

sys.path.append(BASE_DIR)

from core import src

if __name__ == '__main__':
    src.run()
# 九宫格布局
from PySide2.QtWidgets import *
from PySide2.QtCore import *

app=QApplication([])

wd=QWidget()
wd.resize(500,500)
wd.move(300,300)

# 总的小控件个数
w_num=9
# 设置每行总列数
cl_num=3

# 每个小控件宽度
w_width=wd.width()/cl_num

# 旧方法
    # 总行数
    # print('取余',w_num%cl_num)
    # # 取余 有余数则+1
    # if w_num%cl_num: 
    #     r_num=w_num//cl_num+1
    # else:
    #     r_num=w_num//cl_num
    # 每个小控件高度
    # w_height=wd.height()/r_num
    # 生成控件
    # for i in range(1,w_num+1):
    #     # 生成一个小控件
    #     w=QWidget(wd)
    #     w.resize(w_width,w_height)
    #     # 设定move的x和y
    #     # 对列数取余1，2，0
    #     n=i%cl_num

    #     if n:
    #         w_x=(n-1)*w_width
    #         w_y=(i//cl_num)*w_height
    #     else:
    #         w_x=(cl_num-1)*w_width
    #         w_y=(i//cl_num-1)*w_height
    #     # print(w_x,w_y)    
    #     w.move(w_x,w_y)
    #     w.setStyleSheet('background-color:red; border:1px solid cyan')

# 正确思路
# 九宫格布局案例 可以引申到n宫格
#           3列
# |   0列 |   1列 |   2列  |
# |———————|———————|———————|   ————————
# |    0  |    1  |    2  |     0行
# |———————|———————|———————|   ————————
# |    3  |    4  |    5  |     1行
# |———————|———————|———————|   ————————
# |    6  |    7  |    8  |     2行
# |———————|———————|———————|   ————————
# 每个控件编号如图，行号如图，列号如图，均从0计算
# 编号对总列数取整 等于 行号
# 编号//总列数= 行号
# 编号对总列数取余 等于 列号
# 编号 % 总列数 = 列号

# 总编号=实际总数量-1
# 最大行号=总编号//总列数
# 实际总行数=最大行号+1

# 那么 通用公式：
    # 实际总行数=(实际总数量-1)//总列数+1

# 总行数用通用公式 实际总行数=(实际总数量-1)//每行列数+1 更简单 
r_num=(w_num-1)//cl_num+1

# 每个小控件高度
w_height=wd.height()/r_num

print(w_width,w_height,r_num)

# 用九宫格方案 控件编号和行号还有列号都从0计算  该解决方案 显然比 旧方案 更方便
for i in range(0,w_num):
    # 生成一个小控件
    w=QWidget(wd)
    w.resize(w_width,w_height)
    # 设定move的x和y
    # i为控件编号 编号对列数取余 0、1、2*宽度 列号x宽度即为w_x
    w_x=i%cl_num*w_width
    # 编号对列数取整 即为行号 行号*高度 即为w_y 
    w_y=i//cl_num*w_height
    # print(w_x,w_y)    
    w.move(w_x,w_y)
    # 奇数背景为红 偶数背景为绿 
    if i%2:
        w.setStyleSheet('background-color:red; border:1px solid cyan')
    else:
        w.setStyleSheet('background-color:green; border:1px solid cyan')


wd.show()

app.exec_()
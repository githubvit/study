from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('布局管理QFormLayout的学习')
        self.setup_ui()


    def setup_ui(self):
        # 网格布局(多行多列)
        # 操作类似excel表的单元和单元合并，达到一种表格结构。 

        # 定义三个子控件，不用设置父对象、父控件
        lb1=QLabel('标签1')
        lb1.setStyleSheet('background-color:cyan')
        lb2=QLabel('标签2')
        lb2.setStyleSheet('background-color:red')
        lb3=QLabel('标签3')
        lb3.setStyleSheet('background-color:blue')
        lb4=QLabel('标签4')
        lb4.setStyleSheet('background-color:orange')
        
        # 1 定义布局对象
        grid_layout=QGridLayout()

        # 2 设置布局
        self.setLayout(grid_layout)

        # 3 添加控件
        # grid_layout.addWidget(lb1)
        # grid_layout.addWidget(lb2)
        # grid_layout.addWidget(lb3)

        # 以上达到的效果就是盒式垂直布局的效果
        # 共3行1列
        #  ____________
        # |_____lb1____|
        # |_____lb2____|
        # |_____lb3____|

        # 而作为网格布局的添加控件,要注意添加控件的位置 哪一行 哪一列 
        # 而如果要想实现合并多行多列的效果，就要继续添加 占几行 占几列 ，这就把上面的位置称为起始位置

        # grid_layout.addWidget(lb1,0,0)
        # grid_layout.addWidget(lb2,0,1)
        # grid_layout.addWidget(lb3,1,0)
        # 共2行2列
        #  ___________
        # |_lb1_|_lb2_|
        # |_lb3_|_____|
        # 

        # grid_layout.addWidget(lb1,0,0)
        # grid_layout.addWidget(lb2,0,1)
        # grid_layout.addWidget(lb3,1,0,3,2) # 合并 起始位置 1,0,占据3行2列

        # 共4行2列
        #  ___________
        # |_lb1_|_lb2_|
        # |           |
        # |    lb3    |
        # |___________|
        # 

        # 4 添加布局

        lb5=QLabel('标签5')
        lb5.setStyleSheet('background-color:yellow')
        lb6=QLabel('标签6')
        lb6.setStyleSheet('background-color:green')
        lb7=QLabel('标签7')
        lb7.setStyleSheet('background-color:pink')

        # 定义布局对象
        v_layout=QVBoxLayout()

        # 将5 6 7添加到水平布局中
        v_layout.addWidget(lb5)
        v_layout.addWidget(lb6)
        v_layout.addWidget(lb7)

        grid_layout.addWidget(lb1,0,0)
        grid_layout.addWidget(lb2,0,1)
        grid_layout.addWidget(lb3,1,0,3,3) # 合并 起始位置 1,0,占据3行3列
        # 添加布局
        grid_layout.addLayout(v_layout,4,0,1,4) # 合并 起始位置 4，0，占据1行4列

        # 共5行4列
        #  ___________
        # |_lb1_|_lb2_|___
        # |               |
        # |    lb3        |
        # |_______________|___
        # |_____v_layout______|
        # 
        
        # 5 获取
        # 5.1 获取某条目的位置
        # 总共有4个条目，lb1,lb2,lb3,v_layout（算一个条目）。
        # 获取索引号为0的条目的位置情况 即lb1的位置情况
        # print(grid_layout.getItemPosition(0))#(0, 0, 1, 1) 起始位置0，0 占据1行1列
        # 获取索引号为2的条目的位置情况 即lb3的位置情况
        # print(grid_layout.getItemPosition(2))#(1, 0, 3, 3) 起始位置1, 0 占据3行3列

        # 5.2 获取某个位置的条目 
        # 获取0，0位置的条目 即 lb1
        # print(grid_layout.itemAtPosition(0,0)) #<PySide2.QtWidgets.QWidgetItem object at 0x0000015B969BB648>
        # print(grid_layout.itemAtPosition(0,0).widget().text()) # 标签1

        # 获取1,0位置的条目 即lb3 
        # 由于lb3 占据的位置较大，所以多个位置获取到条目都是lb3 比如 2，0和3，0等
        print(grid_layout.itemAtPosition(1,0).widget().text()) # 标签3

        # 6 列宽行高
        # 设置最小列宽和行高，使得不能一直被压缩
        # 默认的最小列宽和行高，都是保证标签文本可以被看清的最小建议尺寸。
        # 设置某列最小列宽
        grid_layout.setColumnMinimumWidth(0,50)#(列索引号，列宽)
        # 设置某行最小行高
        grid_layout.setRowMinimumHeight(1,50)#(行索引号，行高)

        # 7 拉伸系数
        # 行拉伸系数
        # 设置0行的拉伸系数为1 由于其他行没有设拉伸系数，相当于=0，所以，0行占据所有空白，其他行被压缩至最小名义尺寸。
        # 只有0行会随着窗口的大小变化而变化，直到压缩到最小列宽行高时。
        # 其他行不会变化。
        grid_layout.setRowStretch(0,1)

        # 列拉伸系数
        # 设置0列的拉伸系统为1
        # 由于其他列的拉伸系数=0，所以，0列占据所有空白。跟随窗口变化，直至最小。
        # 其他列保持最小名义尺寸，不随窗口变化。
        grid_layout.setColumnStretch(0,1)

        # 8 案例 使得盒子布局中的标签5占据所有空白。

        # 8.1 修改标签5的伸缩因子或叫拉伸系数

        v_layout.setStretchFactor(lb5,1)

        # 8.2 修改盒子布局在网格布局中的拉伸系数

        # 设定盒子布局起始位置4，0占据所有空白
        # 设定行号4的拉伸系数为1
        grid_layout.setRowStretch(4,1)
        # 关闭前面0行的拉伸系数
        # 设定行号0的拉伸系数为0 
        grid_layout.setRowStretch(0,0)

        # 前面已经把0列的拉伸系数设为1，所以不用设了。

        # 9 间距
        # 查看默认的水平和垂直间距
        print(grid_layout.spacing()) # 6
        # 单独查看水平和垂直间距
        print(grid_layout.horizontalSpacing()) # 6
        print(grid_layout.verticalSpacing()) # 6

        # 修改垂直间距
        # grid_layout.setVerticalSpacing(60)
        # 修改水平间距
        # grid_layout.setHorizontalSpacing(60)

        # 同时修改
        # grid_layout.setSpacing(60)

        # 10 布局方向——原点角
        # Qt.TopLeftCorner # 左上 默认
        # Qt.TopRightCorner # 右上
        # Qt.BottomLeftCorner # 左下
        # Qt.BottomRightCorner # 右下

        # 原点 改为右下
        # 整个布局从右下开始 
        # 则 0行 0列 在右下  lb1就在右下。
        # grid_layout.setOriginCorner(Qt.BottomRightCorner)

        # 11 获取布局参数
        # 共几行几列
        print(grid_layout.rowCount())    #5
        print(grid_layout.columnCount()) #4

        # 0行1列 单元格 大小
        # 即lb2
        # print(grid_layout.cellRect(0,1)) # PySide2.QtCore.QRect(0, 0, 0, 0) 这里看不到的，要等到window.show()才可以。

        print(grid_layout.itemAtPosition(0,1).widget().text()) #标签2

        


        pass
if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    # 查看 0行1列 单元格 大小 要在窗口show()后
    print(wd.layout().cellRect(0,1)) # PySide2.QtCore.QRect(339, 11, 30, 12)
    app.exec_()
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('布局管理QBoxLayout的学习')
        self.setup_ui()


    def setup_ui(self):
        # 布局管理器不是界面控件，而是界面控件的定位策略。
        # 1 定义布局管理器对象
        # 2 在该布局对象内添加子控件
        # 3 把该布局对象交给需要设置的父控件
        

        # 定义三个子控件，不用设置父对象、父控件
        lb1=QLabel('标签1')
        lb1.setStyleSheet('background-color:cyan')
        lb2=QLabel('标签2')
        lb2.setStyleSheet('background-color:red')
        lb3=QLabel('标签3')
        lb3.setStyleSheet('background-color:blue')
        lb4=QLabel('标签4')
        lb4.setStyleSheet('background-color:orange')

        # 定义布局对象
        h_layout=QBoxLayout(QBoxLayout.LeftToRight)

        # 为对象添加布局控件
        h_layout.addWidget(lb1)
        h_layout.addWidget(lb2)
        h_layout.addWidget(lb3)
        h_layout.addWidget(lb4)

        

        # 设置布局
        self.setLayout(h_layout)
        
        # 一 每秒调整一次布局 
        # 通过该例 明白 对于pyqt5 方向QBoxLayout.LeftToRight只是QBoxLayout的枚举值（0-3）
        # 知道后期可以不断调整布局方向
        timer=QTimer(self)
        def change_layout():
            # 让其加1对4取余
            h_layout.setDirection((h_layout.direction()+1)%4) # pyqt5支持 pyside2不支持

        # timer.timeout.connect(change_layout)

        # timer.start(1000)

        # 调整布局
        # h_layout.setDirection(QBoxLayout.TopToBottom)

        # 二 插入
        # 1 插入控件
        # 在lb1后插入新标签lb5
        lb5=QLabel('标签5')
        lb5.setStyleSheet('background-color:yellow')
        h_layout.insertWidget(1,lb5)#(位置索引,插入的控件)

        # 2 插入布局
        # 在lb1后面插入布局
        lb6=QLabel('标签6')
        lb6.setStyleSheet('background-color:green')
        lb7=QLabel('标签7')
        lb7.setStyleSheet('background-color:pink')

        new_layout=QBoxLayout(QBoxLayout.TopToBottom)
        new_layout.addWidget(lb6)
        new_layout.addWidget(lb7)

        h_layout.insertLayout(1,new_layout)#(位置索引,插入的布局)

        # 三 移除控件
        # 移除标签1
        # h_layout.removeWidget(lb1) # 第一步
        # 处理移除的标签1 
        # 当然也可以直接隐藏，不用removeWidge，看上去就没了
        # lb1.hide()
        # show出来，就还原了
        # lb1.show()

        # 四 添加和插入空白 
        # 空白：占据一定大小尺寸的空白，并且不会随着窗口的大小而变。
        # 可以用来加大控件之间的距离，因为，控件之间的距离本来就不会随着窗口大小的改变而改变
        # h_layout.addSpacing(20)#（尺寸）加在后面看不清楚
        # 插入在标签1后 希望加大标签1和后面的标签或布局之间的距离到20
        h_layout.insertSpacing(1,20)#(位置索引,空白的尺寸) 这个20已经包含了原来控件之间的距离。
       
        lb8=QLabel('标签8')
        lb8.setStyleSheet('background-color:white')
        # 在黄5红2之间插入 要计算空白的索引
        h_layout.insertWidget(4,lb8)

        # 五 添加弹簧 伸缩因子
    

       
        


        pass
if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('布局管理')
        self.setup_ui()


    def setup_ui(self):
        # 布局管理器不是界面控件，而是界面控件的定位策略。
        # 1 定义布局管理器对象
        # 2 把该布局对象交给需要设置的父控件
        # 3 在该布局对象内添加子控件

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
        v_layout=QBoxLayout(QBoxLayout.TopToBottom)

        # 设置对象
        # self.setLayout(v_layout)

        # 为对象添加布局控件
        v_layout.addWidget(lb1)
        v_layout.addWidget(lb2)
        v_layout.addWidget(lb3)

        # 一 控件替换
        # 标签4替换标签2
        v_layout.replaceWidget(lb2,lb4) # 这只是第一步 现在看是乱的

        # 第二步 对被替换下的标签不能不管，可以隐藏、删除或将其添加到别的管理器中

        # 1 隐藏被替换的标签2 将其隐藏
        # lb2.hide() 
        # 设置对象即 self.setLayout(v_layout) 放在前面不行，看不到lb4，只有放到后面，才能看到效果 

        # 2 删除被替换的标签2 
        # 定义删除了的信号
        lb2.destroyed.connect(lambda : print('标签2被删除了'))   
        # 删除 
        # 现在lb2被替换 就已经被管理器断开 现在还在引用lb2的是 self  即其父控件
        # 因此，巧用设定其父控件为None 断开其所有引用 让其引用计数为0 达到删除的目的
        lb2.setParent(None)

        # 二 布局嵌套 
        # 也就是 在一个布局中添加另一个布局
        # 设置标签5，6，7 水平布局
        # 把该布局放在上面布局的最后一行
        lb5=QLabel('标签5')
        lb5.setStyleSheet('background-color:yellow')
        lb6=QLabel('标签6')
        lb6.setStyleSheet('background-color:green')
        lb7=QLabel('标签7')
        lb7.setStyleSheet('background-color:pink')

        # 定义水平布局对象
        h_layout=QHBoxLayout() # 默认从左到右
        # h_layout=QVBoxLayout() #默认从上到下

        # 将5 6 7添加到水平布局中
        h_layout.addWidget(lb5)
        h_layout.addWidget(lb6)
        h_layout.addWidget(lb7)

        # 在垂直布局中添加水平布局
        v_layout.addLayout(h_layout)
        h_layout.setSpacing(5)
        h_layout.setMargin(5)
        v_layout.setSpacing(0) # 如果子布局没有进行spacing设置，就会margin直接成为子布局的spacing，如果设置过就不会。
        v_layout.setMargin(0)  # 如果子布局没有进行margin设置，就会直接成为子布局的margin，如果设置过就不会。
        


        # 设置对象
        self.setLayout(v_layout)

        # 调整布局
        # v_layout.setDirection(QBoxLayout.LeftToRight) # 不会影响子布局的布局，子布局保持原来的方向。
        




        pass
if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
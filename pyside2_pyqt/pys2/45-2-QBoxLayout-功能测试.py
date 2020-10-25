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
        # h_layout.addWidget(lb1)
        # h_layout.addWidget(lb2)
        # h_layout.addWidget(lb3)
        # h_layout.addWidget(lb4)

        # 一 控件伸缩因子 弹簧
        # 上面的添加方式，每个控件随着窗口大小的变化都是一样的，平均分布。伸缩因子默认值=0
        # 现在添加伸缩因子
        # h_layout.addWidget(lb1,1)
        # h_layout.addWidget(lb2,2)
        # h_layout.addWidget(lb3,1)
        # 这就是把父控件在该水平方向（当有足够空白时）分为4份，lb1占1份，lb2占2份，lb3占1份。
        # 窗口变大（当有足够空白时）这三个控件在该水平方向保持该比例变大，拉大过程中保持lb2=2lb1.
        # 当父控件窗口空白部分被压缩为0时，则标签123在该水平方向保持相同的最小建议尺寸，只能被拉大不能被压缩。
        # 从不能被压缩拉大时，先拉大lb2，当lb2在该方向拉大到等于lb1和lb3两倍时，lb1和lb3才开始被拉大。

        # 二 空白伸缩因子
        # 1 添加空白伸缩因子，默认值都为0. 
        # h_layout.addWidget(lb1) # 保持最小建议尺寸 不会随窗口变化
        # h_layout.addStretch() # 该空白伸缩因子的优先级最高 占据了全部空白 压缩到最小时则保持和标签控件同样大小。
        # h_layout.addWidget(lb2) # 保持最小建议尺寸 不会随窗口变化
        
        # 2 添加空白伸缩因子
        h_layout.addWidget(lb1,1) # 有空白就占据1份 压缩到最小时则保持最小建议尺寸
        h_layout.addStretch(2) # 有空白就占据2份 压缩到最小时则保持和标签控件同样大小,没有则为0。
        h_layout.addWidget(lb2,3) # 有空白就占据3份 压缩到最小时则保持最小建议尺寸

        # 设置布局
        self.setLayout(h_layout)

        # 三 修改伸缩因子
        # 1 修改控件的伸缩因子
        # 修改lb1的伸缩因子为3
        h_layout.setStretchFactor(lb1,3)
        
        # 2 修改布局的伸缩因子

        # 插入布局
        # 在lb1后面插入布局
        lb6=QLabel('标签6')
        lb6.setStyleSheet('background-color:green')
        lb7=QLabel('标签7')
        lb7.setStyleSheet('background-color:pink')
 
        new_layout=QBoxLayout(QBoxLayout.TopToBottom)
        new_layout.addWidget(lb6)
        new_layout.addWidget(lb7)
 
        h_layout.insertLayout(3,new_layout)#(位置索引,插入的布局) 没有设置伸缩因子 保持最小建议尺寸
        # h_layout.insertLayout(3,new_layout,5)#(位置索引,插入的布局,伸缩因子)
        # 修改布局的伸缩因子
        # h_layout.setStretchFactor(new_layout,5)


        pass
if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
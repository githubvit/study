from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class MyLabel(QLabel):
    # 合适的尺寸建议大小 名义尺寸
    def sizeHint(self):
        return QSize(300,200) #尺寸如果小于最小建议尺寸 就按最小建议尺寸 

    # 最小尺寸的建议大小
    # layout 永远不会把一个控件的尺寸设置的比最小的建议尺寸小，
    # 除非设置了最小尺寸setMinimumSize() 或者 尺寸策略是Ignore。
    def minimumSizeHint(self):
        return QSize(100,100)
# 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('布局尺寸策略')
        self.setup_ui()

    def setup_ui(self):
        lb1=MyLabel('标签1') # 有自定义的最小建议尺寸和名义尺寸
        lb1.setStyleSheet('background-color:cyan')
        lb2=QPushButton('标签2-按钮') #只能水平拉伸
        lb2.setStyleSheet('background-color:red')
        lb3=QLabel('标签3')
        lb3.setStyleSheet('background-color:blue')
        lb4=QLabel('标签4')
        lb4.setStyleSheet('background-color:orange')

        v_layout=QVBoxLayout()

        self.setLayout(v_layout)
        v_layout.addWidget(lb1)
        v_layout.addWidget(lb2)
        v_layout.addWidget(lb3)
        v_layout.addWidget(lb4)

        
        # 尺寸策略 QSizePolicy
        # qt默认就已经为所有控件设置了合适的尺寸策略
        # 比如按钮和标签的尺寸策略就不同： 标签可以随窗口水平和垂直拉伸，按钮则只能在水平方向拉伸。
        # 尺寸策略取值

        # 1 水平和垂直方向分开设置尺寸策略

        # Fixed 保持名义尺寸 不放大和缩小
        # lb1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)#(水平方向尺寸策略，垂直方向尺寸策略)
        # 水平方向固定不动 垂直方向可以缩放 
        # lb1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Minimum)
        # 水平方向固定不动 垂直方向以名义尺寸为最大尺寸 以最小建议尺寸为最小尺寸
        # lb1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Maximum) # 垂直方向 lb1的变化在100到200之间
        # 水平方向固定不动 垂直方向以名义尺寸为第一级最小尺寸 ，当所有空白都归零，就继续压缩至最小尺寸。
        # lb1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Preferred) # 垂直方向 lb1的变化在100到200之间
        # 水平方向固定不动 垂直方向优先级高于Preferred, 垂直空白都被lb2给拿走。
        # 注意：当都被压缩至最小再拉大过程中，先被拉大的时lb1，因为空白要先给有名义尺寸的控件，当lb1达到名义尺寸后，然后再按优先级给lb2.
        # lb2.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding) 
        # 水平方向固定不动 垂直方向可以小到没有。
        # lb1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Ignored) 
        
        # 2 用尺寸策略对象设置尺寸策略
        # 定义尺寸策略对象 （水平策略，垂直策略）
        sp=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Ignored)
        # 设置把lb1隐藏也保留位置 必须放在尺寸策略设置之前，才有效
        sp.setRetainSizeWhenHidden(True)
        lb1.setSizePolicy(sp)
        # lb1.hide()

        # 3 setFixedSize 
        # 不管设置了什么尺寸策略，固定尺寸设置是最高优先级
        lb1.setFixedSize(100,100)
        lb2.setFixedSize(400,100)


        pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
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

        # 一 先定义三个子控件，不用设置父对象、父控件
        lb1=QLabel('标签1')
        lb1.setStyleSheet('background-color:cyan')
        lb2=QLabel('标签2')
        lb2.setStyleSheet('background-color:red')
        lb3=QLabel('标签3')
        lb3.setStyleSheet('background-color:blue')

        # 二 定义布局对象 
        # 布局抽象类 QLayout 是布局的基类 有如下子类：
            # 盒式布局 QBoxLayout 有两个子类，也可以不用子类，用方向即可
                # 水平布局 QHBoxLayout
                # 垂直布局 QVBoxLayout 
                # 四个方向：
                    # QBoxLayout.TopToBottom
                    # QBoxLayout.BottomToTop
                    # QBoxLayout.LeftToRight
                    # QBoxLayout.RightToLeft

            # 网格布局 QGridLayout
            # 表单布局 QFormLayout
            # 页面布局 QPageLayout

        # 由于  QLayout 是抽象类，必须子类化才能使用，因此用盒式布局 QBoxLayout子类来测试QLayout功能
        
        # v_layout=QBoxLayout(QBoxLayout.BottomToTop) #默认是QBoxLayout.TopToBottom
        v_layout=QVBoxLayout()
        

        # 三 窗口控件设置布局  为 刚定义的布局对象v_layout
        self.setLayout(v_layout)

        # 四 给布局对象添加先前定义的三个标签 则 三个 标签平分窗口  会自适应窗口的变化
        v_layout.addWidget(lb1)
        v_layout.addWidget(lb2)
        v_layout.addWidget(lb3)


        #自动填充
        # lb2.hide() 

        # 给lb1 添加文本 随着文本的添加会不断增加lb1的高度，压缩lb2和lb3的高度，父控件窗口的总高度不变；
        # 当lb2和lb3已被压到极限（为最低），lb1还在继续添加，这时lb1继续增高，lb2和lb3不变，导致父控件窗口的总高度在不断增加
        # timer=QTimer(lb1)
        # timer.timeout.connect(lambda : lb1.setText(lb1.text()+'\n'+'123'))
        # timer.start(500)


        # 五 调整布局参数   
        
        # 布局对象参数：方向、边距、子控件项目距离
        # 默认布局边距 11 控件距离 6
        # print(v_layout.margin(),v_layout.spacing())#11 6

        # 设置单一边距
        v_layout.setMargin(0)
        # 设置多个不同边距
        # v_layout.setContentsMargins(20,30,40,50)#(左、上、右、下)
        # 设置子控件间的距离
        v_layout.setSpacing(0)
        
        # 布局对象调整布局方向 非常方便
        # v_layout.setDirection(QBoxLayout.LeftToRight) #必须有方向参数
        # 接着可以用父控件调整布局方向 只有在布局调整为横向时，下面的才有效
        # self.setLayoutDirection(Qt.RightToLeft)


        # 六 子控件
        # 通过布局设置self.setLayout(v_layout)和为布局对象添加子控件 v_layout.addWidget(lbn)
        # 都确定了父控件self
        # print(self.children()) #看到布局对象和三个标签都是窗口的子控件、子对象
        # [<PySide2.QtWidgets.QBoxLayout(0x25d7881bb10) at 0x0000025D78B9C308>, 
        # <PySide2.QtWidgets.QLabel(0x25d781fe8d0) at 0x0000025D78B9C288>, 
        # <PySide2.QtWidgets.QLabel(0x25d781fe940) at 0x0000025D78B9C248>, 
        # <PySide2.QtWidgets.QLabel(0x25d781fe0f0) at 0x0000025D78B9C2C8>]

        
        pass
if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
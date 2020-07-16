from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('LCD数字显示控件QLCDNumber的学习')
        self.setup_ui()


    def setup_ui(self):
        # 计时器显示 ，每隔1秒减一
        ld=QLCDNumber(self)
        self.ld=ld
        ld.resize(100,50)
        ld.move(10,10)
        
        # 起始显示100
        self.num=100
        ld.display(self.num)
        ld.setStyleSheet('background-color:#fff')

        # 在ld上挂一个计时器
        self.timer=QTimer(ld)
        # 计时器 timeout信号
        self.timer.timeout.connect(self.change_num)
        # 计时器启动 间隔1秒    
        self.timer.start(1000)
        pass

    # 减一
    def change_num(self):
        self.num-=1
        if self.num<=0:
            self.timer.stop()
            print('结束')
        self.ld.display(self.num)


if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
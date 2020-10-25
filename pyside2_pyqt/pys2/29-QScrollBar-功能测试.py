from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('滚动条QScrollBar的学习')
        self.setup_ui()

    def setup_ui(self):
        # 一般是结合QAbstractScrollArea使用
        # 滚动条通常包括四个单独的控件：滑块、上、下滚动箭头和页面控件
        # 默认是垂直滚动条
        sb = QScrollBar(self)
        sb.resize(30, 200)
        sb.move(100, 100)
        # 设置水平滚动条
        sb2 = QScrollBar(Qt.Horizontal, self)
        sb2.resize(200, 30)
        sb2.move(150, 100)

        sb.valueChanged.connect(lambda val: print(val))
        # 设置大步长 会调整滑块宽度
        sb.setPageStep(50) # 默认的范围是(0,99),大步长设为50，则按两次pageUp,就到顶了，所以，滑块宽度是空白部分的一半。
        # 当前有两个滚动条，用垂直滚动条设置捕捉键盘，则保证键盘会驱动sb，否则，键盘不会驱动任何滚动条。
        sb.grabKeyboard() 
        # sb2.grabKeyboard() #只能设置1个滚动条，如果设置了多个，则后面的会覆盖前面的设置
        pass
        

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
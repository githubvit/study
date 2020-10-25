from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

# 样式获取工具
from qt_css import get_stlye


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('QSS控件样式4-样式冲突')
        self.setup_ui()

    def setup_ui(self):
        btn1=QPushButton('按钮1')
        btn1.setObjectName('okButton')
        btn1.adjustSize()
        btn2=QPushButton('按钮2')
        # btn2.setObjectName('okButton')
        btn2.adjustSize()
        h_layout=QHBoxLayout()
        h_layout.addWidget(btn1)
        h_layout.addWidget(btn2)

        v_layout=QVBoxLayout(self)
        v_layout.addLayout(h_layout)
  


        pass
if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    # 用样式文件设置样式
    # 选择器[:伪状态]{
            # 声明
        # } 
    filepath=r'D:\pyj\st\study\pyside2_pyqt\pys2\test2.css'
    get_stlye(filepath,app)
    app.exec_()
    
# 样式盒子模型
    # 1 外边距    margin
    # 2 边框      border
    # 3 内边距    padding
    # 4 内容区块  content

        
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
        self.setWindowTitle('QSS控件样式3-样式声明')
        self.setup_ui()

    def setup_ui(self):
        lb1=QLabel('标签测试')
        # lb1.resize(300,300)
        # lb1.move(100,100)
        sbx=QSpinBox()
        cbx=QCheckBox('样式测试')
        v_layout=QVBoxLayout()
        self.setLayout(v_layout)
        v_layout.addWidget(lb1)
        v_layout.addWidget(sbx)
        v_layout.addWidget(cbx)

        pass
if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    # 用样式文件设置样式
    # 选择器[:伪状态]{
            # 声明
        # } 
    filepath=r'D:\pyj\st\study\pyside2_pyqt\pys2\test1.css'
    get_stlye(filepath,app)
    app.exec_()
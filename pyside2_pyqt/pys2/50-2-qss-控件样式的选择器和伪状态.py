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
        self.setWindowTitle('QSS控件样式2-样式选择器')
        self.setup_ui()

    def setup_ui(self):
        # qss样式是解决控件的背景、文字、边框的样式效果，针对的是控件样式，不是布局样式。
        
        box1=QWidget(self)
        box1.setObjectName('box1')
        box2=QWidget(self)
        box2.setObjectName('box2')

        v_layout=QVBoxLayout()
        self.setLayout(v_layout)

        v_layout.addWidget(box1)
        v_layout.addWidget(box2)

        
        lb1=QLabel('标签1',box1) 
        lb1.setObjectName('label_1')
        lb1.setProperty('notice_leve','error')#(key,value)
        lb1.move(50,50)
        lb1.resize(200,50)
        
        
        btn1=QPushButton('按钮1',box1)
        btn1.move(150,50)

        cbx=QCheckBox('复选框',box1)
        # cbx.resize(100,50)
        cbx.move(300,20)

        # 设置三态 
        cbx.setTristate(True)
        

        lb2=QLabel('标签2',box2)
        lb2.move(50,50)
        lb2.setProperty('notice_leve','warning')#(key,value)
        lb2.resize(200,50)

        btn2=QPushButton('按钮2',box2)
        btn2.move(150,50)
    
        
        lb3=QLabel('标签3',box2)
        lb3.setObjectName('lb3')
        lb3.move(50,20)

        box3=QWidget(box2)
        box3.setObjectName('box3')
        box3.move(300,20)
        btn4=QPushButton('按钮4',box3)
        btn4.move(20,20)
        pass

if __name__ == "__main__":
    app=QApplication([])

    wd=Window()
    wd.show()

    # 按钮3
    other_btn=QPushButton('按钮3 另一个窗口的按钮')
    other_btn.show()

    # 用样式文件设置样式
    # 选择器[:伪状态]{
            # 声明
        # } 
    filepath=r'D:\pyj\st\study\pyside2_pyqt\pys2\test.css'
    get_stlye(filepath,app)

    app.exec_()
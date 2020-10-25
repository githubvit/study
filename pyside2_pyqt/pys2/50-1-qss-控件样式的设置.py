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
        self.setWindowTitle('QSS控件样式1-样式的设置')
        self.setup_ui()

    def setup_ui(self):
        # qss样式是解决控件的背景、文字、边框的样式效果，针对的是控件样式，不是布局样式。
        box1=QWidget(self)
        box1.setObjectName('box1')
        box2=QWidget(self)
        box2.setObjectName('box2')

        # 1 局部设置 qss
        # 直接在控件上调用setStyleSheet方法，会影响子控件。
        # 参考作用范围：控件本身、子控件
        # box1.setStyleSheet('background-color:orange;') 
        # box2.setStyleSheet('background-color:cyan;')

        # 1.1 如果只想作用在box1的按钮上，使用 选择器 指定范围
        # box1.setStyleSheet('QPushButton { background-color:orange;}')
        
        # 1.2 如果想作用在整个窗口的按钮上 不作用在另一个窗口的按钮3上
        self.setStyleSheet('QPushButton { background-color:orange;}')
        
        

        v_layout=QVBoxLayout()
        

        v_layout.addWidget(box1)
        v_layout.addWidget(box2)
        self.setLayout(v_layout)

        
        lb1=QLabel('标签1',box1) 
        lb1.setObjectName('label_1')
        lb1.move(50,50)
        
        btn1=QPushButton('按钮1',box1)
        btn1.move(150,50)
        

        lb2=QLabel('标签2',box2)
        lb2.move(50,50)
        btn2=QPushButton('按钮2',box2)
        btn2.move(150,50)

        
    
      
        pass

if __name__ == "__main__":
    app=QApplication([])

    wd=Window()
    wd.show()
    # 按钮3
    other_btn=QPushButton('按钮3 另一个窗口的按钮')
    other_btn.show()

    # 2 全局设置
    # 指定全局的QApplication对象，调用对应的setStyleSheet方法
    # app.setStyleSheet(qss_sheet_str)
    # 参考作用范围：应用程序所有控件
    # 最终作用范围：通过选择器二次筛选
    # 2.1 所有按钮都变色
    # app.setStyleSheet('QPushButton { background-color:orange;}')
    # 2.2 让标签1变红色 
    # 通过 id选择器 即给lb1命名
    # app.setStyleSheet('#label_1{ background-color:red;}')
    # 2.3 叠加2.1和2.2
    # app.setStyleSheet('QPushButton{ background-color:orange;} #label_1{ background-color:red;}')

    # 3 使用文件方式
    # 把样式单独做成文件，实现样式和业务逻辑的解耦。
    # 修改或添加样式只要操作样式文件即可。
    # 不会像直接在控件上设置样式那样，影响子控件，像在这里通过选择器设置box1和box2的背景，就不会影响各自的子控件。
   
    # with open(r'D:\pyj\st\study\pyside2_pyqt\pys2\test.css','r',encoding='utf-8') as f:
        # css_str=f.read() 
        # print(css_str)
        # app.setStyleSheet(css_str)
    # 把这个封装成一个工具，可以给不同的app或widget用。
    # 传入样式文件路径 和 需要该样式文件的对象（比如app\QWidget）是整个应用程序还是某个控件。即可。
    filepath=r'D:\pyj\st\study\pyside2_pyqt\pys2\test.css'
    get_stlye(filepath,app)
    app.exec_()
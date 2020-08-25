'''
停靠/悬浮控件 QDockWidget

'''
from PySide2.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QListWidget,QDockWidget,QMainWindow,\
    QHBoxLayout,QVBoxLayout,QTabWidget,QFormLayout,QRadioButton,QCheckBox,QLabel,QStackedWidget,QTextEdit
from PySide2.QtCore import *
from PySide2.QtGui import *

# class Window(QWidget):
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDockWidget的学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        
        # 一 定义 停靠控件
        dock=QDockWidget('悬浮/停靠',self)
        # dock.setWindowTitle('悬浮/停靠')

        # 二 定义 列表控件
        listmenu=QListWidget()
        listmenu.addItems(['列表项1','列表项2','列表项3','列表项4'])

        # 三 设置 将列表控件设置为停靠控件
        dock.setWidget(listmenu)

        # 四 设置中心小部件 (用带布局的QMainWindow做窗体)
        te=QTextEdit(self)
        self.setCentralWidget(te)

        # 五 设置初始停靠区域 (用带布局的QMainWindow做窗体)
        # QMainWindow才有.addDockWidget方法
        self.addDockWidget(Qt.LeftDockWidgetArea,dock)

        # 四 布局(用不带布局的QWidget做窗体)
        # 通过控制布局 可以设定停靠区域

        # layout=QHBoxLayout(self)
       
        # layout.addWidget(dock) 
        # layout.addWidget(te)

        # 六 停靠/悬浮
        # 按 还原 悬浮
        # 双击悬浮标题栏 停靠

        # 带布局的QMainWindow默认就有停靠区域，可以上下左右停靠。
        

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass
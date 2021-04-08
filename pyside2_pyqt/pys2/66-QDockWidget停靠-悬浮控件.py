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
        # dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        dock.setFeatures(dock.AllDockWidgetFeatures)
       

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
        # 
        # layout.addWidget(dock) 
        # layout.addWidget(te)
        

        # 六 停靠/悬浮
        # 按 还原 悬浮
        # 双击悬浮标题栏 停靠

        # 带布局的QMainWindow默认就有停靠区域，可以上下左右停靠。
       
        

        # 七 停靠控件 api

        # setWidget() 	在Dock窗口区域设置QWidget

        # setFloating()	设置Dock窗口是否可以浮动，如果设置为True，则表示可以浮动

        # setAlllowedAreas()	
			
            # 设置窗口可以停靠的区域
          
            # LeftDockWidgetArea:左侧停靠区域
		    # RightDockWidgetArea:右侧停靠区域
		    # TopDockWidgetArea:顶部停靠区域
		    # BottomDockWidgetArea:底部停靠区域


		# setFearures()	
			
            # 设置停靠窗口的功能属性
	
            # DockWidgetClosable:可关闭
            # DockWidgetMovable：可移动
            # DockWidgetFloatable：可漂浮
            # DockWidgetVerticalTitleBar：在左边显示垂直的标签栏
            # AllDockWidgetFeatures:具有前三种属性的所有功能
            # NoDockWidgetFeatures:无法关闭，不能悬浮，不能移动
        # dock.setFeatures(dock.DockWidgetClosable)
        # dock.setFeatures(dock.DockWidgetMovable)
        
        # 去除 停靠控件dock 顶部边框 标题栏
        # 思路就是新建一个空的QWidget，然后填充进顶部。
        # 这样就没有了标题栏了，也就不能关闭或悬浮了。
        # titleBar=QWidget()
        # dock.setTitleBarWidget(titleBar)
        

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass
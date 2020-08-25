'''
多文档 窗口
QMdiArea
QMdiSubWindow

知识点补充：
Qt Main Window框架
主窗口为构建应用程序的用户界面提供了一个框架。
Qt有用于主窗口管理的QMainWindow及其相关类。
QMainWindow有自己的布局，你可以在其中添加QToolBars、QDockWidgets、QMenuBar和QStatusBar。
布局有一个中心区域，可以被任何类型的小部件占用。您可以看到下图的布局。

注意:不支持创建没有中心小部件的主窗口。您必须有一个中心小部件，即使它只是一个占位符。

中心小部件通常是标准的Qt小部件，比如QTextEdit或QGraphicsView。
定制小部件还可以用于高级应用程序。使用setCentralWidget()设置中心小部件。

'''
from PySide2.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QListWidget,QDockWidget,QMdiArea,QMdiSubWindow,\
    QHBoxLayout,QVBoxLayout,QTabWidget,QFormLayout,QRadioButton,QCheckBox,QLabel,QStackedWidget,QTextEdit,QMainWindow,QMenu,QAction
from PySide2.QtCore import *
from PySide2.QtGui import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('多文档窗口的学习')
        self.resize(500,500)
        self.setup_ui()
        self.con=0

    def setup_ui(self):
        # 一 在菜单栏上设置菜单
        # 1 获取窗体菜单栏
        menubar=self.menuBar() 
        # menubar.setStyleSheet('background:#ffe')

        # 2 在菜单栏上定义菜单
        menu=menubar.addMenu('多窗口菜单')
        
        # 添加菜单项
        # menu.addActions([QAction('新建(New)',menu),QAction('层叠(Cascade)',menu),QAction('展开(Tiled)',menu)])
        menu.addAction('新建(New)')
        menu.addAction('层叠(Cascade)')
        menu.addAction('平铺(Tiled)')
        # 信号与槽
        menu.triggered.connect(self.windowaction)

        # 二 定义多窗口区域
        area=QMdiArea()
        self.area=area

        # 三 设置中心小部件
        # 将多窗口区域定义为中心小部件
        self.setCentralWidget(area) 

    def windowaction(self,action):
        item_text=action.text()
        self.con+=1
        # print(item_text)
        # 新建窗口
        if item_text=="新建(New)":
            # 定义多窗口中的子窗口对象
            sub=QMdiSubWindow()
            sub.resize(150,150)
            # 在子窗口中添加一个控件
            sub.setWidget(QTextEdit())
            # 设置子窗口标题
            sub.setWindowTitle(f'子窗口{self.con}')
            # 添加子窗口对象到多窗口中
            self.area.addSubWindow(sub)
            sub.show()
            pass
        # 层叠窗口
        if item_text=="层叠(Cascade)":
            self.area.cascadeSubWindows()
            pass
        # 平铺窗口
        if item_text=="平铺(Tiled)":
            self.area.tileSubWindows()
            pass
        pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass
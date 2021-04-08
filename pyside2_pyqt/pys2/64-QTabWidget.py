'''
选项卡控件 QTabWidget
   
多页面典型案例


'''
from PySide2.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,\
    QHBoxLayout,QVBoxLayout,QTabWidget,QFormLayout,QRadioButton,QCheckBox,QLabel
from PySide2.QtCore import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTabWidget的学习')
        # self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
       
        # 定义选项页
        tab=QTabWidget()
        self.tab=tab
        # 定义多页面
        tab1=QWidget()
        tab2=QWidget()
        tab3=QWidget()
        self.tab1=tab1
        self.tab2=tab2
        self.tab3=tab3
        # 将多个页面添加到选项页
        tab.addTab(tab1,'选项页1')
        tab.addTab(tab2,'选项页2')
        tab.addTab(tab3,'选项页3')
        # 布局
        layout=QVBoxLayout(self)
        layout.addWidget(tab)
        
        # 加载每个tab页面
        self.tab1_ui()
        self.tab2_ui()
        self.tab3_ui()

        # 根据索引改变选项页名称 
        # 从 选项页1 变为 联系方式
        # self.tab.setTabText(0,'联系方式')
        # # 从 选项页2 变为 个人详细信息
        # self.tab.setTabText(1,'个人详细信息')
        # # 从 选项页3 变为 教育程度
        # self.tab.setTabText(2,'教育程度')

        # 选项页的关闭

        # 为选项页添加 可关闭按钮
        tab.setTabsClosable(True)
        # 点击关闭按钮 
        # 会发出 tabCloseRequested信号 并 传递 int 参数，int 是选项页的索引，从右从0开始，移动选项卡则选项页的索引会变
        # 利用该信号 调用 removeTab(int) 方法 即可关闭 该选项页
        # tab.tabCloseRequested.connect(self.close_tab)
        tab.tabCloseRequested.connect(lambda v: self.tab.removeTab(v)) # 用匿名函数更方便

    # 关闭选项页
    def close_tab(self,v):
        self.tab.removeTab(v)
        
    # 为每一个选项页定制一个方法
    def tab1_ui(self):
        # 放个表单
        layout=QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())
        self.tab1.setLayout(layout)
        pass 

    def tab2_ui(self):
        # 表单
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow('性别',sex)
        layout.addRow('生日',QLineEdit())
        self.tab2.setLayout(layout)
        
    def tab3_ui(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('英语'))
        self.tab3.setLayout(layout)
        pass 
        
        

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass
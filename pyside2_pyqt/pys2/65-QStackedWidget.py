'''
堆栈多页面控件 QStackedWidget 

加载多页面 同时只显示一页。

由于选项卡多页面控件QTabWidget的分页是固定模式，

我们把选项卡和多页面分开，就可以用堆栈多页面控件QStackedWidget实现更多的分页模式，

比如左边用列表QListWidget，右边用堆栈分页QStackedWidget。通过在左边切换列表，实现右边堆栈多页面的切换。
   
多页面典型案例


'''
from PySide2.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QListWidget,\
    QHBoxLayout,QVBoxLayout,QTabWidget,QFormLayout,QRadioButton,QCheckBox,QLabel,QStackedWidget
from PySide2.QtCore import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QStackedWidget的学习')
        # self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
       
        # 一 定义左侧列表
        left_list=QListWidget()
        self.left_list=left_list
        # 列表插入列表项 (索引，列表项)
        left_list.insertItem(0,'联系方式')
        left_list.insertItem(1,'个人信息')
        left_list.insertItem(2,'教育程度')

        # 二 定义右侧堆栈多页面
        # 1 定义堆栈控件
        right_stack=QStackedWidget()
        self.right_stack=right_stack
        # 2 定义多页面
        stack1=QWidget()
        stack2=QWidget()
        stack3=QWidget()

        self.stack1=stack1
        self.stack2=stack2
        self.stack3=stack3

        # 3 将多个页面添加到堆栈控件
        right_stack.addWidget(stack1)
        right_stack.addWidget(stack2)
        right_stack.addWidget(stack3)

        # 4 加载多页面
        self.stack1_ui()
        self.stack2_ui()
        self.stack3_ui()

        # 三 布局
        layout=QHBoxLayout(self)
        layout.addWidget(left_list,1)
        layout.addWidget(right_stack,2)

        

        # 四 将 左边列表 和 右边堆栈 联系起来
        # 通过 左边列表页 当前行号变化事件 获取列表项的索引 改变堆栈页的索引 实现多页面切换
        left_list.currentRowChanged.connect(self.change_page)


    # 为每一个堆栈页定制一个方法
    def stack1_ui(self):
        # 放个表单
        layout=QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())
        # 给多页面添加布局    
        self.stack1.setLayout(layout)
        
    def stack2_ui(self):
        # 表单
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow('性别',sex)
        layout.addRow('生日',QLineEdit())
        # 给多页面添加布局 
        self.stack2.setLayout(layout)
        
    def stack3_ui(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        layout.addWidget(QCheckBox('英语'))
        # 给多页面添加布局 
        self.stack3.setLayout(layout)

    # 槽函数 联动左left_list和右right_stack
    def change_page(self,index):
        print(type(index))
        # 用获取左侧列表索引 index 设置右侧堆栈页的索引 实现切换
        self.right_stack.setCurrentIndex(index)


if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass
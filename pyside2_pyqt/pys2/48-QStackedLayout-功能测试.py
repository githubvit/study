from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('布局管理QStackedLayout的学习')
        self.setup_ui()

    def setup_ui(self):
        # QStackedLayout 堆叠布局
        # 同一时刻只能显示一个控件。

        # 1 创建布局管理器对象
        # stack_layout=QStackedLayout()

        # 2 把布局对象设置给父控件
        # self.setLayout(stack_layout)
        # 两步并一步
        stack_layout=QStackedLayout(self)


        # 3 给布局对象添加控件或布局
        # 控件
        lb1=QLabel('标签1')
        lb1.setStyleSheet('background-color:cyan')
        lb2=QLabel('标签2')
        lb2.setStyleSheet('background-color:red')
        lb3=QLabel('标签3')
        lb3.setStyleSheet('background-color:blue')
        lb4=QLabel('标签4')
        lb4.setStyleSheet('background-color:orange')

        # 布局
        lb5=QLabel('标签5')
        lb5.setStyleSheet('background-color:yellow')
        lb6=QLabel('标签6')
        lb6.setStyleSheet('background-color:green')
        lb7=QLabel('标签7')
        lb7.setStyleSheet('background-color:pink')

        # 定义布局对象
        v_layout=QVBoxLayout()

        # 将5 6 7添加到水平布局中
        v_layout.addWidget(lb5)
        v_layout.addWidget(lb6)
        v_layout.addWidget(lb7)

        # 为stack_layout添加控件或布局
        print(stack_layout.addWidget(lb1)) # 返回索引 0
        print(stack_layout.addWidget(lb2)) # 返回索引 1
        print(stack_layout.addWidget(lb3)) # 返回索引 2
        # print(stack_layout.addChildLayout(v_layout))


        # 4 插入控件
        # print('插入前-当前索引',stack_layout.currentIndex()) #插入前-当前索引 0
        # print(stack_layout.insertWidget(0,lb4)) # 插入当前索引位置 是看不到效果的 但是已经插入 从前后的打印结果看出来
        # print('插入后-当前索引',stack_layout.currentIndex()) #插入后-当前索引 1

        # 插入的位置不存在，就插在最后，并返回插入的位置索引。
        print(stack_layout.insertWidget(10,lb4)) # 3

        # 5 从索引号获取控件
        # print(stack_layout.widget(3)) #<PySide2.QtWidgets.QLabel(0x217448d9710) at 0x0000021744C4A508>
        print(stack_layout.widget(3).text()) # 标签4

        # 6 切换堆叠控件
        # 6.1 通过索引
        # 设置为标签2
        # stack_layout.setCurrentIndex(1)
        # 6.2 通过名称
        # stack_layout.setCurrentWidget(lb4)

        # 信号
        # 当前控件索引变化
        stack_layout.currentChanged.connect(lambda idx: print(idx))

        # 移除控件信号
        stack_layout.widgetRemoved.connect(lambda idx: print('移除了',idx))

        # 6.3 案例 每秒切换一次
        timer=QTimer(self)
        # timer.timeout.connect(lambda : (stack_layout.setCurrentIndex((stack_layout.currentIndex()+1)%stack_layout.count())))
        timer.start(1000)
        
        # 7 展示模式
        # 7.1 默认模式 
        # 只有当前控件可见，其余不可见
        # QStackedLayout.StackOne
        # 在这种模式下 当把当前控件隐藏，则都不可见
        # 获取当前索引
        # idx=stack_layout.currentIndex()
        
        # 获取当前索引控件 并隐藏
        # stack_layout.widget(idx).hide()
        # 把当前标签设小的时候也看不见后面的
        # stack_layout.widget(idx).setFixedSize(100,100)


        
        # 7.2 都可见模式
        # QStackedLayout.StackAll
        # 设置当前模式都可见
        # stack_layout.setStackingMode(QStackedLayout.StackAll)
        # 隐藏当前控件，则 可以看到后面的控件。
        # 获取当前索引
        # idx=stack_layout.currentIndex()
        # 获取当前索引控件 并隐藏
        # stack_layout.widget(idx).hide()

        # 把当前标签设小的时候也可以看见后面的
        # stack_layout.widget(idx).setFixedSize(100,100)

        # 8 移除控件
        # 移除当前控件 后面的控件会显示出来（即使是默认展示模式）
        # print('删前的当前标签',stack_layout.widget(idx).text())
        # lb1.destroyed.connect(lambda : print('标签1被释放'))
        # stack_layout.removeWidget(stack_layout.widget(idx))
        # 获取新的当前控件
        # print('删后的当前标签',stack_layout.widget(stack_layout.currentIndex()).text())

        
     
        
        pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
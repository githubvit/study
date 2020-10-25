
# QWidget继承自QObject，具有QObject的所有功能
# QWidget是所有可视控件的基类
# QWidget(parent:no,flag:默认是Qt.Widget)
# flag:控制窗口类型（Qt.Widget、Qt.Window、Qt.Dialog、...）和外观样式（hint）


# 顶层窗口用户空间和顶层窗口外部框架

# 获取api
    # x()和y() pos()如果是顶层，则都是包含外部框架
    # width()、heigh()、size()都是不包含任何外部框架的。
    # geometry()获得用户空间的位置和尺寸组合（cx,cy,width,heigh），不包含任何外部框架。
    # rect()是用户空间位置在(0,0)的尺寸组合（0,0,width,height）。
    # frameSize()和frameGeometry()显然都是包含框架尺寸的

    # 注意: 控件显示完毕之后, 获取的具体位置或者尺寸数据才会正确

# 设置api
    # move(x,y) 包含外部框架的
    # resize(width,heigh)仅指用户空间，不包含外部框架的
    # setGeometry(cx,cy,width,heigh)仅指用户空间，不包含外部框架，控件显示完毕之后, 设置的具体位置或者尺寸数据才会正确。
    # adjustSize() 根据内容自适应大小
    # setFixdSize() 设置固定尺寸

from PySide2.QtWidgets import *
from PySide2.QtCore import *

app=QApplication([])

wd=QWidget()
wd.setWindowTitle('QWidget大小位置')
wd.move(100,100)
wd.resize(500,500)
# 1 正确获取和设置大小位置应在wd.show()以后
# print(wd.geometry())#PySide2.QtCore.QRect(100, 100, 500, 500)
# wd.setGeometry(0, 0, 150, 150)
# 
# 2 案例 自适应大小
label = QLabel(wd)
label.setText("社会顺")
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")
label.adjustSize()
def changeCao():
    new_content = label.text() + "社会顺"
    label.setText(new_content)
    # label.resize(label.width() + 100, label.height())
    #设置为自适应大小
    label.adjustSize()


btn = QPushButton(wd)
btn.setText("增加内容")
btn.move(100, 300)
btn.clicked.connect(changeCao)

wd.show()
# 控件显示完毕之后, 获取的具体位置或者尺寸数据才会正确
# print(wd.geometry()) #PySide2.QtCore.QRect(101, 131, 500, 500)
# 控件显示完毕之后,setGeometry设置的具体位置或者尺寸数据才会正确
# wd.setGeometry(0, 0, 150, 150)
# wd.setGeometry(100, 100, 150, 150)

app.exec_()
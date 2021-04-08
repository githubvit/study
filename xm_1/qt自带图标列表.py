from PySide2.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QLabel,QTableWidget,QListView,QStyle,QGridLayout
from PySide2.QtCore import Qt,Slot
from PySide2.QtGui import QIcon,QStyleHints,QPixmap,QPalette,QColor
# QPixmap 像素图控件是用来处理图像的控件之一。
# 它用于将优化后的图像显示在屏幕上。
# 在我们的代码示例中，我们将使用QPixmap 控件在程序窗口上显示图像。

import os,sys

app=QApplication([])
wd=QWidget()

wd.setGeometry(1000,400,500,400)
wd.setWindowTitle('Qt内置图标')
# 获取内置图标列表
splist=[]
for item in dir(QStyle):
    if item.startswith('SP_'):
        splist.append(item)

print(len(splist)) # 79 共79个内置图标
# print(hasattr(QStyle,splist[0])) #True
# print(getattr(QStyle,splist[0],None)) # PySide2.QtWidgets.QStyle.StandardPixmap.SP_ArrowBack 返回箭头
grid_layout=QGridLayout(wd)
column=9
for i,p in enumerate(splist):
    # print(i,p)
    icon=app.style().standardIcon(getattr(QStyle,splist[i],None))
        # app.style().standardIcon(QStyle.SP_MediaPlay)
    btn=QPushButton()
    btn.setIcon(icon)
    btn.setText(str(i))
    btn.adjustSize()
    btn.setToolTip(p)
    # row=round(i/column)#取整
    row,col=divmod(i,column)#求商 余
    # m,s=divmod(s1,60)
    grid_layout.addWidget(btn,row,col)




wd.show()
app.exec_()
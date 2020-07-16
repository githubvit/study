# 1 单选按钮

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

app=QApplication([])
wd=QWidget()
wd.setWindowTitle('QRadioButton按钮的学习')
wd.resize(500,500)
rb1=QRadioButton(wd)
rb1.setText('男-&Male') #设置快捷键 Alt+m
rb1.move(50,50)
rb2=QRadioButton(wd)
rb2.setText('女-&Female') #设置快捷键 Alt+f
rb2.move(50,100)
# 设置图标
rb2.setIcon(QIcon(r'D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png'))
# 设置图标大小
# rb2.setIconSize(QSize(60,60))
# 查看自动排他性m
print(rb1.autoExclusive())#True
# 取消自动排他性
# rb1.setAutoExclusive(False)
# 查看是否可选
print(rb1.isCheckable())
# 查看是否选中
print(rb1.isChecked())
# 设置默认选中
# rb1.setChecked(True)
# rb2.setChecked(True)
# 设置不可用
# rb2.setEnabled(False)

# 信号
# 选中状态切换
rb1.toggled.connect(lambda val: print('rb1状态',val))



wd.show()
app.exec_()
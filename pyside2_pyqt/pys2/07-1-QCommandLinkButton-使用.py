# 继承自QPushButton，除了普通按钮文本之外，它还允许描述性文本
# 它的用途类似于单选按钮的用途，因为它用于在一组互斥选项之间进行选择
# 作为向导和对话框中单选按钮的替代选项

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
# from PyQt5.Qt import *

app=QApplication([])
wd=QWidget()
wd.setWindowTitle('QCommandLinkButton使用')
wd.resize(500,500)


btn = QCommandLinkButton("标题", "描述", wd)
# btn.setText("标题2")
# 设置描述
# btn.setDescription("社会顺哥")
btn.setIcon(QIcon(r"D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png"))
# 获取描述
print(btn.description())
# 看起来像扁平 但是 不是扁平化 天生就是平面按钮
print(btn.isFlat())#False
# 信号和QPushButton一致
btn.clicked.connect(lambda : print('获取成功',btn.description()))
wd.show()
app.exec_()
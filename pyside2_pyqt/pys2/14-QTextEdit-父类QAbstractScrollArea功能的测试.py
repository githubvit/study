from PySide2.QtWidgets import *

app=QApplication([])
wd=QWidget()
wd.setWindowTitle('滚动区域QAbstractScrollArea的学习')
wd.resize(500,500)

# 是滚动区域的低级抽象类 是框架类QFrame的子类，是QTextEdit的父类
# 只能用子类展示QAbstractScrollArea抽象类的功能
te=QTextEdit(wd)
te.setPlaceholderText('用来展示父类QAbstractScrollArea滚动区域类功能')

# 1 设置水平和垂直滚动条

from PySide2.QtCore import Qt
# 滚动条策略 
    # Qt.ScrollBarAsNeeded 默认
    # Qt.ScrollBarAlwaysOn 
    # Qt.ScrollBarAlwaysOff

# te.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded) # 默认 需要才显示
te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
# te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

# 2 设置角落控件
from PySide2.QtGui import QIcon
btn = QPushButton(wd)
btn.setIcon(QIcon(r"D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png"))
btn.pressed.connect(lambda :print("xxx"))

te.setCornerWidget(btn)

wd.show()
app.exec_()
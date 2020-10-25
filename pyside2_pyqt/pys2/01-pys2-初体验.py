# pyqt或pyside2的优点 或称为什么采用该GUI框架，是因为该框架
    # 面向对象
    # 信号与槽的机制
    # 界面设计与业务代码完全隔离
from PySide2.QtWidgets import QApplication,QWidget,QLabel

app=QApplication([])

wd=QWidget()
wd.setWindowTitle('标题')
wd.resize(500,500)
wd.move(400,200)

# lb=QLabel(wd)
# lb.resize(50,30)
# lb.setText('标签1')
lb=QLabel('标签',wd)
lb.move(200,200)

wd.show()

app.exec_()


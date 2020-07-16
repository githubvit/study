from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

app=QApplication([])

wd=QWidget()
wd.setWindowTitle('多选按钮QCheckBox')
wd.resize(500,500)

# 查看QCheckBox类继承的父类
print(QCheckBox.__bases__)

cb1=QCheckBox('&python',wd)
cb1.setIcon(QIcon(r'pyside2_pyqt\pys2\xxx.png'))
cb1.setIconSize(QSize(30,30))
cb1.move(50,50)

# 设置三态
# 选中 勾  未选中 空  半选中 方
cb1.setTristate(True) # 点一下 是方 半选中 再点 是 勾 全选
# 设置半选中
cb1.setCheckState(Qt.PartiallyChecked)

# 设置了三态 的 信号 用 stateChanged
cb1.stateChanged.connect(lambda state: print(state))# 0 空 1 半选中 2 选中
# 如果用来toggled 不会报错 选中和半选中都是True 
# cb1.toggled.connect(lambda val: print(val))
wd.show()

app.exec_()
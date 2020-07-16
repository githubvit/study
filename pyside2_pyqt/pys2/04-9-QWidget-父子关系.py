# 0. 导入需要的包和模块
from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *
import sys



app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("父子关系学习")
window.resize(500, 500)

label1 = QLabel(window)
# label1.setParent()
label1.setText("标签1")
label1.move(200, 200)

label2 = QLabel(window)
# label1.setParent()
label2.setText("标签2")
label2.move(50, 50)

label3 = QLabel(window)
# label1.setParent()
label3.setText("标签3")
label3.move(100, 100)

# 1 childAt(x, y) 获取在指定坐标的子控件 不含边界，一定要小于边界
print(label1.width(),label1.height())
print(window.childAt(299, 229),label1)
print(window.childAt(300, 229))
# 2 parentWidget() 获取指定控件的父控件
print(label2.parentWidget(),window)
# 3 childrenRect() 获取所有子控件组成的边界矩形
print(window.childrenRect())
# (x,y,width,height)
#PySide2.QtCore.QRect(50, 50, 250, 180) 


window.show()
sys.exit(app.exec_())
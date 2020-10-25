from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

app = QApplication([])

# 1 设定顶层窗口类型和外观 无边框
window = QWidget()          #创建控件时就设定了窗口的类型为 QWidget类型
# 设定顶层窗口外观样式setWindowFlags(外观样式)
window.setWindowFlags(Qt.FramelessWindowHint) #无边框外观


window.setWindowTitle("顶层窗口")
window.resize(500, 500)

# 2 设定窗口半透明
# window.setWindowOpacity(0.8)

# 3 设定关闭
btn=QPushButton(window)
btn.setText('关闭')
btn.move(200,200)
btn.clicked.connect(window.close)



window.show()

app.exec_()

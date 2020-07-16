from PySide2.QtWidgets import *

app=QApplication([])

#  2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("最小尺寸最大尺寸限定")
# window.resize(500, 500)
# window.setFixedSize(500, 500)
window.setMinimumSize(200, 200)
window.setMaximumSize(500, 500)

# window.setMinimumWidth(500)
# window.setMaximumWidth(800)
window.resize(1000, 1000)

window.show()
print(window.geometry())
# PySide2.QtCore.QRect(1030, 290, 500, 500)
app.exec_()
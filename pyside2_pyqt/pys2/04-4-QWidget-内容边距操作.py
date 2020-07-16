from PySide2.QtWidgets import *

app=QApplication([])

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("内容边距的设定")
window.resize(500, 500)

label = QLabel(window)
label.setText("社会我顺哥, 人狠话不多")#默认水平靠左，垂直居中。
label.resize(300, 300)

label.setStyleSheet("background-color: cyan;")
# 设置内容边距 setContentsMargins(左, 上, 右, 下)
label.setContentsMargins(100, 200, 0, 0)
# 获取内容边距 getContentsMargins()
print(label.getContentsMargins())
# 获取内容区域 contentsRect() （c_x,c_y,c_width,c_height）
print(label.contentsRect())

# 2.3 展示控件
window.show()
app.exec_()
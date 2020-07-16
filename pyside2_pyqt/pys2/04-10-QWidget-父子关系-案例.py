# 0. 导入需要的包和模块
from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *
import sys
# 案例：点击了哪个子控件则哪个子控件背景变化

# 方案一 在标签点击事件中捕捉
# class Label(QLabel):
#     def mousePressEvent(self, QMouseEvent):
#         if self.styleSheet()=="background-color: red;":
#             self.setStyleSheet('background-color:cyan')
#         else:
#             self.setStyleSheet("background-color: red;")

# 方案二 在窗口点击事件中捕捉
class Window(QWidget):
    def mousePressEvent(self, evt):
        local_x = evt.x()
        local_y = evt.y()
        # 查找点击点坐标的子控件
        sub_widget = self.childAt(local_x, local_y)
        if sub_widget is not None:
            if sub_widget.styleSheet() == "background-color: red;":
                sub_widget.setStyleSheet('background-color:cyan')
            else:
                sub_widget.setStyleSheet("background-color: red;")
            print(sub_widget.styleSheet())
        print("被点击了", local_x, local_y)

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# window = Window()
# 2.2 设置控件
window.setWindowTitle("父子关系-子控件背景变化")
window.resize(500, 500)

for i in range(1, 11):
    # label = QLabel(window)
    label = Label(window)
    label.setText("标签" + str(i))
    label.move(40*i, 40*i)
    label.setStyleSheet('background-color:cyan')


# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())
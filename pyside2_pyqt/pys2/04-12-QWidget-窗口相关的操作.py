# 0. 导入需要的包和模块
from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *
import sys

class Window(QWidget):
    # 监听点击 在最大和还原之间切换
    def mousePressEvent(self, QMouseEvent):

        if self.isMaximized():
            # self.show() #这个不会还原
            self.showNormal()
        else:
            self.showMaximized()


app = QApplication(sys.argv)

window = Window()
window.resize(500, 500)
window.setWindowTitle("w1")
# 1 图标
icon = QIcon(r"pyside2_pyqt\pys2\xxx.png")
window.setWindowIcon(icon)
#
# # QIcon
# print(window.windowIcon())
#
# 2 标题
window.setWindowTitle(" ")
# print(window.windowTitle())
#
# 3 不透明度 setWindowOpacity(float 0.0-1.0 )
window.setWindowOpacity(0.9)
# print(window.windowOpacity())

# 4 窗口状态
# 状态 state
# Qt.WindowNoState  无状态 即普通状态
print(window.windowState())
# 

# window.setWindowState(Qt.WindowMinimized)     #最小化状态
# window.setWindowState(Qt.WindowMaximized)     #最大化状态
# window.setWindowState(Qt.WindowFullScreen)    #全屏状态

# 状态判断 isxxx优先使用
print(window.isActiveWindow())  #是活动窗口吗 不要用 window.windowState() == Qt.WindowMaximized
print(window.isMaximized())     #是最大化窗口吗
print(window.isMinimized())     #是最小化窗口吗
print(window.isFullScreen())    #是全屏窗口吗
print(window.windowState() == Qt.WindowNoState) #是普通状态吗 这个没有isxxx


w2 = QWidget()
w2.setWindowTitle("w2")


window.show()
w2.show()

# 5 最大最小化全屏显示
# window.showMaximized()
# window.showFullScreen()
# window.showMinimized()

window.setWindowState(Qt.WindowActive)        #活动状态 当有多个窗口时 设为当前窗口 

sys.exit(app.exec_())
from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

# 监听绘制事件
class Window(QWidget):
    def paintEvent(self, evt):
        print("窗口被绘制了")
        return super().paintEvent(evt)

class Btn(QPushButton):
    def paintEvent(self, evt):
        print("按钮被绘制了")
        return super().paintEvent(evt)


app = QApplication([])

window = Window()

window.setWindowTitle("交互状态")
window.resize(500, 500)


btn = Btn(window)
btn.setText("按钮")
# 1 是否可用 
# setEnabled(bool) 状态 isEnabled()
print(btn.isEnabled())

# btn.setEnabled(False)#设置不可用

btn.destroyed.connect(lambda : print("按钮被释放了"))

# 2 是否显示/隐藏
# btn.setVisible(False)
# btn.setHidden(True)
# btn.hide()
#
# 3 是否编辑 加* [*]
window.setWindowTitle("交互状态[*]") 
# window.setWindowModified(True) 
print(window.isWindowModified())

# 4 关闭
# btn.deleteLater()
# btn.setAttribute(Qt.WA_DeleteOnClose, True)#设置关闭后删除按钮对象 即释放按钮
# btn.close()#如果设置了上面的属性，则关闭就会释放按钮，没有上面的设置，关闭不会释放按钮
# btn.setVisible(False)#设为不可见按钮不会被释放

# 5 活动窗口 (当有两个同级窗口，比如两个顶层窗口)
w2=QWidget()

w2.show()

window.show()
w2.raise_() #把w2放到前面
print(w2.isActiveWindow())# False 不是活动窗口，即使把w2放到前面，也是False。
# 设定w2为活动窗口
w2.setWindowState(Qt.WindowActive)
print(w2.isActiveWindow())# True
app.exec_()
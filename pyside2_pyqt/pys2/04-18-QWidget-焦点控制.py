
from PySide2.QtWidgets import *
from PySide2.QtCore import *
# from PyQt5.Qt import *
import sys

# 鼠标按下切换子控件焦点
class Window(QWidget):
    def mousePressEvent(self, evt):
        print(self.focusWidget())#打印获取焦点的控件
        self.focusNextChild()#切换到下一个
        # self.focusPreviousChild()#切换到前一个
        # self.focusNextPrevChild(True) #就是 self.focusNextChild()
        # self.focusNextPrevChild(False) #就是 self.focusPreviousChild()


app = QApplication(sys.argv)


window = Window()

window.setWindowTitle("焦点控制")
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(50, 50)
le2 = QLineEdit(window)
le2.move(100, 100)
le3 = QLineEdit(window)
le3.move(150, 150)

# 文本框获取焦点的顺序，默认是按照定义的先后顺序，并不是名称的顺序或界面位置的高低。
# le2 = QLineEdit(window)
# le2.move(100, 100)
# le1 = QLineEdit(window)
# le1.move(50, 50)
# le3 = QLineEdit(window)
# le3.move(150, 150)


# setTabOrder仅仅是用来 调整 两个子控件的焦点顺序 因此只有两个参数
# setTabOrder是类的静态方法，用类调用，不是用对象调用
# QWidget.setTabOrder(le1, le3)
# QWidget.setTabOrder(le3, le2) # 仅仅表示 le3 在 le2 前 或 le2在le3后

# 获取焦点
# le2.setFocus()
# 设置焦点获取策略
# le2.setFocusPolicy(Qt.TabFocus)#仅Tab键
# le2.setFocusPolicy(Qt.ClickFocus)#仅单击
# le2.setFocusPolicy(Qt.StrongFocus)#上面两种方法都可 默认
# le2.setFocusPolicy(Qt.NoFocus)#不能通过上两种方式获得焦点,只有通过代码setFocus才能使其获得焦点

# le2.setFocus()
# 取消焦点
# le2.clearFocus()

print(window.focusWidget())
window.show()

# print(le1)
# print(le2)
# print(le3)

# le2.setFocus()

# 没有人为设置获取焦点时，获取当前窗口内部-所有子控件当中获取焦点的那个控件 
# 无论放在show()前或后面 都打印None 要放在某个事件里，事件响应后才可获取到
# 说明焦点是绘制事件结束后加上去的

# 如果在获取焦点控件前 人为 设置一个控件获取焦点，就可以获取到。
# print(window.focusWidget())


# le1.clearFocus()

sys.exit(app.exec_())
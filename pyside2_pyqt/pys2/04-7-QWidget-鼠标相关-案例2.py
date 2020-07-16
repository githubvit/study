from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

# 案例2  监听鼠标进出和键盘事件
class MyLabel(QLabel):
    # 鼠标离开label控件事件
    def leaveEvent(self,mv):
        print('鼠标离开')
        self.setText('谢谢惠顾！')

    # 鼠标进入label控件事件    
    def enterEvent(self,mv):
        print('鼠标进入')
        self.setText('欢迎光临！')

    # label监听键盘事件 要捕获键盘 才能监听到
    # keyReleaseEvent(QKeyEvent)监听键盘释放
    def keyPressEvent(self,kevt):
        # kevt 是 QKeyEvent事件对象

        # 普通键监听kevt.key() 监听tab键
        if kevt.key()== Qt.Key_Tab:
            print('用户点击了Tab键位')

        # 修饰键监听 
        # Qt.ShiftModifier shift修饰键 
        # Qt.ControlModifier ctrl修饰键
        # Qt.AltModifier     Alt修饰键
        if kevt.modifiers() == Qt.ControlModifier and kevt.key()== Qt.Key_S:
            print('用户点击了Ctrl+S')
        
        
        # 多个修饰键要用 按位或键'|'
        # 为什么是按位或
        # 3  == 2 | 1
        # 10
        # 01
        # 11  == 3
        # ctrl+shift+A 监听
        if kevt.modifiers() == Qt.ControlModifier | Qt.AltModifier and kevt.key()== Qt.Key_A:
            print('用户点击了Ctrl+Alt+A')

   
app=QApplication([])

wd=QWidget()
wd.setWindowTitle('监听鼠标进出和键盘事件')
wd.resize(500,500)

lb=MyLabel(wd)
lb.resize(300,300)
lb.setStyleSheet('background-color:cyan')
lb.move(100,100)
lb.setContentsMargins(120, 0, 0, 0)
# 捕获grab键盘Keyboard 取消键盘输入releaseKeyboard
lb.grabKeyboard() 
# lb.grabShortcut()#捕获快捷键，须要设置setShortcutEnabled(true);取消抓取快捷键releaseShortcut
# lb.grabMouse()#捕获鼠标  取消鼠标输入releaseMouse
# lb.grabGesture()#捕获手势 ungrabGesture取消抓取手势 

wd.show()

app.exec_()
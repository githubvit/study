
from PySide2.QtWidgets import *

from PySide2.QtGui import *
from PySide2.QtCore import *
# from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("按钮的功能测试-抽象类")
window.resize(500, 500)

# btn = QPushButton(window)


# # *************1.文本操作***************开始
# btn.move(50,20)
# btn.setText("1")
# def plus_one():
    # print("加一")
    # num = int(btn.text()) + 1
    # btn.setText(str(num))
# 
# btn.pressed.connect(plus_one)
# # *************1.文本操作***************结束


# # *************2.图标操作***************开始

# icon = QIcon(r"pyside2_pyqt\pys2\xxx.png")
# btn.setIcon(icon)
# # #
# size = QSize(50, 50)
# btn.setIconSize(size)

# print(btn.icon())
# print(btn.iconSize())

# # *************2.图标操作***************结束


# # *************3.快捷键的设定***************开始

# 空格键就是默认的快捷键
# btn.pressed.connect(lambda :print("按钮被点击了"))
# 方式1: 按钮由文本的 在字母前加&符号，表示 alt+该字母 就是点击快捷键
# btn.setText("&abc") 
# btn.setText("abc") 
# 方式2: 没有提示文本的 直接用setShortcut("Alt+a")定义快捷键
# btn.setShortcut("Alt+d")#该方式对按钮点击加1，加到2就不灵了。就动了一下

# # *************3.快捷键的设定***************结束


# # *************4.自动重复***************开始
# 应用场景：直播间 送花 游戏中射击 当不松手的时候自动重复发送信号
# 设置自动重复
# btn.setAutoRepeat(True) #按住按钮不松手，按钮数字会不断往上加。
# 设置初次检测延迟 初次延迟2秒
# btn.setAutoRepeatDelay(2000)
# 设置自动重复检测间隔 延长到1秒
# btn.setAutoRepeatInterval(1000)
# 查看是否设置了自动重复
# print(btn.autoRepeat())
# print(btn.autoRepeatInterval())
# print(btn.autoRepeatDelay())

# # *************4.自动重复***************结束


# # *************5.按钮状态***************开始
# # 还有isEnable 是否可用 isDown 是否按下没松开
# push_button = QPushButton(window)
# push_button.setText("这是QPushButton")
# push_button.move(100, 100)
# # # 单选
# radio_button = QRadioButton(window)
# radio_button.setText("这是一个radio")
# radio_button.move(100, 150)
# # # 多选
# checkbox = QCheckBox(window)
# checkbox.setText("这是checkbox")
# checkbox.move(100, 200)

# # #状态样式选择器 按住状态 背景变红
# push_button.setStyleSheet("QPushButton:pressed {background-color: red;}")
# #
# # # 把三个按钮, 置为按下状态
# push_button.setDown(True)
# radio_button.setDown(True)
# checkbox.setDown(True)

# # 设置可选
# push_button.setCheckable(True) #push_button 默认是不可选的设置为可选 就可用了

# # # 是否可选
# print(push_button.isCheckable())    #False 设置可选后则 为 True
# print(radio_button.isCheckable())   #True
# print(checkbox.isCheckable())       #True
# # # 设置选中
# radio_button.setChecked(True) 
# push_button.setChecked(True)
# checkbox.setChecked(True)
# # # 是否选中
# print(push_button.isChecked())
# print(radio_button.isChecked())
# print(checkbox.isChecked())
# #
# def cao():
    # push_button.toggle() 
    # radio_button.toggle() #toggle()在 选中和非选中 状态间切换
    # checkbox.toggle()
#     # toggle() 就是原有的选择状态取反
#     # push_button.setChecked(not push_button.isChecked()) #这个也是状态切换 = push_button.toggle() 
# #
# #
# btn.pressed.connect(cao)
# push_button.toggled.connect(lambda : print('push_button状态切换成功'))
# radio_button.toggled.connect(lambda : print('radio_button状态切换成功'))
# checkbox.toggled.connect(lambda : print('checkbox状态切换成功'))
# # #
# # # 设置是否可用
# push_button.setEnabled(False)
# radio_button.setEnabled(False)
# checkbox.setEnabled(False)
# # 即使这里设置了三个按钮不可用，但是点击btn,通过槽函数三个按钮依然可以切换

# *************5.按钮状态***************结束



# *************6.排他性设置***************开始
# 排他性是指 如果同时存在多个按钮, 而此时所有按钮又设置了排他性,
# 则在同一时刻只能选中一个按钮

# 单选按钮就有排他性，多选按钮排他性就为False

# for i in range(0, 3):
    # btn = QPushButton(window)
    # btn = QRadioButton(window)
    # btn = QCheckBox(window)
    # btn.setText("btn" + str(i))
    # btn.move(50 * i, 50 * i)
# 
    # btn.setAutoExclusive(True) #设置自动排他
    # print(btn.autoExclusive())
    # print(btn.isCheckable())
    # btn.setCheckable(True)


# btn = QPushButton(window)
# btn.setText("btn3")
# btn.move(200, 200)
# btn.setCheckable(True)
# *************6.排他性设置***************结束


# *************7.按钮模拟点击***************开始

# btn = QPushButton(window)
# btn.setText("这是按钮")
# btn.move(200, 200)
# btn.pressed.connect(lambda :print("点击了这个按钮"))
# 
# 设置模拟点击
# btn.click()
# 设置动画模拟点击 指点击的动作会有个动画过程 其余和普通点击一样
# btn.animateClick(4000)#蓝色持续4秒退回到灰色 槽函数不会延迟
# 
# 点击按钮2 驱动模拟点击按钮
# btn2 = QPushButton(window)
# btn2.setText("按钮2")
# def test():
    # btn.click()
    # btn.animateClick(4000)
# btn2.pressed.connect(test)

# *************7.按钮模拟点击***************结束


# *************8.设置按钮点击有效区域及按钮四大信号***************开始

class Btn(QPushButton):
    # 这个函数规定了按钮中的有效点击区域
    def hitButton(self, point): #该函数 返回True 才能是有效的 才能发射相应信号
        print(point) # 返回的是控件内部的坐标
        # 如果在控件的右侧就是有效的 反之无效
        # if point.x() > self.width() / 2:
            # return True
        # return False
# 
        # 通过给定的一个点坐标, 计算与圆心的距离
        yuanxin_x = self.width() / 2
        yuanxin_y = self.height() / 2

        hit_x = point.x()
        hit_y = point.y()

        # 设置有效点击区域为圆内
        # ((x1 - x2) 平方 + (y1 - y2) 平方) 开平方
        import math
        distance = math.sqrt(math.pow(hit_x - yuanxin_x, 2) + math.pow(hit_y - yuanxin_y, 2))
        if distance < self.width() / 2:
            return True
# 
        # 如果距离 < 半径  True
        # 返回 False
        return False
# 
    # 绘制事件 绘制内切圆
    def paintEvent(self, evt):
        super().paintEvent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100, 150, 200), 6))

        painter.drawEllipse(self.rect())
# 
btn = Btn(window)
btn.move(100, 100)
btn.setText("点击")
btn.resize(200, 200)
btn.setCheckable(True)
# 四个信号
btn.pressed.connect(lambda : print("按钮被按下了"))

btn.released.connect(lambda : print("按钮鼠标被释放了"))

btn.clicked.connect(lambda value: print("按钮被点击", value))  #这个value是选中或未选中

btn.toggled.connect(lambda value: print("按钮选中状态发生了改变", value))
# *************8.设置按钮点击有效区域及按钮四大信号***************结束

window.show()

sys.exit(app.exec_())
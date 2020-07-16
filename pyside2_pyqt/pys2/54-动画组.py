from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *   

    # QAnimationGroup  动画组
        # 将一组动画 ，同时播放或按序播放。
        # 功能：
            # 添加动画
                # QAnimationGroup.addAnimation(QAbstractAnimation)
            # 插入动画
                # QAnimationGroup.insertAnimation(QAbstractAnimation)
            # 移除动画
                # QAnimationGroup.removeAnimation(QAbstractAnimation)
            # 获取动画
                # QAnimationGroup.animationAt(int)
            # 获取并移除
                # QAnimationGroup.takeAnimation(int)
            # 获取动画个数
                # QAnimationGroup.animationCount()
            # 清空动画
                # QAnimationGroup.clear() 

        # QParallelAnimationGroup 并行动画
            
        # QSequentialAnimationGroup 串行动画
            # QSequentialAnimationGroup.addPause(暂停时长毫秒) 增加暂停
            # 或者添加暂停动画对象 产生暂停
            # QSequentialAnimationGroup.addAnimation(QPauseAnimation)




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,800)
        self.setWindowTitle('动画组的学习')
        self.setup_ui()

    def setup_ui(self):
        # 两个按钮，一个顺时针转，一个逆时针转。
        red_btn=QPushButton('红色按钮',self)
        green_btn=QPushButton('绿色按钮',self)
        red_btn.setStyleSheet('background-color:red;')
        green_btn.setStyleSheet('background-color:green;')
        w=100
        h=100
        red_btn.resize(w,h)
        green_btn.resize(w,h)
        red_btn.move(0,0)
        green_btn.move(150,150)
        # 创建动画对象 设置目标对象和属性
        animation1=QPropertyAnimation(red_btn,b'pos',self)

        animation2=QPropertyAnimation(green_btn,b'pos',self)

        # 设置属性值 
        # 因为要转圈 所依要用插值
        animation1.setKeyValueAt(0,QPoint(0,0))
        animation1.setKeyValueAt(0.25,QPoint(0,700))
        animation1.setKeyValueAt(0.5,QPoint(700,700))
        animation1.setKeyValueAt(0.75,QPoint(700,0))
        animation1.setKeyValueAt(1,QPoint(0,0))

        animation2.setKeyValueAt(0,QPoint(150,150))
        animation2.setKeyValueAt(0.25,QPoint(550,150))
        animation2.setKeyValueAt(0.5,QPoint(550,550))
        animation2.setKeyValueAt(0.75,QPoint(150,550))
        animation2.setKeyValueAt(1,QPoint(150,150))

        # 设置时长
        animation1.setDuration(5000)
        animation2.setDuration(5000)

        # 建立动画组对象
        animation_group=QParallelAnimationGroup(self) #并行
        # animation_group=QSequentialAnimationGroup(self) #串行
        # 加入动画组
        animation_group.addAnimation(animation1)
        animation_group.addAnimation(animation2)
        

        animation_group.start()

   
        
        pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
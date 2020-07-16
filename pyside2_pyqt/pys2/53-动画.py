from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

# 动画
# QAbstractAnimation 
    # 功能：
        # 循环操作 
            # 设置循环次数
            # QAbstractAnimation.setLoopCount(int) ,loopCount()
            # 获取动画的当前循环
            # QAbstractAnimation.currentLoop()
            # 获取当前循环内的时间
            # QAbstractAnimation.currentLoopTime()
        # 动画方向
            # 设置动画方向
            # QAbstractAnimation.setDirection(QAbstractAnimation.Direction)
            # 获取方向
            # QAbstractAnimation.direction()->QAbstractAnimation.Direction
            # 方向
            # QAbstractAnimation.Direction：
                # QAbstractAnimation.Forward 
                # QAbstractAnimation.Backward 
                
        # 时间操作：
            # 单次时长
                # QAbstractAnimation.duration()
            # 动画总时长
                # QAbstractAnimation.totalDuration()
            # 当前时长
                # QAbstractAnimation.currentTime()

        # 动画状态：
            # QAbstractAnimation.state(QAbstractAnimation.State)
            # QAbstractAnimation.State:
                # QAbstractAnimation.Stopped
                # QAbstractAnimation.Paused
                # QAbstractAnimation.Running
        # 常用属性：
            # QAbstractAnimation.start()
            # QAbstractAnimation.pause()    #暂停
            # QAbstractAnimation.resume()   #恢复
            # QAbstractAnimation.stop()
            # QAbstractAnimation.setCurrentTime(int)
            # QAbstractAnimation.setPaused(bool)

    # 动画常用信号
        # 当前循环索引改变
        # QAbstractAnimation.currentLoopChanged(int) 
        # 当前动画的方向改变
        # QAbstractAnimation.directionChanged(QAbstractAnimation.Direction newDirection)
        # 动画完毕
        # QAbstractAnimation.finished()
        # 动画状态改变
        # QAbstractAnimation.stateChanged(QAbstractAnimation.newState,QAbstractAnimation.oldState)


        
    # QPauseAnimation
        # 暂停动画
        # 在串行动画中使用
        # QPauseAnimation.setDuration(int) #设置暂停时长
    # QVariantAnimation 变量动画
        # 设置时长 
            # QVariantAnimation.setDuration(int msecs)
        # 开始和结束值
            # QVariantAnimation.setStartValue(),startValue()
            # QVariantAnimation.setEndValue(),endValue()
        # 关键值
            # QVariantAnimation.setKeyValueAt()
            # QVariantAnimation.setKeyValues()
        # 动画曲线
            # QVariantAnimation.setEasingCurve(self,Union[QEasingCurve,QEasingCurve.Type])
            # 取值 https://doc.qt.io/qt-5/qeasingcurve.html#Type-enum
        # QPropertyAnimation 属性动画
            # 1 构造动画对象并设置目标属性
                # 常用属性
                    # geometry
                    # pos
                    # size
                    # windowOpacity          

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
            # 




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('动画的学习')
        self.setup_ui()

    def setup_ui(self):
        btn=QPushButton('测试按钮',self)
        btn.move(100,100)
        btn.resize(200,200)
        btn.setStyleSheet('background-color:cyan;')

        # 1 创建动画对象 并且设置目标属性
        # animation=QPropertyAnimation(self)
        # 设置目标对象
        # animation.setTargetObject(btn)
        # 设置属性
        # animation.setPropertyName(b'pos')#bytes类型

        # 构造函数2 上面三步并一步
        animation=QPropertyAnimation(btn,b'pos',self)     #位置
        # animation=QPropertyAnimation(btn,b'size',self)    #尺寸
        # animation=QPropertyAnimation(btn,b'geometry',self)  #位置+尺寸
        animation1=QPropertyAnimation(self,b'windowOpacity',self)  #创建新对象 窗口透明度

        # 2 设置属性值 开始值 插值 结束值 
        animation.setStartValue(QPoint(0,0))
        animation.setEndValue(QPoint(300,300))

        # animation.setStartValue(QSize(0,0))
        # animation.setEndValue(QSize(300,300))

        # animation.setStartValue(QRect(0,0,0,0))
        # animation.setEndValue(QRect(300,300,300,300))

        # 窗口透明度
        animation1.setStartValue(1)
        animation1.setKeyValueAt(0.25,0) # 在动画时长 0.25 即1/4时，属性值变为0
        animation1.setKeyValueAt(0.5,1)  # 在动画时长 0.5 即1/2时，属性值变为1
        animation1.setEndValue(0.3)

        # 3 设置动画时长
        animation.setDuration(5000)
        # animation1.setDuration(3000) #窗口透明度
        
        # 4 设置动画曲线
        # animation.setEasingCurve(QEasingCurve.InQuad) # 先慢后快 半个向上抛物线
        # animation.setEasingCurve(QEasingCurve.OutQuad) # 先快后慢 半个向上抛物线
        # animation.setEasingCurve(QEasingCurve.InBounce) # 开始有弹簧效果
        animation.setEasingCurve(QEasingCurve.OutBounce) # 结束有弹簧效果 这个有质感

        # 7 设置方向 倒放 必须在start()前
        # animation.setDirection(QAbstractAnimation.Backward)#循环
# 
        # 5 启动动画
        animation.start()
        # animation1.start()#窗口透明度

        # 6 循环操作
        # 设定循环次数
        animation.setLoopCount(3)

        # 获取循环次数、总时长和单次时长
        print(animation.loopCount(),animation.totalDuration(),animation.duration())
        # 3 15000 5000

        # 获取当前次数、时长
        btn.clicked.connect(lambda : print('当前循环次数',animation.currentLoop(),'当前循环时间',animation.currentLoopTime(),'当前时间',animation.currentTime()))
        # 当前循环次数 0 当前循环时间 4303 当前时间 4303
        # 当前循环次数 1 当前循环时间 1479 当前时间 6479
        # 当前循环次数 1 当前循环时间 3063 当前时间 8063
        # 当前循环次数 1 当前循环时间 4472 当前时间 9472
        # 当前循环次数 2 当前循环时间 2639 当前时间 12639
        # 当前循环次数 2 当前循环时间 4384 当前时间 14384
        # 当前循环次数 2 当前循环时间 5000 当前时间 15000
        # 当前循环次数 2 当前循环时间 5000 当前时间 15000
        # 当前循环次数 2 当前循环时间 5000 当前时间 15000

        # 8 动画的暂停和恢复
        def animation_operation():
            if animation.state()==QAbstractAnimation.Running:
                animation.pause()
                # animation.stop()
            elif animation.state()==QAbstractAnimation.Stopped:
                animation.start()
                # animation.start(QAbstractAnimation.KeepWhenStopped) #停止时保持 默认
                # animation.start(QAbstractAnimation.DeleteWhenStopped)#停止时删除 动画，
                # 
            elif animation.state()==QAbstractAnimation.Paused:
                animation.resume()
            else:
                animation.stop()

        btn.clicked.connect(animation_operation)

        # 循环信号
        animation.currentLoopChanged.connect(lambda val: print('改变了当前循环次数——',val))
        animation.finished.connect(lambda : print('动画结束'))
        animation.stateChanged.connect(lambda ns,os: print(f'状态改变，从 {os} 变为 {ns}'))
                
        pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('滑动输入QSlide的学习')
        self.setup_ui()

    def setup_ui(self):
        sd=QSlider(self)
        sd.resize(30,200)
        sd.move(50,50)

        lb=QLabel(self)
        lb.resize(50,50)
        lb.move(100,100)
        lb.setStyleSheet('background-color:#fff;border:1px solid #ccc;font-size:30px;')

        # 监听 滑动条
        sd.valueChanged.connect(lambda val: lb.setText(str(val)))

        # 设置范围 默认(0,99) 步长 1 大步长 10
        # sd.setRange(-99,99)
        sd.setMaximum(100)
        sd.setMinimum(-100)

         # 显示刻度
        # sd.setTickPosition(QSlider.TicksRight)
        sd.setTickPosition(QSlider.TicksLeft)
        # sd.setTickPosition(QSlider.TicksBothSides)

        # 设置步长
        # sd.setSingleStep(2) # 小步长 键盘 上下方向
        sd.setPageStep(20)   # 大步长 键盘 翻页 pageDown Up 同步刻度

        
        # 设置当前数值
        sd.setValue(10) #有0默认为0 无0默认最小 

        # 跟踪设置 
        # print(sd.hasTracking()) # 默认是True 滑块与值同步  否则 False 滑动时值不变 松开才显示值
        # sd.setTracking(False)

        # 滑块位置的设置
        # sd.setSliderPosition(88)
        # sd.setValue(88)

        # 信号
        # sd.sliderMoved.connect(lambda val:print(val))
        # sd.actionTriggered.connect(lambda val:print(val))
           # 0 = QAbstractSlider.SliderNoAction
           # 1 = QAbstractSlider.SliderSingleStepAdd 键盘 方向 +
           # 2 = QAbstractSlider.SliderSingleStepSub 键盘 方向 -
           # 3 = QAbstractSlider.SliderPageStepAdd   键盘 翻页 +
           # 4 = QAbstractSlider.SliderPageStepSub   键盘 翻页 -
           # 5 = QAbstractSlider.SliderToMinimum     键盘 Home
           # 6 = QAbstractSlider.SliderToMaximum     键盘 End
           # 7 = QAbstractSlider.SliderMove   鼠标 滚轮
        # sd.rangeChanged.connect(lambda min, max:print(min, max))

        # sd.setMaximum(99)

        # 倒立外观 
        # sd.setInvertedAppearance(True) # 大小翻转
        # sd.setInvertedControls(True)   # 键盘上下翻转
        
        # 设为水平滑块
        # sd.resize(200,30)
        # sd.setOrientation(Qt.Horizontal)
       
        pass
        

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
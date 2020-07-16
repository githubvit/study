# from PySide2.QtWidgets import *
# from PySide2.QtCore import *
# from PySide2.QtGui import *

from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('进度条对话框QProgressDialog的学习')
        self.setup_ui()


    def setup_ui(self):
        # 进度条对话框：
            # 提供了一个缓慢的操作进度反馈，
            # 为用户提供终止操作的机会。
        # 进度条、取消按钮
        # bar=QProgressDialog(self) 
        # 构造函数2
       
        bar=QProgressDialog('xx1','xx2',0,100,self) #(标签文本，cancel按钮文本，最小值（必须是整型），最大值（必须是整型）)
        # 默认的最大、最小、当前值  100 0 -1    
        print(bar.maximum(),bar.minimum(),bar.value()) #默认的当前值 是 -1 = 最小值-1
        # 会自动弹出非模态对话框，要等4秒后才看到。
        # 默认等待时间 为 4秒，也就是打开窗口 4秒后 才弹出进度条对话框，
        # 当用户的进度在4秒内完成了，就不会展示进度条。
        # 比如，用户下载的文件很小，瞬间完成，就不会有进度条对话框出现。
        # print(bar.minimumDuration())#4000
        # 设置最小等待时间 0
        # bar.setMinimumDuration(0)#这样就会马上弹出，不等待
        bar.setValue(95) #必须是整型
        
        # 自动关闭
        # 默认情况是值满了后会自动关闭，现在设置值满后 非自动关闭
        # bar.setAutoClose(False)
        # 自动重置
        # 满值后会自动重置为-1（最小值-1）,进度条为灰色，无进度值。关闭自动重置，进度条会显示100%，然后停住。
        # bar.setAutoReset(False) # 也会使得 满值后 对话框不会自动关闭
        # 对话框自动关闭的前提：要有两个True 默认就是这样的
        print(bar.autoClose())  #True
        print(bar.autoReset())  #True

        
        # 手动弹出 就会立即弹出没有最小等待时间
        bar.open() # 模态
        # bar.open(lambda : print('点击了取消')) #  pyside2 open不接收槽函数 pyqt5可以

        # 模拟进度
        timer=QTimer(bar)
        def start_item():
            # 用代码点击取消 会关闭对话框
            # bar.cancel()
            # 用鼠标点击取消，不会关闭对话框，会重置进度条
            # if bar.value()== bar.maximum() or bar.wasCanceled(): # 一定要先关闭自动重置（bar.setAutoReset(False)），否则永远拿不到bar.maximum() 
            if bar.value()== bar.maximum()-1 or bar.wasCanceled():# 
            # if bar.value()== bar.maximum()-1 :# 用caleled信号控制calel按钮点击
                print('结束')
                #结束计时器
                timer.stop()
                
            bar.setValue(bar.value()+1)
           
        timer.timeout.connect(start_item)
        timer.start(500) #500ms间隔
        # 信号 Canceled
        # bar.canceled.connect(timer.stop)
        

        pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
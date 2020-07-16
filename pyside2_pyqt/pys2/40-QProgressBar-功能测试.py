# 范围 当前值
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('进度条QProgressBar的学习')
        self.setup_ui()


    def setup_ui(self):
        bar=QProgressBar(self)
        bar.resize(200,30)
        # 默认范围
        print(bar.minimum(),bar.maximum()) # 0 100
        # 设定当前值
        bar.setValue(50)
        
        # 繁忙模式
        # 当你获取不到数值范围，就好像很忙，进度条就呈现繁忙模式：没有进度条的前进，只看到不断转动的表盘，也没有进度文本。
        # bar.setRange(0,0)

        # 安装案例
        bar1=QProgressBar(self)
        self.bar1=bar1
        bar1.resize(200,30)
        bar1.move(100,100)
        self.val=0
        bar1.setValue(self.val)
        bar1.setVisible(False)

        
        btn1=QPushButton(self)
        self.btn1=btn1
        btn1.setText('安装结束')
        btn1.adjustSize()
        btn1.move(150,150)
        btn1.setVisible(False)
        btn1.clicked.connect(lambda : self.close()) # 结束安装 关闭窗口

        btn=QPushButton(self)
        btn.setText('安装')
        btn.adjustSize()
        btn.move(50,50)
        btn.clicked.connect(self.progress) 

        

    def progress(self):
        # 安装进度条
        self.bar1.setVisible(True)
        
        # 点击按钮 安装
        # 用计时器模拟
        timer=QTimer(self)
        def start_install():
            val=self.bar1.value()
            # +1
            val+=1
            if val>=100:
                self.bar1.setValue(val)
                # 安装结束  
                self.btn1.setVisible(True)
                timer.stop()
                print('结束安装')          
            
            self.bar1.setValue(val)

        timer.timeout.connect(start_install)
        timer.start(100)
        # 安装完毕 显示安装完毕标签

        pass

if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
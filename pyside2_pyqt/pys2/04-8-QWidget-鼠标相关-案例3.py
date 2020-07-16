from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *
# 监听如下三件事，即可实现用户区移动鼠标，主窗口跟随移动
# 鼠标按下
# 鼠标移动
# 鼠标释放

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('窗口移动')
        self.move(600,300)
        self.setup_ui()
        self.move_flag=False #防止鼠标跟踪 造成崩溃
    
    def setup_ui(self):
        pass

    def mousePressEvent(self,evt): 
        # QMouseEvent
        # 判断鼠标按钮是左键 杜绝右键移动
        if evt.button()==Qt.LeftButton:
            # 捕获鼠标按下点的起始xy值 绝对坐标
            self.mouse_x=evt.globalX()
            self.mouse_y=evt.globalY()
            print('鼠标按下')
            # 鼠标按下时原点位置
            self.origin_x=self.x()
            self.origin_y=self.y()
            # 当按下时 设置移动标志 可以移动
            self.move_flag=True

    def mouseMoveEvent(self,evt):
        # 防止 鼠标跟踪 设置移动标志 self.move_flag
        if self.move_flag:
            # 移动的距离
            desc_x=evt.globalX()-self.mouse_x
            desc_y=evt.globalY()-self.mouse_y
            print(desc_x,desc_y)
            # 移动的具体尺寸
            self.move(self.origin_x+desc_x,self.origin_y+desc_y)
            print('鼠标移动...')

    def mouseReleaseEvent(self,evt):
        # 将标志还原 保证鼠标可以释放
        self.move_flag=False
        print('鼠标释放了')  

if __name__ == "__main__":
     
    app=QApplication([])

    # 用户区移动鼠标 主窗口跟随移动

    window=Window()
    # 设置鼠标跟踪
    window.setMouseTracking(True)
    # 因为设置了鼠标跟踪，mouseMoveEven事件会自动响应，就会造成程序崩溃；
    # 因此，设置移动标志位 move_flag 作为mouseMoveEven的开关。平时默认是关闭的；
    # 当点击时打开开关，释放时又关闭。这就保证了即使设置了鼠标跟踪，也不会导致程序崩溃。

    window.show()

    app.exec_()
from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *
app=QApplication([])

# 案例要求 标签跟随鼠标移动
# 鼠标跟踪
class MyWidget(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(500,500)
        self.setWindowTitle("标签跟随鼠标移动")
        self.lb=QLabel(self)
        self.lb.setText('跟随鼠标')
        self.lb.setStyleSheet('background-color:cyan')
        # 设置鼠标跟踪
        self.setMouseTracking(True)
        self.cursor_diy()

    # 自定义鼠标形状
    def cursor_diy(self):
        # 用图片自定义鼠标形状
        # 获取图片
        pixmap=QPixmap(r'pyside2_pyqt\pys2\xxx.png')
        # 调整图片大小 (宽，高)
        new_pixmap=pixmap.scaled(50,50)
        # 设定图片为鼠标形状 热点区域为图片尾部右下角
        cursor=QCursor(new_pixmap,50,50)
        # 设定当前鼠标形状为新定义的鼠标形状
        self.setCursor(cursor)

    # 定义鼠标移动具体函数
    def mouseMoveEvent(self,mv):
        self.lb.move(mv.x(),mv.y())#这是相对应用程序的坐标=localPos()
        print('鼠标移动',mv.x(),mv.y(),mv.localPos()) # 相对应用程序窗体的位置
        


wd=MyWidget()

wd.show()

app.exec_()
from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *
app=QApplication([])

# 鼠标跟踪
class MyWidget(QWidget):
    def __init__(self,parent=None):
        # 2.2 继承父类初始化
        super().__init__(parent) 
        #设定鼠标跟踪
        # self.setMouseTracking(True)
        # self.setWindowFlag(Qt.FramelessWindowHint)#无边框
    # 定义鼠标移动具体函数
    def mouseMoveEvent(self,mv):
        # QMouseEvent
        # mv 是QMouseEventt事件对象，可以获取鼠标的全局或局部位置
        # print('鼠标移动',mv.globalPos()) # 相对于桌面的位置
        print('鼠标移动',mv.localPos()) # 相对应用程序窗体的位置
        # 鼠标移动 PySide2.QtCore.QPoint(869, 577)
        # 鼠标移动 PySide2.QtCore.QPointF(10.000000, 14.000000)
        # return super().mouseMoveEvent(mv) #没有这个 就阻断了move信号的发送
        # 鼠标移动信号不像press和click有信号发射，必须要重写mouseMoveEvent方法。
    

window=MyWidget()
window.setWindowTitle('鼠标相关')
window.resize(500,500)
window.move(600,300)

# 3 鼠标跟踪
 
# 查看是否设置了鼠标跟踪
print(window.hasMouseTracking())
# 设定了鼠标跟踪，则不用按住鼠标移动，只要鼠标在窗体内移动，mouseMoveEvent移动事件就会响应
# 鼠标未跟踪，则要按住鼠标左或右键在窗体内移动，则mouseMoveEvent移动事件会响应。


# 1 设定鼠标形状 WaitCursor\BusyCursor\UpArrowCursor\PointingHandCursor

# 窗口拉伸鼠标形状
# 精确选择 Qt.CrossCursor 
# 水平分割 Qt.SplitHCursor 即左右拉伸
# 垂直分割 Qt.SplitVCursor 即上下拉伸
# 水平拉伸 Qt.SizeHorCursor
# 垂直拉伸 Qt.SizeVerCursor
# 左上右下拉伸 Qt.SizeFDiagCursor
# 右上左下拉伸 Qt.SizeBDiagCurso
# 移动光标  Qt.SizeAllCursor
# 默认是 Qt.ArrowCursor
# 常用鼠标形状 http://blog.sina.com.cn/s/blog_a6fb6cc90101fsoe.html

# window.setCursor(Qt.WaitCursor)

# 设定控件鼠标形状
lb=QLabel(window)
lb.setText('鼠标变禁止')
lb.resize(300,300)
lb.setStyleSheet('background-color:cyan')
lb.setContentsMargins(100,0,0,0)
lb.setCursor(Qt.ForbiddenCursor)
# lb.setCursor(Qt.CrossCursor)

# 用图片自定义鼠标形状
# 获取图片
pixmap=QPixmap(r'pyside2_pyqt\pys2\xxx.png')
# 调整图片大小 (宽，高)
new_pixmap=pixmap.scaled(50,50)
# 设定图片为鼠标形状 热点区域为图片尾部右下角
cursor=QCursor(new_pixmap,50,50)
# 设定当前鼠标形状为新定义的鼠标形状
window.setCursor(cursor)

# 2 设定鼠标起始位置
# window.cursor().setPos(700,400)
# 获取鼠标位置
# print(window.cursor().pos())

window.show()

app.exec_()
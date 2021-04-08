# QRubberBand 橡皮筋选中控件
    # 描述
    	# 提供一个矩形或线来指示选择或边界
    	# 一般结合鼠标事件一同协作
    # 继承
    	# QWidget
    # 功能作用
    	# 构造函数
    		# QRubberBand(QRubberBand.Shape, QWidget)
			# 形状
    			# QRubberBand.Line      线形
    			# QRubberBand.Rectangle	矩形
    	# 移动
    		# move(x, y)
    		# move(QPoint)
    	# 调整大小
    		# resize(width, height)
    		# resize(QSize)
    	# 统一设置
    		# setGeometry(int x, int y, int width, int height)
    		# setGeometry(QRect rect)
    	# 形状获取
    		# shape() -> QRubberBand.Shape
    # 信号
    	# 继承父类
    
    	
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('选中控件QRubberBand的学习')
        self.setup_ui()

    def setup_ui(self):
        rb = QRubberBand(QRubberBand.Rectangle, self)#(形状，父控件)
        # 
		# 统一定义 位置和大小
        rb.setGeometry(10, 10, 60, 60)
        print(rb.isVisible()) # False 默认看不见
        rb.show()
if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
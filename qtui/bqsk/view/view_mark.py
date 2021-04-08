from PySide2.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QGraphicsPixmapItem,QGraphicsView
from PySide2.QtCore import Slot,QEvent,Qt
from PySide2.QtGui import QKeySequence,QPixmap,QPicture,QImage,QPalette,QPainter,QPen,QColor,QPaintEngine
# from PySide2.QtWidgets import *
# from PySide2.QtCore import *
# from PySide2.QtGui import*

import os,sys

# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_mark import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
# from core.split_music import split_music

class MarkUi(QWidget,Ui_Form):
    
    def __init__(self,parent=None):
        # 3 继承父类初始化
        super().__init__(parent) 
        # 4 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)
        self.text_te.paintEvent=self.grv_paintEvent

     # 绘制事件 绘制内切圆
    def grv_paintEvent(self, evt):
        
        painter = QPainter(QPaintEngine())
        pen=QPen(QColor(100, 150, 200), 6)
        painter.setPen(pen)

        painter.drawEllipse(0, 0, 100, 100)

        return super().paintEvent(evt)

if __name__ == "__main__":
    app=QApplication([]) 
    wd=MarkUi()
    wd.show()
    app.exec_()
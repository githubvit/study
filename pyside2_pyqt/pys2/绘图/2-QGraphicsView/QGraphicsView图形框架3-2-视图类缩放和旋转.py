
'''
34.3-2 视图类 缩放 和 旋转
既然图元已经添加好，场景也已经设置好，那我们通常就可以调用视图的一些方法来对图元做一些变换，
比如放大、缩小和旋转等。
请看下方代码：
'''
import sys
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 500, 500)
        self.ellipse = self.scene.addEllipse(QRectF(200, 200, 50, 50), brush=QBrush(QColor(Qt.blue)))
        self.rect = self.scene.addRect(QRectF(300, 300, 50, 50), brush=QBrush(QColor(Qt.red)))
        self.ellipse.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.rect.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        self.setScene(self.scene)

        self.press_x = None

    # 1
    def wheelEvent(self, event):
        if event.angleDelta().y() < 0:
            self.scale(0.9, 0.9)
        else:
            self.scale(1.1, 1.1)
        # super().wheelEvent(event)

    # 2
    def mousePressEvent(self, event):
        self.press_x = event.x()
        # super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.x() > self.press_x:
            self.rotate(10)
        else:
            self.rotate(-10)
        # super().mouseMoveEvent(event)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
'''
1. 在鼠标滚轮事件中，调用scale()方法来来放大和缩小视图。
这里并没有必要调用父类的事件函数，因为我们不需要将事件传递给场景以及图元；

2. 重新实现鼠标按下和移动事件函数，首先获取鼠标按下时的坐标，然后判断鼠标是向左移动还是向右。
如果向右的话，则视图顺时针旋转10度，否则逆时针旋转10度。

放大和缩小

旋转

当然视图还提供了很多方法，比如同样可以用items()和itemAt()来获取图元，
也可以设置视图背景、视图图缓存模式和鼠标拖曳模式等等。大家可按需查阅(这里讲多了怕混乱(ー`´ー))。
'''
'''
34.1-3 QGraphicsItem分组
所谓分组也就是将各个图元进行分类，分到一起的图元就会共同行动(选中、移动以及复制等)。
我们通过下面的代码来演示下：
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsScene, \
                            QGraphicsView, QGraphicsItemGroup


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        # 1  实例化四个图元，两个为矩形，两个为椭圆，并调用setRect()方法设置坐标和大小；
        self.rect1 = QGraphicsRectItem()
        self.rect2 = QGraphicsRectItem()
        self.ellipse1 = QGraphicsEllipseItem()
        self.ellipse2 = QGraphicsEllipseItem()

        self.rect1.setRect(100, 30, 100, 30)
        self.rect2.setRect(100, 80, 100, 30)
        self.ellipse1.setRect(100, 140, 100, 20)
        self.ellipse2.setRect(100, 180, 100, 50)

        # 2 实例化两种画笔和两种画刷，用于 图元 的 样式设置；
        pen1 = QPen(Qt.SolidLine)
        pen1.setColor(Qt.blue)
        pen1.setWidth(3)
        pen2 = QPen(Qt.DashLine)
        pen2.setColor(Qt.red)
        pen2.setWidth(2)

        brush1 = QBrush(Qt.SolidPattern)
        brush1.setColor(Qt.blue)
        brush2 = QBrush(Qt.SolidPattern)
        brush2.setColor(Qt.red)

        self.rect1.setPen(pen1) # 设置 图元rect1 的边线 轮廓
        self.rect1.setBrush(brush1) # 设置  图元rect1 的内部 填充 
        self.rect2.setPen(pen2)
        self.rect2.setBrush(brush2)
        self.ellipse1.setPen(pen1)
        self.ellipse1.setBrush(brush1)
        self.ellipse2.setPen(pen2)
        self.ellipse2.setBrush(brush2)

        # 3 实例化两个QGraphicsGroup分组对象，将图元添加到分组。
        self.group1 = QGraphicsItemGroup()
        self.group2 = QGraphicsItemGroup()
        self.group1.addToGroup(self.rect1)
        self.group1.addToGroup(self.ellipse1)
        self.group2.addToGroup(self.rect2)
        self.group2.addToGroup(self.ellipse2)
        self.group1.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable) # 设定分组可移动可选中
        self.group2.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        print(self.group1.boundingRect())
        print(self.group2.boundingRect())

        # 4 将分组添加到场景当中。
        self.scene.addItem(self.group1)
        self.scene.addItem(self.group2)

        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


'''
1. 实例化四个图元，两个为矩形，两个为椭圆，并调用setRect()方法设置坐标和大小；

2. 实例化两种画笔和两种画刷，用于图元的样式设置；

3. 实例化两个QGraphicsGroup分组对象，并将矩形和椭圆都添加进来。rect1和ellipse1在group1里，而rect2和ellipse2在group2里。
接着调用setFlags()方法设置属性，让分组可以选中和移动。boundRect()方法放回一个QRectF值，该值可以显示出分组的边界位置和大小；

4. 将分组添加到场景当中。

蓝色的矩形和椭圆为一组，选中和移动组中的一个图元，就同时选中和移动组中的其他图元，效果就是整个组同时被选中和移动；红色的同理。
黑色边框即为边界，其位置和大小可用boundRect()方法来获取。
QGraphicsItemGroup分组的边界的位置和大小由其中的图元整体所决定。

---
'''
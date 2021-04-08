'''

34.2 QGraphicsScene场景类
在之前的小节中，我们要往场景中添加图元的话都是先把图元实例化好，再调用场景的addItem()方法进行添加。
不过场景其实还提供了以下方法让我们可以快速添加图元：

当然场景还提供了很多用于管理图元的方法。我们通过下面的代码来学习下：

'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        # 1
        self.rect = self.scene.addRect(100, 30, 100, 30)
        self.ellipse = self.scene.addEllipse(100, 80, 50, 40)
        self.pic = self.scene.addPixmap(QPixmap(r'D:\pyj\st\study\pyside2_pyqt\pys2\rose.png').scaled(60, 60))
        self.pic.setOffset(100, 130)

        self.rect.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.ellipse.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)

        self.setScene(self.scene)

        # 2
        print(self.scene.items())
        print(self.scene.items(order=Qt.AscendingOrder))
        print(self.scene.itemsBoundingRect())
        print(self.scene.itemAt(110, 40, QTransform()))

        # 3
        self.scene.focusItemChanged.connect(self.my_slot)

    def my_slot(self, new_item, old_item):
        print('new item: {}\nold item: {}'.format(new_item, old_item))

    # 4
    def mouseMoveEvent(self, event):
        print(self.scene.collidingItems(self.ellipse, Qt.IntersectsItemShape))
        super().mouseMoveEvent(event)

    # 5 还需要修改
    def mouseDoubleClickEvent(self, event):
        item = self.scene.itemAt(event.pos(), QTransform())
        self.scene.removeItem(item)
        super().mouseDoubleClickEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

'''

1. 直接调用场景的addRect(), addEllipse()和addPixmap()方法来添加图元。
这里需要大家了解一个知识点：
    先添加的图元处于后添加的图元下方(Z轴方向)，大家可以自己运行下代码然后移动下图元，
    之后就会发现该程序中图片图元处于最上方，椭圆其次，而矩形处于最下方。
    不过我们可以通过调用图元的setZValue()方法来改变上下位置(请查阅文档来了解，这里不详细解释)。

    接着设置图元的Flag属性。
    这里多出来的一个 ItemIsFocusable 表示让图元可以聚焦(默认是无法聚焦的)，
    该属性跟下面第3小点中要讲的 foucsItemChanged 信号有关；

2. 调用items()方法可以返回场景中的所有图元，返回值类型为列表。
返回的元素默认以降序方式(Qt.DescendingOrder)，也就是从上到下进行排列(QPixmapItem, QEllipseItem, QRectItem)。
可修改order参数的值，让列表中返回的元素按照升序方式排列。
 
 itemsBoundingRect()返回所有图元所构成的整体的边界。

 itemAt()可以返回指定位置上的图元，如果在这个位置上有两个重叠的图元的话，那就返回最上面的图元，
 传入的QTransform()跟图元的Flag属性ItemIgnoresTransformations有关，
 由于这里没有设置该属性我们直接传入QTransform()就行(这里不细讲，
 否则可能就会比较混乱了，大家可以先单纯记住，之后再深入研究)；

3. 场景有个focusChangedItem信号，当我们选中不同的图元时，该信号就会发出，前提是图元设置了ItemIsFocusable属性。
该信号可以传递两个值过来，第一个是新选中的图元，第二个是之前选中的图元；

4. 调用场景的collidingItems()可以打印出在指定碰撞触发条件下，所有和目标图元发生碰撞的其他图元；

5. 我们在图元上双击下，就可以调用removeItem()方法将其删除。注意这里其实直接给itemAt()传入event.pos()是不准确的，
因为event.pos()其实是鼠标在视图上的坐标而不是场景上的坐标。大家可以把窗口放大，然后再双击试下，
会发现图元并不会消失，这是因为视图大小跟场景大小不再一样，坐标也发生了改变。具体解决方案请看34.4小节。


控制台打印内容：
    [<PyQt5.QtWidgets.QGraphicsPixmapItem object at 0x00000175A5F3B048>, <PyQt5.QtWidgets.QGraphicsEllipseItem object at 0x00000175A5D27F78>, 
    <PyQt5.QtWidgets.QGraphicsRectItem object at 0x00000175A5D27EE8>]
    [<PyQt5.QtWidgets.QGraphicsRectItem object at 0x00000175A5D27EE8>, <PyQt5.QtWidgets.QGraphicsEllipseItem object at 0x00000175A5D27F78>, <PyQt5.QtWidgets.QGraphicsPixmapItem object at 0x00000175A5F3B048>]
    PyQt5.QtCore.QRectF(99.5, 29.5, 101.0, 91.0)
    <PyQt5.QtWidgets.QGraphicsRectItem object at 0x00000175A5D27EE8>


双击某个图元，将其删除：

​---
'''
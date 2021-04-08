'''
34.1-4 QGraphicsItem图元类 碰撞检测
碰撞检测在游戏中的用处非常大，
比如在飞机大战游戏中，如果子弹没有和敌机做碰撞检测处理的话，那敌机就不会被消灭，奖励也不会增加，游戏也就没有什么意思。

我们通过下面这个例子来带大家了解如何对图元进行碰撞检测：

    界面上有一个矩形图元和一个椭圆图元，两者都可以选中和移动。
    我们就对两者进行碰撞检测。在此之前我们先了解下boundingRect()边界和shape()形状的区别。
    请看下方的椭圆图元：
        当选中这个图元时，虚线部分显示的就是该图元的边界，而形状就指的是图元本身，也就是黑色实线部分。
        碰撞检测可以以边界为范围或者以形状为范围。
        假如我们在代码中以边界为范围，那椭圆的虚线跟矩形图元一碰到，就会触发碰撞检测， Qt.IntersectsItemBoundingRect 外框交互；
        如果以形状为范围，那只有在椭圆的黑色实线跟矩形碰到的情况下，碰撞检测才会触发，t.IntersectsItemShape 形状交互。


下面是几种具体的检测方式：

    常量                            值          触发条件

    Qt.ContainsItemShape            0x0         以形状为范围，当前图元被其他图元完全包含住

    Qt.IntersectsItemShape          0x1         以形状为范围，当前图元被完全包含或者与其他图元有交集

    Qt.ContainsItemBoundingRect     0x2         以边界为范围，当前图元被其他图元完全包含住

    Qt.IntersectsItemBoundingRect   0x3         以边界为范围，当前图元被完全包含或者与其他图元有交集

下面请看代码示例：

'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsScene, \
                            QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        self.rect = QGraphicsRectItem()
        self.ellipse = QGraphicsEllipseItem()
        self.rect.setRect(120, 30, 50, 30)
        self.ellipse.setRect(100, 180, 100, 50)
        self.rect.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.ellipse.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

        self.scene.addItem(self.rect)
        self.scene.addItem(self.ellipse)

        self.setScene(self.scene)

    def mouseMoveEvent(self, event):
        # 调用椭圆图元的collidesWithItem()方法来指定要与之进行碰撞检测的其他图元 self.rect以及检测方式 Qt.IntersectsItemBoundingRect 。
        if self.ellipse.collidesWithItem(self.rect, Qt.IntersectsItemBoundingRect):
            # 1 当椭圆外框虚线 与 矩形 碰撞 输出 [] 空列表
            # 2 当椭圆外形实线 与 矩形 碰撞 输出 [<PyQt5.QtWidgets.QGraphicsRectItem object at 0x00000233B3ABECA8>] 列表
            print(self.ellipse.collidingItems(Qt.IntersectsItemShape))# 与 椭圆发生shape外形碰撞的图元 是个列表
        super().mouseMoveEvent(event)

    # def mouseMoveEvent(self, event):
    #     if self.rect.collidesWithItem(self.ellipse, Qt.IntersectsItemBoundingRect):
    #         print(self.rect.collidingItems(Qt.IntersectsItemShape))
    #     super().mouseMoveEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

'''
初始化函数中的代码想必大家都懂了，这里就不再讲述，我们重点来看mouseMoveEvent()事件函数。

我们调用椭圆图元的collidesWithItem()方法来指定要与之进行碰撞检测的其他图元以及检测方式。
其他图元指的就是矩形图元，而且我们可以看到这里是以椭圆的边界为范围，而且只要两个图元有交集就会触发检测。
如果碰撞条件成立，那么collidesWithItem()就会返回一个True，那么此时if条件判断也就成立。

collidingItems()方法在指定检测方式后可以返回所有符合碰撞条件的其他图元，返回值类型为列表。
这里的检测方式是以形状为范围的，同样有交集即可。

那mouseMoveEvent()事件函数所要表达的意思就是：当椭圆的边界和矩形接触，那么if条件判断就成立，不过此时打印的还只是空列表，
因为椭圆本身(黑色实线)并还没有跟矩形有所接触。不过当接触了之后控制台就会输出包含矩形图元的列表了。


请大家调用矩形图元的collidesWithItem()和collidingItems()方法来尝试下，看看有什么不同。
也就是把mouseMoveEvent()事件函数修改如下：

    def mouseMoveEvent(self, event):
        if self.rect.collidesWithItem(self.ellipse, Qt.IntersectsItemBoundingRect):
            print(self.rect.collidingItems(Qt.IntersectsItemShape))
        super().mouseMoveEvent(event)


---
'''
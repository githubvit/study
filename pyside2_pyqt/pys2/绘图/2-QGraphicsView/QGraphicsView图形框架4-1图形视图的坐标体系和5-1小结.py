'''
34.4 图形视图的坐标体系
图形视图基于笛卡尔坐标系，视图，场景和图元都有各自的坐标。

视图坐标以左上角为原点，向右为x正轴，向下为y正轴(所有的鼠标事件最开始用的都是视图坐标)：


场景坐标以中心为原点，向右为x正轴，向下为y正轴(场景坐标描述的是最顶层图元的位置)：


图元坐标跟场景坐标一样(描述子图元的位置)：


图形视图提供了三种坐标系之间相互转换的函数，以及图元与图元之间的转换函数：


好，我们现在来讲解下34.2小节中的那个问题，代码如下：
'''
import sys
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        self.rect = self.scene.addRect(100, 30, 100, 30)
        self.ellipse = self.scene.addEllipse(100, 80, 50, 40)
        self.pic = self.scene.addPixmap(QPixmap(r'D:\pyj\st\study\pyside2_pyqt\pys2\rose.png').scaled(60, 60))
        self.pic.setOffset(100, 130)

        self.rect.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.ellipse.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        self.setScene(self.scene)

    # def mouseDoubleClickEvent(self, event):
        # item = self.scene.itemAt(event.pos(), QTransform())
        # self.scene.removeItem(item)
        # #报错 QGraphicsScene::removeItem: cannot remove 0-item
        # super().mouseDoubleClickEvent(event)
    # 在上面这个程序中，视图大小为600x600，而场景大小只有300x300。
    # 此时运行程序，我们双击的话是删除不了图元的，
    # 原因就是我们所获取的event.pos()是视图上的坐标，但是self.scene.itemAt()需要的是场景坐标。
    # 把视图坐标传给场景的itemAt()方法是获取不到任何图元的，所以我们应该要进行转换！
    # 把mouseDoubleClickEvent()事件函数修改如下即可：

    def mouseDoubleClickEvent(self, event):
        point = self.mapToScene(event.pos())
        item = self.scene.itemAt(point, QTransform())
        self.scene.removeItem(item)
        super().mouseDoubleClickEvent(event)
    # 调用视图的mapToScene()方法将视图坐标转换为场景坐标，这样图元就可以找到，也就自然而然可以删除掉了。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

'''
在上面这个程序中，视图大小为600x600，而场景大小只有300x300。
此时运行程序，我们双击的话是删除不了图元的，原因就是我们所获取的event.pos()是视图上的坐标，
但是self.scene.itemAt()需要的是场景坐标。
把视图坐标传给场景的itemAt()方法是获取不到任何图元的，所以我们应该要进行转换！

把mouseDoubleClickEvent()事件函数修改如下即可：

def mouseDoubleClickEvent(self, event):
    point = self.mapToScene(event.pos())
    item = self.scene.itemAt(point, QTransform())
    self.scene.removeItem(item)
    super().mouseDoubleClickEvent(event)
调用视图的mapToScene()方法将视图坐标转换为场景坐标，这样图元就可以找到，也就自然而然可以删除掉了。



​34.5 小结
1. 事件的传递顺序为视图->场景->图元，如果是在图元父子类之间传递的话，那传递顺序是从子类到父类；

2. 碰撞检测的范围分为边界和形状两种，需要明白两者的不同；

3. 要给QGraphicsItem加上信号和槽机制以及动画的话，就自定义一个继承于QGraphicsObject的类；

4. 往场景中添加QLabel, QLineEdit, QPushButton等控件，我们需要用到QGraphicsProxyWidget；

5. 视图，场景和图元都有自己的坐标系，注意使用坐标转换函数进行转换；

6. 图形视图框架知识点太多，笔者写本章的目的只是尽量带大家入门，个别地方可能会没有解释详细，请各位谅解。
关于更多细节，大家可以在Qt Assistant中搜索“Graphics View Framework”来进一步了解。

'''
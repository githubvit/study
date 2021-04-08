'''
34.1-2 事件传递顺序

QGraphicsItem还支持以下特性：

鼠标按下、移动、释放和双击事件，以及鼠标悬浮事件、滚轮事件和右键菜单事件
键盘输入事件
拖放事件
分组
碰撞检测
实现事件函数非常简单，这里就不细讲，我们重点要来了解下它在图形视图框架中的是如何传递的。请看下面的代码：
'''
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsScene, QGraphicsView


class CustomItem(QGraphicsRectItem):
    def __init__(self):
        super(CustomItem, self).__init__()
        self.setRect(100, 30, 100, 30)

    def mousePressEvent(self, event):
        print('event from QGraphicsItem')
        super().mousePressEvent(event)


class CustomScene(QGraphicsScene):
    def __init__(self):
        super(CustomScene, self).__init__()
        self.setSceneRect(0, 0, 300, 300)

    def mousePressEvent(self, event):
        print('event from QGraphicsScene')
        super().mousePressEvent(event)


class CustomView(QGraphicsView):
    def __init__(self):
        super(CustomView, self).__init__()
        self.resize(300, 300)

    def mousePressEvent(self, event):
        print('event from QGraphicsView')
        super().mousePressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = CustomView()
    scene = CustomScene()
    item = CustomItem()

    scene.addItem(item)
    view.setScene(scene)

    view.show()
    sys.exit(app.exec_())
'''
    图元，场景和视图其实都有各自的事件函数，我们在上面分别继承了QGraphicsRectItem,
  QGraphicsScene以及QGraphicsView,并重新实现了各自的mousePressEvent()事件函数，
  在其中我们都打印一句话来让用户知道是哪个函数被执行了。

    我们在矩形框内点击之后，发现控制台输入如下信息：
        event from QGraphicsView
        event from QGraphicsScene
        event from QGraphicsItem


    由此可见，事件的传递顺序为视图->场景->图元。

    有一点大家需要注意，重新实现事件函数的话我们必须要调用相应的父类事件函数，否则事件无法顺利传递下去。
    假如我把CustomView类中事件函数下的super().mousePressEvent(event)这行代码删除掉，
    那么控制台只会输出"event from QGraphicsView"：
'''


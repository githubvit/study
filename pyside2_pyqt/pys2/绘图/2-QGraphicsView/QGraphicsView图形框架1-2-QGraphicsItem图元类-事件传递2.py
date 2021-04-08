# 事件传递之父子图元
# 一个图元中可以添加另一个图元(一个图元可以是另一个图元的父类)，那此时图元之间的事件传递顺序又是如何的呢？请看下面代码：

import sys
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsScene, QGraphicsView


class CustomItem(QGraphicsRectItem):
    def __init__(self, num):
        super(CustomItem, self).__init__()
        self.setRect(100, 30, 100, 30)
        self.num = num

    def mousePressEvent(self, event):
        print('event from QGraphicsItem{}'.format(self.num))
        super().mousePressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene()
    item1 = CustomItem(1)
    item2 = CustomItem(2)
    item2.setParentItem(item1)

    scene.addItem(item1)
    view.setScene(scene)

    view.show()
    sys.exit(app.exec_())

# 因为实例化的是两个一样的矩形图源，为了进行区分，
# 我们在CustomItem的初始化函数中加入一个num参数，然后在事件函数中打印出实例化时所传入的数字即可。

# 调用setParentItem()方法将item1设置为item2的父类，然后将item1添加到场景中(item2自然也被加入)。

# 在矩形框中点击，控制台打印如下：
    # event from QGraphicsItem2
    # event from QGraphicsItem1

# 由此可见，事件是由子图元传递到父图元的。

# 同理，如果不加super().mousePressEvent(event)，那么事件就会停止传递，最后也就只会显示"event from QGraphicsItem2"。


# 请大家一定要搞清楚事件的传递顺序，这样才能更好地使用图形视图框架。
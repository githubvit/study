from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import *
# from PyQt5.QtPrintSupport import *

import os
import sys

'''
参考：
1 https://blog.csdn.net/LaoYuanPython/article/details/102527871
为了方便起见，可以使用 registerEventType()函数为应用程序注册和保留自定义事件类型。
这样做可以避免意外地重新使用应用程序中其他地方已在使用的自定义事件类型。

用户自定义 事件的值 必须在QEvent.User事件到QEvent.MaxUser事件之间，其中QEvent.User事件的常量值为1000，
QEvent.MaxUser事件的常量值为65535。

2 http://blog.sina.com.cn/s/blog_6483fa330102xp0y.html
创建自定义事件，要使用QCoreApplication的以下静态方法：

    sendEvent(QObject receiver, QEvent event) - 事件被QCoreApplication的notify()函数直接发送给receiver对象，
                                                返回值是事件处理函数的返回值。使用这个函数必须要在栈上创建对象；

    postEvent(QObject receiver, QEvent event) - 事件添加到事件对列是并立即返回，等待处理。 
                                                这种方法是线程安全的，因此它可以在多线程应用程序中用于在线程之间交换事件。
                                                另外，使用这个函数必须要在堆上创建对象。

    这两个函数中的 receiver参数为事件发往的 控件；event参数可为标准事件类的事件( 如QMouseEvent)对象，
    也可以是继承自QEvent的类 class对象。
    以下是发送MouseButtonPress事件给标签控件的代码：
        e = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress,
            QtCore.QPointF(5, 5), QtCore.Qt.LeftButton,
            QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)

        QtCore.QCoreApplication.sendEvent(self.label, e)

    要发送自定义事件，您必须创建一个QEvent的继承类，    
    并在类中使用registerEventType( )静态函数注册自定义事件，
    同时将事件标识符存储在类属性中。

        class MyEvent(QtCore.QEvent):
            idType = QtCore.QEvent.registerEventType()
            
            def init(self, data):
                QtCore.QEvent.init(self, MyEvent.idType)
                self.data = data

            def get_data(self):
                return self.data

    将MyEvent事件发送到标签控件的代码：
        QtCore.QCoreApplication.sendEvent(self.label, MyEvent(“512”))
    可以使用event(self，even)或customEvent(self，event)方法来处理自定义事件。例如：
        def customEvent(self, e):
            if e.type() == MyEvent.idType:
            self.setText(“Received data: {0}”.format(e.get_data()))

'''
# 自定义事件对象 继承自 QEvent
class MyEvent(QEvent):
    # 注册事件类型
    idType = QEvent.registerEventType()

    # 事件对象初始化
    def __init__(self, data):
        # QEvent.__init__(self, MyEvent.idType)
        super().__init__(MyEvent.idType) # 注意 必须有 事件类型 QEvent.Type 这个参数 
        self.data = data
        print("MyEvent.idType ", MyEvent.idType) # MyEvent.idType  65535

    # 事件对象 函数
    def get_data(self):
        return self.data


class MainWidget(QMainWindow):

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
    
        self.setWindowTitle("QMainWindow 例子")
        self.resize(400, 200)

        self.emit_btn = QPushButton("emit", self)

        self.emit_btn.clicked.connect(self.call_back_emit_btn)

        self.label = QLabel("Hello", self)

        self.label.setGeometry(50, 50, 200, 20)

        self.fire_btn = QPushButton("fire", self)

        self.fire_btn.clicked.connect(self.call_back_fire_btn)
        self.fire_btn.move(0, 100)

        # 实例化 自定义事件 对象
        # self.emit_event = MyEvent("xxs512")
        # self.fire_event = MyEvent("yyy215")
        dic={'a':1}
        lst=['aaa','bbb']
        self.emit_event = MyEvent(dic['a'])
        self.fire_event = MyEvent(lst)
        

    def call_back_emit_btn(self):
        pass
        # 激发自定义事件
        QCoreApplication.sendEvent(self, self.emit_event)

    def call_back_fire_btn(self):
        pass
        # 激发自定义事件
        QCoreApplication.sendEvent(self, self.fire_event)

    #  设置自定义事件 动作 要重写自定义事件customEvent  类似 事件过滤
    def customEvent(self, e):
        print("customEvent:", e.type()) # customEvent: 65535
        if e.type() == MyEvent.idType:
            self.label.setText(f"Received : {e.get_data()}")# 调用自定义事件 函数 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())

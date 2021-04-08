'''
34.2-2  添加控件
我们还可以向场景中添加QLabel, QLineEdit, QPushButton, QTableWidget等简单或者复杂的控件，
甚至可以直接添加一个主窗口。接下来通过完成以下界面来带大家进一步了解(就是第三章布局管理中的界面例子)：

代码如下：
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsWidget, QGraphicsGridLayout, \
                            QGraphicsLinearLayout, QLabel, QLineEdit, QPushButton


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(220, 110)
        # 1
        self.user_label = QLabel('Username:')
        self.pwd_label = QLabel('Password:')
        self.user_line = QLineEdit()
        self.pwd_line = QLineEdit()
        self.login_btn = QPushButton('Log in')
        self.signin_btn = QPushButton('Sign in')

        # 2
        self.scene = QGraphicsScene()
        self.user_label_proxy = self.scene.addWidget(self.user_label)
        self.pwd_label_proxy = self.scene.addWidget(self.pwd_label)
        self.user_line_proxy = self.scene.addWidget(self.user_line)
        self.pwd_line_proxy = self.scene.addWidget(self.pwd_line)
        self.login_btn_proxy = self.scene.addWidget(self.login_btn)
        self.signin_btn_proxy = self.scene.addWidget(self.signin_btn)
        print(type(self.user_label_proxy))  # <class 'PyQt5.QtWidgets.QGraphicsProxyWidget'>

        # 3
        self.g_layout = QGraphicsGridLayout()
        self.l_h_layout = QGraphicsLinearLayout()
        self.l_v_layout = QGraphicsLinearLayout(Qt.Vertical)
        self.g_layout.addItem(self.user_label_proxy, 0, 0, 1, 1)
        self.g_layout.addItem(self.user_line_proxy, 0, 1, 1, 1)
        self.g_layout.addItem(self.pwd_label_proxy, 1, 0, 1, 1)
        self.g_layout.addItem(self.pwd_line_proxy, 1, 1, 1, 1)
        self.l_h_layout.addItem(self.login_btn_proxy)
        self.l_h_layout.addItem(self.signin_btn_proxy)
        self.l_v_layout.addItem(self.g_layout)
        self.l_v_layout.addItem(self.l_h_layout)

        # 4
        self.widget = QGraphicsWidget()
        self.widget.setLayout(self.l_v_layout)

        # 5
        self.scene.addItem(self.widget)
        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

'''
1. 实例化需要的控件，因为父类不是QGraphicsView，所以不加self；

2. 实例化一个场景对象，然后调用addWidget()方法来添加控件。
addWidget()方法返回的值其实是一个QGraphicsProxyWidget代理对象，控件就是嵌入到该对象所提供的代理层中。
user_label_proxy跟user_label的状态保持一致，如果我们禁用或者隐藏了user_label_proxy，
那么相应的user_label也会被禁用或者隐藏掉，那我们就可以在场景中通过控制代理对象来操作控件(不过信号和槽还是要直接应用到控件上，代理对象不提供)。

3. 进行布局，注意这里用的是图形视图框架中的布局管理器：
    QGraphicsGridLayout网格布局和QGraphicsLinearLayout线形布局(水平和垂直布局结合)。
    不过用法其实差不多，只不过调用的方法是addItem()而不是addWidget()或者addLayout()了。
    线形布局默认是水平的，我们可以在实例化的时候传入Qt.Vertical来进行垂直布局(图形视图还有个锚布局QGraphicsAnchorLayout，这里不再讲解，
    相信大家文档也可以看的明白)；

4. 实例化一个QGraphicsWidget，这个跟QWidget类似，只不过是用在图形视图框架这边，
调用setLayout()方法来设置整体布局；

5. 将QGraphicsWidget对象添加到场景中，QGraphicsProxyWidget中嵌入的控件自然也就在场景上了，
最后将场景显示在视图中就可以了。
'''
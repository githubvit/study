
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *



# for i in QtWidgets.__dict__.items():
#     print(i)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject继承结构测试()
        # self.QObject对象名称和属性的操作()
        # self.QObject对象的父子关系操作()
        self.QObject信号的操作()
        # self.QObject对象类判定()
        # self.QObject对象删除()
        pass
        
    
    def QObject继承结构测试(self):
        # print(QObject.__subclasses__())
        print(QWidget.__subclasses__())
        # mros = QWidget.mro()
        # mro()查找继承类，会一直追溯到python的原始类object。
        # mros = QObject.mro()
        
        mros = QWidget.mro()
        # print(mros)
        for mro in mros:
            print(mro)

    def QObject对象名称和属性的操作(self):

        # ************名称和属性测试API***************开始
        obj = QObject()
        # 设定名称
        obj.setObjectName("notice")
        print(obj.objectName())
        # 设定属性
        obj.setProperty("notice_level", "error")
        obj.setProperty("notice_level2", "warning")
        # 获取属性值
        print(obj.property("notice_level"))
        # 查看属性名
        print(obj.dynamicPropertyNames())
        # **************名称和属性测试API**************结束

        # *************案例演示***************开始
        with open("pyside2_pyqt\pys2\QObject.css", "r") as f:
            # qApp.setStyleSheet(f.read())
            self.setStyleSheet(f.read())
        #     # vscode不识别.qss文件，报错：
        #         #   FileNotFoundError: [Errno 2] No such file or directory: 'QObject.qss'
        #     # 解决 使用 vscode 的相对路径或绝对路径即可，右击就可以复制绝对或相对路径

        label = QLabel(self)
        label.setObjectName("notice")
        label.setProperty("notice_level", "warning")
        label.setText("社会我顺哥")

        label2 = QLabel(self)
        label2.move(100, 100)
        label2.setObjectName("notice")
        label2.setProperty("notice_level", "error")
        label2.setText("人狠话不多")

        label3 = QLabel(self)
        label3.setText("xxxx")
        label3.move(150, 150)

        btn = QPushButton(self)
        btn.setObjectName("notice")
        btn.setText("btn")
        btn.move(50, 50)
        # 对于样式文件
        # /* 对象名称即id,qt中大量的重复名称显然不好，造成重复id，
        # 尽管qt没有限制名称重复，但习惯上还是要保持名称不能重复。
        # label label2 btn 都setObjectName("notice")
        # 显然这是个错误的示范， */

        label.setStyleSheet("font-size: 16px; color: red;")

        # *************案例演示***************结束

    def QObject对象的父子关系操作(self):
        # *************测试API***************开始
        # obj0 = QObject()
        # obj0 = QWidget()
        # obj1 = QObject()
        # obj2 = QObject()
        # obj3 = QObject()
        # obj4 = QObject()
        # obj5 = QObject()
        # print("obj0", obj0)
        # print("obj1", obj1)
        # print("obj2", obj2)
        # print("obj3", obj3)
        # print("obj4", obj4)
        # print("obj5", obj5)
        # # #
        # obj1.setParent(obj0)
        # obj2.setParent(obj0)
        # obj2.setObjectName("2")
        # label = QLabel()
        # label.setParent(obj0) # 可视化控件的父对象只能是QWidget类型 所以当obj0 = QObject()报错
        # # #
        # # #
        # obj3.setParent(obj1)
        # obj3.setObjectName("3")
        # # #
        # obj4.setParent(obj2)
        # obj5.setParent(obj2)
        # # #
        # print(obj1.parent())
        # # 获取直接子对象
        # print("获取直接子对象",obj0.children())
        # # 找一个 只能获取1个直接子对象
        # print("找一个 只能获取1个直接子对象",obj0.findChild(QObject))
        # # 查找子对象(类型，名称) 
        # print("查找子对象(类型，名称) ",obj0.findChild(QObject, "3")) # 类型 QObject, 名字 '3'
        # print("查找子对象(类型，名称) ",obj0.findChild(QObject, "1")) # 类型 QObject, 名字 '1' 找不到 返回 None
        # # print(obj0.findChild(QObject, "3", Qt.FindDirectChildrenOnly)) #不支持第三个参数查找方式，qt5可以
        
        # # 找多个 查找是QObject的子孙
        # print("看到所有的子孙",obj0.findChildren(QObject))
        # # 会看到所有的子孙包括label,因为QObject是所有控件的基类
       
        # print(obj0.findChildren(QWidget))
        # # 只能看到label，只有label是属于QWidget。
        
        # print(obj0.findChildren(QLabel))
        # 这就只能看到label了

        # *************测试API***************结束
        # *************内存管理机制***************开始
        # 当父对象被销毁时，这个QObject也会被销毁
        obj1 = QObject()
        self.obj1 = obj1#给obj1添加指针，即挂在某个对象上，这样就不会自动销毁，必须用del手动销毁
        obj2 = QObject()

        obj2.setParent(obj1)

        # 监听obj2对象被释放
        obj2.destroyed.connect(lambda : print("obj2对象被释放了"))

        del self.obj1
        # *************内存管理机制***************结束

    def QObject信号的操作(self):
        # destroyed 销毁和 objectNameChanged 改变对象名称两个信号
        self.obj = QObject()
        # # obj.destroyed
        # # obj.objectNameChanged
        # # def destroy_cao(obj):
        # #     print("对象被释放了", obj)
        # #
        # # self.obj.destroyed.connect(destroy_cao)
        # #
        # # del self.obj
        def obj_name_cao(name):
            print("对象名称发生了改变", name)
        #
        def obj_name_cao2(name):
            print("对象名称发生了改变2", name)
    
        #
        self.obj.objectNameChanged.connect(obj_name_cao)
        self.obj.objectNameChanged.connect(obj_name_cao2)
        # PySide2.QtCore.SignalInstance()
    
        # 返回连接到信号signal的槽slot的数量
        # print('slot数量',self.obj.receivers("objectNameChanged")) # 错误的示范X
        # print(self.obj.objectNameChanged) #<PySide2.QtCore.SignalInstance object at 0x0000023874A4F750>
        # print(type(self.obj.objectNameChanged))#<class 'PySide2.QtCore.SignalInstance'>
        # print('slot数量',self.obj.receivers(self.obj.objectNameChanged)) # pyqt5可以，pyside2报 TypeError 参数必须是receivers(bytes)
        
        
        self.obj.setObjectName("xxx")
        

        
        # 信号屏蔽
        # 1 屏蔽某个控件的某个信号 x控件.x信号.disconnect()
        # 2 屏蔽和释放某个控件的所有信号 
        #   屏蔽 控件.blockSignals(True)
        #   释放 控件.blockSignals(False)
        #   查看 控件.signalsBlocked()

        # 屏蔽  self.obj.setObjectName("ooo") 这次名称改变
        # self.obj.objectNameChanged.disconnect()
        # print(self.obj.signalsBlocked(), "1")
        self.obj.blockSignals(True)
        print(self.obj.signalsBlocked(), "2")
        self.obj.setObjectName("ooo")
       
        # 解除屏蔽
        # self.obj.blockSignals(False)
        # print(self.obj.signalsBlocked(), "3")
        #
        self.obj.setObjectName("xxoo")

        # *************信号与槽案例***************开始
        btn = QPushButton(self)
        btn.setText("点击我")
        def cao():
            print("点我嘎哈?")
        
        btn.clicked.connect(cao)


        # *************信号与槽案例***************结束
        pass

    def QObject对象类判定(self):
        # *************API***************开始
        # obj = QObject()
        # w = QWidget()
        # btn = QPushButton()
        # label = QLabel()
        # 
        # objs = [obj, w, btn, label]
        # for o in objs:
            # print(o.isWidgetType())
            # print(o.inherits("QWidget"))#对象是否是QWidget类
            # print(o.inherits("QPushButton"))#对象是否是QPushButton类
        # *************API***************结束

        # *************案例***************开始
        label1 = QLabel(self)
        label1.setText("社会我顺哥")
        label1.move(100, 100)

        label2 = QLabel(self)
        label2.setText("人狠话不多")
        label2.move(150, 150)

        # del label2
        # label2.deleteLater()
 
        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(200, 200)
 
 
 
        # for widget in self.findChildren(QLabel):
            # widget.setStyleSheet("background-color: cyan;")

        for widget in self.children():
            print(widget)
            # if widget.isWidgetType():
            if widget.inherits("QLabel"): #如果是QLabel类
                widget.setStyleSheet("background-color: cyan;")
        # *************案例***************结束

    def QObject对象删除(self):
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()
        
        obj3 = QObject()

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda : print("obj1被释放了"))
        obj2.destroyed.connect(lambda : print("obj2被释放了"))
        obj3.destroyed.connect(lambda : print("obj3被释放了"))

        # del obj2 
        # 由于python都是引用，所以，del语句作用在变量上，而不是数据对象上。
        # del删除的是变量，而不是数据
        # 所以当前删除的是 obj2临时变量和真正数据对象的引用
        # 该数据对象还被obj1引用着。而obj1还被self.obj1挂着，所以没有被删除
        # obj1.deleteLater()
        obj2.deleteLater()
        # deleteLater()会在 稍后 切除和obj1的关系，从而实现销毁obj2.
        print(obj1.children()) # 只能获取直接子对象
        print(obj1.findChildren(QObject)) # 获取符合 该类型要求 的所有子孙对象
        print(obj2)
        # 会先执行上面两行打印，再去销毁，真正的去释放相关的对象
        # 以后控件的删除都要使用deleteLater()，而不能使用del ,
        # 因为控件都被self即主控件引用着。只有使用deleteLater()才能切断和主控件之间的关系。



def QWidget控件的父子关系():
    # 1 父控件裁剪子控件
    # win1 = QWidget()
    # win1.setWindowTitle("红色")
    # win1.resize(500, 500)
    # win1.setStyleSheet("background-color: red;")
    # win1.show()
    
    # win2 = QWidget()
    # win2.setWindowTitle("绿色")
    # win2.setStyleSheet("background-color: green;")
    # win2.setParent(win1)
    # win2.resize(1000, 100)
    # win2.show()
    
    # 2 统一修改子控件背景 .findChildren(QLabel)
    win_root = QWidget()
    label1 = QLabel()
    label1.setText("label1")
    label1.setParent(win_root)
    label2 = QLabel()
    label2.move(50, 50)
    label2.setText("label2")
    label2.setParent(win_root)
    label3 = QLabel()
    label3.move(80, 80)
    label3.setText("label3")
    label3.setParent(win_root)
    btn = QPushButton(win_root)
    btn.move(100, 100)
    btn.setText("btn")
    win_root.show()
    # 统一修改子控件背景 .findChildren(QLabel)
    for sub_widget in win_root.findChildren(QLabel):
        print(sub_widget)
        sub_widget.setStyleSheet("background-color: cyan;")


# 不管怎么改标题，都加上前缀 撩课
def 信号与槽():
    window=QWidget()
    # 连接窗口标题变化的信号  与  槽
    def cao(title):
        # print("窗口标题变化了", title)
        # window.windowTitleChanged.disconnect()
        window.blockSignals(True) # 先禁掉title
        print('是否屏蔽信号',window.signalsBlocked())
        window.setWindowTitle("撩课-" + title) # 加前缀
        # window.blockSignals(True) # 后禁掉title  不行 必须加在前面 
        window.blockSignals(False) # 再打开
        # window.windowTitleChanged.connect(cao)
    window.windowTitleChanged.connect(cao)
    window.setWindowTitle("Hello Sz")
    window.setWindowTitle("Hello Sz2")
    # window.setWindowTitle("Hello Sz3")
    window.show()

if __name__ == "__main__":
    app=QApplication([])
    # QWidget控件的父子关系()
    # win_root = QWidget()
    # label1 = QLabel()
    # label1.setText("label1")
    # label1.setParent(win_root)
    # label2 = QLabel()
    # label2.move(50, 50)
    # label2.setText("label2")
    # label2.setParent(win_root)
    # label3 = QLabel()
    # label3.move(80, 80)
    # label3.setText("label3")
    # label3.setParent(win_root)
    # btn = QPushButton(win_root)
    # btn.move(100, 100)
    # btn.setText("btn")
    # win_root.show()
    # 统一修改子控件背景 .findChildren(QLabel)
    # for sub_widget in win_root.findChildren(QLabel):
        # print(sub_widget)
        # sub_widget.setStyleSheet("background-color: cyan;")
    # wd=Window()
    # wd.show()
    信号与槽()
    app.exec_()
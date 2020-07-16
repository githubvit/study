from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# from PyQt5.Qt import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('下拉菜单QComboBox的学习')
        self.setup_ui()

    def setup_ui(self):
        # 构造函数
        cb = QComboBox(self)
        self.cb=cb
        cb.resize(100,25)
        cb.move(100,50)
        # 添加条目项
			# addItem(str, userData: Any = None) (显示文本,数据)
			# addItem(QIcon, str, userData: Any = None) (图标,显示文本,数据)
			# addItems(Iterable[str])
        cb.addItems(["abc", "123", "456"]) #批量增加
        cb.addItem(QIcon(r"D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png"), "撩课", {"name": "itlike"}) # (图标,显示文本,数据)
        
        # 常用数据获取
        btn = QPushButton(self)
        self.btn=btn
        btn.move(cb.x()+cb.width()+20, 50)
        btn.setText("测试按钮")
        # btn.clicked.connect(lambda :print(cb.count()))#总条目
        # btn.clicked.connect(lambda :print(cb.currentIndex())) #获取当前条目索引
        # btn.clicked.connect(lambda :print(cb.currentText()))  #获取当前条目文本
        # btn.clicked.connect(lambda :print(cb.currentData()))  #获取当前条目数据
        # btn.clicked.connect(lambda : btn.setIcon(cb.itemIcon(cb.currentIndex()))) #获取当前索引图标，将获取的图标设置给按钮，当前没有图标不报错。
        
        # 获取最后一个条目的图标、文本、数据
        # 注意：按钮的clicked 会传递bool值参数，为了避免影响最后索引的获取，将其设为‘_’,关闭该参数的获取。
        # pyqt5适用，pyside2 报错 TypeError: <lambda>() missing 1 required positional argument: '_'
        # btn.clicked.connect(lambda _, idx = cb.count()-1:print(cb.itemIcon(idx), cb.itemText(idx), cb.itemData(idx)))

        # btn.clicked.connect(lambda:print(cb.itemIcon(cb.count()-1), cb.itemText(cb.count()-1), cb.itemData(cb.count()-1)))
        
        # def get_lastdata(val):
        #     print(val) #False
        #     idx = cb.count()-1
        #     print(cb.itemIcon(idx), cb.itemText(idx), cb.itemData(idx))

        # btn.clicked.connect(get_lastdata)
        
        # btn.clicked.connect(lambda :cb.addItem("it"))     #增加条目  代码可以重复增加 输入框不行
        # btn.clicked.connect(lambda :cb.clear())           #清空条目
        cb.setEditable(True)
        # btn.clicked.connect(lambda :cb.clearEditText())   #清空可编辑文本框 前提要设 可编辑 
        # btn.clicked.connect(lambda :cb.showPopup())       #弹出下拉菜单
        # btn.clicked.connect(lambda :cb.setCurrentIndex(2))  #设置当前索引

        # 数据限制
        # cb.setMaxCount(6)                 #设置最多条目数
        # cb.setEditable(True)              #设置文本框可编辑，回车后增加条目数
        # cb.setMaxVisibleItems(6)          #设置菜单可显示最多条目数，超出会显示滚动条
        # cb.setDuplicatesEnabled(True)     #设置可重复 默认不可以 用代码可以输入


        # 数据补全
        # cb.setCompleter(QCompleter(["abc", "123", "456"])) #完成器，下拉菜单的完成器要设置和下拉菜单一致


        # 信号
        # 选中条目变化
        cb.activated[str].connect(lambda val:print("条目被激活", val))
        # 
        # cb.currentIndexChanged[str].connect(lambda val:print("当前索引发生改变", val))
        # cb.currentTextChanged.connect(lambda val:print("当前文本发生改变", val))
        # cb.editTextChanged.connect(lambda val:print("当前编辑文本发生改变", val))
        # cb.highlighted[int].connect(lambda val:print("高亮发生改变", val))
        # cb.highlighted[str].connect(lambda val:print("高亮发生改变", val))



        # 常用操作：
        # cb.setFrame(False)            #取消框架
        # cb.setIconSize(QSize(60, 60))
        # cb.setSizeAdjustPolicy(QComboBox.AdjustToContents) #组合框尺寸策略设置为将始终根据内容进行调整



        # 增加条目
        # cb.addItem("xx1")
        # cb.addItem("xx2")
        # cb.addItem(QIcon("xxx.png"), "xx3")
        # cb.addItems(["1", "2", "3"])
        # cb.addItems(("1", "2", "3"))
        # cb.addItems("123")#会把字符串变成可迭代对象后，再增加条目，因此，是和上面的效果是一样的。
        # 插入条目
        # cb.insertItem(1, "xxx")
        # cb.insertItem(1, QIcon("xxx.png"), "xxx")
        # cb.insertItems(1, ("1", "a", "b"))
        # 设置图标 文本 覆盖方式
        # cb.setItemIcon(2, QIcon(r"pyside2_pyqt\pys2\xxx.png"))
        # cb.setItemText(2, "社会顺")
        # 移除条目
        # cb.removeItem(2)
        # 插入分割线
        # cb.insertSeparator(2)
        # 设置当前序号
        # cb.setCurrentIndex(1)
        # 设置当前文本 前提是 下拉框要设置为可编辑的 
        # cb.setCurrentText("社会顺") #结果是增加了一个条目
        # cb.setItemText(cb.currentIndex(),"社会顺")# 结果是改变了一个条目

        # 设置 mvc
        # 用不同的view来展示相应的数据model，达到自定义下拉选择框的目的。
        # 比如展示多级项目列表model,就可以用树形view。

        # cb.setEditable(True)          #设置可编辑
        # cb.setEditText("itlike")      #设置可编辑文本
        # cb.resize(300, 30)            
        # print(QAbstractItemModel.__subclasses__()) #查看子类
        # model = QStandardItemModel() #设置标准模型
        # 定义模型对象
        # item1 = QStandardItem("item1")    
        # item2 = QStandardItem("item2")    
        # item22 = QStandardItem("item22")  
        # 将22设为2的子模型
        # item2.appendRow(item22)
        # 给模型添加模型对象
        # model.appendRow(item1)
        # model.appendRow(item2)
        # cb.setModel(model)
        # 用树形视图 展示 该模型对象
        # cb.setView(QTreeView(cb))

        # pass

    def resizeEvent(self,evt):
        self.btn.move(self.cb.x()+self.cb.width()+20, 50)
        pass

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
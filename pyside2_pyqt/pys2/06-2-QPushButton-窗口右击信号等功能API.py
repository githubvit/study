from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
# from PyQt5.Qt import *
# 3 默认右击信号
class Window(QWidget):
    # 右击事件默认响应函数
    def contextMenuEvent(self,evt):
        print("默认上下文菜单调用这个方法")
        # 生成右击菜单
        self.right_hit_menu()
        # 展示右击菜单 绝对坐标
        self.menu.exec_(evt.globalPos())
    # 设置右击菜单
    def right_hit_menu(self):
        # 定义菜单
        menu=QMenu(self)
        self.menu=menu
        # QMenu()功能
        # 添加加子菜单    menu.addMenu()
            # 添加 最近打开 子菜单
        # 定义子菜单
        sub_menu=QMenu(menu)
        sub_menu.setIcon(QIcon(r'pyside2_pyqt\pys2\xxx.png'))
        sub_menu.setTitle('最近打开')#设置子菜单标题，这里就不是setText

        # 添加行为      menu.addAction()
            # 添加 新建 打开 退出 等行为
            # QAction() setText() setIcon()...
            # triggered 发射信号
        # 定义行为  
        # new_action=QAction(QIcon()
        # new_action.setText('新建')
        # new_action.setIcon(QIcon(r'pyside2_pyqt\pys2\xxx.png'))
        # 简化写法
        new_action=QAction(QIcon(r'pyside2_pyqt\pys2\xxx.png'),'新建',menu)
        # 接收 triggered 发射信号
        new_action.triggered.connect(lambda : print('新建'))
        
        open_action=QAction(QIcon(r'pyside2_pyqt\pys2\xxx.png'),'打开',menu)
        open_action.triggered.connect(lambda : print('打开'))
        exit_action=QAction('退出',menu)
        exit_action.triggered.connect(lambda : print('退出'))

        # 给sub_menu添加行为
        # 定义子菜单行为对象
        file1_action=QAction('XXXXX1.X',sub_menu)
        file1_action.triggered.connect(lambda : print('打开文件xxxx1.x'))

        file2_action=QAction('XXXXX2.X',sub_menu)
        file2_action.triggered.connect(lambda : print('打开文件xxxx2.x'))

        file3_action=QAction('XXXXX3.X',sub_menu)
        file3_action.triggered.connect(lambda : print('打开文件xxxx3.x'))
        # 把行为对象添加到子菜单
        sub_menu.addAction(file1_action)
        sub_menu.addAction(file2_action)
        sub_menu.addSeparator()#分割线
        sub_menu.addAction(file3_action)

        # 把定义的行为添加到菜单
        menu.addAction(new_action)
        menu.addAction(open_action)

        # 添加子菜单 sub_menu
        menu.addMenu(sub_menu)
        # 添加分割线    menu.addSeparator()
            # 在 打开和退出两个行为间 添加分割线
        menu.addSeparator()   
        menu.addAction(exit_action)
        

app=QApplication([])
wd=Window()
wd.resize(500,500)

# 1 按钮扁平化 即无边框阴影 背景
btn=QPushButton('扁平化',wd)
# btn 是否扁平
print(btn.isFlat())
# btn 设置扁平 
btn.setFlat(True)
# 设置扁平后，背景无效
btn.setStyleSheet('background-color:cyan')

# 2 默认处理
# 应用于QDialog这种 打开文件对话框上 的打开、取消等按钮，打开会设置为默认。
btn2=QPushButton('自动默认',wd)
btn2.move(50,50)
# btn2是自动默认吗
print(btn2.autoDefault()) #False
# btn2是默认吗
print(btn2.isDefault())  #False

# btn2设置为自动默认
# btn2.setAutoDefault(True)
# 这样设置完，打开不不是自动默认，要点击过后，才会变成自动默认，按钮周边有一圈光线。

# btn2设置为默认
btn2.setDefault(True)
# 打开即默认，按钮周边有一圈光线。

# 4 自定义右击信号 

# 自定义后 Window对象的默认事件函数不会响应 定义后会发射 customContextMenuRequested 信号
# 响应函数就变为该信号的槽函数
# 设置右击策略为 自定义上下文策略 
wd.setContextMenuPolicy(Qt.CustomContextMenu)
# 信号 槽函数 展示菜单
def show_menu(point):
    print('自定义上下文')
    # 建立菜单
    wd.right_hit_menu()
    # 展示菜单
    # 将坐标转换为绝对坐标
    globalPoint=wd.mapToGlobal(point)
    # # 展示菜单（绝对位置坐标）
    wd.menu.exec_(globalPoint)
# 绑定信号槽函数 
wd.customContextMenuRequested.connect(show_menu)


wd.show()
app.exec_()
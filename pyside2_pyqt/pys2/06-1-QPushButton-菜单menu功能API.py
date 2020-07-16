from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
# from PyQt5.Qt import *
app=QApplication([])
wd=QWidget()
wd.resize(500,500)

# 建立QPushButton按钮
# QPushButton(图标,文本,父控件)
btn=QPushButton(QIcon(r'pyside2_pyqt\pys2\xxx.png'),'按钮1',wd)

# QPushButton按钮设置菜单 setMenu(QMenu()) 
# 定义QMenu(btn)对象
menu=QMenu(btn)

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

# 将menu设置为btn的下拉菜单
btn.setMenu(menu)

wd.show()
# 菜单展示  要 放在主窗口展示后 
# btn.showMenu()# 等于 btn.click()
# btn模拟点击
# btn.click()
app.exec_()
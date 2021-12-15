# 工具栏按钮

# 提供了一个快速访问按钮
# 通常是在工具栏内部使用
# 工具按钮通常不显示文本标签，而是显示图标

# 继承自QAbstractButton

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# from PyQt5.Qt import *

app=QApplication([])
wd=QMainWindow()
wd.setWindowTitle("QToolButton使用")
wd.resize(500,500)

# 1 创建按钮
tb=QToolButton(wd)
tb.setText("工具")
tb.setIcon(QIcon(r'pyside2_pyqt\pys2\xxx.png'))
tb.setIconSize(QSize(60,60))#会影响箭头
tb.adjustSize()
# 设置工具按钮样式风格
# tb.setToolButtonStyle(Qt.ToolButtonTextOnly)
    # Qt.ToolButtonIconOnly #默认
    	# 仅显示图标
    # Qt.ToolButtonTextOnly
    	# 仅显示文字
    # Qt.ToolButtonTextBesideIcon
    	# 文本显示在图标旁边
    # Qt.ToolButtonTextUnderIcon
    	# 文本显示在图标下方
    # Qt.ToolButtonFollowStyle
    	# 遵循风格
  
# 设置文本显示在图标下方
# tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
# tb.adjustSize()
# 设置提示
tb.setToolTip('这是一个新建按钮')

# 2 箭头
# 设置了箭头后图标就无效了。箭头优先级高于图标
# setArrowType(Qt.ArrowType)
    # Qt.ArrowType
    	# Qt.NoArrow
    		# 无箭头
    	# Qt.UpArrow
    		# 向上箭头
    	# Qt.DownArrow
    		# 向下箭头
    	# Qt.LeftArrow
    		# 向左箭头
    	# Qt.RightArrow
    		# 向右箭头
# tb.setArrowType(Qt.NoArrow) 
# tb.setArrowType(Qt.RightArrow) 
# tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) #文字在图标的右边
# tb.adjustSize()

# 3 自动提升 就是QToolButton扁平化 setAutoRaise(bool) 
tb.setAutoRaise(True) #和背景融为一体。

# 4 菜单设置
# 工具按钮，按住不松，弹出菜单
# 定义菜单
menu=QMenu(tb)
sub_menu=QMenu('菜单1',menu)
# sub_menu.setTitle('菜单1')
# sub_menu.setIcon(QIcon(r'pyside2_pyqt\pys2\QObject.css'))
action1=QAction('行为1',menu)
action2=QAction('行为2',menu)
# 给action1设定数据
# 定义数据
data1={'a':1,'b':[2,3,4],'c':'中文'}
# 设定数据
action1.setData(data1)
# 给action2设定数据
# 定义数据
data2={'d':True,'e':[2,3,4],'f':'pyside2_pyqt\pys2\QObject.css'}
# 设定数据
action1.setData(data1)
action1.triggered.connect(lambda:print('行为1的triggered响应'))
action2.setData(data2)
menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action1)
menu.addAction(action2)
# 添加菜单
tb.setMenu(menu)
# 取消 tb.setMenu(menu)设置后 下拉菜单的角标 menu-indicator
# tb.setStyleSheet("QToolButton::menu-indicator{image:none;}")

# 5 设置菜单弹出模式
# 不设置默认是按住一会才弹出
# setPopupMode(QToolButton.ToolButtonPopupMode)
    # QToolButton.DelayedPopup #默认
    	# 鼠标按住一会才显示
        # 鼠标按住一会 会阻断tb的clicked信号
    # QToolButton.MenuButtonPopup
    	# 有一个专门的指示箭头
    	# 点击箭头才显示 无延迟
        # 点击箭头 tb的cliked信号无效 非箭头部分按钮tb的clicked有效
    # QToolButton.InstantPopup
    	# 点了按钮就显示 无延迟 
        # tb的cliked信号无效

# tb.setPopupMode(QToolButton.InstantPopup)
tb.setPopupMode(QToolButton.MenuButtonPopup)
tb.clicked.connect(lambda : print('点击有效'))

# 6 信号
# triggered(QAction *action)
	# 当点击某个action时触发, 并会将action传递出来
	# 小技巧
		# QAction对象可以通过
			# setData(Any)
				# 绑定数据
			# data()
				# 获取数据
# QToolButton的triggered与QAction还是不同的，QAction的triggered是连在每个action对象上。
# QToolButton这个triggered是绑定在菜单的父控件tb上，等于绑定了所有菜单子控件中action的triggered
# QToolButton这个triggered还可以获取具体是哪个action，以及获取该action上的数据。

tb.triggered.connect(lambda action: print('响应的行为',action.data()))

wd.show()
app.exec_()
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

app=QApplication([])

wd=QWidget()
wd.setWindowTitle('按钮组QButtonGroup')
wd.resize(500,500)

# 2 按钮组 
# 是抽象的按钮容器，并不可见，继承自QObject不是QWidget.
# 2.1 创建按钮组
y_ngrp=QButtonGroup(wd)
m_fgrp=QButtonGroup(wd)

# 2.2 创建按钮
yes_btn=QRadioButton('&yes',wd)#设置快捷键 alt+y
# yes_btn.setText('&yes')
yes_btn.move(50,50)
no_btn=QRadioButton('&no',wd)#设置快捷键 alt+n
# no_btn.setText('&no')
no_btn.move(100,50)

y_btn=QRadioButton('是',wd)
y_btn.move(50,100)

n_btn=QRadioButton('否',wd)
n_btn.move(100,100)

m_btn=QRadioButton('男-&Male',wd)#设置快捷键 alt+m
m_btn.move(50,200)
f_btn=QRadioButton('女-&Female',wd)#设置快捷键 alt+f
f_btn.move(50,250)

# 2.3 操作按钮组

# 2.3.1 给按钮组添加按钮 

# y_ngrp.addButton(yes_btn)
# y_ngrp.addButton(no_btn)
# y_ngrp.addButton(y_btn)
# y_ngrp.addButton(n_btn)
# 给按钮组添加按钮 并设置id
y_ngrp.addButton(yes_btn,1)
y_ngrp.addButton(no_btn,2)
y_ngrp.addButton(y_btn,3)
y_ngrp.addButton(n_btn,4)


m_fgrp.addButton(m_btn)
m_fgrp.addButton(f_btn)


# 2.3.2 为y_ngrp组，设置排他性为False
# y_ngrp.setExclusive(False)

# 2.3.3 为y_ngrp组，删除按钮, 就是把该按钮踢出群了，是移除关系，不是把按钮真的删除了。
y_ngrp.removeButton(no_btn)

# 2.3.4 获取该组中的按钮
print(y_ngrp.buttons()) 

# 2.3.5 y_ngrp按钮组ID操作
# id不唯一
# 按钮组默认会给每个按钮分配id，按-1、-2、-3....
# 为区分，我们自己设定id一般用正号，即1、2、3....

# (1)为y_ngrp按钮组中的按钮设置ID
y_ngrp.setId(y_btn,4)  #后面设置的id会覆盖之前设置的id 

# (2)获取按钮组中某按钮的id 
print(y_ngrp.id(y_btn)) #4
print(y_ngrp.id(n_btn)) #4 id可以重 

# (3)获取按钮组中某id的按钮
print(y_ngrp.button(4)) # 如果有重复,只获取定义按钮靠前的一个。没有，返回None

# (4)查看该组中选中按钮的id
yes_btn.setChecked(True)
print(y_ngrp.checkedId())

# 2.3.6 按钮组信号
    # buttonClicked(int/QAbstractButton)
    	# 当按钮组中的按钮被点击时, 发射此信号，信号类型可以是int即发射id，也可以是按钮对象，可以选择发射类型。
    # buttonPressed(int/QAbstractButton)
    	# 当按钮组中的按钮被按下时, 发射此信号
    # buttonReleased(int/QAbstractButton)
    	# 当按钮组中的按钮被释放时, 发射此信号
    # buttonToggled(QAbstractButton, bool)
    	# 当按钮组中的按钮被切换状态时, 发射此信号

# 获取id案例
def cao(val):
    if isinstance(val,int):#如果传过来的是id，就直接打印，
        print(val)
    else:                  #否则传过来的是按钮对象，就用 按钮组.id(按钮对象) 获取id
        print(y_ngrp.id(val))#对于buttonToggled信号，每次有两行值 一行是 选中 的是谁，还有一行是 取消选中 的是谁
y_ngrp.buttonToggled.connect(cao)
# 对于可以发射不同类型的信号，用[]进行信号类型选择
# y_ngrp.buttonClicked[int].connect(cao)

wd.show()
app.exec_()
# 系统托盘图标设置
from PySide2.QtWidgets import QApplication,QWidget,QSystemTrayIcon
from PySide2.QtGui import QIcon


app=QApplication([])
# 设置这个窗口 是为了 初始学习时该内容 关闭用，让系统图标可以随着app的关闭 退出
wd=QWidget()
wd.resize(200,300)

# 1 设置系统图标对象
sicon=QSystemTrayIcon()

# 2 给系统图标对象添加图标
sicon.setIcon(QIcon(r'D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png'))

# 3 显示系统图标
# 一定要有这个 不然看不到
sicon.show()

# slot
def clickedIcon(reason):
    # print(reason)
    
    # PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.Context 1 右键
    # PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick 2 左键双击
    # PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.Trigger 3 左键
    # PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.MiddleClick  4 中键
    if reason==1:
        print('单击右键')
    elif reason==2:
        print('双击左键')
    elif reason==3:
        print('单击左键')
    elif reason==4:
        print('单击中键')
    else:
        print('不知道')

# 4 信号
sicon.activated.connect(clickedIcon)  # 点击信号
    
wd.show()
app.exec_()
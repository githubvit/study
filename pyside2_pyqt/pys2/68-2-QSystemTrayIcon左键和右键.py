# 系统托盘图标左键界面和右键菜单
from PySide2.QtWidgets import *
from PySide2.QtGui import *




class SIcon(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        # 信号与槽
        self.activated.connect(self.clickedIcon)  # 点击信号
        # 挂载右键菜单
        self.r_menu()

    # 槽函数
    def clickedIcon(self,reason):
        # print(type(reason))
        
        # PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.Context 1 右键
        # PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick 2 左键双击
        # PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.Trigger 3 左键
        # PySide2.QtWidgets.QSystemTrayIcon.ActivationReason.MiddleClick  4 中键
        if reason==1:
            print('单击右键')
            # 显示菜单
            self.contextMenu()
        elif reason==2:
            print('双击左键')
        elif reason==3:
            print('单击左键')
            # 打开主界面
        elif reason==4:
            print('单击中键')
        else:
            print('不知道')

    # 右键菜单
    def r_menu(self):
        menu=QMenu()

        # make_key=QAction('制作密钥',self)

        exit=QAction('退出(&x)',self,triggered=self.app_exit)      #这样写 快捷键x 才有用
        
        # exit.setShortcut(QKeySequence('x'))    #这里设置快捷键 只是用来显示而已 不起作用
        # exit.triggered.connect(self.app_exit)

        menu.addAction('制作密钥')
        menu.addAction('加密')
        menu.addAction('解密')

        # 添加分割线 
        menu.addSeparator()  

        menu.addAction(exit)
        
        self.setContextMenu(menu)        

    # 退出函数 直接调用实例化的QApplication对象 app 的退出函数quit  
    # 必须和实例名保持一致；这就导致程序对象必须命名为 app
    def app_exit(self):
        # self.hide() #关闭图标 实际上没有也可以 程序退出即可
        app.quit()  #退出程序
        print('退出了。。。')
       
if __name__ == "__main__":

    app=QApplication([])

    # 1 设置系统图标对象
    sicon=SIcon()
    # 2 给系统图标对象添加图标
    sicon.setIcon(QIcon(r'D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png'))
    # 3 显示系统图标
    # 一定要有这个 不然看不到
    # sicon.clickedIcon.connect(lambda v: print(v))
    sicon.show()
    

    app.exec_()
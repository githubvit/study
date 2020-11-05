# 加密解密 系统图标
from PySide2.QtWidgets import QApplication,QSystemTrayIcon,QMenu,QAction
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal

import os,sys



# 一 取得项目根目录加入系统目录
BASE_DIR=os.path.dirname(__file__)
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入加解密主程序
import m_encrypter


class SIcon(QSystemTrayIcon):
    # 信号
    main_ui_signal=Signal() # 左键 打开主界面 信号
    m_k_signal=Signal()     # 右键 制作密钥 信号
    encrypt_signal=Signal() # 右键 加密 信号
    decrypt_signal=Signal() # 右键 解密 信号
    exit_signal=Signal()    # 右键 退出 信号

    def __init__(self):
        super().__init__()

        # 1 挂载图标
        self.setIcon(QIcon(r'D:\pyj\st\study\pyside2_pyqt\pys2\mmx\resource\img\safe2-removebg-preview.png'))

        # 2 信号与槽
        self.activated.connect(self.clickedIcon)  # 点击信号
        
        # 3 挂载右键菜单
        self.r_menu()


    # 槽函数
    def clickedIcon(self,reason):
        
        if reason==1:
            print('单击右键')
            # 显示 系统 右键菜单
            self.contextMenu()
        elif reason==2:
            print('双击左键')
        elif reason==3:
            print('单击左键')
            # 发射 打开主界面 信号
            self.main_ui_signal.emit()
        elif reason==4:
            print('单击中键')
        else:
            print('不知道')

    # 右键菜单
    def r_menu(self):
        # 新建菜单对象
        menu=QMenu()

        # 新建行为对象 1 打开目录
        open_key_dir=QAction('打开密钥目录',self,triggered=self.open_key_dir_fc)
        open_encrypt_dir=QAction('打开加密文件目录',self,triggered=self.open_encrypt_dir_fc)
        open_decrypt_dir=QAction('打开解密文件目录',self,triggered=self.open_decrypt_dir_fc)


        # 新建行为对象 2 发射信号
        make_key=QAction('制作密钥',self,triggered=self.m_k_signal.emit)
        encrypt_file=QAction('加密',self,triggered=self.encrypt_signal.emit)
        decrypt_file=QAction('解密',self,triggered=self.decrypt_signal.emit)
        exit_action=QAction('退出(&x)',self,triggered=self.exit_emit)      #这样写 快捷键x 才有用 
        
         

        # 为菜单添加行为
        menu.addAction(open_key_dir)
        menu.addAction(open_encrypt_dir)
        menu.addAction(open_decrypt_dir)
        
        # 添加分割线 
        menu.addSeparator()  

        menu.addAction(make_key)
        menu.addAction(encrypt_file)
        menu.addAction(decrypt_file)

        # 添加分割线 
        menu.addSeparator()  

        menu.addAction(exit_action)
        
        # 给 系统图标 设置 右键菜单( 放入新建的菜单对象 )
        self.setContextMenu(menu)    


    #解决打包设定没有console时，程序退出时弹出报错Failed to execute script encrypter_icon,可以关闭，没有影响，不好看。
    def exit_emit(self):
        self.hide()
        self.exit_signal.emit()
        self.setParent(None)

    # 制作密钥
    def m_key(self):
        # 1 输入制作密钥的名字 作为保存 
        pass

    # 退出函数 直接调用实例化的QApplication对象 app 的退出函数quit  
    # 必须和实例名保持一致；这就导致程序对象必须命名为 app
    def app_exit(self):
        # self.hide() #关闭图标 实际上没有也可以 程序退出即可
        app.quit()  #退出程序
        print('退出了。。。')


    def open_key_dir_fc(self):
        key_dir=m_encrypter.smt_key_dir()
        print(f'右键打开密钥目录{key_dir}')
        os.startfile(key_dir)

    def open_encrypt_dir_fc(self):
        encrypt_dir=m_encrypter.smt_encrypt_dir()
        print(f'右键打开加密文件目录{encrypt_dir}')
        os.startfile(encrypt_dir)

    def open_decrypt_dir_fc(self):
        decrypt_dir=m_encrypter.smt_decrypt_dir()
        print(f'右键打开解密文件目录{decrypt_dir}')
        os.startfile(decrypt_dir)
       
if __name__ == "__main__":

    app=QApplication([])

    # 1 设置系统图标对象
    sicon=SIcon()
    

    # 3 显示系统图标
    # 一定要有这个 不然看不到
    
    sicon.show()
    
    # 4 信号监测
    sicon.main_ui_signal.connect(lambda : print('打开主界面信号'))
    sicon.m_k_signal.connect(lambda : print('制作密钥信号'))
    sicon.encrypt_signal.connect(lambda : print('加密信号'))
    sicon.decrypt_signal.connect(lambda : print('解密信号'))
    sicon.exit_signal.connect(lambda : print('退出信号'))

    app.exec_()
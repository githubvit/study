from PySide2.QtWidgets import QApplication
import sys,os

#找到项目根目录
BASE_DIR=os.path.dirname(__file__) # 取得父目录，即项目根目录
# 找到view目录
view_path=r'%s\view'%BASE_DIR 
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)
# 把view目录导入sys
sys.path.append(view_path)

# from PyQt5.Qt import QApplication
# 入口文件
# 引入view
from view_login import LoginUi
from view_register import RegisterUi
from view_calculate import CalculateUi

if __name__ == "__main__":    
    app=QApplication([])
    # 主界面 1
    login_pane=LoginUi()
    # 子界面 1
    register_pane=RegisterUi(login_pane)
    # register_pane.move(0,0)
    register_pane.hide() #初始隐藏

    # 主界面 2
    calculate_pane=CalculateUi()
    
    calculate_pane.hide()

    
    # 槽函数

    # 打开注册窗口
    def go_register():
        register_pane.show()
        
       
    # 关闭注册窗口
    def exit_register():
        register_pane.hide()
        
    # 登录验证
    def check_login(u,p):
        if u=='123' and p=='456':
            print('登录成功')
            # 关闭登录界面
            login_pane.hide()
            # 显示计算器界面  
            # calculate_pane.move(login_pane.x(),login_pane.y())  
            calculate_pane.show()
            # 
        else:
            # 调用 内部的登录错误动画api
            login_pane.error_login_animation()

    # 信号
    # 打开和退出注册窗口 
    login_pane.go_register_signal.connect(go_register)
    register_pane.exit_signal.connect(exit_register)
    # 测试注册窗口和登录窗口用户名和密码信号
    register_pane.register_signal.connect(lambda n,p: print('注册窗口的用户名和密码',n,p))
    # login_pane.login_signal.connect(lambda u,p: print('--登录窗口的用户名--密码',u,'--',p))
    # 登录验证
    login_pane.login_signal.connect(check_login)


    
    login_pane.show()
    app.exec_()
from PySide2.QtWidgets import QApplication,QWidget,QMessageBox,QFrame
from PySide2.QtCore import Signal,Slot,Qt,QSequentialAnimationGroup,QPropertyAnimation,QAbstractAnimation

# from PyQt5.Qt import *

# 1 调入从 Designer 设计师 转成的py文件中的  界面类

# from Ui_main import Ui_Form
from Ui_register import Ui_Form

# 2 class 多继承 

class RegisterUi(QWidget,Ui_Form):
    # 自定义信号
    # exit_signal=pyqtSignal() #点击退出按钮信号
    # register_signal=pyqtSignal(str,str) #点击注册按钮信号 传递用户名和密码
    exit_signal=Signal() #点击退出按钮信号
    register_signal=Signal(str,str) #点击注册按钮信号 传递用户名和密码
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs) # 这里必须有parent，不能是parent=None，否则闪退。
        # 解决背景图片没有了的问题
        self.setAttribute(Qt.WA_StyledBackground,True)  
        # # 打包时，该问题有出现了 改为继承自QFrame
        # 依然出现问题
        # 3 导入界面类setupUi函数，填入self参数作为父类。
        self.setupUi(self)
        
        
        # 手动在设置一遍背景，因为打包后，背景透明
        # 
        #动画位置初始值
        self.target=[self.about_btn,self.reset_btn,self.exit_btn]
        self.target_pos=[target.pos() for target in self.target]
        

    # 4 用slot装饰器添加槽函数 on_控件名称(id)_信号
    # @pyqtSlot() #pyqt5 的装饰器
    @Slot()
    def on_about_btn_clicked(self):
        # print('关于')
        # 弹出对话框
        QMessageBox.about(self,'标题','文本 http://www.baidu.com')

    # @pyqtSlot()
    @Slot()
    def on_reset_btn_clicked(self):
        # print('重置')
        self.name_le.clear()
        self.pwd_le.clear()
        self.cfm_le.clear()

    # @pyqtSlot()
    @Slot()
    def on_exit_btn_clicked(self):
        # print('退出')
        # 发射退出信号
        self.exit_signal.emit()
    
    # @pyqtSlot(bool)
    @Slot(bool)
    def on_Menu_btn_clicked(self,val):
        # print('菜单',val)
        
        # 定义动画组
        animation_group=QSequentialAnimationGroup(self)
        # 定义动画对象
        for idx,target in enumerate(self.target):
            animation=QPropertyAnimation(target,b'pos',self)
            # 设置值
            animation.setStartValue(self.Menu_btn.pos())
            animation.setEndValue(self.target_pos[idx])
        
            # 设置时长
            animation.setDuration(500)
            # 设置动画曲线
            # animation.setEasingCurve(QEasingCurve.OutBounce)
       
            # 加入动画组
            animation_group.addAnimation(animation)
            
        
        # 制作 菜单 收拢和展开动画 
        # 当val=True  收拢
        if val:
            animation_group.setDirection(QAbstractAnimation.Backward)
        else:
            animation_group.setDirection(QAbstractAnimation.Forward)

        # 开始 不保留动画
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)
    
    # @pyqtSlot() 
    @Slot()
    def on_register_btn_clicked(self):
        # print('注册')
        # 发射注册信号
        self.register_signal.emit(self.name_le.text(),self.pwd_le.text())

    # 注册按钮的可用与否
    def register_btn_enable(self):
        # 获取输入框文本
        name=self.name_le.text().strip()
        pwd=self.pwd_le.text().strip()
        cfm=self.cfm_le.text().strip()
        # 比较
        if len(name)>0 and len(pwd)>0 and len(cfm)>0 and pwd==cfm:
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)
    # @pyqtSlot(str)
    @Slot(str)
    def on_name_le_textChanged(self,text):
        # print(text)
        self.register_btn_enable()
    
    # @pyqtSlot(str)
    @Slot(str)
    def on_pwd_le_textChanged(self,text):
        # print(text)
        self.register_btn_enable()
    
    # @pyqtSlot(str)
    @Slot(str)
    def on_cfm_le_textChanged(self,text):
        # print(text)
        self.register_btn_enable()
    

if __name__ == "__main__":
    app=QApplication([])
    wd=RegisterUi()
    # 监测自定义信号
    wd.exit_signal.connect(lambda : print('激发exit_signal'))
    wd.register_signal.connect(lambda u,p: print('激发了register_signal',u,p))
    wd.show()
    app.exec_()
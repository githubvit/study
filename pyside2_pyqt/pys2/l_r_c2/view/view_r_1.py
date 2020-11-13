from PySide2.QtWidgets import QApplication,QWidget,QMessageBox,QFrame
from PySide2.QtCore import Signal,Slot,Qt,QSequentialAnimationGroup,QParallelAnimationGroup,QPropertyAnimation,QAbstractAnimation,QEasingCurve
import os,sys
# from PyQt5.Qt import *


# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)
# 把资源管理文件qrc转换的py资源文件也放在根目录下，因为ui转换的py界面文件，导入py资源文件，都是直接导入 import .._rc 。

# 二 基本操作 
#  基本操作完成就可以打开界面了
# （固定步骤：1 导入界面多继承 2 继承父类初始化  3 self.setupUi(self)）

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
# from resource.ui.Ui_r_1 import Ui_Form

# class R1Ui(QWidget,Ui_Form):
#     def __init__(self):
#         # 2 继承父类初始化
#         super().__init__() 
      
#         # 3 导入界面类setupUi函数，填入 self 参数作为父类。
#         self.setupUi(self)


# 三 扩充操作
# 1 右上角菜单按钮动画
    # 菜单按钮已经被设为checkable，默认不是checked。
    # 初始先将关于、重置、退出三个按钮置于菜单位置
    # 点击后，菜单按钮为checked，将关于、重置、退出三个按钮置于当前ui界面各自的位置
    # 定义动画对象列表
        # 列表 taglist=[关于、重置、退出三个按钮]
    # 取得动画列表对象当前定义的ui位置
        # 用列表 tagpos=[item.pos() for i in self.taglist]    
# 2 各个slot
# 3 对外的信号
from resource.ui.Ui_r_1 import Ui_Form

class R1Ui(QWidget,Ui_Form):
    # 对外信号
    # 定义退出信号
    registerExit_signal=Signal()
    # 定义注册信号 传递用户名和密码
    registerSignal=Signal([str,str])
    def __init__(self):
        super().__init__() 
        self.setupUi(self)

        # 定义动画对象列表和取得当前位置
        # 用列表，则有序，上下就可以对的上
        self.taglist=[self.au_btn,self.ex_btn,self.rst_btn]
        self.tagpos=[item.pos() for item in self.taglist]

        # 收拢三个动画按钮到菜单按钮后面去
        self.collect_btn()

    # 收拢三个动画按钮到菜单后面去
    def collect_btn(self):
        for i in self.taglist:
            i.move(self.mn_btn.pos())

    # 菜单按钮
    @Slot(bool)
    def on_mn_btn_clicked(self,v):
        print('菜单按钮测试',v)
        self.mn_anmotion(v)
    # 动画
    def mn_anmotion(self,v):
        # 定义动画组对象
        # a_group=QSequentialAnimationGroup(self)#串行动画组
        a_group=QParallelAnimationGroup(self)#并行动画组
        # 用动画列表对象定义动画
        for idx,tagert in enumerate(self.taglist):
            # print(idx,tagert)
            # 用属性动画定义动画对象
            a_item=QPropertyAnimation(tagert,b'pos',self)
            # 定义起始和终止位置
            a_item.setStartValue(self.mn_btn.pos())
            a_item.setEndValue(self.tagpos[idx])
            # 设置动画时长
            a_item.setDuration(500)
            # 设置动画曲线
            # a_item.setEasingCurve(QEasingCurve.OutBounce)#弹簧
            # 加入动画组
            a_group.addAnimation(a_item)

        # 设置动画的方向
        # 发现动画后，菜单按钮被挡住，点不到了。在ui编辑器designer中选中菜单按钮，点击放在前面按钮，即解决，则菜单按钮始终在最前。
        if v:
            a_group.setDirection(QAbstractAnimation.Forward)#调整了一下Forward和Backward，现在顺了。
            
        else:
            a_group.setDirection(QAbstractAnimation.Backward)
            
        # 动画组开始动画 
        a_group.start(QAbstractAnimation.DeleteWhenStopped)#不保留动画

    # 关于
    @Slot()
    def on_au_btn_clicked(self):
        print('关于')
        # 弹出消息对话框
        QMessageBox.about(self,'title-标题','text-关于.........111111111111\n111111111111111111111111111\n11111111111111111111\n1111111111111111111111')
    # 重置
    @Slot()
    def on_rst_btn_clicked(self):
        print('重置')
        self.u_le.clear()
        self.p_le.clear()
        self.c_le.clear()
    # 退出
    @Slot()
    def on_ex_btn_clicked(self):
        print('退出')
        # 向外发射register_exit信号
        self.registerExit_signal.emit()

    # 注册按钮默认是不可用的，当三个输入框都有值，并且两个密码框的值完全相等后，才可以变成enable
    def reg__btn_enable(self):
        val=len(self.u_le.text().strip()) and len(self.p_le.text().strip()) and len(self.c_le.text().strip()) and self.p_le.text()==self.c_le.text()
        self.reg_btn.setEnabled(val)
       

    @Slot()
    def on_u_le_textChanged(self):
        # print(self.u_le.text())
        self.reg__btn_enable()
    @Slot()
    def on_p_le_textChanged(self):
        # print(self.p_le.text())
        self.reg__btn_enable()
    @Slot()
    def on_c_le_textChanged(self):
        # print(self.c_le.text())
        self.reg__btn_enable()
    
    # 注册按钮 向外发射注册信号 传递用户名和密码
    @Slot()
    def on_reg_btn_clicked(self):
        print('注册')
        # 发射注册信号
        self.registerSignal.emit(self.u_le.text(),self.p_le.text())



if __name__ == "__main__":
    app=QApplication([])
    wd=R1Ui()
    wd.show()
    # 监测自定义向外发射的信号
    wd.registerExit_signal.connect(lambda : print('收到registerExit注册退出信号'))
    wd.registerSignal.connect(lambda u,p: print(f'收到registerSignal注册信号，传递用户名{u}和密码{p}'))
    app.exec_()
    
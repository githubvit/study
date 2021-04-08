from PySide2.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QLabel,QTableWidget,QListView,QSizeGrip
from PySide2.QtCore import Qt,Slot
from PySide2.QtGui import QIcon,QStyleHints
import qtawesome as qta #引入图标

import os,sys



# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from Ui_test2 import Ui_MainWindow

class Test2Ui(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        # 2 继承父类初始化
        super().__init__() 

        # 设置移动flag 防止鼠标跟踪
        self.move_flag=False
        
        # 3 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 4 设置无边框
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)#设置背景透明

        # 5 设置主窗口始终置顶
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # 6 设置窗口透明度
        # self.setWindowOpacity(0.5)

        # 7 设置窗口最小化 最大化 关闭 这样就调出了边框
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowMinMaxButtonsHint|Qt.WindowCloseButtonHint)
        
        # 8 添加  Font Awesome, Elusive Icons or Material Design Icons. 字体图标 
        # 清空文字 
        self.cls_btn.setText('')
        self.max_btn.setText('')
        self.min_btn.setText('')
        # 添加图标
        # cls_icon=qta.icon('fa.close',scale_factor=1.3,color='white')
        cls_icon=qta.icon('mdi.close',scale_factor=1.3,color='white')#使用 Material Design Icons图标 线条要细很多
        self.cls_btn.setIcon(cls_icon)
        # max_icon=qta.icon('fa.window-maximize',color='white')
        max_icon=qta.icon('mdi.border-all-variant',scale_factor=1,color='white')#使用 Material Design Icons图标
        self.max_btn.setIcon(max_icon)
        # min_icon=qta.icon('fa.window-minimize',color='white')
        # min_icon=qta.icon('ei.minus',color='white')#使用Elusive Icons图标 这个比上面好 上面的偏下
        min_icon=qta.icon('mdi.minus',scale_factor=1.3,color='white')#使用 Material Design Icons图标 线条要细很多
        self.min_btn.setIcon(min_icon)

        # 9 新的窗口移动实现
        # 用定义的函数moveWindow覆盖标题栏控件top_wgt的鼠标移动事件mouseMoveEvent

        # 为了避免top_wgt可变（可点击、可输入）子控件的点击影响移动，
        # 就要添加能否移动开关self.move_enable。
        # 只有当鼠标用左键点击在窗体上（即不可变的部分，不可变的控件如lable，也是窗体的一部分），
        # 才可以打开开关，点在可变子控件上不是点击在窗体上，就不能打开开关，不能移动。
        # 否则子控件的鼠标移动，也会作用到父控件，带来紊乱。
        self.move_enable=False
        self.top_wgt.mouseMoveEvent=self.moveWindow
        
        # 10 拉伸
        self.sizegrip=QSizeGrip(self.top_wgt) # 左上角 拉伸
        self.sizegrip2=QSizeGrip(self.cls_btn) # 右上角 拉伸
        self.sizegrip2.setStyleSheet('margin-left:40px;width:5px;height:5px;')
        # 一般放在右下角 即 状态栏的右下角。

    # 添加关闭功能 
    @Slot()
    def on_cls_btn_clicked(self):
        print('关闭')
        self.close()

    # 添加主窗口移动功能
    
    # 实现窗口移动
    # 监听三件事 设置移动flag
    # def mousePressEvent(self,evt):
    #     # 取两点原始绝对坐标
    #      # 判断鼠标按钮是左键 杜绝右键移动
    #     if evt.button()==Qt.LeftButton:
    #         # 捕获鼠标按下点的起始xy值 绝对坐标
    #         self.mouse_x=evt.globalX()
    #         self.mouse_y=evt.globalY()
    #         print('鼠标按下')
    #         # 鼠标按下时窗口原点位置
    #         self.origin_x=self.x()
    #         self.origin_y=self.y()
    #         # 开启移动flag
    #         self.move_flag=True
        
    # def mouseMoveEvent(self,evt):
    #     # 防止 鼠标跟踪 设置移动标志 self.move_flag
    #     if self.move_flag:
    #         # 计算距离
    #         # 移动的距离
    #         desc_x=evt.globalX()-self.mouse_x
    #         desc_y=evt.globalY()-self.mouse_y
    #         # print(desc_x,desc_y)
    #         # 移动原点
    #         # 移动的具体尺寸 把按下点移动的距离传递给原点即可
    #         self.move(self.origin_x+desc_x,self.origin_y+desc_y)
    #         print('鼠标移动...')
      
    # def mouseReleaseEvent(self,evt):
    #     # 将标志还原 保证鼠标可以释放
    #     self.move_flag=False
    #     print('鼠标释放了')   

    # 新的窗口移动实现
    # 把移动的主题功能组织好，def moveWindow(self,event)
    # 给到具体的控件上（覆盖自定义的标题栏区域 self.top_wgt 的mouseMoveEvent事件函数），而不是窗体。
    # self.top_wgt.mouseMoveEvent=self.moveWindow
    def mousePressEvent(self,event):
        self.originPos = event.globalPos() 
        # 点击在窗体上才会有初始位置 
        # 而哪些不可变的控件会成为窗体 比如label 而btn和le等可点击可输入则不会。
        # 空白的部分也会成为窗体，总之不可变的部分就会成为窗体的一部分。
        if event.buttons() == Qt.LeftButton:
            self.move_enable=True #打开 移动开关
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    def moveWindow(self,event):
        # MOVE WINDOW
        if self.move_enable and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.originPos)
            self.originPos = event.globalPos()
            # event.accept()

    def mouseReleaseEvent(self,event):
        # 恢复不能移动
        self.move_enable=False

if __name__ == "__main__":
    app=QApplication([])
    wd=Test2Ui()
    wd.show()
    app.exec_()
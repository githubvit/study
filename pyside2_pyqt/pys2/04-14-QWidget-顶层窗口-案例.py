from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

# 设定无边框样式 
# 自定义最小化、最大化（还原）、关闭按钮
# 设定窗口移动

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowFlags(Qt.FramelessWindowHint) #设定无边框样式
        self.setWindowTitle('顶层窗口——无边框样式')
        self.setWindowOpacity(0.8)#设定窗口半透明
        
        # 设定按钮宽高及边距
        self.btn_width=40
        self.btn_height=30
        self.btn_margin=10

        # 设置移动flag 防止鼠标跟踪
        self.move_flag=False
        
        self.setup_ui()


    # 自定义最小化、最大化（还原）、关闭
    def setup_ui(self):
        
        # 关闭按钮
        self.close_btn=QPushButton(self)
        self.close_btn.resize(self.btn_width,self.btn_height)
        self.close_btn.setText('关闭')
        self.close_btn.clicked.connect(self.close)

        # 还原—最大化按钮
        self.max_btn=QPushButton(self)
        self.max_btn.resize(self.btn_width,self.btn_height)
        self.max_btn.setText('最大化')
        self.max_btn.clicked.connect(self.max_norm)

        # 最小化按钮
        self.min_btn=QPushButton(self)
        self.min_btn.resize(self.btn_width,self.btn_height)
        self.min_btn.setText('最小化')
        self.min_btn.clicked.connect(self.showMinimized)
    
    # 设置最大化按钮槽函数
    def max_norm(self):
        # 先获取窗口状态
        # if self.windowState()==Qt.WindowMaximized: #用这个状态判断，点还原至少点两下
        if self.isMaximized():#用这个状态判断 点击很顺利
            self.showNormal()
            self.max_btn.setText('最大化')
        else:
            self.showMaximized()
            self.max_btn.setText('还原')
            
        

    # 监听窗口大小变化resizEvent 
    # 一定只要在这里move按钮，不然按钮不会自适应窗口大小变化
    def resizeEvent(self,evt):
        self.close_btn_x=self.width()-self.btn_width
        self.close_btn_y=self.btn_margin
        self.close_btn.move(self.close_btn_x,self.close_btn_y)
        

        self.max_btn_x=self.close_btn_x-self.btn_width
        self.max_btn_y=self.btn_margin
        self.max_btn.move(self.max_btn_x,self.max_btn_y)

        self.min_btn_x=self.max_btn_x-self.btn_width
        self.min_btn_y=self.btn_margin
        self.min_btn.move(self.min_btn_x,self.min_btn_y)
        

       
    
    # 实现窗口移动
    # 监听三件事 设置移动flag
    def mousePressEvent(self,evt):
        # 取两点原始绝对坐标
         # 判断鼠标按钮是左键 杜绝右键移动
        if evt.button()==Qt.LeftButton:
            # 捕获鼠标按下点的起始xy值 绝对坐标
            self.mouse_x=evt.globalX()
            self.mouse_y=evt.globalY()
            print('鼠标按下')
            # 鼠标按下时窗口原点位置
            self.origin_x=self.x()
            self.origin_y=self.y()
            # 开启移动flag
            self.move_flag=True
        
    def mouseMoveEvent(self,evt):
        # 防止 鼠标跟踪 设置移动标志 self.move_flag
        if self.move_flag:
            # 计算距离
            # 移动的距离
            desc_x=evt.globalX()-self.mouse_x
            desc_y=evt.globalY()-self.mouse_y
            # print(desc_x,desc_y)
            # 移动原点
            # 移动的具体尺寸 把按下点移动的距离传递给原点即可
            self.move(self.origin_x+desc_x,self.origin_y+desc_y)
            print('鼠标移动...')
      
    def mouseReleaseEvent(self,evt):
        # 将标志还原 保证鼠标可以释放
        self.move_flag=False
        print('鼠标释放了')  

if __name__ == "__main__":

    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
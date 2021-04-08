from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QSizeGrip
from PySide2.QtCore import Signal,Slot,Qt,QEvent
from PySide2.QtGui import QIcon

import os,sys



# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 二 显示ui框架 （2.1 2 3 即可显示ui 2.4 开始属于扩展 动作部分）
# 2.1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_nobk import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序



class NobkUi(QWidget,Ui_Form):
    
    def __init__(self):
        # 2.2 继承父类初始化
        super().__init__() 
  
        # 2.3 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

## --------------------------------- 从这里开始是nobk无边框项目内容 ---------------------------------

        # 1 设置无边框
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 设置背景透明
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # 2 设置 list_wgt 可见与不可见 通过边栏点击切换

        self.list_wgt.hide()#默认隐藏

          

        # self.left_wgt.mousePressEvent= show_list_wgt

        # 3 设置退出
        # self.cls_btn.clicked.connect(self.close) # 由于对self.cls_btn设置了过滤器 就要在过滤事件中 设置关闭 此处就注释掉

        # 4 设置点击标题栏窗口移动                      ***
        # 也就是说 窗口的移动是通过 标题栏的移动事件 来实现的。
        # 4.1
        # 用定义的移动函数moveWindow 覆盖 标题栏控件btl_wgt的鼠标移动事件mouseMoveEvent

        # 为了避免btl_wgt可变（可点击、可输入）子控件的点击影响移动，
        # 就要添加能否移动开关self.move_enable。
        # 只有当鼠标用左键点击在窗体上（即不可变的部分，不可变的控件如lable，也是窗体的一部分），
        # 才可以打开开关，点在可变子控件上不是点击在窗体上，就不能打开开关，不能移动。
        # 否则子控件的鼠标移动，也会作用到父控件，带来紊乱。
        self.move_enable=False
        self.btl_wgt.mouseMoveEvent=self.moveWindow


        # 5 最大化-还原切换
        # self.max_btn.clicked.connect(self.max_restore)
        # 双击标题栏 也可切换
        self.btl_wgt.mouseDoubleClickEvent=lambda evt: self.max_restore()

        # 6 最小化
        # self.min_btn.clicked.connect(self.showMinimized)

        # 7 拉伸                                    *****
        #  设定窗口最小值
        self.setMinimumSize(600,500)
        #  设置列表栏 初始最小值
        self.list_wgt_minWidth=200
        #  设置右框的最小值 #用来换算列表栏在拉动过程中的最大值
        self.right_wgt_minWidth=300


        # 7.1 原来底部状态栏的 角部拉伸
        # self.sizegrip=QSizeGrip(self.logo_wgt)
        # self.sizegrip.setStyleSheet('background-position:center;')

        # 7.2 正常拉伸 四边四角拉伸
        # 思路应该是这样：
            # 这里我们将一个窗口划分为  三行三列 9个区域，分别为

                # 左上（1,1）、中上（1，2）、右上（1,3）

                # 左中（2,1）、 中中（2,2）、右中（2,3）

                # 左下（3,1）、中下（3，2）、 右下（3,3）
    
            # 1.当鼠标移动时候，我们首先判断这个光标处于哪个区域

            # 2.当鼠标移动到不同区域，鼠标的形状是不同的。

            # 3.当鼠标按住，计算鼠标按住移动的偏移量，根据 中中（2,2） 之外的区域的拉伸特性，来重新设置窗口的坐标。

        # self.line_width=2
        # 获取当前窗口尺寸,应答放在窗口打开后去获取，因此，拉伸的动作也是在show之后调用。window_stretch
        # print('当前窗口尺寸',self.geometry()) #当前窗口尺寸 PySide2.QtCore.QRect(0, 0, 1000, 500) 无法获取窗口坐标

        # 7.1.1 设置鼠标跟踪，这是窗口拉伸必要的步骤
        
        self.mouseTracking_set(True)
        # 设置拉伸动作开关 当打开时 就要关闭移动开关
        self.stretch_enable=False   # 如果为真（即靠近了拉伸区域） 让鼠标变化 表示处于拉伸预备状态 能拉
        self.stretch_start=False    # 如果 鼠标左键点击了 才能 开始拉
        self.area_code='22'      # 区域代码  22 表示不拉伸
        # 8 事件过滤器 
        # 使用：要先安装过滤器，再再事件过滤函数中进行事件过滤，才会有效果。
        # 8.1 安装过滤器 发生事件的控件.installEventFilter(从谁的过滤函数 eventFilter 中过滤)
        self.filter_wgt_list=[self.cls_btn,self.min_btn,self.max_btn,self.left_wgt]
        for wgt in self.filter_wgt_list:
            wgt.installEventFilter(self)
        
        # 在下面的8.2中用 self 的 事件过滤函数 self.eventFilter 对 self.cls_btn控件 进行 事件过滤
        # self.cls_btn.installEventFilter(self)
        # self.min_btn.installEventFilter(self)
        # self.max_btn.installEventFilter(self)
        # self.left_wgt.installEventFilter(self)

    # 边栏开关
    def show_list_wgt(self):
        if not self.stretch_enable:
           
            if self.list_wgt.isVisible():
                # print('1')
                self.list_wgt.hide()
            else:
                # print('2')
                self.list_wgt.show()  
    
    # 窗口 移动事件
    def mouseMoveEvent(self,evt):
        # print(evt.globalPos())
        # print(evt.globalX(),evt.globalY())
        # print(evt.localPos())
        
        # print(evt.x(),evt.y())
        # print(self.area_division())

        if self.isMaximized():#最大就不用 拉伸了
            # 列表栏拉伸
            # 列表栏控件可见，列表栏应该可以拉伸
            if self.list_wgt.isVisible():
                x=evt.x()
                y=evt.y()
                area=self.area_division() # 获取区域划分的结果
                if self.stretch_start and self.area_code=='22.1':
                    # 列表 拉伸
                    sd=self.stretch_data(evt)
                    # 列表list_wgt 的拉伸
                    # 只改变列表的宽度其余不变
                    # 在布局中改变控件尺寸，不是resize，而是设定最小宽度或最小高度。
                    lw=sd['lw']-sd['dx']
                    # 设置最大
                    lw_max=sd['ow']-self.right_wgt_minWidth-self.left_wgt.width()
                    if lw >= lw_max:
                        lw=lw_max

                    self.list_wgt.setMinimumWidth( lw if lw>0 else 0 ) # 大于0才设置 如果小于0 就设置为0，避免出现负值而导致报错
                    if self.list_wgt.width()<self.list_wgt_minWidth: # 如果小于初始最小就让其归零。相当于隐藏了。
                        self.list_wgt.setMinimumWidth(0)

                   

                else:
                    # 列表 区域响应
                    if y>area['y1'] and y<area['y2'] and x>=area['x2.1'] and x<=area['x2.2']:
                        # 打开拉伸开关
                        self.stretch_enable=True
                        self.setCursor(Qt.SizeHorCursor) #左右拉伸光标
                        # 改变区域码
                        self.area_code='22.1'
                    else:
                        # 其余区域 关闭拉伸开关
                        self.stretch_enable=False
                        self.setCursor(Qt.ArrowCursor) 
                
            return

        if self.stretch_start:
            # 窗口拉伸
            self.window_stretch(evt)
        else:
            # 区域响应
            self.area_response(evt)
        

        return super().mouseMoveEvent(evt) 

    # 窗口拉伸之 区域响应
    def area_response(self,evt):
        x=evt.x()
        y=evt.y()
        area=self.area_division() # 获取区域划分的结果
        # print(area)

        # 先按行分
        if  y<=area['y1']:
            # print('在第一行 1')
            # 再按列分
            if  x<=area['x1']:
                # print('在第一列 1')
                # 打开拉伸开关
                self.stretch_enable=True
                # 左上 设定鼠标形状
                self.setCursor(Qt.SizeFDiagCursor)
                
                # 改变区域码
                self.area_code='11'

            elif x>area['x1'] and x<area['x2']:
                # print('在第二列 2')
                # 中上 
                # 打开拉伸开关
                self.stretch_enable=True
                self.setCursor(Qt.SizeVerCursor)
               
                # 改变区域码
                self.area_code='12'
                
            else:
                # print('在第三列 3')
                # 右上
                # 打开拉伸开关
                self.stretch_enable=True
                self.setCursor(Qt.SizeBDiagCursor) 
                
                # 改变区域码
                self.area_code='13'

        elif y>area['y1'] and y<area['y2']:
            # print('在第二行 2')
            if  x<=area['x1']:
                # print('在第一列 1')
                # 左中
                # 打开拉伸开关
                self.stretch_enable=True
                self.setCursor(Qt.SizeHorCursor)
                
                # 改变区域码
                self.area_code='21'
                
            elif x>area['x1'] and x<area['x2']:
                # 嵌入列表区域响应
                if self.list_wgt.isVisible() and x>=area['x2.1'] and x<=area['x2.2']:
                    # 打开拉伸开关
                    self.stretch_enable=True
                    self.setCursor(Qt.SizeHorCursor) #左右拉伸光标
                    # 改变区域码
                    self.area_code='22.1'

                else:
                    # print('在第二列 2')
                    # 中中 常规箭头
                    # 关闭拉伸开关                         *******
                    self.stretch_enable=False
                    self.setCursor(Qt.ArrowCursor)
                    # 改变区域码
                    self.area_code='22'
                
            else:
                # print('在第三列 3')
                # 右中
                # 打开拉伸开关
                self.stretch_enable=True
                self.setCursor(Qt.SizeHorCursor)
                
                # 改变区域码
                self.area_code='23'
                
        else:
             # print('在第三行 3')
            if x<=area['x1']:
                # print('在第一列 1')
                # 左下
                # 打开拉伸开关
                self.stretch_enable=True
                self.setCursor(Qt.SizeBDiagCursor)
               
                # 改变区域码
                self.area_code='31'
     
            elif x>area['x1'] and x<area['x2']:
                # print('在第二列 2')
                # 中下
                # 打开拉伸开关
                self.stretch_enable=True
                self.setCursor(Qt.SizeVerCursor)
               
                # 改变区域码
                self.area_code='32'
      
            else:
                # print('在第三列 3')
                # 右下 设定鼠标形状
                # 打开拉伸开关
                self.stretch_enable=True
                self.setCursor(Qt.SizeFDiagCursor)
                
                # 改变区域码
                self.area_code='33'
                
    # 窗口拉伸之 区域划分
    def area_division(self):
        w=self.width()
        h=self.height()
        c=5 # 边框厚度
        res={
            'x1':c,
            'x2':w-c,
            'x3':w,
            'y1':c,
            'y2':h-c,
            'y3':h,
        }
        # 列表栏如果可见 定义拉伸左右拉伸区域 22.1
        if self.list_wgt.isVisible():
            x_l1=self.list_wgt.x()+self.list_wgt.width()
            res['x2.1']=x_l1-c
            res['x2.2']=x_l1+c

        return res

    # 窗口拉伸之 设置鼠标自动跟踪
    def mouseTracking_set(self,bool):
        # 鼠标跟踪 不是一设置就有效果的，如果有多级遮挡，就必须一级一级来设置，才能有效。
        self.setMouseTracking(bool)
        
        # 为了避免被子控件遮挡导致的问题，需要把所有可视子控件都设置 鼠标跟踪
        for item in self.findChildren(QWidget): #采用这种方式 避免下面这样一个一个设置
            # print(item)
            item.setMouseTracking(bool)
            

        # self.cnt_wgt.setMouseTracking(True)
        # self.left_wgt.setMouseTracking(True)
        # self.right_wgt.setMouseTracking(True)
        # self.list_wgt.setMouseTracking(True)
         
        # self.btl_wgt.setMouseTracking(True)
  
    # 窗口拉伸之 拉伸数据 
    def stretch_data(self,evt):
        
        # 开始拉伸
        if self.stretch_enable and self.stretch_start:
            # print('显示后，窗口尺寸',self.geometry())
            # 计算移动距离 用 外部的x，y
            # 鼠标的坐标
            gx=evt.globalX()
            gy=evt.globalY()
            # 窗口的坐标
            ox=self.origin_x
            oy=self.origin_y
            # 窗口的大小
            ow=self.origin_w
            oh=self.origin_h

            # 鼠标点击的坐标
            mcx=self.mouse_clicked_x
            mcy=self.mouse_clicked_y

            # 移动的距离
            dx=mcx-gx
            dy=mcy-gy


            res={
                'gx':gx,'gy':gy,'ox':ox,'oy':oy,'ow':ow,'oh':oh,'dx':dx,'dy':dy
            }
            # 如果列表栏可见 获取列表栏鼠标点击时的宽度
            if self.list_wgt.isVisible():
                res['lw']=self.list_wgt_width
                res['rw']=self.right_wgt_width
            return res

    # 窗口拉伸之 拉伸前预备动作
    def prepare_stretch(self,event):
        self.move_enable=False  #关闭 移动开关
        # 拉伸事项
        # 1 关闭鼠标跟踪 
        # 保证 此刻 窗口移动事件 mouseMoveEvent 响应的是鼠标左键按下后的动作
        self.mouseTracking_set(False) 
        # 2 打开 开始拉升
        self.stretch_start=True
        # 3 传递此刻的坐标 即 拉伸前的初始值
        # 窗口的坐标
        self.origin_x=self.geometry().x()
        self.origin_y=self.geometry().y()
        # 窗口的大小
        self.origin_w=self.width()
        self.origin_h=self.height()
        # 鼠标点击的坐标
        self.mouse_clicked_x=event.globalX()
        self.mouse_clicked_y=event.globalY()
        # print('初始值',self.origin_x,self.origin_y,self.origin_w,self.origin_h,self.mouse_clicked_x,self.mouse_clicked_y)
        # 获取区域代码
        # print('区域代码',self.area_code)

        # 如果列表栏可见 获取鼠标点击时的宽度
        if self.list_wgt.isVisible():
            self.list_wgt_width=self.list_wgt.width()
            self.right_wgt_width=self.right_wgt.width()

    # 窗口拉伸之 窗口拉伸   
    def window_stretch(self,evt):

        sd=self.stretch_data(evt)
        if self.stretch_start: #只有当开始拉升时，sd才会有数据
            if self.area_code=='11':
                # 左上 拉伸
                # 特点：起始的ox oy 就是gx和gy，把移动量用来改变窗体的宽高即可。
                mx=sd['gx']
                my=sd['gy']
                wd=sd['ow']+sd['dx']
                ht=sd['oh']+sd['dy']
                

            elif self.area_code=='12':
                # 中上 拉伸
                # 特点：起始的ox 不动 就是改变oy，把移动量用来改变窗体的高即可。
                mx=sd['ox']
                my=sd['gy']
                wd=sd['ow']
                ht=sd['oh']+sd['dy']
                
            elif self.area_code=='13':
                # 右上 拉伸
                # 特点：起始的ox,oy不动，把移动量用来改变窗体的大小即可。
                mx=sd['ox']
                my=sd['gy']
                wd=sd['ow']-sd['dx']
                ht=sd['oh']+sd['dy']

            elif self.area_code=='21':
                # 左中 拉伸
                # 特点：起始的ox动,oy不动，把移动量用来改变窗体的宽度即可。
                mx=sd['gx']
                my=sd['oy']
                wd=sd['ow']+sd['dx']
                ht=sd['oh']

            elif self.area_code=='22.1':
                
                # 列表list_wgt 的拉伸
                # 只改变列表的宽度其余不变
                # 在布局中改变控件尺寸，不是resize，而是设定最小宽度或最小高度。

                lw=sd['lw']-sd['dx']
                # 设置最大
                lw_max=sd['ow']-self.right_wgt_minWidth-self.left_wgt.width()
                if lw >= lw_max:
                    lw=lw_max

                self.list_wgt.setMinimumWidth( lw if lw>0 else 0 ) # 大于0才设置 如果小于0 就设置为0，避免出现负值而导致报错
               
                if self.list_wgt.width()< self.list_wgt_minWidth:
                    self.list_wgt.setMinimumWidth(0)
                
                # print('只改变列表的宽度其余不变',sd['lw']-sd['dx'])
                # 其余不变
                mx=sd['ox']
                my=sd['oy']
                wd=sd['ow']
                ht=sd['oh']

                pass
            elif self.area_code=='23':
                # 右中 拉伸
                # 特点：起始的ox动,oy不动，把移动量用来改变窗体的宽度即可。
                mx=sd['ox']
                my=sd['oy']
                wd=sd['ow']-sd['dx']
                ht=sd['oh']
                

            elif self.area_code=='31':
                # 左下  拉伸
                # 特点：起始的ox就是gx,oy不动，把移动量用来改变窗体的大小。
                mx=sd['gx']
                my=sd['oy']
                wd=sd['ow']+sd['dx']
                ht=sd['oh']-sd['dy']

            elif self.area_code=='32':
                # 中下 拉伸
                # 特点：起始的ox 不动 就是改变oy，把移动量用来改变窗体的高即可。
                mx=sd['ox']
                my=sd['oy']
                wd=sd['ow']
                ht=sd['oh']-sd['dy']

            elif self.area_code=='33':
                # 右下 拉伸
                # 特点：起始的ox、oy不动，把移动量用来改变窗体的大小。
                mx=sd['ox']
                my=sd['oy']
                wd=sd['ow']-sd['dx']
                ht=sd['oh']-sd['dy']
            else:
                # 不动
                mx=sd['ox']
                my=sd['oy']
                wd=sd['ow']
                ht=sd['oh']

            # 这一步别忘了，窗口拉伸的停止位置。
            # 一定要设置窗口最小值，才会有停止位置。
            if wd<=self.minimumWidth():
                mx=self.geometry().x() 
            if ht<=self.minimumHeight():
                my=self.geometry().y()

            # 保证最小右边框
            if self.right_wgt.width()<self.right_wgt_minWidth:
                self.right_wgt.setMinimumWidth(self.right_wgt_minWidth)
            

            self.setGeometry(mx,my,wd,ht)


    # def resizeEvent(self,evt):
    #     print('重设大小事件')
    #     print(evt.size())

   
    # 避免没有刷新
    # 设置了无边框窗口之后，里面的内容就不会及时刷新了
    # 需要重写显示事件

    # def showEvent(self,evt):
    #     self.setAttribute(Qt.WA_Mapped)

    # def leaveEvent(self,evt):
    #     print('离开',dir(evt))#离开没有位置 evt.pos()
        
    # def enterEvent(self,evt):
    #     print('进入',evt.pos())

    # 最大化-还原切换
    def max_restore(self):
        # 先获取窗口状态
        if self.isMaximized():#用这个状态判断 点击很顺利
            self.showNormal()
            icon1=QIcon(u":/16x16/resource/img/cil-window-maximize.png")#图标是designer的资源路径
            self.max_btn.setIcon(icon1)
        else:
            self.showMaximized()
            icon2=QIcon(u":/16x16/resource/img/cil-window-restore.png")
            self.max_btn.setIcon(icon2)  
    
    def mousePressEvent(self,event):
        # 点击在窗体上才会有初始位置 
        self.originPos = event.globalPos() 
        
        # 而哪些不可变的控件会成为窗体 比如label 而btn和le等可点击可输入则不会。
        # 空白的部分也会成为窗体，总之不可变的部分就会成为窗体的一部分。

        if event.buttons() == Qt.LeftButton:
            # 拉伸开关优先
            if self.stretch_enable:
                # 拉伸预备动作
                self.prepare_stretch(event)
            else:
                # 移动开关
                self.move_enable=True       # 打开 移动开关
                self.stretch_start=False    # 关闭 开始拉升 
            # print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
        return super().mousePressEvent(event)
    
    # 4.2 
    # 移动窗口实现
    # 把移动的主题功能组织好，def moveWindow(self,event)
    # 给到具体的控件上（覆盖自定义的标题栏区域 self.top_wgt 的mouseMoveEvent事件函数），而不是窗体。
    # self.btl_wgt.mouseMoveEvent=self.moveWindow

    # 窗口移动程序 覆盖 自定义标题栏的鼠标移动事件
    def moveWindow(self,event):
        # 7.1.2 响应窗口的鼠标跟踪设置，
        # 由于该程序覆盖了self.top_wgt.mouseMoveEvent 即顶部自定义标题栏的鼠标移动事件，
        # 因此要想self.top_wgt和其子控件设置的鼠标跟踪有效果，
        # 就必然要引入整个窗体的鼠标移动程序，
        # 这样才能使得self.top_wgt极其子控件设置的鼠标跟踪，响应整个窗口的鼠标移动事件，

        # 从而实现鼠标的变化，完成窗口拉伸。
        self.mouseMoveEvent(event) 
        
        # 窗口移动
        if self.move_enable and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.originPos)
            self.originPos = event.globalPos()
            event.accept()#表示该事件不再往上传递
            # 事件传递顺序 os→app→子控件→父控件→...

    def mouseReleaseEvent(self,event):
        # 状态复位
        self.reset_state(event)
        return super().mouseReleaseEvent(event)

    # 状态复位
    def reset_state(self,evt):
        # 恢复不能移动
        self.move_enable=False
        # 拉伸复位
        # 设置鼠标跟踪
        self.mouseTracking_set(True) 
        self.stretch_enable=False # 表示处于拉伸预备状态 能拉
        self.stretch_start=False # 鼠标左键点击了 才能 开始拉
        # 区域响应 
        # 既然恢复了鼠标跟踪 为什么还要设置区域响应？
        # 因为鼠标释放时不动，则就不会有 mouseMoveEvent事件发生，就不会执行区域响应，为了保证鼠标响应，则必须设置区域响应。
        self.area_response(evt)
        # 获取区域代码
        # print('区域代码',self.area_code)

        # 列表栏状态 如果 释放时 列表栏宽度为0，则就设置为隐藏，
        # 并将最小宽度改为self.list_wgt_minWidth 200，这样下次打开时，就不会是0而看不见了。 
        if self.list_wgt.width()==0:
            self.list_wgt.hide()
            self.list_wgt.setMinimumWidth(self.list_wgt_minWidth)
    



    # 8.2 事件过滤动作函数 
    # 对于 关闭、最大、最小按钮要进行 事件过滤 
    def eventFilter(self,watched,evt):
        # watched 事件发生的控件  evt.type() 事件的类型

        # 对于 self.cls_btn 控件 发生的 QEvent.MouseButtonPress 类型的事件 过滤
        
        # 注意 
        # 1 在 8.1 要先对 self.cls_btn 控件 安装 事件过滤器 并指名 使用 self 的过滤函数 eventFilter
        #  即 self.cls_btn.installEventFilter(self)

        # 2 要关闭self.cls_btn 控件的clicked 事件，否则会有影响。
        # print(evt)
        # print(watched)
        # print(dir(evt))
        # print(dir(watched))

        # if watched==self.cls_btn and evt.type()==QEvent.MouseButtonPress:
        if watched in self.filter_wgt_list and evt.type()==QEvent.MouseButtonPress:
            # 当是鼠标事件后，QEvent对象evt就可以用.buttons()，否则报错 因为QEvent是没有buttons的。
            if evt.buttons()==Qt.LeftButton:
                # print('MouseButton Press事件过滤器')
                if self.stretch_enable:
                    # 拉伸前预备动作
                    self.prepare_stretch(evt)
                    print('可以拉伸')
                else:
                    if watched==self.cls_btn:
                        # 3 退出设置
                        self.close()
                    if watched==self.min_btn:
                        # 最小化
                        self.showMinimized()
                    if watched==self.max_btn:
                        # 最大化/还原
                        self.max_restore()
                    if watched==self.left_wgt:
                        # 边栏开关
                        self.show_list_wgt()
                        
        if watched in self.filter_wgt_list  and evt.type()==QEvent.MouseButtonRelease:
            # print(' MouseButton Release  事件过滤器')
            # 状态复位
            self.reset_state(evt)
              
        return super().eventFilter(watched,evt)


if __name__ == "__main__":
    
    app=QApplication([])
    wd=NobkUi()
    print('是否有鼠标跟踪',wd.hasMouseTracking())
    wd.show()
    # wd.window_stretch() # 窗口拉伸
    
    app.exec_()
一 练习本
1 数据源
2 核心功能
3 界面

二 知识点
1 数据源
2 界面
    1 视频展示
    2 页面展示
        知识点
        例题
        课堂练习

三 就是做一件事 记英语单词

1 显示中文 写出英文
2 显示英文 写出中文
3 读音
4 填空

四 test2.ui
 1 邮箱、设置、主题按钮：
    使得btn按钮鼠标放上去 hover 的时候，没有边框阴影，就像一个平面，比如vscode菜单的效果。
    就要设置无边框border:none;但要有最小宽度minwidth：50px。
 
 2 登录 升级vip按钮：
    使得btn按钮的范围最小，就是文字大小。比如腾讯视频标题栏中最小、最大、关闭等按钮。
    设置无边框border:none;最小宽度可用为0 minwidth：0。

 3 新的窗口移动实现  
   
   3.1 概述

      实现无边框窗口的移动。

   3.2 实现按住窗体即可移动

      对于无边框窗口的移动，原来的设计是通过重写 窗口的三个鼠标事件(鼠标点击事件、鼠标移动事件、鼠标释放事件)函数 得以实现，这样实现的结果是
      点击窗体的任一部分都可以移动窗口。
         def __init__(self):
            # 2 继承父类初始化
            super().__init__()
            # 设置移动flag 防止鼠标跟踪
            self.move_flag=False
        

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

   3.3 实现点击窗体的特定部分才可移动

      现在的改进：点击窗体的特定部分，才能移动，比如顶部自定义的标题栏区域。
      窗体的鼠标点击事件和鼠标释放事件还是要重写，
      把原来重写鼠标移动事件，改为自定义移动函数。
      用自定义移动函数覆盖窗体特定部分的鼠标移动事件函数即可。

      def __init__(self):
        # 2 继承父类初始化
        super().__init__()

        # 新的窗口移动实现
        # 用定义的函数moveWindow覆盖标题栏控件top_wgt的鼠标移动事件mouseMoveEvent

        # 为了避免top_wgt可变（可点击、可输入）子控件的点击影响移动，
        # 就要添加能否移动开关self.move_enable。
        # 只有当鼠标用左键点击在窗体上（即不可变的部分，不可变的控件如lable，也是窗体的一部分），
        # 才可以打开开关，点在可变子控件上不是点击在窗体上，就不能打开开关，不能移动。
        # 否则子控件的鼠标移动，也会作用到父控件，带来紊乱。
        self.move_enable=False
        self.top_wgt.mouseMoveEvent=self.moveWindow 


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
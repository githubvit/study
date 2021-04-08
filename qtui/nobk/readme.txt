无边框窗口nobk项目记录

    1. 解决窗口移动问题
    
    2. 解决窗口拉伸问题 *****


目录结构：
    让模块结构和项目结构尽量保持一致，尽量避免引入过程的修改。
    模块名
        resouce
            img     图标、及背景图片文件夹
            ui      designer设计师ui文件夹 以及 ui转换成py文件的文件夹
        view 
            各个界面的视图文件
        readme.txt

本节收获：

1.  如何在一个界面文件view中，实现某个子控件的某个事件的特色功能； 自定义函数——>覆盖控件事件

        self.moveWindow=self.moveWindow

    通过 按住 标题栏 移动 才能 移动窗口 功能 的实现，掌握通过 自定义 移动函数self.moveWindow，
    然后用 移动函数 覆盖 标题栏移动事件self.moveWindow 的方式。
        
    即可以定义 一个函数（比如self.moveWindow），然后覆盖 某个子控件（比如 self.btl_wgt）的某个事件(比如 mouseMoveEvent事件)，
    从而实现某个控件（比如 self.btl_wgt）某个事件（比如 mouseMoveEvent事件）的特色功能。

2.  窗口拉伸 功能的实现
    
    通过观察别的软件的窗口拉伸，比如浏览器、vs、...，了解到该功能的细节：
    
    分成三步，鼠标自由移动时的边框感应，和 按住鼠标之后的拉伸，以及松开鼠标后的状态复位。

    对于前两步，也就是 ，没按住鼠标（设置了鼠标跟踪）的 mouseMoveEvent事件，和按住鼠标的mouseMoveEvent事件。
    
    首先 是 移动，边框感应 导致 鼠标变化，我们定义为 区域感应（self.area_response(evt)），
    不同的区域带来不同的鼠标外形。
    
        这就带来了如何划分区域（self.area_division() ）的问题，对于窗口，按 九宫格 划分区域
    
            #这里我们将一个窗口划分为  三行三列 9个区域，分别为

            # 左上（1,1）、中上（1，2）、右上（1,3）

            # 左中（2,1）、中中（2,2）、右中（2,3）

            # 左下（3,1）、中下（3，2）、 右下（3,3）


            这个九宫格 最大的区域就是 中中（2,2），这是默认区域，鼠标为箭头。

            其余都是边框区域(非常细小，一般边框感应粗细常数 c=5)，呈现不同的拉伸鼠标外形。

            以 中中（2,2）为中心，对称的鼠标外形是一致的。
        
            比如左上和右下，中上和中下，左中和右中，左下和右上。

        划分好了区域，还要移动时，鼠标能感应到，

            这就要设置鼠标自动跟踪，涉及到子控件的鼠标跟踪。

            了解到 鼠标跟踪 不是一设置就有效果的，如果有多级遮挡，就必须一级一级来设置，才能有效。

            自定义鼠标跟踪，self.mouseTracking_set(True)。   

    
    其次 是 当移动感应到边框区域 按住后 则可以开始拉伸，按住不放，拖拽鼠标开始拉伸（self.window_stretch(evt)）。
    
        按住鼠标的鼠标移动，不同于没有按住鼠标的鼠标移动，不会执行区域感应的功能，而是执行拉伸的功能。
    
        只会记住按住鼠标那一刻鼠标的形状，和鼠标的区域代码。

        在按住鼠标的那一刻 会记住 预备拉伸用的数据  执行# 拉伸预备动作self.prepare_stretch(event)。

        按住并开始移动，则执行 该 区域代码 拉伸 应有的动作 # 窗口拉伸self.window_stretch(evt)。

        拉伸要有停止位，一般指最小高度和最小宽度，到了最小宽度 ，如果拉伸使得宽度还要继续变小，则 x （窗口的横坐标）就不能再变了；
        到了最小高度 ，如果拉伸使得高度还要继续变小，则 y （窗口的纵坐标）就不能再变了。


3.  释放 鼠标时 要 进行 状态复位 # 状态复位self.reset_state(event)
        不管是移动窗口，
        还是窗口拉伸，
        松开鼠标的刹那，都要进行状态复位。

4.  事件过滤器的使用
    
    解决 关闭、最大、最小等按钮控件在拉伸时不响应。
    
    所以用事件过滤器过滤出这些控件在拉伸时的事件，让其响应。
    
    从而实现这些控件的同一事件可以根据不同的状态，实现不同的响应功能。

    第一步，在初始化__init__时，给需要过滤的控件安装事件过滤器

        要先安装过滤器，再在事件过滤函数中进行事件过滤，才会有效果。

        安装过滤器 
            发生事件的控件.installEventFilter(用谁的过滤函数 eventFilter 中过滤)
            给一堆控件安装过滤器
            self.filter_wgt_list=[self.cls_btn,self.min_btn,self.max_btn,self.left_wgt]
            for wgt in self.filter_wgt_list:
                wgt.installEventFilter(self)

    第二步，在过滤对象的过滤事件中，对控件的特定事件进行过滤
        
        对于过滤控件如果定义了某个信号和槽，该信号对过滤事件是有影响的，则要关闭。
        
        可以将该信号要实现的功能放到过滤器中来实现。

        注意 QEvent对象evt在不同的事件类型中可以有不同的api。

        def eventFilter(self,watched,evt):
            # watched 事件发生的控件  evt.type() 事件的类型

            # 对于 self.cls_btn 控件 发生的 QEvent.MouseButtonPress 类型的事件 过滤
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
                print(' MouseButton Release  事件过滤器')
                # 状态复位
                self.reset_state(evt)

            return super().eventFilter(watched,evt)
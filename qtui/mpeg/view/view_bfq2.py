from PySide2.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QLabel,QFileDialog,QVBoxLayout,\
QMessageBox,QFileSystemModel,QToolTip,QTreeView,QScrollArea,QShortcut,QStyle,QDockWidget
from PySide2.QtCore import Signal,Slot,QEvent,QDir,QModelIndex,QUrl,Qt
from PySide2.QtGui import QKeySequence,QPalette
from PySide2.QtMultimedia import QMediaContent,QMediaPlayer,QAbstractVideoSurface
from PySide2.QtMultimediaWidgets import QVideoWidget
import os,sys

import fitz 



# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_bfq2 import Ui_MainWindow

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
# from core.split_music import split_music

class Bfq2Ui(QMainWindow,Ui_MainWindow):
    
    def __init__(self,parent=None):
        # 3 继承父类初始化
        super().__init__(parent) 
      
        # 4 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # self.list_onoff_act
        # self.login_act
        # self.setting_act
    
        # self.lst_dwgt
        # self.lst_wgt

      # 一 左边
        # 目录列表 显示 
        self.tl_show()
        
        # 用事件过滤器 设置 目录列表的提示ToolTip
        # 安装过滤器
        self.lst_tv.installEventFilter(self)


        # 双击 view目录中的文件 右边的选项卡增加一页 addTab(widget,title) title=文件名 
        self.lst_tv.doubleClicked.connect(self.selected_index)

      # 二 右边 QMainWindow中心控件

        # 点击关闭按钮会发出tabCloseRequested信号传递 int 参数，int 是选项页的索引，从右从0开始，移动选项卡则选项页的索引会变
        # self.cnt_tab_tbwgt.tabCloseRequested.connect(lambda v: print('关闭',v))
        self.cnt_tab_tbwgt.tabCloseRequested.connect(self.clos_tabpage)

        self.open_file_list=[] #避免重复打开

        # 缩放
        # 定义缩放快捷键
        self.minus_shortcut=QShortcut(QKeySequence('Ctrl+-'),self.cnt_tab_tbwgt) # 快捷键 父对象 缩小
        self.minus_shortcut.activated.connect(self.zoom_out)
        self.plus_shortcut=QShortcut(QKeySequence('Ctrl+='),self.cnt_tab_tbwgt)  # 放大
        self.plus_shortcut.activated.connect(self.zoom_in)
        self.reset_shortcut=QShortcut(QKeySequence('Ctrl+z'),self.cnt_tab_tbwgt) # 复位100% 
        self.reset_shortcut.activated.connect(self.zoom_0)

      # 三 其他
       
        # 关闭播放器和笔记区
        self.media_dwgt.hide()
        self.mark_dwgt.hide()
        self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))#利用标准图标集中的图标

        self.meida_set()
       

        

  # 一 左边
    # 打开或关闭目录列表   
    @Slot()
    def on_list_onoff_act_triggered(self):
        if self.lst_dwgt.isVisible():
            self.lst_dwgt.hide()
        else:
            self.lst_dwgt.show()

    # 过滤器 
    def eventFilter(self,watcher,evt):
        if watcher==self.lst_tv and evt.type()==QEvent.ToolTip:
            # print('提示事件',dir(evt))
            # 获取鼠标所在点的文件名
            # 关键在于获取所在点的index_model,要用indexAt(event.pos())来获取
            # print(self.lst_tv.currentIndex()) # currentIndex是不变的
            # print(self.t_model.fileName(self.lst_tv.indexAt(evt.pos())))# 根据位置获取index  indexAt(pos)  *****
            file_name=self.t_model.fileName(self.lst_tv.indexAt(evt.pos()))
            if file_name:
                # 用提示类的showText(位置,文本)，即可显示提示
                # 位置要用全局globalPos()
                QToolTip.showText(evt.globalPos(),file_name)

        if watcher==self.media_dwgt and evt.type()==QEvent.Close:
            print('捕捉 到 播放器悬浮区 按钮关闭事件')
            self.vc_player.stop() # 关闭 播放器
        # 问题 如果 播放器 悬浮 然后关闭， 再点击目录打开播放器，播放则看不到画面，只听到声音
        # 如果 播放器  悬浮 不关闭，此时点击目录，则可正常播放，该播放器悬浮状态没有被关闭过，可以正常播放。
            if self.media_dwgt.isFloating():
                print('是悬浮的')
                # self.vc_player.setVideoOutput(self.vw) #重新挂载一次 看看能不能看到画面

                
        return super().eventFilter(watcher,evt)
    
    # 目录区 搜索框
    @Slot()
    def on_sch_lst_le_textChanged(self):
        if self.sch_lst_le.text().strip():
            # 使用过滤显示设置
            text=self.sch_lst_le.text()
            # print(text)
            self.tl_show(text)
        else:
            # 恢复到平常显示
            self.tl_show()  
            
    # 目录 过滤 显示 解决搜索问题
    def tl_show(self,text=None):
        # 设置model
        self.t_model=QFileSystemModel()
        # 关联View
        self.lst_tv.setModel(self.t_model)

        # 设置model根目录
        # self.t_path=r'F:\OneDrive - 中国加油！武汉加油！' # 用这个目录 过滤就不行 因为太大 造成内存不够 过滤目录一片空白
        self.t_path=r'F:\OneDrive - 中国加油！武汉加油！\02初中\数学\初中数学朱韬\人教版 初中数学' # 这个目录小 过滤可用 效果可以
        self.t_model.setRootPath(self.t_path)
      
        # 设置view根索引 为 model的根路径的索引 这样view和model的索引才能保持一致
        self.lst_tv.setRootIndex(self.t_model.index(self.t_path))

        # 隐藏列
        self.lst_tv.setColumnHidden(1,True) # size 列
        self.lst_tv.setColumnHidden(2,True) # type 列
        self.lst_tv.setColumnHidden(3,True) # Date Modified 即 Modifiedtime 列

        # 关闭列头
        self.lst_tv.setHeaderHidden(True) 

        # 过滤
        # 被过滤的文件会变成灰色
        self.t_model.setNameFilterDisables(False) # 被过滤掉的灰色文件不显示
        # 如果 text 不为None 则 执行 过滤
        if text: 
            self.t_model.setNameFilters([f'*{text}*']) # 中文过滤 没有问题
            # 注：setNameFilters参数只接受列表。
            # 展开全部过滤结果
            self.t_model.directoryLoaded.connect(self.lst_tv.expandAll)
 
    # 双击 目录中的文件 右边的选项卡增加一页 addTab(widget,title) title=文件名
    def selected_index(self,index_model):

        # print('参数类型',type(index_model)) # <class 'PySide2.QtCore.QModelIndex'>
        # print('文件名：',self.t_model.fileName(index_model))# 用 QModelIndex 获取文件名
        # print('文件路径',self.t_model.filePath(index_model)) # 获取文件路径
        # print('文件大小',self.t_model.size(index_model)) # 获取文件大小 返回的是字节数 int

        # print('文件类型',self.t_model.type(index_model)) # 获取文件类型 
        # 返回描述节点类型的文字，
        # 如硬盘符是 "Drive"，
        # 文件夹是 "FileFolder"，
        # 文件则用具体的后缀描述，如 "txt File"、"exe File"、"pdf File"等。
        
        # print('是目录吗？',self.t_model.isDir(index_model)) # 判断是否是目录
        # print('该项数据',self.t_model.itemData(index_model)) # 获取 该项数据
       
        
        filename=self.t_model.fileName(index_model)
        filepath=self.t_model.filePath(index_model)
        filetype=self.t_model.type(index_model)

        # 如果是文件 
        if os.path.isfile(filepath):
            # 如果 是 pdf 文件 右边的选项卡增加一页 
            if filetype=='pdf File' and filepath not in self.open_file_list:
                self.add_tabpage(filename,filepath)

            elif filetype in ['flv File','mp4 File','mkv File']:
                self.media_play(filepath)
                

  # 二 右边

    # 增加tab页
    def add_tabpage(self,filename,filepath):
        tab=QWidget()#引入pdf 转换
        i=self.cnt_tab_tbwgt.addTab(tab,filename) # 增加一页 会返回增加的Tab页索引
        self.cnt_tab_tbwgt.setTabToolTip(i,filename) # 利用索引 设定TabBar提示
        self.pdf_tab_page(tab,filepath)#加载pdf_tab页的内容
        tab.setProperty('path',filepath) #设置路径属性 便于关闭时 获取该路径
        self.open_file_list.append(filepath)

    # pdf_tab页的内容
    def pdf_tab_page(self,parent,pdf_file):
        # QScrollArea的用法
        pdf_area1=QScrollArea() # 窗口
        pdf_cnt_wgt=QWidget()   # 内容
        
        pdf_area1.setWidget(pdf_cnt_wgt) # 给窗口设置内容

        # 设置布局
        cnt_layout=QVBoxLayout(parent)
        cnt_layout.addWidget(pdf_area1)

        # 加载pdf 

        # 取得 pdf 对象 doc
        doc=fitz.open(pdf_file)
        # 循环该对象 并定义标签加载 该对象
        v_layout=QVBoxLayout(pdf_cnt_wgt)
        # 定义一个容器 空文件
        page_img='page.png'
        # 放大1.333333倍
        zn=1.333333
        zoom_x=zn
        zoom_y=zn
        mtx=fitz.Matrix(zoom_x,zoom_y).preRotate(0)
        for i,page in enumerate(doc):
            # 转为图形
            pix=page.getPixmap(matrix=mtx,alpha=False)
            # print(dir(pix))
            # 放入容器 即保存
            pix.writePNG(page_img)

            # 定义label
            lab=QLabel()
            # 放入图片
            lab.setPixmap(page_img)

            # 添加每一页的名字和宽高属性  用于缩放
            lab.setObjectName(f'lab{i}')
            lab.setProperty('w',pix.w)
            lab.setProperty('h',pix.h)

            # 放入布局
            v_layout.addWidget(lab)

        pdf_cnt_wgt.adjustSize() # 保证内容区合适大小                 ******
        # 添加内容区控件的名字和宽高属性 用于缩放
        pdf_cnt_wgt.setObjectName('cnt_wgt')
        pdf_cnt_wgt.setProperty('w',pdf_cnt_wgt.width())
        pdf_cnt_wgt.setProperty('h',pdf_cnt_wgt.height())

        pass  

    # 关闭选项页 应该把打开文件列表中的 文件路径 删除
    def clos_tabpage(self,v):
        # 获取该 tab 页 的属性
        wgt=self.cnt_tab_tbwgt.widget(v)
        filepath=wgt.property('path')
        # print(filepath)
        self.cnt_tab_tbwgt.removeTab(v)
        # 清理打开文件列表
        if filepath:
            # 从列表中删除该文件路径
            self.open_file_list.remove(filepath)

    # 放大
    def zoom_in(self):
        # 取出当前页
        widget=self.cnt_tab_tbwgt.currentWidget()

        # print(widget.property('path'))

        if widget.property('path'):
            # 取 lab
            for lab in widget.findChildren(QLabel):
                # 用添加的宽高属性 缩放
                w=lab.width()+lab.property('w')*0.1
                h=lab.height()+lab.property('h')*0.1
                if w/lab.property('w') >1.5:
                    w=lab.property('w')*1.5
                    h=lab.property('h')*1.5
                # print(w,h)
                lab.resize(w,h)
                lab.setScaledContents(True) # 设定 图片大小适合label 
            # 取 内容区域
            cnt_wgt=widget.findChild(QWidget,'cnt_wgt')
            # print(cnt_wgt.property('w'),cnt_wgt.property('h'))
            # 同步缩放内容区域
            cnt_wgt_w=cnt_wgt.width()+cnt_wgt.property('w')*0.1
            cnt_wgt_h=cnt_wgt.height()+cnt_wgt.property('h')*0.1
            if cnt_wgt_w/cnt_wgt.property('w') > 1.5:
                cnt_wgt_w=cnt_wgt.property('w')*1.5
                cnt_wgt_h=cnt_wgt.property('h')*1.5
            
            cnt_wgt.resize(cnt_wgt_w,cnt_wgt_h)
            
        # print('zoom in')

    # 缩小
    def zoom_out(self):
        # 取出当前页
        widget=self.cnt_tab_tbwgt.currentWidget()

        # print(widget.property('path'))

        if widget.property('path'):
            # 取 lab
            for lab in widget.findChildren(QLabel):
                # 用添加的宽高属性 缩放
                w=lab.width()-lab.property('w')*0.1
                h=lab.height()-lab.property('h')*0.1
                if w/lab.property('w') <0.5:
                    w=lab.property('w')*0.5
                    h=lab.property('h')*0.5
                # print(w,h)
                lab.resize(w,h)
                lab.setScaledContents(True) # 设定 图片大小适合label 
            # 取 内容区域
            cnt_wgt=widget.findChild(QWidget,'cnt_wgt')
            # print(cnt_wgt.property('w'),cnt_wgt.property('h'))
            # 同步缩放内容区域
            cnt_wgt_w=cnt_wgt.width()-cnt_wgt.property('w')*0.1
            cnt_wgt_h=cnt_wgt.height()-cnt_wgt.property('h')*0.1
            if cnt_wgt_w/cnt_wgt.property('w') < 0.5:
                cnt_wgt_w=cnt_wgt.property('w')*0.5
                cnt_wgt_h=cnt_wgt.property('h')*0.5
            
            cnt_wgt.resize(cnt_wgt_w,cnt_wgt_h)
        # print('zoom out')

    # 重置为100%
    def zoom_0(self):
        # 取出当前页
        widget=self.cnt_tab_tbwgt.currentWidget()

        print(widget.property('path'))

        if widget.property('path'):
            # 取 lab
            for lab in widget.findChildren(QLabel):
                w=lab.property('w')
                h=lab.property('h')
                # print(w,h)
                lab.resize(w,h)
                lab.setScaledContents(True) # 设定 图片大小适合label 
            # 取 内容区域
            cnt_wgt=widget.findChild(QWidget,'cnt_wgt')
            # print(cnt_wgt.property('w'),cnt_wgt.property('h'))
            cnt_wgt.resize(cnt_wgt.property('w'),cnt_wgt.property('h'))
        # print('zoom_0')

  # 三 其他
    # 播放设置
    def meida_set(self):
        # 播放
        # 播放控件设置
        # 第一步 创建 video 视频 控件 
        vw=QVideoWidget()
        self.vw=vw
        v_layout=QVBoxLayout(self.play_wgt)
        v_layout.addWidget(vw)

        # 第二步：创建视频播放的QMediaplayer对象；
        self.vc_player=QMediaPlayer(self.media_dwgt,QMediaPlayer.VideoSurface)

        # 第三步 将视频输出到视频控件上
        self.vc_player.setVideoOutput(vw)

        # 声音设置
        self.vc_player.setVolume(self.voice_sdr.value())

        self.voice_sdr.setValue(10)
        self.mtu_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))

        
        # 播放器对象 读完耗时时的播放处理
        self.vc_player.durationChanged.connect(self.play_handle)
        # 播放位置变化时 推动 进度条
        self.vc_player.positionChanged.connect(self.progrcess_change)
        # 播放器错误处理
        self.vc_player.error.connect(self.handle_player_errors)

        # 播放器状态变化
        self.vc_player.stateChanged.connect(self.vc_player_setIcon)
        # self.vc_player.mediaStatusChanged.connect(lambda v: print('mediaStatusChanged状态',v))


        # QMediaPlayer.State.StoppedState
        # QMediaPlayer.State.PlayingState
        # QMediaPlayer.State.PausedState
        # QMediaPlayer.State.

        # 播放悬浮区 可见变化 传递 bool 可见 True 不可见 False
        # 当播放器位置改变 会影响到播放器 播放
        # 因为当dockwidget控件位置改变 悬浮时 都会经历 visibilityChanged 信号既有False 又有 True 这个过程，因此该信号不可用。
        # self.media_dwgt.visibilityChanged.connect(self.vc_player_handle) #  当 关闭 播放悬浮区时 即 V = False 停止 播放  

        # 因此，由于 dockwidget控件可见变化信号 visibilityChanged 不能用于 关闭 播放器，
        # 所以，这里用事件过滤器 捕捉播放器悬浮区 按钮关闭事件 进行 播放器的关闭
        # 捕捉播放器悬浮区 按钮关闭事件
        self.media_dwgt.installEventFilter(self)

        # 播放悬浮区 浮动  传递 
        # self.media_dwgt.dockLocationChanged.connect(self.vc_player_handle_state)


    # 播放多媒体
    def media_play(self,filepath):
        # print(filepath)
        
        if not self.media_dwgt.isVisible():
            
            # 打开media
            self.media_dwgt.show()

        if self.width() < 1000:
            # 扩展ui播放器宽度 不然会挤占文本区的宽度
            w=self.width()+500
            self.resize(w,self.height())
        # 第四步 视频文件设置 设定要播放的内容 filepath
        vc_file=QMediaContent(QUrl.fromLocalFile(filepath))
        self.vc_player.setMedia(vc_file)
        
    @Slot()
    def on_play_btn_clicked(self):
        if self.vc_player.state() == QMediaPlayer.PlayingState:
            self.vc_player.pause()
        else:
            self.vc_player.play()
            
    # 响应播放器的状态变化 设置图标
    def vc_player_setIcon(self,state):
        if state == QMediaPlayer.PlayingState:
            self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    # 播放进度条 控制进度 滑动进度条sliderMoved
    @Slot(int)
    def on_process_sdr_sliderMoved(self,val):#不要用 valueChanged 因为 播放就会推动进度条的变化
        if self.vc_player.duration():
            self.vc_player.setPosition(val)
    
    
    # 播放加载事件 
    def play_handle(self,val):
        if val:
            # 设置进度条的范围
            self.process_sdr.setRange(0,val)
            # 设置时间显示的时分秒
            sec=round(val/1000)#取整
            h,s1=divmod(sec,3600)#求商 余
            m,s=divmod(s1,60)
            
            if m<10 :
                m='0'+str(m)

            if s<10 :
                s='0'+str(s)
            
            # 时间标签可见
            self.right_lb.show()
            self.left_lb.show()

            self.left_lb.setText('0:00:00')
            self.right_lb.setText(f'{h}:{m}:{s}')
        pass

    # 进度条   跟随 播放
    # 时间标签 跟随 播放
    def progrcess_change(self,v):
        # 进度条   跟随 播放
        self.process_sdr.setValue(v)
        
        # 时间标签 跟随播放
        sec=round(v/1000)#取整
        h,s1=divmod(sec,3600)#求商 余
        m,s=divmod(s1,60)
        
        if m<10 :
            m='0'+str(m)
        if s<10 :
            s='0'+str(s)

        self.left_lb.setText(f'{h}:{m}:{s}')
        pass

    # 关闭播放器 当播放器位置改变 会影响到播放器 播放
    # 因为当dockwidget控件位置改变 悬浮时 都会经历 visibilityChanged 信号既有False 又有 True 这个过程，因此该信号不可用。
    # def vc_player_handle(self,v):
        # print('播放器悬浮区 visibilityChanged 信号 self.media_dwgt.visibilityChanged',v)
        # if self.media_dwgt.isVisible:
            # print('有吗')
            # self.vc_player.stop()

    # 播放器错误处理 
    # error 事件 会 带有错误类消息 e
    def handle_player_errors(selfd,e):
        # print('456',e)
        # 显示错误提示框
        QMessageBox.critical(self,'错误',f'错误:{e}')
        pass

    # 播放器悬浮区 地址变化信号
    # def vc_player_handle_state(self,v):
        # print('播放器悬浮区 dockLocationChanged 信号 self.media_dwgt.dockLocationChanged ',v)
        # 播放器悬浮区 悬浮  PySide2.QtCore.Qt.DockWidgetArea.NoDockWidgetArea
        # 播放器悬浮区 悬浮  PySide2.QtCore.Qt.DockWidgetArea.RightDockWidgetArea


    # 声音
    # 用滑动条进行音量控制
    @Slot(int)
    def on_voice_sdr_valueChanged(self,val):
        # print(val)
        self.vc_player.setVolume(val)
        
    # 静音按钮 mtu_btn
    @Slot()
    def on_mtu_btn_clicked(self):
        if self.vc_player.isMuted():
            self.vc_player.setMuted(False)
            self.voice_sdr.setValue(10) # 有声音
            self.mtu_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        else:
            self.vc_player.setMuted(True)
            self.voice_sdr.setValue(0) # 静音
            self.mtu_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolumeMuted))


if __name__ == "__main__":
    
    app=QApplication([])
    wd=Bfq2Ui()
    wd.show()
    app.exec_()
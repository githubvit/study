from PySide2.QtWidgets import QApplication,QWidget,QMainWindow,QVBoxLayout,QDockWidget
from PySide2.QtCore import Signal,Slot,QEvent,Qt
from PySide2.QtGui import QKeySequence

import os,sys

# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_bqsk_kj import Ui_MainWindow

# 2 框架用view文件
from view_file_explorer import FileExplorerUi # 导入资源管理区域 view 文件
from view_pdf_reader import PdfReaderUi  # 导入pdf阅读器区域 view 文件
from view_media_player import MediaPlayerUi # 导入media播放区域 view 文件
from view_mark import MarkUi # 导入笔记区域 view 文件
from view_start_page import StartPageUi #导入开始页面 view 文件

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
# from core.split_music import split_music

class BqskUi(QMainWindow,Ui_MainWindow):
    
    def __init__(self,parent=None):
        # 3 继承父类初始化
        super().__init__(parent) 
      
        # 4 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

      # 开始页面 
        # 1 引入view
        self.start_vw=StartPageUi()
        # 交给开始页面区 
        self.import_view_wgt(self.start_vw,self.text_start_wgt)
        # 定义开始页面 有 开始属性 便于捕捉 关闭用
        self.text_start_wgt.setProperty('startpage',True)
        

      # 目录区
        # self.action_onoff_tl
        # self.tl_dwgt
        # self.tl_wgt

        # 导入该区域view文件

        # 资源管理器 导入

        # 1 建立要引入的控件
        self.file_folder=r'F:\OneDrive - 中国加油！武汉加油！\02初中\数学\初中数学朱韬\人教版 初中数学'

        self.tl_fe=FileExplorerUi(self.file_folder)

        self.import_view_wgt(self.tl_fe,self.tl_wgt)
        

        # 双击 索引 动作
        self.tl_fe.lst_trv.doubleClicked.connect(self.selected_index)

      # 阅读区
        # self.text_twgt
        # self.text_start_wgt
        # pdf阅读器

        # 点击关闭按钮会发出tabCloseRequested信号传递 int 参数，int 是选项页的索引，从右从0开始，移动选项卡则选项页的索引会变
        # self.text_twgt.tabCloseRequested.connect(lambda v: print('关闭',v))
        self.text_twgt.tabCloseRequested.connect(self.clos_tabpage)

        self.open_file_list=[] #避免重复打开


      # 播放区
        self.media_dwgt.hide()
        # self.media_wgt

        # 视频播放器
       
        # 导入 播放器 view
        self.media_vw=MediaPlayerUi()
        # 设置到 播放区
        self.import_view_wgt(self.media_vw,self.media_wgt)
        
        # 捕捉播放器悬浮区 按钮关闭事件 以实现 点击播放区关闭按钮 可以关闭播放器 
    
        self.media_dwgt.installEventFilter(self)

        # 一直有个问题：                                                                                       ******
            # 当播放区悬浮，即floating时，点击关闭按钮，则下次打开播放器就看不到画面，
            # 该问题在之前的mpeg文件夹下view文件夹中的 view_boq2.py中也一直存在
        # 现在的解决办法是：
            # 当悬浮时，通过设置特征值 setFeatures 使其没有关闭按钮，所以无法关闭。
                # self.media_dwgt.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
            # 不悬浮时，又通过设置特征值 setFeatures 使其有关闭按钮，所以可以关闭。
                # self.media_dwgt.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
            # 因此，要关闭播放器，就必须在不悬浮的位置，即可以停靠的位置关闭。
            # 就避免了悬浮时关闭带来的问题。

        # 利用 位置变化信号 捕捉悬浮，改变设置，解决问题
        self.media_dwgt.dockLocationChanged.connect(self.floating_change_Features)


      # 笔记区
        self.mark_dwgt.hide()
        # self.mark_wgt
        # 画板
        self.mark_vw=MarkUi()
        # 设置到 笔记区
        self.import_view_wgt(self.mark_vw,self.mark_wgt)

    
    # 统一 引入格式
    # 把要引入的控件 wgt 放在 框架的哪个部分 parent
    def import_view_wgt(self,wgt,parent):      
        # 1 设置布局
        v_layout=QVBoxLayout(parent)
        # 修改布局
        v_layout.setMargin(0) # 外边距
        v_layout.setSpacing(0) # 子控件的距离
        # 2 添加控件
        v_layout.addWidget(wgt)

  # 一 目录区

    # 打开或关闭目录列表   
    @Slot()
    def on_action_onoff_tl_triggered(self):
        if self.tl_dwgt.isVisible():
            self.tl_dwgt.hide()
        else:
            self.tl_dwgt.show()

    # 双击 目录中的文件 右边的选项卡增加一页 
    def selected_index(self,index_model):

        # print('参数类型',type(index_model)) # <class 'PySide2.QtCore.QModelIndex'>
        # print('文件名：',self.tl_fe.fe_model.fileName(index_model))# 用 QModelIndex 获取文件名
        # print('文件路径',self.tl_fe.fe_model.filePath(index_model)) # 获取文件路径
        # print('文件大小',self.tl_fe.fe_model.size(index_model)) # 获取文件大小 返回的是字节数 int

        # print('文件类型',self.tl_fe.fe_model.type(index_model)) # 获取文件类型 
        # 返回描述节点类型的文字，
        # 如硬盘符是 "Drive"，
        # 文件夹是 "FileFolder"，
        # 文件则用具体的后缀描述，如 "txt File"、"exe File"、"pdf File"等。
        
        # print('是目录吗？',self.tl_fe.fe_model.isDir(index_model)) # 判断是否是目录
        # print('该项数据',self.tl_fe.fe_model.itemData(index_model)) # 获取 该项数据
        
        filename=self.tl_fe.fe_model.fileName(index_model)
        filepath=self.tl_fe.fe_model.filePath(index_model)
        filetype=self.tl_fe.fe_model.type(index_model)

        if os.path.isfile(filepath):
            # 如果 是 pdf 文件 并且不再打开文件列表里 阅读器选项卡增加一页  
            if filetype=='pdf File' and filepath not in self.open_file_list:
                self.add_tabpage(filename,filepath)
            elif filetype in ['flv File','mp4 File','mkv File']:
                self.media_play(filepath)
                

  # 二 阅读区

    # 增加tab页
    def add_tabpage(self,filename,filepath):
        tab=QWidget()#引入pdf 转换
        i=self.text_twgt.addTab(tab,filename) # 增加一页  addTab(widget,title) title=文件名 会返回增加的Tab页索引
        self.text_twgt.setTabToolTip(i,filename) # 利用索引 设定TabBar提示

        # 1 定义引入的pdf控件
        pdf_widget=PdfReaderUi(filepath)    # 加载pdf
        # 设置到 阅读区
        self.import_view_wgt(pdf_widget,tab) # 设置给tab

        tab.setProperty('path',filepath) # 设置路径属性 便于关闭时 获取该路径
        self.open_file_list.append(filepath)


    # 关闭选项页 应该把打开文件列表中的 文件路径 删除
    def clos_tabpage(self,v):
        # 获取该 tab 页 的属性
        wgt=self.text_twgt.widget(v)
        filepath=wgt.property('path')
        # print(filepath)
        # 关闭tab页
        self.text_twgt.removeTab(v)
        
        # 如果是开始页面 要关闭背景音乐播放器
        if wgt.property('startpage'):
            self.start_vw.mc_player.stop()

        # 如果是有路径属性的页面  就清理打开文件列表 否则再点击该文件就无法打开
        elif filepath:
            # 从列表中删除该文件路径
            self.open_file_list.remove(filepath)

    # 打开/关闭 开始页
    @Slot()
    def on_action_start_page_triggered(self):
        # 是否存在 开始页
        v=self.text_twgt.indexOf(self.text_start_wgt)
        # 当存在会输出 值 否则 会输出 -1
        # print(v)
        if self.text_twgt.isTabEnabled(v): #当v=-1时 .isTabEnabled(v) 输出 False
            # print('有')
            # 停止播放
            self.start_vw.mc_player.stop()
            # 移除tab页
            sid=self.text_twgt.indexOf(self.text_start_wgt)
            self.text_twgt.removeTab(sid)
            
        else:
            # print('没有')
            # 在0位插入开始页
            self.text_twgt.insertTab(0,self.text_start_wgt,'start')
            self.text_twgt.setTabToolTip(0,'start') 
            # 播放音乐
            self.start_vw.mc_player.play()
            
  

  # 三 播放区
    # 播放多媒体
    def media_play(self,filepath):
        # print(filepath)
        if not self.media_dwgt.isVisible():
            # 打开media
            self.media_dwgt.show()
        
        if self.width() < 1000:
            # 扩展ui播放器宽度 不然会挤占文本区的宽度
            w=self.width()+400
            self.resize(w,self.height())

        self.media_vw.load_media_file(filepath)

    # 重写过滤事件函数 
    def eventFilter(self,watcher,evt):
        # 用过滤器 捕捉 播放区按钮关闭事件 
        if watcher==self.media_dwgt and evt.type()==QEvent.Close:
            self.media_vw.vc_player.stop()
        return super().eventFilter(watcher,evt) 

    # 解决浮动时 不可停靠区 不能让其关闭，必须在停靠区才能关闭
    # 浮动时，去掉其开关按钮，让其无法关闭即可。
    def floating_change_Features(self):
        if self.media_dwgt.isFloating():
            self.media_dwgt.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        else:
            self.media_dwgt.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)

  # 四 笔记区
    # 打开/关闭 笔记区
    @Slot()
    def on_action_onoff_mark_triggered(self):
        if self.mark_dwgt.isVisible():
            self.mark_dwgt.hide()
        else:
            self.mark_dwgt.show()


if __name__ == "__main__":
    
    app=QApplication([])
    wd=BqskUi()
    wd.show()
    app.exec_()
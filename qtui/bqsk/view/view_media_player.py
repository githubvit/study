from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QStyle,QVBoxLayout
from PySide2.QtCore import Slot,QUrl
from PySide2.QtMultimedia import QMediaContent,QMediaPlayer,QAbstractVideoSurface
from PySide2.QtMultimediaWidgets import QVideoWidget

import os,sys

# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_media_player import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
# from core.split_music import split_music

class MediaPlayerUi(QWidget,Ui_Form):
    
    def __init__(self,parent=None):
        # 3 继承父类初始化
        super().__init__(parent) 

        
        # 4 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        

        self.meida_setting()

    def meida_setting(self):
        # 播放
        # 播放控件设置
        # 第一步 创建 video 视频 控件 
        vw=QVideoWidget()
        self.vw=vw
        v_layout=QVBoxLayout(self.video_wgt)
        v_layout.setMargin(0)
        v_layout.setSpacing(0)
        v_layout.addWidget(vw)

        # 第二步：创建视频播放的QMediaplayer对象；
        self.vc_player=QMediaPlayer(self)

        # 第三步 将视频输出到视频控件上
        # self.vc_player.setVideoOutput(vw)

        # 声音设置
        self.vc_player.setVolume(self.vol_sld.value())

        self.vol_sld.setValue(10)
        self.vol_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))

        # 初始播放图标
        self.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        # 进度标签不可见
        self.left_lb.hide()
        self.right_lb.hide()
        # 播放按钮不可用
        self.play_btn.setEnabled(False)

    def load_media_file(self,media_file):
        # 第三步 将视频输出到视频控件上
        self.vc_player.setVideoOutput(self.vw)
        # 第四步 视频文件设置 设定要播放的内容 
        vc_file=QMediaContent(QUrl.fromLocalFile(media_file))
        self.vc_player.setMedia(vc_file)

        # 播放器对象 读完耗时时的播放处理
        self.vc_player.durationChanged.connect(self.play_handle)
        # 播放位置变化时 推动 进度条
        self.vc_player.positionChanged.connect(self.progrcess_change)
        # 播放器错误处理
        self.vc_player.error.connect(self.handle_player_errors)

        # 播放器状态变化
        self.vc_player.stateChanged.connect(self.vc_player_setIcon)

    # 播放按钮 
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
    def on_process_sld_sliderMoved(self,val):#不要用 valueChanged 因为 播放就会推动进度条的变化
        if self.vc_player.duration():
            self.vc_player.setPosition(val)
    
    
    # 播放加载事件 
    def play_handle(self,val):
        if val:
            # 设置进度条的范围
            self.process_sld.setRange(0,val)
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

            # 播放按钮可用
            self.play_btn.setEnabled(True)

            self.vc_player.play()
        pass

    # 进度条   跟随 播放
    # 时间标签 跟随 播放
    def progrcess_change(self,v):
        # 进度条   跟随 播放
        self.process_sld.setValue(v)
        
        # 时间标签 跟随播放
        sec=round(v/1000)#取整
        h,s1=divmod(sec,3600)#求商 余
        m,s=divmod(s1,60)
        
        if m<10 :
            m='0'+str(m)
        if s<10 :
            s='0'+str(s)

        self.left_lb.setText(f'{h}:{m}:{s}')

     # 播放器错误处理 
    # error 事件 会 带有错误类消息 e
    def handle_player_errors(selfd,e):
        # print('456',e)
        # 显示错误提示框
        QMessageBox.critical(self,'错误',f'错误:{e}')
        pass


    # 声音
    # 用滑动条进行音量控制
    @Slot(int)
    def on_vol_sld_valueChanged(self,val):
        # print(val)
        self.vc_player.setVolume(val)
        
    # 静音按钮 mtu_btn
    @Slot()
    def on_vol_btn_clicked(self):
        if self.vc_player.isMuted():
            self.vc_player.setMuted(False)
            self.vol_sld.setValue(10) # 有声音
            self.vol_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        else:
            self.vc_player.setMuted(True)
            self.vol_sld.setValue(0) # 静音
            self.vol_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolumeMuted))

if __name__ == "__main__":
    app=QApplication([])
    media_file=r'F:\sbq\02初中\数学\初中数学朱韬\人教版 初中数学\初一\1. 第01讲 有理数初步（一）.flv'
    wd=MediaPlayerUi()
    wd.load_media_file(media_file)
    wd.show()
    app.exec_()
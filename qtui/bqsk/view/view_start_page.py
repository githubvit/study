from PySide2.QtWidgets import QApplication,QWidget,QMainWindow,QVBoxLayout,QDockWidget,QStyle,QFileDialog
from PySide2.QtCore import Signal,Slot,QEvent,Qt,QUrl
from PySide2.QtGui import QKeySequence
from PySide2.QtMultimedia import QMediaContent,QMediaPlayer

import os,sys

# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_start_page import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
# from core.split_music import split_music

class StartPageUi(QWidget,Ui_Form):
    
    def __init__(self,parent=None):
        # 3 继承父类初始化
        super().__init__(parent) 

        
        # 4 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 图标设定
        self.music_open_btn.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))#更换背景音乐
        self.music_play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) #播放音乐
        self.vol_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        # 定义音乐播放器对象
        self.mc_player=QMediaPlayer()

        # 设定背景音乐声音
        # 设定滑动条的数值范围
    
        self.vol_sld.setRange(0,30)
        val=13
        self.vol_sld.setValue(val)
        self.mc_player.setVolume(val)

        # 设定要播放的内容
        m_file=r'F:\song\study1-纯净.aac'
        mc_file=QMediaContent(QUrl.fromLocalFile(m_file))
        # 交给播放器
        self.mc_player.setMedia(mc_file)

        # 当读到耗时时，会有值,自动播放。
        self.mc_player.durationChanged.connect(self.mc_player_handle)

        # 播放器状态变化
        self.mc_player.stateChanged.connect(self.mc_player_setIcon)

        # 隐藏
        self.music_open_btn.setVisible(False)
        self.music_play_btn.setVisible(False)
        self.vol_btn.setVisible(False)
        self.vol_sld.setVisible(False)
# 
        # 利用leave 和 enter 事件 设置自动隐藏
        self.st_bt_wgt.leaveEvent=self.leave_st_bt_wgt
        self.st_bt_wgt.enterEvent=self.enter_st_bt_wgt

    # 播放按钮 
    @Slot()
    def on_music_play_btn_clicked(self):
        if self.mc_player.state() == QMediaPlayer.PlayingState:
            self.mc_player.pause()
        else:
            self.mc_player.play()
            
    # 响应播放器的状态变化 设置按钮图标
    def mc_player_setIcon(self,state):
        if state == QMediaPlayer.PlayingState:
            self.music_play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.music_play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def mc_player_handle(self,val):
        if val:
            # 播放
            self.mc_player.play()

    # 选择播放的音乐文件 设定要播放的媒体内容
    @Slot()
    def on_music_open_btn_clicked(self):
        # 打开对话框
        m_file=QFileDialog.getOpenFileName(self,'选择音乐文件')[0]
        if m_file != '':
           # 设定要播放的内容
           mc_file=QMediaContent(QUrl.fromLocalFile(m_file))
           # 交给播放器
           self.mc_player.setMedia(mc_file)

    # 用滑动条进行音量控制
    @Slot(int)
    def on_vol_sld_valueChanged(self,val):
        # print(val)
        self.mc_player.setVolume(val)

    # 利用leave 和 enter 事件 设置自动隐藏
    def leave_st_bt_wgt(self,evt):
        # print('离开')
        self.music_open_btn.setVisible(False)
        self.music_play_btn.setVisible(False)
        self.vol_btn.setVisible(False)
        self.vol_sld.setVisible(False)
    def enter_st_bt_wgt(self,evt):
        # print('进入')
        self.music_open_btn.setVisible(True)
        self.music_play_btn.setVisible(True)
        self.vol_btn.setVisible(True)
        self.vol_sld.setVisible(True)


if __name__ == "__main__":
    app=QApplication([]) 
    wd=StartPageUi()
    wd.show()
    app.exec_()
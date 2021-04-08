from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog,QHBoxLayout,QVBoxLayout
from PySide2.QtMultimedia import QMediaContent,QMediaPlayer,QAbstractVideoSurface
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtCore import QUrl,Qt
from PySide2.QtGui import QPalette

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
#     QSlider, QStyle, QSizePolicy, QFileDialog
# import sys
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtGui import QIcon, QPalette
# from PyQt5.QtCore import Qt, QUrl

app=QApplication([])
wd=QWidget()
wd.setGeometry(1000,500,500,400)
wd.setWindowTitle('videoplay')

# 播放视频


# 第一步 创建 video 视频 控件 
vw=QVideoWidget()
# vw.setGeometry(0,0,500,300)

# 设置视频控件的背景为黑
vp=vw.palette()
vp.setColor(QPalette.Window, Qt.black)
vw.setPalette(vp)

# 第二步 显示视频控件
# vw.show() 不用设 


open_btn=QPushButton()
open_btn.setText('打开文件对话框')
open_btn.adjustSize()
# open_btn.move(20,310)   


bt_play=QPushButton()
bt_play.setText('播放')
# bt_play.move(200,310)
bt_play.adjustSize()

bt_pause=QPushButton()
bt_pause.setText('暂停')
# bt_pause.move(280,310)
bt_pause.adjustSize()

bt_stop=QPushButton()
bt_stop.setText('停止')
# bt_stop.move(360,310)
bt_stop.adjustSize()

h_layout=QHBoxLayout()
h_layout.addWidget(open_btn)
h_layout.addWidget(bt_play)
h_layout.addWidget(bt_pause)
h_layout.addWidget(bt_stop)

v_layout=QVBoxLayout(wd)
v_layout.addWidget(vw)
v_layout.addLayout(h_layout)


# 第三步：创建视频播放的QMediaplayer对象；
vc_player=QMediaPlayer(wd,QMediaPlayer.VideoSurface)

# 第四步 将视频输出到视频控件上
vc_player.setVideoOutput(vw)
vc_player.setVolume(10)

# 第五步：设置当前播放的媒体文件；
def get_video():
    v_file=QFileDialog.getOpenFileName(wd,'选择视频文件')[0]
    vc_file=QMediaContent(QUrl.fromLocalFile(v_file))
    vc_player.setMedia(vc_file)

    print('音量',vc_player.volume()) # 默认 100 最大

# 第六步：播放控制。
open_btn.clicked.connect(get_video)
bt_play.clicked.connect(vc_player.play)
bt_pause.clicked.connect(vc_player.pause)
bt_stop.clicked.connect(vc_player.stop)



wd.show()

app.exec_()
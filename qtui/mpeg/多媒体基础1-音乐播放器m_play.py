from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog
from PySide2.QtMultimedia import QMediaContent,QMediaPlayer,QAbstractVideoSurface
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtCore import QUrl

# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# import sys



app=QApplication([])

wd=QWidget()
wd.setGeometry(1000,500,400,80)
wd.setWindowTitle('musicplay')

open_btn=QPushButton(wd)
open_btn.setText('打开文件对话框')
open_btn.adjustSize()
open_btn.move(150,10)   
# open_btn.clicked.connect(self.get_path)

bt_play=QPushButton(wd)
bt_play.setText('播放')
bt_play.move(50,40)
bt_play.adjustSize()

bt_pause=QPushButton(wd)
bt_pause.setText('暂停')
bt_pause.move(150,40)
bt_pause.adjustSize()

bt_stop=QPushButton(wd)
bt_stop.setText('停止')
bt_stop.move(250,40)
bt_stop.adjustSize()


# 播放音乐
# 第一步：创建QMediaplayer对象；
mc_player=QMediaPlayer()
mc_player.setVolume(30)
# 
# 第二步：设置当前播放的媒体文件；
def get_music():
    m_file=QFileDialog.getOpenFileName(wd,'选择音乐文件',r'C:\Users\69598\Downloads\Video','mp3(*.mp3);;aac(*.aac)','mp3(*.mp3)')[0]
    mc_file=QMediaContent(QUrl.fromLocalFile(m_file))
    mc_player.setMedia(mc_file)

    print('音量',mc_player.volume()) # 默认 100 最大
# 第三步：播放。
open_btn.clicked.connect(get_music)
bt_play.clicked.connect(mc_player.play)
bt_pause.clicked.connect(mc_player.pause)
bt_stop.clicked.connect(mc_player.stop)



wd.show()

app.exec_()

# 播放 aac 文件遇到如下错误 
# DirectShowPlayerService::doRender: Unknown error 0x80040266.
# 原因：没有解码插件 
# 解决：
#   下载并安装万能解码器 下载并安装  LAVFilters：https://github.com/Nevcairiel/LAVFilters/releases  ⭐⭐⭐⭐⭐
#   下载了.exe版本，直接按步骤安装，即可，不需要重启电脑。
#   



# 如果文件路径不对的，则会显示如下错误：

# DirectShowPlayerService::doSetUrlSource: Unresolved error code 0x80004005 ()
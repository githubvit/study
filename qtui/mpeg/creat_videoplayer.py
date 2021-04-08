from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
 
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon(r'D:\pyj\st\study\path-to-save.png'))
    
        # 建立控件调色板对象
        p =self.palette() # palette 调色板
        # 设置该对象 （为该对象 相应部分 设置颜色）
        p.setColor(QPalette.Window, Qt.black) # 设置 控件背景 为 黑色
        # p.setColor(QPalette.WindowText, Qt.blue) # 设置 控件字体 为 蓝色
        # p.setColor(QPalette.Button, Qt.green) # 设置 按钮 为 绿色 好像 没有效果
        # p.setColor(QPalette.ButtonText, Qt.blue) # 设置 按钮字体 为 蓝色 有用
        # QPalette.Background 过时 用 QPalette.Window 替代了

        # 将调色板对象赋值给控件
        self.setPalette(p)
 
        self.init_ui()
 
 
        self.show()
 
 
    def init_ui(self):
 
        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
 
        #create videowidget object
        videowidget = QVideoWidget()
 
        #create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)
 
        #create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))#利用标准图标集中的图标
        self.playBtn.clicked.connect(self.play_video)
 
 
 
        #create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
 
 
 
        #create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
 
 
        #create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)
 
        #set widgets to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)
 
 
 
        #create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)
 
 
        self.setLayout(vboxLayout)
 
        self.mediaPlayer.setVideoOutput(videowidget)
 
 
        #media player signals
 
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
 
 
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
 
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
 
 
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
 
        else:
            self.mediaPlayer.play()
 
 
    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)
 
            )
 
        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
 
            )
 
    def position_changed(self, position):
        self.slider.setValue(position)
 
 
    def duration_changed(self, duration):
        self.slider.setRange(0, duration)
 
 
    def set_position(self, position):
        self.mediaPlayer.setPosition(position)
 
 
    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())
 
 
 
 
 
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
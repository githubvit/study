from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog,QMessageBox
from PySide2.QtCore import Signal,Slot,QUrl
from PySide2.QtMultimedia import QMediaContent,QMediaPlayer
import os,sys

from concurrent.futures import ThreadPoolExecutor  # 线程池
from threading import current_thread
import time

# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_bfq1 import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
from core.split_music import split_music

class Bfq1Ui(QWidget,Ui_Form):
    
    def __init__(self,parent=None):
        # 3 继承父类初始化
        super().__init__(parent) 
      
        # 4 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 定义播放器对象
        self.mc_player=QMediaPlayer()

        # 控件
        # 按钮
        # 播放
        self.play_btn.clicked.connect(self.mc_player.play)
        self.pause_btn.clicked.connect(self.mc_player.pause)
        self.stop_btn.clicked.connect(self.mc_player.stop)

        # 刚载入文件是读不到耗时的 duration=0
        # self.mc_player.currentMediaChanged.connect(lambda: print('当前媒体内容变化时',self.mc_player.state(),self.mc_player.duration()))
        # 当读到耗时时，会有值。
        # self.mc_player.durationChanged.connect(lambda v:print('耗时值变化时',self.mc_player.duration(),v))
        self.mc_player.durationChanged.connect(self.duration_val)

        # 播放位置变化时 推动 进度条
        self.mc_player.positionChanged.connect(self.progrcess_val)

        # 播放器错误处理
        self.mc_player.error.connect(self.handle_errors)

        # 音频文件夹 默认值为None
        self.output_dir=None
        # self.open_music_btn
        # self.open_files_btn
        # self.save_files_btn 
        # 滑块
        # self.vol_sld
        # self.h_sld

        # 刚打开时 隐藏进度标签
        self.start_time_lb.hide()
        self.end_time_lb.hide()
    
    # 选择播放的音乐文件 设定要播放的媒体内容
    @Slot()
    def on_open_music_btn_clicked(self):
        # 打开对话框
        self.m_file=QFileDialog.getOpenFileName(self,'选择音乐文件')[0]
        if self.m_file != '':
            # 设定要播放的内容
            mc_file=QMediaContent(QUrl.fromLocalFile(self.m_file))
            
            # 交给播放器
            self.mc_player.setMedia(mc_file)
            # 设置播放控制按钮可用
            self.play_btn.setEnabled(True)
            self.pause_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)
            self.vol_sld.setEnabled(True)
            self.h_sld.setEnabled(True)
            # 音量初始值
            self.start_vol()
            
        else:
            # 设置播放控制按钮不可用
            self.play_btn.setEnabled(False)
            self.pause_btn.setEnabled(False)
            self.stop_btn.setEnabled(False)
            self.vol_sld.setEnabled(False)
            self.h_sld.setEnabled(False)

    # 音量初始值
    def start_vol(self):
        if self.vol_sld.isEnabled:
            # 设定滑动条的数值范围
            self.vol_sld.setRange(0,100)
            val=10
            self.vol_sld.setValue(val)
            self.mc_player.setVolume(val)
    # 用滑动条进行音量控制
    @Slot(int)
    def on_vol_sld_valueChanged(self,val):
        # print(val)
        self.mc_player.setVolume(val)


    # 当读到耗时 时 的动作
    def duration_val(self,val):
        if val:
            # 设置进度条的范围
            self.h_sld.setRange(0,val)
            # 设置时间显示的时分秒
            sec=round(val/1000)#取整
            h,s1=divmod(sec,3600)#求商 余
            m,s=divmod(s1,60)
            
            if m<10 :
                m='0'+str(m)

            if s<10 :
                s='0'+str(s)
            
            # 时间标签可见
            self.end_time_lb.show()
            self.start_time_lb.show()

            self.start_time_lb.setText('0:00:00')
            self.end_time_lb.setText(f'{h}:{m}:{s}')


    # 播放进度条 控制进度 滑动进度条sliderMoved
    @Slot(int)
    def on_h_sld_sliderMoved(self,val):#不要用 on_h_sld_valueChanged 因为 播放就会推动进度条的变化
        if self.mc_player.duration():
            self.mc_player.setPosition(val)
    
    # 进度条   跟随 播放
    # 时间标签 跟随 播放
    def progrcess_val(self,v):
        # 进度条   跟随 播放
        self.h_sld.setValue(v)
        
        # 时间标签 跟随播放
        sec=round(v/1000)#取整
        h,s1=divmod(sec,3600)#求商 余
        m,s=divmod(s1,60)
        
        if m<10 :
            m='0'+str(m)
        if s<10 :
            s='0'+str(s)

        self.start_time_lb.setText(f'{h}:{m}:{s}')
        

    # 播放器错误处理 
    # error 事件 会 带有错误类消息 e
    def handle_errors(self,e):
        # print('456',e)
        # 显示错误提示框
        QMessageBox.critical(self,'错误',f'错误:{e}')
        # 置播放控制按钮不可用
        self.play_btn.setEnabled(False)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.h_sld.setEnabled(False)
        self.vol_sld.setEnabled(False)

    
    # 选择要切割的文件
    @Slot()
    def on_open_files_btn_clicked(self):
        self.file_list=QFileDialog.getOpenFileNames(self,'选择要切割音频的文件')[0]
        # print(self.files)#列表
        if len(self.file_list):
            # 设置保存按钮和切割按钮可用
            self.save_files_btn.setEnabled(True)
            self.split_btn.setEnabled(True)
            self.code_cbx.setEnabled(True)

    # 选择提取的音频保存的文件夹
    @Slot()
    def on_save_files_btn_clicked(self):
        self.output_dir=QFileDialog.getExistingDirectory(self,'选择一个文件夹')
        # print(self.output_dir)
        pass

    # 选择编码器
    # @Slot(str)
    # def on_code_cbx_activated(self,val):
    #     print('编码器',val)
    #     pass

    # 切割音频
    @Slot()
    def on_split_btn_clicked(self):
        # 切割音频
        # 编码器
        code=self.code_cbx.currentText()

        
        try:
            # 多线程操作
            pool=ThreadPoolExecutor(len(self.file_list))#
             
            for item in self.file_list:
            
                pool.submit(split_music,item,code,self.output_dir)

            pool.shutdown()

            QMessageBox.about(self,'提示','提取音频完成')

        except Exception as e:

            # 显示错误提示框
            QMessageBox.critical(self,'错误',f'错误:{e}') 

            print('错误',e)

        # 置文件列表为空 输出目录为None
        self.file_list=[]
        self.output_dir=None
        # 设置保存按钮和切割按钮 不可用
        self.save_files_btn.setEnabled(False)
        self.split_btn.setEnabled(False)
        self.code_cbx.setEnabled(False)
        

if __name__ == "__main__":
    
    app=QApplication([])
    wd=Bfq1Ui()
    wd.show()
    app.exec_()
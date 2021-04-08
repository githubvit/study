'''
简介：
    examples的位置 D:\Anaconda3\Lib\site-packages\PySide2\examples 文件夹下

    俄罗斯方块游戏
        D:\Anaconda3\Lib\site-packages\PySide2\examples\widgets\widgets\tetrix.py


    examples-
        |
        |
        |---3d  qt3D绘图  不用二维QWidget 用3d class Window(Qt3DExtras.Qt3DWindow):
            |
            |        from PySide2.QtCore import(Property, QObject, QPropertyAnimation, Signal)
            |        from PySide2.QtGui import (QGuiApplication, QMatrix4x4, QQuaternion, QVector3D)
            |        from PySide2.Qt3DCore import (Qt3DCore)
            |        from PySide2.Qt3DExtras import (Qt3DExtras)
            |
        |---axcontainer  QtAxContainer的使用 
            |        
            |        是qt用来调用 ActiveX 组件的容器
            |        ActiveX是Microsoft对于一系列策略性面向对象程序技术和工具的称呼，其中主要的技术是组件对象模型（COM）。
            |        在有目录和其它支持的网络中，COM变成了分布式COM（DCOM）。
            |        ActiveX控件是可以在应用程序和网络中计算机上重复使用的程序对象。
            |        创建它的主要技术是Microsoft的ActiveX技术，其中主要是组件对象模型（COM）。
            |        ActiveX 控件是一种可重用的软件组件，通过使用 ActiveX控件，可以很快地在网址、台式应用程序、以及开发工具中加入特殊的功能。
            |        
            |           ActiveX容器是一个可以作为自动化服务器、控件和文档宿主的应用程序
            |       
            |       from PySide2.QtAxContainer import QAxSelect, QAxWidget
            |       from PySide2.QtWidgets import (QAction, QApplication, QDialog,
            |           QMainWindow, QMessageBox, QToolBar)
            |       
        |---callout.py 折线图 /donutbreakdown.py 饼图/legend.py 立柱图/lineandbar.py 折线和立柱/memoryusage.py
            |       /modeldata.py 数据表和折线图/nestedonusts.py 网络饼图/percentbarchart.py 百分比立柱图
            |        前言
            |            继QWT、QCustomPlot绘制折线图之后，在Qt5.7版本后将Qt Charts加入到了Qt模块中。
            |            我们可以方便的使用这个模块，不用学复杂的QWT了。
            |            Qt Charts可以绘制很多样式的图形，比如折线、饼图等，可以根据Qt自带的示例来看，可以帮助更快的做出效果。
            |        简述
            |            用Qt Charts绘制，大概分为四个部分：
            |                数据（QXYSeries）、QChart(不知怎么称呼)、坐标轴（QAbstractAXis）和视图（QChartView）。
            |            
            |            要注意的是:
            |                  QChart要先添加数据（QXYSeries），再加载坐标轴(加载轴的过程是先添加轴到Chart上，
            |               再附加轴到Series上)。这个一定要注意，我之前就是不清楚这部分，然后一直出问题。
            |            
            |            还有一点就是：
            |                  QChartView是继承的是QGraphicsView，QChart继承的是QGraphicsWidget，
            |                所以我们可以用图形视图框架的知识，在其上面进行拓展，Qt自带的项目Callout，我觉得就是很好的示例。
            |
            |          from PySide2.QtCharts import QtCharts
            |
            |
        |---\corelib\threads\mandelbrot.py 曼德布洛特(Mandelbrot)集合  多线程学习
            |                    """PySide2 port of the corelib/threads/mandelbrot example from Qt v5.x, originating from PyQt"""
            |
            |                       from PySide2.QtCore import (Signal, QMutex, QMutexLocker, QPoint, QSize, Qt,
            |                            QThread, QWaitCondition)
            |
            |        \tools\regexp.py  正则表达式
            |                   rx = QtCore.QRegExp(pattern)
            |                
            |              \codecs\dodecs.py 文本转码器
            |                   QtCore.QTextCodec
            |              
            |              \settingseditor\settingseditor.py    设置编辑 比如改注册表 添加环境变量等功能开发
            | 
        |---\multimedia\player.py  多媒体播放器
            |                    from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
            |                    from PySide2.QtMultimediaWidgets import QVideoWidget 
            |
            |            \camera.py  捕捉摄像头
            |                    from PySide2.QtGui import QGuiApplication, QDesktopServices, QIcon
            |                    from PySide2.QtGui import QImage, QPixmap
            |                    from PySide2.QtMultimedia import QCamera, QCameraImageCapture, QCameraInfo
            |                    from PySide2.QtMultimediaWidgets import QCameraViewfinder
            |
            |            \audiooutput.py 捕捉声卡
            |                    from math import pi, sin
            |                    from struct import pack
            |
            |                    from PySide2.QtCore import QByteArray, QIODevice, Qt, QTimer, qWarning
            |                    from PySide2.QtMultimedia import (QAudio, QAudioDeviceInfo, QAudioFormat,
            |                            QAudioOutput)
            |
            |
            |
        |---\tutorial\t1.py~t14.py 教程 从t9 开始看 有 painter绘图 动画 牵扯到坐标的平移变换等手法。
                        t9.py 位置 D:\Anaconda3\Lib\site-packages\PySide2\examples\tutorial\t9.py

                        从t9 到 t14 逐步完成了 炮打砖块 的小游戏。

            |
            |
            |                   
            |
            | 
            |
            |
            |        
            |                       
            |
            |
            |
            |
            |        
            |
            |
            |
            |
        |
        |
        |
        |
        |
        |
        |
         
         
         
         



         
         
         

         
         

         
         
         

        
        |       
        |       
        |       
        |       
        |
        |
        |
        |
        |
        |        
        |        
        |        


















'''
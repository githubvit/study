# 03-QObject
    # 导入的包
    # pyqt5 
    # from PyQt5.Qt import *
    
    # pyside2
    # from PySide2.QtWidgets import *
    # from PySide2.QtCore import * 
    # from PySide2.QtGui import * 

    # 要使用QObject ，必须导入from PySide2.QtCore import *
    # 不然报：NameError: name 'QObject' is not defined
    
    # 1 QObject 继承结构测试
    # pyqt5
        # [<class 'PyQt5.QtCore.QAbstractAnimation'>, <class 'PyQt5.QtCore.QAbstractEventDispatcher'>, <class 'PyQt5.QtCore.QAbstractItemModel'>, <class 'PyQt5.QtCore.QAbstractState'>, <class 'PyQt5.QtCore.QAbstractTransition'>, <class 'PyQt5.QtCore.QIODevice'>, <class 'PyQt5.QtCore.QCoreApplication'>, <class 'PyQt5.QtCore.QEventLoop'>, <class 'PyQt5.QtCore.QFileSelector'>, <class 'PyQt5.QtCore.QFileSystemWatcher'>, <class 'PyQt5.QtCore.QItemSelectionModel'>, <class 'PyQt5.QtCore.QLibrary'>, <class 'PyQt5.QtCore.QMimeData'>, <class 'PyQt5.QtCore.QObjectCleanupHandler'>, <class 'PyQt5.QtCore.QPluginLoader'>, <class 'PyQt5.QtCore.QSettings'>, <class 'PyQt5.QtCore.QSharedMemory'>, <class 'PyQt5.QtCore.QSignalMapper'>, <class 'PyQt5.QtCore.QSocketNotifier'>, <class 'PyQt5.QtCore.QThread'>, <class 'PyQt5.QtCore.QThreadPool'>, <class 'PyQt5.QtCore.QTimeLine'>, <class 'PyQt5.QtCore.QTimer'>, <class 'PyQt5.QtCore.QTranslator'>, <class 'PyQt5.QtCore.QWinEventNotifier'>, <class 'PyQt5.QtNetwork.QAbstractNetworkCache'>, <class 'PyQt5.QtNetwork.QDnsLookup'>, <class 'PyQt5.QtNetwork.QHttpMultiPart'>, <class 'PyQt5.QtNetwork.QLocalServer'>, <class 'PyQt5.QtNetwork.QNetworkAccessManager'>, <class 'PyQt5.QtNetwork.QNetworkConfigurationManager'>, <class 'PyQt5.QtNetwork.QNetworkCookieJar'>, <class 'PyQt5.QtNetwork.QNetworkSession'>, <class 'PyQt5.QtNetwork.QTcpServer'>, <class 'PyQt5.QtGui.QAbstractTextDocumentLayout'>, <class 'PyQt5.QtGui.QClipboard'>, <class 'PyQt5.QtGui.QValidator'>, <class 'PyQt5.QtGui.QDrag'>, <class 'PyQt5.QtGui.QInputMethod'>, <class 'PyQt5.QtGui.QMovie'>, <class 'PyQt5.QtGui.QOffscreenSurface'>, <class 'PyQt5.QtGui.QOpenGLContext'>, <class 'PyQt5.QtGui.QOpenGLContextGroup'>, <class 'PyQt5.QtGui.QOpenGLDebugLogger'>, <class 'PyQt5.QtGui.QOpenGLShader'>, <class 'PyQt5.QtGui.QOpenGLShaderProgram'>, <class 'PyQt5.QtGui.QOpenGLTimeMonitor'>, <class 'PyQt5.QtGui.QOpenGLTimerQuery'>, <class 'PyQt5.QtGui.QOpenGLVertexArrayObject'>, <class 'PyQt5.QtGui.QWindow'>, <class 'PyQt5.QtGui.QPdfWriter'>, <class 'PyQt5.QtGui.QScreen'>, <class 'PyQt5.QtGui.QSessionManager'>, <class 'PyQt5.QtGui.QStyleHints'>, <class 'PyQt5.QtGui.QSyntaxHighlighter'>, <class 'PyQt5.QtGui.QTextObject'>, <class 'PyQt5.QtGui.QTextDocument'>, <class 'PyQt5.QtWidgets.QWidget'>, <class 'PyQt5.QtWidgets.QAbstractItemDelegate'>, <class 'PyQt5.QtWidgets.QAction'>, <class 'PyQt5.QtWidgets.QActionGroup'>, <class 'PyQt5.QtWidgets.QLayout'>, <class 'PyQt5.QtWidgets.QButtonGroup'>, <class 'PyQt5.QtWidgets.QStyle'>, <class 'PyQt5.QtWidgets.QCompleter'>, <class 'PyQt5.QtWidgets.QDataWidgetMapper'>, <class 'PyQt5.QtWidgets.QGesture'>, <class 'PyQt5.QtWidgets.QGraphicsAnchor'>, <class 'PyQt5.QtWidgets.QGraphicsEffect'>, <class 'PyQt5.QtWidgets.QGraphicsObject'>, <class 'PyQt5.QtWidgets.QGraphicsTransform'>, <class 'PyQt5.QtWidgets.QGraphicsScene'>, <class 'PyQt5.QtWidgets.QScroller'>, <class 'PyQt5.QtWidgets.QShortcut'>, <class 'PyQt5.QtWidgets.QSystemTrayIcon'>, <class 'PyQt5.QtWidgets.QUndoGroup'>, <class 'PyQt5.QtWidgets.QUndoStack'>, <class 'PyQt5.QtQml.QJSEngine'>, <class 'PyQt5.QtQml.QQmlComponent'>, <class 'PyQt5.QtQml.QQmlContext'>, <class 'PyQt5.QtQml.QQmlEngineExtensionPlugin'>, <class 'PyQt5.QtQml.QQmlExpression'>, <class 'PyQt5.QtQml.QQmlExtensionPlugin'>, <class 'PyQt5.QtQml.QQmlFileSelector'>, <class 'PyQt5.QtQml.QQmlPropertyMap'>, <class 'PyQt5.QAxContainer.QAxObject'>, <class 'PyQt5.QtBluetooth.QBluetoothDeviceDiscoveryAgent'>, <class 'PyQt5.QtBluetooth.QBluetoothLocalDevice'>, <class 'PyQt5.QtBluetooth.QBluetoothServer'>, <class 'PyQt5.QtBluetooth.QBluetoothServiceDiscoveryAgent'>, <class 'PyQt5.QtBluetooth.QBluetoothTransferManager'>, <class 'PyQt5.QtBluetooth.QBluetoothTransferReply'>, <class 'PyQt5.QtBluetooth.QLowEnergyController'>, <class 'PyQt5.QtBluetooth.QLowEnergyService'>, <class 'PyQt5.QtDBus.QDBusAbstractAdaptor'>, <class 'PyQt5.QtDBus.QDBusAbstractInterface'>, <class 'PyQt5.QtDBus.QDBusPendingCallWatcher'>, <class 'PyQt5.QtDBus.QDBusServiceWatcher'>, <class 'PyQt5.QtDesigner.QDesignerFormEditorInterface'>, <class 'PyQt5.QtDesigner.QDesignerFormWindowManagerInterface'>, <class 'PyQt5.QtDesigner.QExtensionFactory'>, <class 'PyQt5.QtDesigner.QExtensionManager'>, <class 'PyQt5.QtDesigner.QPyDesignerContainerExtension'>, <class 'PyQt5.QtDesigner.QPyDesignerCustomWidgetCollectionPlugin'>, <class 'PyQt5.QtDesigner.QPyDesignerCustomWidgetPlugin'>, <class 'PyQt5.QtDesigner.QPyDesignerMemberSheetExtension'>, <class 'PyQt5.QtDesigner.QPyDesignerPropertySheetExtension'>, <class 'PyQt5.QtDesigner.QPyDesignerTaskMenuExtension'>, <class 'PyQt5.QtHelp.QHelpEngineCore'>, <class 'PyQt5.QtHelp.QHelpFilterEngine'>, <class 'PyQt5.QtHelp.QHelpSearchEngine'>, <class 'PyQt5.QtMultimedia.QAbstractVideoFilter'>, <class 'PyQt5.QtMultimedia.QAbstractVideoSurface'>, <class 'PyQt5.QtMultimedia.QMediaObject'>, <class 'PyQt5.QtMultimedia.QMediaControl'>, <class 'PyQt5.QtMultimedia.QAudioInput'>, <class 'PyQt5.QtMultimedia.QAudioOutput'>, <class 'PyQt5.QtMultimedia.QAudioProbe'>, <class 'PyQt5.QtMultimedia.QMediaRecorder'>, <class 'PyQt5.QtMultimedia.QCameraExposure'>, <class 'PyQt5.QtMultimedia.QCameraFocus'>, <class 'PyQt5.QtMultimedia.QCameraImageCapture'>, <class 'PyQt5.QtMultimedia.QCameraImageProcessing'>, <class 'PyQt5.QtMultimedia.QMediaPlaylist'>, <class 'PyQt5.QtMultimedia.QMediaService'>, <class 'PyQt5.QtMultimedia.QRadioData'>, <class 'PyQt5.QtMultimedia.QSound'>, <class 'PyQt5.QtMultimedia.QSoundEffect'>, <class 'PyQt5.QtMultimedia.QVideoProbe'>, <class 'PyQt5.QtNetworkAuth.QAbstractOAuth'>, <class 'PyQt5.QtNetworkAuth.QAbstractOAuthReplyHandler'>, <class 'PyQt5.QtNfc.QNearFieldManager'>, <class 'PyQt5.QtNfc.QNearFieldShareManager'>, <class 'PyQt5.QtNfc.QNearFieldShareTarget'>, <class 'PyQt5.QtNfc.QNearFieldTarget'>, <class 'PyQt5.QtNfc.QQmlNdefRecord'>, <class 'PyQt5.QtPositioning.QGeoAreaMonitorSource'>, <class 'PyQt5.QtPositioning.QGeoPositionInfoSource'>, <class 'PyQt5.QtPositioning.QGeoSatelliteInfoSource'>, <class 'PyQt5.QtLocation.QGeoCodeReply'>, <class 'PyQt5.QtLocation.QGeoCodingManager'>, <class 'PyQt5.QtLocation.QGeoCodingManagerEngine'>, <class 'PyQt5.QtLocation.QGeoRouteReply'>, <class 'PyQt5.QtLocation.QGeoRoutingManager'>, <class 'PyQt5.QtLocation.QGeoRoutingManagerEngine'>, <class 'PyQt5.QtLocation.QGeoServiceProvider'>, <class 'PyQt5.QtLocation.QPlaceReply'>, <class 'PyQt5.QtLocation.QPlaceManager'>, <class 
        # 'PyQt5.QtLocation.QPlaceManagerEngine'>, <class 'PyQt5.QtQuick.QQuickItem'>, <class 'PyQt5.QtQuick.QQuickImageResponse'>, <class 'PyQt5.QtQuick.QQuickItemGrabResult'>, <class 'PyQt5.QtQuick.QQuickRenderControl'>, <class 'PyQt5.QtQuick.QQuickTextDocument'>, <class 'PyQt5.QtQuick.QQuickTextureFactory'>, <class 'PyQt5.QtQuick.QSGAbstractRenderer'>, <class 'PyQt5.QtQuick.QSGTexture'>, <class 'PyQt5.QtQuick.QSGEngine'>, <class 'PyQt5.QtQuick.QSGTextureProvider'>, <class 'PyQt5.QtQuick3D.QQuick3DObject'>, <class 
        # 'PyQt5.QtRemoteObjects.QRemoteObjectAbstractPersistedStore'>, <class 'PyQt5.QtRemoteObjects.QRemoteObjectReplica'>, <class 'PyQt5.QtRemoteObjects.QRemoteObjectNode'>, <class 'PyQt5.QtSensors.QSensor'>, <class 'PyQt5.QtSensors.QSensorReading'>, <class 'PyQt5.QtSql.QSqlDriver'>, <class 'PyQt5.QtSvg.QSvgRenderer'>, <class 'PyQt5.QtTest.QAbstractItemModelTester'>, <class 'PyQt5.QtTest.QSignalSpy'>, <class 'PyQt5.QtWebChannel.QWebChannel'>, <class 'PyQt5.QtWebChannel.QWebChannelAbstractTransport'>, <class 'PyQt5.QtWebSockets.QMaskGenerator'>, <class 'PyQt5.QtWebSockets.QWebSocket'>, <class 'PyQt5.QtWebSockets.QWebSocketServer'>, <class 'PyQt5.QtWinExtras.QWinJumpList'>, <class 'PyQt5.QtWinExtras.QWinTaskbarButton'>, <class 'PyQt5.QtWinExtras.QWinTaskbarProgress'>, <class 'PyQt5.QtWinExtras.QWinThumbnailToolBar'>, <class 'PyQt5.QtWinExtras.QWinThumbnailToolButton'>, <class 'PyQt5.QtXmlPatterns.QAbstractMessageHandler'>, <class 'PyQt5.QtXmlPatterns.QAbstractUriResolver'>]

        # <class 'PyQt5.QtCore.QObject'>
        # <class 'sip.wrapper'>
        # <class 'sip.simplewrapper'>
        # <class 'object'> 
    # pyside2
        # [<class 'PySide2.QtCore.QTranslator'>, <class 'PySide2.QtCore.QTimer'>, <class 'PySide2.QtCore.QTimeLine'>, <class 'PySide2.QtCore.QThreadPool'>, <class 'PySide2.QtCore.QThread'>, <class 'PySide2.QtCore.QItemSelectionModel'>, <class 'PySide2.QtCore.QIODevice'>, <class 'PySide2.QtCore.QPluginLoader'>, <class 'PySide2.QtCore.QSocketNotifier'>, <class 'PySide2.QtCore.QMimeData'>, <class 'PySide2.QtCore.QSignalMapper'>, <class 'PySide2.QtCore.QWinEventNotifier'>, <class 'PySide2.QtCore.QSettings'>, <class 'PySide2.QtCore.QFileSystemWatcher'>, <class 'PySide2.QtCore.QFileSelector'>, <class 'PySide2.QtCore.QEventLoop'>, <class 'PySide2.QtCore.QCoreApplication'>, <class 'PySide2.QtCore.QAbstractTransition'>, <class 'PySide2.QtCore.QAbstractState'>, <class 'PySide2.QtCore.QAbstractItemModel'>, <class 'PySide2.QtCore.QAbstractEventDispatcher'>, <class 'PySide2.QtCore.QAbstractAnimation'>, <class 'PySide2.QtGui.QOpenGLDebugLogger'>, <class 'PySide2.QtGui.QOpenGLContextGroup'>, <class 'PySide2.QtGui.QOpenGLContext'>, <class 'PySide2.QtGui.QOffscreenSurface'>, <class 'PySide2.QtGui.QSyntaxHighlighter'>, <class 'PySide2.QtGui.QStyleHints'>, <class 'PySide2.QtGui.QAbstractTextDocumentLayout'>, <class 'PySide2.QtGui.QSessionManager'>, <class 'PySide2.QtGui.QScreen'>, <class 
        # 'PySide2.QtGui.QInputMethod'>, <class 'PySide2.QtGui.QPyTextObject'>, <class 'PySide2.QtGui.QWindow'>, <class 'PySide2.QtGui.QPdfWriter'>, <class 'PySide2.QtGui.QValidator'>, <class 'PySide2.QtGui.QTextObject'>, <class 'PySide2.QtGui.QDrag'>, <class 'PySide2.QtGui.QOpenGLVertexArrayObject'>, <class 'PySide2.QtGui.QOpenGLTimerQuery'>, <class 'PySide2.QtGui.QOpenGLTimeMonitor'>, <class 'PySide2.QtGui.QOpenGLShaderProgram'>, <class 'PySide2.QtGui.QOpenGLShader'>, <class 'PySide2.QtGui.QClipboard'>, <class 'PySide2.QtGui.QTextDocument'>, <class 'PySide2.QtGui.QMovie'>, <class 'PySide2.QtWidgets.QLayout'>, <class 'PySide2.QtWidgets.QDataWidgetMapper'>, <class 'PySide2.QtWidgets.QCompleter'>, <class 'PySide2.QtWidgets.QGraphicsTransform'>, <class 'PySide2.QtWidgets.QButtonGroup'>, <class 'PySide2.QtWidgets.QActionGroup'>, <class 'PySide2.QtWidgets.QAction'>, <class 'PySide2.QtWidgets.QAbstractItemDelegate'>, <class 'PySide2.QtWidgets.QStyle'>, <class 'PySide2.QtWidgets.QGraphicsScene'>, <class 'PySide2.QtWidgets.QWidget'>, <class 'PySide2.QtWidgets.QGraphicsObject'>, <class 'PySide2.QtWidgets.QUndoStack'>, <class 'PySide2.QtWidgets.QShortcut'>, <class 'PySide2.QtWidgets.QUndoGroup'>, <class 'PySide2.QtWidgets.QScroller'>, <class 'PySide2.QtWidgets.QGraphicsItemAnimation'>, <class 'PySide2.QtWidgets.QGraphicsEffect'>, <class 'PySide2.QtWidgets.QGraphicsAnchor'>, <class 'PySide2.QtWidgets.QGesture'>, <class 'PySide2.QtWidgets.QSystemTrayIcon'>]

        # <class 'PySide2.QtCore.QObject'>
        # <class 'Shiboken.Object'>
        # <class 'object'>
    
    # 2 QObject 对象名称和属性的操作
    # 应用场景中 对于 .qss样式文件的支持
    # pyqt5支持
    # with open("QObject.qss", "r") as f:
        # qApp.setStyleSheet(f.read())
        # pyside2不支持qApp 

        # self.setStyleSheet(f.read())
        # vscode不识别.qss文件，报错：
            #   FileNotFoundError: [Errno 2] No such file or directory: 'QObject.qss'
        # 解决 使用 vscode 的相对路径或绝对路径即可，右击就可以复制绝对或相对路径
    
    # pyside2要将 qApp 改为 self  
    
    # 3 QObject 对象的父子关系操作
    # 找一个
    # pyqt5 
        # 查找子对象(类型，名称，查找方式（递归查找（默认，会一查到底），只找子对象 Qt.FindDirectChildrenOnly）)
        # print(obj0.findChild(QObject, "3")) #递归查找
        # print(obj0.findChild(QObject, "3", Qt.FindDirectChildrenOnly)) 
    # pyside2 不支持第三个参数 查找方式
    # print(obj0.findChild(QObject, "3")) #递归查找，会在子子孙孙中一查到底
    
    # 4 QObject 信号的操作
        # 返回连接到信号signal的槽slot的数量
        # pyqt5 
        # print(self.obj.receivers(self.obj.objectNameChanged))
        # pyside2 报

# 事件机制
    # 导入的包
    # pyqt5
        # from PyQt5.Qt import *

    # pyside2
        # from PySide2.QtWidgets import *
        # from PySide2.QtCore import *    #QEvent对象
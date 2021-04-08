# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_page.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(706, 542)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 26pt \"\u534e\u6587\u7425\u73c0\";\n"
"background-color: rgb(240, 240, 240);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.st_bt_wgt = QWidget(Form)
        self.st_bt_wgt.setObjectName(u"st_bt_wgt")
        self.st_bt_wgt.setMinimumSize(QSize(0, 23))
        self.st_bt_wgt.setStyleSheet(u"#st_bt_wgt{background-color: rgb(230, 230, 230);}")
        self.horizontalLayout_2 = QHBoxLayout(self.st_bt_wgt)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.music_open_btn = QPushButton(self.st_bt_wgt)
        self.music_open_btn.setObjectName(u"music_open_btn")
        self.music_open_btn.setMinimumSize(QSize(150, 0))
        self.music_open_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.music_open_btn)

        self.horizontalSpacer = QSpacerItem(317, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.vol_btn = QPushButton(self.st_bt_wgt)
        self.vol_btn.setObjectName(u"vol_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vol_btn.sizePolicy().hasHeightForWidth())
        self.vol_btn.setSizePolicy(sizePolicy)
        self.vol_btn.setMinimumSize(QSize(20, 20))
        self.vol_btn.setMaximumSize(QSize(20, 20))
        self.vol_btn.setFlat(True)

        self.horizontalLayout_2.addWidget(self.vol_btn)

        self.vol_sld = QSlider(self.st_bt_wgt)
        self.vol_sld.setObjectName(u"vol_sld")
        sizePolicy.setHeightForWidth(self.vol_sld.sizePolicy().hasHeightForWidth())
        self.vol_sld.setSizePolicy(sizePolicy)
        self.vol_sld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.vol_sld)

        self.music_play_btn = QPushButton(self.st_bt_wgt)
        self.music_play_btn.setObjectName(u"music_play_btn")
        self.music_play_btn.setMinimumSize(QSize(50, 0))
        self.music_play_btn.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.music_play_btn)


        self.verticalLayout.addWidget(self.st_bt_wgt)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u535a\u9a9e\u4e0a\u8bfe", None))
        self.music_open_btn.setText(QCoreApplication.translate("Form", u"\u66f4\u6362\u80cc\u666f\u97f3\u4e50", None))
        self.vol_btn.setText("")
        self.music_play_btn.setText("")
    # retranslateUi


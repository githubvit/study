# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'media_player.ui'
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
        Form.resize(400, 300)
        Form.setMinimumSize(QSize(400, 300))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.video_wgt = QWidget(Form)
        self.video_wgt.setObjectName(u"video_wgt")
        self.video_wgt.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.video_wgt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_lb = QLabel(Form)
        self.left_lb.setObjectName(u"left_lb")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_lb.sizePolicy().hasHeightForWidth())
        self.left_lb.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.left_lb)

        self.right_lb = QLabel(Form)
        self.right_lb.setObjectName(u"right_lb")
        self.right_lb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.right_lb)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.process_sld = QSlider(Form)
        self.process_sld.setObjectName(u"process_sld")
        self.process_sld.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.process_sld)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.play_btn = QPushButton(Form)
        self.play_btn.setObjectName(u"play_btn")

        self.horizontalLayout_2.addWidget(self.play_btn)

        self.vol_btn = QPushButton(Form)
        self.vol_btn.setObjectName(u"vol_btn")

        self.horizontalLayout_2.addWidget(self.vol_btn)

        self.vol_sld = QSlider(Form)
        self.vol_sld.setObjectName(u"vol_sld")
        self.vol_sld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.vol_sld)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.left_lb.setText(QCoreApplication.translate("Form", u"0:00:00", None))
        self.right_lb.setText(QCoreApplication.translate("Form", u"0:00:00", None))
        self.play_btn.setText("")
        self.vol_btn.setText("")
    # retranslateUi


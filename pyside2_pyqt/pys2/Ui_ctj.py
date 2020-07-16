# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ctj.ui'
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


class Ui_ctj(object):
    def setupUi(self, ctj):
        if not ctj.objectName():
            ctj.setObjectName(u"ctj")
        ctj.resize(412, 222)
        self.horizontalLayout = QHBoxLayout(ctj)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(ctj)
        self.left_frame.setObjectName(u"left_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_frame.sizePolicy().hasHeightForWidth())
        self.left_frame.setSizePolicy(sizePolicy)
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_1 = QPushButton(self.left_frame)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.verticalLayout.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.left_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.left_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.left_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)


        self.horizontalLayout.addWidget(self.left_frame)

        self.frame = QFrame(ctj)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mdiArea = QMdiArea(self.frame)
        self.mdiArea.setObjectName(u"mdiArea")

        self.horizontalLayout_2.addWidget(self.mdiArea)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(ctj)

        QMetaObject.connectSlotsByName(ctj)
    # setupUi

    def retranslateUi(self, ctj):
        ctj.setWindowTitle(QCoreApplication.translate("ctj", u"\u9519\u9898\u96c6", None))
        self.pushButton_1.setText(QCoreApplication.translate("ctj", u"\u586b\u5145\u9898\u5e93", None))
        self.pushButton_2.setText(QCoreApplication.translate("ctj", u"\u5237 \u9898", None))
        self.pushButton_3.setText(QCoreApplication.translate("ctj", u"\u5236\u4f5c\u8bd5\u5377", None))
        self.pushButton_4.setText(QCoreApplication.translate("ctj", u"\u5237 \u5377", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.row1_input = QHBoxLayout()
        self.row1_input.setObjectName(u"row1_input")
        self.xinzi = QPlainTextEdit(Form)
        self.xinzi.setObjectName(u"xinzi")

        self.row1_input.addWidget(self.xinzi)


        self.verticalLayout.addLayout(self.row1_input)

        self.row2_stats = QHBoxLayout()
        self.row2_stats.setObjectName(u"row2_stats")
        self.tonji = QPushButton(Form)
        self.tonji.setObjectName(u"tonji")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tonji.sizePolicy().hasHeightForWidth())
        self.tonji.setSizePolicy(sizePolicy)

        self.row2_stats.addWidget(self.tonji)


        self.verticalLayout.addLayout(self.row2_stats)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7edf\u8ba1\u85aa\u8d44", None))
        self.tonji.setText(QCoreApplication.translate("Form", u"\u7edf\u8ba1", None))
    # retranslateUi


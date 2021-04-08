# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdf_reader.ui'
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
        Form.resize(500, 500)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pdf_sca = QScrollArea(Form)
        self.pdf_sca.setObjectName(u"pdf_sca")
        self.pdf_sca.setMinimumSize(QSize(500, 500))
        self.pdf_sca.setWidgetResizable(True)
        self.pdf_wgt = QWidget()
        self.pdf_wgt.setObjectName(u"pdf_wgt")
        self.pdf_wgt.setGeometry(QRect(0, 0, 498, 498))
        self.pdf_sca.setWidget(self.pdf_wgt)

        self.verticalLayout.addWidget(self.pdf_sca)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi


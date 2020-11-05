# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mui.ui'
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
        Form.resize(336, 50)
        Form.setMinimumSize(QSize(300, 50))
        Form.setMaximumSize(QSize(336, 50))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.m_key_btn = QPushButton(Form)
        self.m_key_btn.setObjectName(u"m_key_btn")

        self.horizontalLayout.addWidget(self.m_key_btn)

        self.encrypt_btn = QPushButton(Form)
        self.encrypt_btn.setObjectName(u"encrypt_btn")

        self.horizontalLayout.addWidget(self.encrypt_btn)

        self.decrypt_btn = QPushButton(Form)
        self.decrypt_btn.setObjectName(u"decrypt_btn")

        self.horizontalLayout.addWidget(self.decrypt_btn)

        self.exit_btn = QPushButton(Form)
        self.exit_btn.setObjectName(u"exit_btn")

        self.horizontalLayout.addWidget(self.exit_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u52a0\u89e3\u5bc6", None))
        self.m_key_btn.setText(QCoreApplication.translate("Form", u"\u5236\u4f5c\u5bc6\u94a5", None))
        self.encrypt_btn.setText(QCoreApplication.translate("Form", u"\u52a0\u5bc6", None))
        self.decrypt_btn.setText(QCoreApplication.translate("Form", u"\u89e3\u5bc6", None))
        self.exit_btn.setText(QCoreApplication.translate("Form", u"\u9000\u51fa(&x)", None))
    # retranslateUi


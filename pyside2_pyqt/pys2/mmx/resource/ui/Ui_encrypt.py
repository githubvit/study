# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'encrypt.ui'
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

import mmx_img_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 100)
        Form.setMinimumSize(QSize(300, 100))
        Form.setMaximumSize(QSize(300, 100))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.file_le = QLineEdit(Form)
        self.file_le.setObjectName(u"file_le")

        self.gridLayout.addWidget(self.file_le, 0, 1, 1, 1)

        self.file_btn = QPushButton(Form)
        self.file_btn.setObjectName(u"file_btn")

        self.gridLayout.addWidget(self.file_btn, 0, 2, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.key_le = QLineEdit(Form)
        self.key_le.setObjectName(u"key_le")

        self.gridLayout.addWidget(self.key_le, 1, 1, 1, 1)

        self.key_btn = QPushButton(Form)
        self.key_btn.setObjectName(u"key_btn")

        self.gridLayout.addWidget(self.key_btn, 1, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)

        self.tip_lb = QLabel(Form)
        self.tip_lb.setObjectName(u"tip_lb")

        self.gridLayout_2.addWidget(self.tip_lb, 1, 0, 1, 1)

        self.encrypt_btn = QPushButton(Form)
        self.encrypt_btn.setObjectName(u"encrypt_btn")
        self.encrypt_btn.setEnabled(False)

        self.gridLayout_2.addWidget(self.encrypt_btn, 1, 1, 1, 1)

        self.path_btn = QPushButton(Form)
        self.path_btn.setObjectName(u"path_btn")
        icon = QIcon()
        icon.addFile(u":/btn/resource/img/open folder yellow.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.path_btn.setIcon(icon)

        self.gridLayout_2.addWidget(self.path_btn, 1, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnMinimumWidth(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6587\u4ef6\u52a0\u5bc6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\uff1a", None))
        self.file_btn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u516c\u94a5\uff1a", None))
        self.key_btn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u516c\u94a5", None))
        self.tip_lb.setText(QCoreApplication.translate("Form", u"\u63d0\u793a\u6807\u7b7e", None))
        self.encrypt_btn.setText(QCoreApplication.translate("Form", u"\u52a0\u5bc6", None))
#if QT_CONFIG(tooltip)
        self.path_btn.setToolTip(QCoreApplication.translate("Form", u"\u6253\u5f00\u52a0\u5bc6\u6587\u4ef6\u76ee\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.path_btn.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'm_key.ui'
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
        Form.resize(300, 60)
        Form.setMinimumSize(QSize(300, 60))
        Form.setMaximumSize(QSize(300, 60))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.key_name_le = QLineEdit(Form)
        self.key_name_le.setObjectName(u"key_name_le")

        self.gridLayout.addWidget(self.key_name_le, 1, 1, 1, 1)

        self.tip_lb = QLabel(Form)
        self.tip_lb.setObjectName(u"tip_lb")
        self.tip_lb.setEnabled(True)
        self.tip_lb.setStyleSheet(u"")

        self.gridLayout.addWidget(self.tip_lb, 0, 1, 1, 2)

        self.mkey_btn = QPushButton(Form)
        self.mkey_btn.setObjectName(u"mkey_btn")
        self.mkey_btn.setEnabled(False)

        self.gridLayout.addWidget(self.mkey_btn, 1, 2, 1, 1)

        self.path_btn = QPushButton(Form)
        self.path_btn.setObjectName(u"path_btn")
        icon = QIcon()
        icon.addFile(u":/btn/resource/img/open folder yellow.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.path_btn.setIcon(icon)

        self.gridLayout.addWidget(self.path_btn, 1, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5236\u4f5c\u5bc6\u94a5", None))
        self.key_name_le.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u540d\u79f0", None))
        self.tip_lb.setText(QCoreApplication.translate("Form", u"\u63d0\u793a\u6807\u7b7e", None))
#if QT_CONFIG(tooltip)
        self.mkey_btn.setToolTip(QCoreApplication.translate("Form", u"\u5236\u4f5c\u7684\u5bc6\u94a5\u4ee5\uff1a\n"
"    \u5bc6\u94a5\u540d\u79f0+_public.pem \u751f\u6210\u516c\u94a5\u6587\u4ef6\uff0c\n"
"    \u5bc6\u94a5\u540d\u79f0+_private.pem \u751f\u6210\u79c1\u94a5\u6587\u4ef6\uff0c\n"
"    \u5206\u522b\u653e\u5728\u5bc6\u94a5\u76ee\u5f55\u7684pub\u76ee\u5f55\u548cpri\u76ee\u5f55\u4e2d\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.mkey_btn.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u5bc6\u94a5\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.path_btn.setToolTip(QCoreApplication.translate("Form", u"\u6253\u5f00\u5bc6\u94a5\u76ee\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.path_btn.setText("")
    # retranslateUi


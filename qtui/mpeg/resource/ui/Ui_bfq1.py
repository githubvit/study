# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bfq1.ui'
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
        Form.resize(413, 191)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_music_btn = QPushButton(Form)
        self.open_music_btn.setObjectName(u"open_music_btn")

        self.horizontalLayout.addWidget(self.open_music_btn)

        self.play_btn = QPushButton(Form)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setEnabled(False)

        self.horizontalLayout.addWidget(self.play_btn)

        self.pause_btn = QPushButton(Form)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setEnabled(False)

        self.horizontalLayout.addWidget(self.pause_btn)

        self.stop_btn = QPushButton(Form)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setEnabled(False)

        self.horizontalLayout.addWidget(self.stop_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.start_time_lb = QLabel(Form)
        self.start_time_lb.setObjectName(u"start_time_lb")
        self.start_time_lb.setMinimumSize(QSize(50, 0))
        self.start_time_lb.setMaximumSize(QSize(50, 16777215))
        self.start_time_lb.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_4.addWidget(self.start_time_lb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.end_time_lb = QLabel(Form)
        self.end_time_lb.setObjectName(u"end_time_lb")
        self.end_time_lb.setMinimumSize(QSize(50, 0))
        self.end_time_lb.setMaximumSize(QSize(50, 16777215))
        self.end_time_lb.setStyleSheet(u"background-color: transparent;")
        self.end_time_lb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.end_time_lb)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.h_sld = QSlider(Form)
        self.h_sld.setObjectName(u"h_sld")
        self.h_sld.setEnabled(False)
        self.h_sld.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.h_sld)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.vol_sld = QSlider(Form)
        self.vol_sld.setObjectName(u"vol_sld")
        self.vol_sld.setEnabled(False)
        self.vol_sld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.vol_sld)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.open_files_btn = QPushButton(self.groupBox)
        self.open_files_btn.setObjectName(u"open_files_btn")

        self.horizontalLayout_3.addWidget(self.open_files_btn)

        self.save_files_btn = QPushButton(self.groupBox)
        self.save_files_btn.setObjectName(u"save_files_btn")
        self.save_files_btn.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.save_files_btn)

        self.code_cbx = QComboBox(self.groupBox)
        self.code_cbx.addItem("")
        self.code_cbx.addItem("")
        self.code_cbx.addItem("")
        self.code_cbx.setObjectName(u"code_cbx")
        self.code_cbx.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.code_cbx)

        self.split_btn = QPushButton(self.groupBox)
        self.split_btn.setObjectName(u"split_btn")
        self.split_btn.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.split_btn)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.open_music_btn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.play_btn.setText(QCoreApplication.translate("Form", u"\u64ad\u653e", None))
        self.pause_btn.setText(QCoreApplication.translate("Form", u"\u6682\u505c", None))
        self.stop_btn.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.start_time_lb.setText(QCoreApplication.translate("Form", u"\u6b63\u5411", None))
        self.end_time_lb.setText(QCoreApplication.translate("Form", u"\u6b63\u5411", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5587\u53ed", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u97f3\u9891\u5207\u5272", None))
        self.open_files_btn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u591a\u5a92\u4f53\u6587\u4ef6", None))
        self.save_files_btn.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u4fdd\u5b58\u7684\u6587\u4ef6\u5939", None))
        self.code_cbx.setItemText(0, QCoreApplication.translate("Form", u"copy", None))
        self.code_cbx.setItemText(1, QCoreApplication.translate("Form", u"aac", None))
        self.code_cbx.setItemText(2, QCoreApplication.translate("Form", u"libmp3lame", None))

        self.split_btn.setText(QCoreApplication.translate("Form", u"\u5207\u5272", None))
    # retranslateUi


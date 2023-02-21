# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_popup.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(560, 310)
        Dialog.setMinimumSize(QSize(560, 310))
        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 20, 521, 271))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout.addWidget(self.label_15)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4, 0, Qt.AlignLeft)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(80, 80))
        self.label_10.setMaximumSize(QSize(80, 80))

        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(200, 50))
        font = QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(200, 50))
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1, Qt.AlignRight|Qt.AlignVCenter)

        self.label_14 = QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 1, 1, 1, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"EG", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"ClamNet", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Antivirus", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"2022", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Copyright:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"@ 2022 EG1,  All Rights Reserved", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Website:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"http://eg1.in", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<eg1dotin@gmail.com>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Powered By: ", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"GUI By: ", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi


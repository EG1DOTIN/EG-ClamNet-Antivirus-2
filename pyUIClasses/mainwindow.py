# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 655)
        MainWindow.setMinimumSize(QSize(930, 655))
        MainWindow.setMaximumSize(QSize(930, 655))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 929, 601))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(22)
        self.label_6.setFont(font)

        self.horizontalLayout.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_29 = QLabel(self.verticalLayoutWidget)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout.addWidget(self.label_29)

        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.tabWidget.setFont(font1)
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayoutWidget = QWidget(self.tab_9)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 901, 411))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_22)

        self.groupBox_16 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMinimumSize(QSize(870, 370))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_16)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 10, 851, 391))
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.groupBox_17 = QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.verticalLayoutWidget_13 = QWidget(self.groupBox_17)
        self.verticalLayoutWidget_13.setObjectName(u"verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setGeometry(QRect(10, 10, 401, 331))
        self.verticalLayout_19 = QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_14)

        self.plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_13)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_19.addWidget(self.plainTextEdit)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_12)


        self.horizontalLayout_23.addWidget(self.groupBox_17)

        self.groupBox_18 = QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.verticalLayoutWidget_12 = QWidget(self.groupBox_18)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(10, 10, 401, 331))
        self.verticalLayout_18 = QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_8)

        self.label_9 = QLabel(self.verticalLayoutWidget_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 150))
        self.label_9.setMaximumSize(QSize(150, 150))
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_18.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.verticalLayoutWidget_12)
        self.label_14.setObjectName(u"label_14")
        font2 = QFont()
        font2.setPointSize(8)
        self.label_14.setFont(font2)

        self.verticalLayout_18.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.verticalLayoutWidget_12)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_18.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_9)


        self.horizontalLayout_23.addWidget(self.groupBox_18)


        self.horizontalLayout_3.addWidget(self.groupBox_16)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_21)

        self.tabWidget.addTab(self.tab_9, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayoutWidget_3 = QWidget(self.tab)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 10, 901, 411))
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_24)

        self.groupBox_8 = QGroupBox(self.horizontalLayoutWidget_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(870, 370))
        self.horizontalLayoutWidget_6 = QWidget(self.groupBox_8)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(30, 90, 811, 224))
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_33)

        self.groupBox_12 = QGroupBox(self.horizontalLayoutWidget_6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(200, 200))
        self.groupBox_12.setMaximumSize(QSize(200, 200))
        self.layoutWidget_2 = QWidget(self.groupBox_12)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(8, 10, 181, 181))
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(2, 2, 2, 2)
        self.label_scan_6 = QLabel(self.layoutWidget_2)
        self.label_scan_6.setObjectName(u"label_scan_6")
        self.label_scan_6.setMinimumSize(QSize(100, 100))
        self.label_scan_6.setMaximumSize(QSize(100, 100))

        self.verticalLayout_23.addWidget(self.label_scan_6, 0, Qt.AlignHCenter)

        self.label_scan_7 = QLabel(self.layoutWidget_2)
        self.label_scan_7.setObjectName(u"label_scan_7")

        self.verticalLayout_23.addWidget(self.label_scan_7, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_22.addWidget(self.groupBox_12)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_34)

        self.groupBox_13 = QGroupBox(self.horizontalLayoutWidget_6)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(200, 200))
        self.groupBox_13.setMaximumSize(QSize(200, 200))
        self.layoutWidget_3 = QWidget(self.groupBox_13)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(8, 10, 181, 181))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(2, 2, 2, 2)
        self.label_scan_8 = QLabel(self.layoutWidget_3)
        self.label_scan_8.setObjectName(u"label_scan_8")
        self.label_scan_8.setMinimumSize(QSize(100, 100))
        self.label_scan_8.setMaximumSize(QSize(100, 100))

        self.verticalLayout_24.addWidget(self.label_scan_8, 0, Qt.AlignHCenter)

        self.label_scan_9 = QLabel(self.layoutWidget_3)
        self.label_scan_9.setObjectName(u"label_scan_9")

        self.verticalLayout_24.addWidget(self.label_scan_9, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_22.addWidget(self.groupBox_13)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_35)

        self.groupBox_14 = QGroupBox(self.horizontalLayoutWidget_6)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(200, 200))
        self.groupBox_14.setMaximumSize(QSize(200, 200))
        self.layoutWidget_4 = QWidget(self.groupBox_14)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(7, 10, 181, 181))
        self.verticalLayout_25 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(2, 2, 2, 2)
        self.label_scan_10 = QLabel(self.layoutWidget_4)
        self.label_scan_10.setObjectName(u"label_scan_10")
        self.label_scan_10.setMinimumSize(QSize(100, 100))
        self.label_scan_10.setMaximumSize(QSize(100, 100))

        self.verticalLayout_25.addWidget(self.label_scan_10, 0, Qt.AlignHCenter)

        self.label_scan_11 = QLabel(self.layoutWidget_4)
        self.label_scan_11.setObjectName(u"label_scan_11")

        self.verticalLayout_25.addWidget(self.label_scan_11, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_22.addWidget(self.groupBox_14)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_36)


        self.horizontalLayout_24.addWidget(self.groupBox_8)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_23)

        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayoutWidget_9 = QWidget(self.tab_5)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(20, 30, 881, 371))
        self.verticalLayout_21 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(self.verticalLayoutWidget_9)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayoutWidget_4 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 20, 311, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.checkBox = QCheckBox(self.horizontalLayoutWidget_4)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_4.addWidget(self.checkBox, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_9)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayoutWidget_5 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 20, 327, 51))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.checkBox_2 = QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_5.addWidget(self.checkBox_2, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.groupBox_4 = QGroupBox(self.verticalLayoutWidget_9)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(430, 290))
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 20, 341, 201))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.radioButton = QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_4.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_4.addWidget(self.radioButton_3)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_4.addWidget(self.checkBox_3)


        self.verticalLayout_3.addWidget(self.groupBox_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)


        self.verticalLayout_21.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_20.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_25 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_25)

        self.pushButton_16 = QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_20.addWidget(self.pushButton_16)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_26)

        self.pushButton_17 = QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_20.addWidget(self.pushButton_17)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_27)

        self.pushButton_18 = QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_20.addWidget(self.pushButton_18)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_28)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_11 = QWidget(self.tab_2)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(20, 30, 881, 371))
        self.verticalLayout_22 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget_11)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(430, 110))
        self.groupBox_3.setMaximumSize(QSize(430, 110))
        self.verticalLayoutWidget_6 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 20, 411, 71))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.label_settings_0 = QLabel(self.verticalLayoutWidget_6)
        self.label_settings_0.setObjectName(u"label_settings_0")
        self.label_settings_0.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_settings_0)

        self.spinBox = QSpinBox(self.verticalLayoutWidget_6)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_6.addWidget(self.spinBox)

        self.label_settings_1 = QLabel(self.verticalLayoutWidget_6)
        self.label_settings_1.setObjectName(u"label_settings_1")
        self.label_settings_1.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_settings_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font1)

        self.verticalLayout_6.addWidget(self.checkBox_4)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.verticalLayoutWidget_11)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(432, 150))
        self.verticalLayoutWidget_7 = QWidget(self.groupBox_5)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 20, 411, 161))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font1)

        self.verticalLayout_7.addWidget(self.checkBox_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.label_settings_2 = QLabel(self.verticalLayoutWidget_7)
        self.label_settings_2.setObjectName(u"label_settings_2")
        self.label_settings_2.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_settings_2)

        self.spinBox_2 = QSpinBox(self.verticalLayoutWidget_7)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_8.addWidget(self.spinBox_2)

        self.label_settings_3 = QLabel(self.verticalLayoutWidget_7)
        self.label_settings_3.setObjectName(u"label_settings_3")
        self.label_settings_3.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_settings_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.label_settings_4 = QLabel(self.verticalLayoutWidget_7)
        self.label_settings_4.setObjectName(u"label_settings_4")
        self.label_settings_4.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_settings_4)

        self.spinBox_3 = QSpinBox(self.verticalLayoutWidget_7)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_9.addWidget(self.spinBox_3)

        self.label_settings_5 = QLabel(self.verticalLayoutWidget_7)
        self.label_settings_5.setObjectName(u"label_settings_5")
        self.label_settings_5.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_settings_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.label_settings_6 = QLabel(self.verticalLayoutWidget_7)
        self.label_settings_6.setObjectName(u"label_settings_6")
        self.label_settings_6.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_settings_6)

        self.spinBox_4 = QSpinBox(self.verticalLayoutWidget_7)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.horizontalLayout_11.addWidget(self.spinBox_4)

        self.label_settings_7 = QLabel(self.verticalLayoutWidget_7)
        self.label_settings_7.setObjectName(u"label_settings_7")
        self.label_settings_7.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_settings_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.groupBox_5)


        self.horizontalLayout_10.addLayout(self.verticalLayout_5)

        self.groupBox_6 = QGroupBox(self.verticalLayoutWidget_11)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(430, 308))
        self.verticalLayoutWidget_8 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 20, 411, 281))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.label_settings_8 = QLabel(self.verticalLayoutWidget_8)
        self.label_settings_8.setObjectName(u"label_settings_8")
        self.label_settings_8.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_settings_8, 0, Qt.AlignLeft)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.label_settings_9 = QLabel(self.verticalLayoutWidget_8)
        self.label_settings_9.setObjectName(u"label_settings_9")
        self.label_settings_9.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_settings_9, 0, Qt.AlignLeft)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)

        self.listWidget = QListWidget(self.verticalLayoutWidget_8)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(80, 150))
        self.listWidget.setMaximumSize(QSize(80, 150))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.listWidget.setFont(font3)

        self.horizontalLayout_13.addWidget(self.listWidget)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.pushButton = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font3)

        self.verticalLayout_9.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font3)

        self.verticalLayout_9.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font3)

        self.verticalLayout_9.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font3)

        self.verticalLayout_9.addWidget(self.pushButton_4)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)


        self.verticalLayout_11.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_12.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.label_settings_10 = QLabel(self.verticalLayoutWidget_8)
        self.label_settings_10.setObjectName(u"label_settings_10")
        self.label_settings_10.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_settings_10, 0, Qt.AlignLeft)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)

        self.listWidget_2 = QListWidget(self.verticalLayoutWidget_8)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setMinimumSize(QSize(80, 150))
        self.listWidget_2.setMaximumSize(QSize(80, 150))
        self.listWidget_2.setFont(font3)

        self.horizontalLayout_14.addWidget(self.listWidget_2)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_19)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.pushButton_5 = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_10.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_10.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_10.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_10.addWidget(self.pushButton_8)


        self.horizontalLayout_14.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_20)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_10.addWidget(self.groupBox_6)


        self.verticalLayout_22.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_29 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_29)

        self.pushButton_19 = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_21.addWidget(self.pushButton_19)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_30)

        self.pushButton_20 = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_21.addWidget(self.pushButton_20)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_31)

        self.pushButton_21 = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_21.addWidget(self.pushButton_21)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_32)


        self.verticalLayout_22.addLayout(self.horizontalLayout_21)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayoutWidget_7 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 10, 901, 411))
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_38)

        self.groupBox_11 = QGroupBox(self.horizontalLayoutWidget_7)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(870, 370))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_11)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 30, 851, 351))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.checkBox_cleaner_6 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_cleaner_6.setObjectName(u"checkBox_cleaner_6")

        self.gridLayout.addWidget(self.checkBox_cleaner_6, 7, 2, 1, 1)

        self.label_cleaner_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_6.setObjectName(u"label_cleaner_6")

        self.gridLayout.addWidget(self.label_cleaner_6, 4, 0, 1, 1)

        self.checkBox_cleaner_4 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_cleaner_4.setObjectName(u"checkBox_cleaner_4")

        self.gridLayout.addWidget(self.checkBox_cleaner_4, 5, 2, 1, 1)

        self.checkBox_cleaner_2 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_cleaner_2.setObjectName(u"checkBox_cleaner_2")

        self.gridLayout.addWidget(self.checkBox_cleaner_2, 3, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 11, 0, 1, 1)

        self.label_cleaner_14 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_14.setObjectName(u"label_cleaner_14")

        self.gridLayout.addWidget(self.label_cleaner_14, 4, 1, 1, 1)

        self.label_cleaner_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_13.setObjectName(u"label_cleaner_13")

        self.gridLayout.addWidget(self.label_cleaner_13, 3, 1, 1, 1)

        self.label_cleaner_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_2.setObjectName(u"label_cleaner_2")

        self.gridLayout.addWidget(self.label_cleaner_2, 1, 1, 1, 1)

        self.checkBox_cleaner_3 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_cleaner_3.setObjectName(u"checkBox_cleaner_3")

        self.gridLayout.addWidget(self.checkBox_cleaner_3, 4, 2, 1, 1)

        self.checkBox_cleaner_7 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_cleaner_7.setObjectName(u"checkBox_cleaner_7")

        self.gridLayout.addWidget(self.checkBox_cleaner_7, 8, 2, 1, 1)

        self.label_cleaner_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_8.setObjectName(u"label_cleaner_8")

        self.gridLayout.addWidget(self.label_cleaner_8, 6, 0, 1, 1)

        self.label_cleaner_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_12.setObjectName(u"label_cleaner_12")

        self.gridLayout.addWidget(self.label_cleaner_12, 2, 1, 1, 1)

        self.label_cleaner_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_9.setObjectName(u"label_cleaner_9")

        self.gridLayout.addWidget(self.label_cleaner_9, 7, 0, 1, 1)

        self.label_cleaner_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_4.setObjectName(u"label_cleaner_4")

        self.gridLayout.addWidget(self.label_cleaner_4, 2, 0, 1, 1)

        self.label_cleaner_1 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_1.setObjectName(u"label_cleaner_1")

        self.gridLayout.addWidget(self.label_cleaner_1, 1, 0, 1, 1)

        self.label_cleaner_18 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_18.setObjectName(u"label_cleaner_18")

        self.gridLayout.addWidget(self.label_cleaner_18, 8, 1, 1, 1)

        self.label_cleaner_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_10.setObjectName(u"label_cleaner_10")

        self.gridLayout.addWidget(self.label_cleaner_10, 8, 0, 1, 1)

        self.checkBox_cleaner_1 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_cleaner_1.setObjectName(u"checkBox_cleaner_1")

        self.gridLayout.addWidget(self.checkBox_cleaner_1, 2, 2, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_5)

        self.pushButton_9 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_18.addWidget(self.pushButton_9)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_18, 11, 1, 1, 1)

        self.label_cleaner_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_15.setObjectName(u"label_cleaner_15")

        self.gridLayout.addWidget(self.label_cleaner_15, 5, 1, 1, 1)

        self.label_cleaner_19 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_19.setObjectName(u"label_cleaner_19")

        self.gridLayout.addWidget(self.label_cleaner_19, 9, 1, 1, 1)

        self.checkBox_cleaner_5 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_cleaner_5.setObjectName(u"checkBox_cleaner_5")

        self.gridLayout.addWidget(self.checkBox_cleaner_5, 6, 2, 1, 1)

        self.label_cleaner_11 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_11.setObjectName(u"label_cleaner_11")

        self.gridLayout.addWidget(self.label_cleaner_11, 9, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 12, 1, 1, 1)

        self.label_cleaner_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_5.setObjectName(u"label_cleaner_5")

        self.gridLayout.addWidget(self.label_cleaner_5, 3, 0, 1, 1)

        self.label_cleaner_17 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_17.setObjectName(u"label_cleaner_17")

        self.gridLayout.addWidget(self.label_cleaner_17, 7, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.label_cleaner_16 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_16.setObjectName(u"label_cleaner_16")

        self.gridLayout.addWidget(self.label_cleaner_16, 6, 1, 1, 1)

        self.checkBox_cleaner_8 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_cleaner_8.setObjectName(u"checkBox_cleaner_8")

        self.gridLayout.addWidget(self.checkBox_cleaner_8, 9, 2, 1, 1)

        self.label_cleaner_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_3.setObjectName(u"label_cleaner_3")

        self.gridLayout.addWidget(self.label_cleaner_3, 1, 2, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)

        self.pushButton_10 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_19.addWidget(self.pushButton_10)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_9)


        self.gridLayout.addLayout(self.horizontalLayout_19, 11, 2, 1, 1)

        self.label_cleaner_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_cleaner_7.setObjectName(u"label_cleaner_7")

        self.gridLayout.addWidget(self.label_cleaner_7, 5, 0, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout)


        self.horizontalLayout_25.addWidget(self.groupBox_11)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_37)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayoutWidget_8 = QWidget(self.tab_6)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 10, 901, 411))
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_40)

        self.groupBox_10 = QGroupBox(self.horizontalLayoutWidget_8)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(870, 370))
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_10)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 30, 851, 351))
        self.verticalLayout_14 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.tableWidget_3 = QTableWidget(self.verticalLayoutWidget_3)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_14.addWidget(self.tableWidget_3)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_15.addWidget(self.pushButton_12)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_10)

        self.pushButton_11 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_15.addWidget(self.pushButton_11)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_11)

        self.pushButton_13 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_15.addWidget(self.pushButton_13)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_12)

        self.pushButton_14 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_15.addWidget(self.pushButton_14)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_13)


        self.verticalLayout_14.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_26.addWidget(self.groupBox_10)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_39)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayoutWidget_9 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 10, 901, 411))
        self.horizontalLayout_27 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_42)

        self.groupBox_7 = QGroupBox(self.horizontalLayoutWidget_9)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(870, 370))
        self.verticalLayoutWidget_10 = QWidget(self.groupBox_7)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 30, 851, 361))
        self.verticalLayout_17 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.label_28 = QLabel(self.verticalLayoutWidget_10)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_16.addWidget(self.label_28)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_10)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_16.addWidget(self.lineEdit)


        self.verticalLayout_17.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)

        self.textEdit_2 = QTextEdit(self.verticalLayoutWidget_10)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(845, 180))

        self.verticalLayout_17.addWidget(self.textEdit_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_6)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_2)

        self.pushButton_15 = QPushButton(self.verticalLayoutWidget_10)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_17.addWidget(self.pushButton_15)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)


        self.verticalLayout_17.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_7)


        self.horizontalLayout_27.addWidget(self.groupBox_7)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_41)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayoutWidget_10 = QWidget(self.tab_7)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(10, 10, 901, 411))
        self.horizontalLayout_28 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_44)

        self.groupBox_9 = QGroupBox(self.horizontalLayoutWidget_10)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(870, 370))
        self.verticalLayoutWidget_5 = QWidget(self.groupBox_9)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 851, 391))
        self.verticalLayout_15 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.commandLinkButton_3 = QCommandLinkButton(self.verticalLayoutWidget_5)
        self.commandLinkButton_3.setObjectName(u"commandLinkButton_3")

        self.verticalLayout_15.addWidget(self.commandLinkButton_3)

        self.commandLinkButton_2 = QCommandLinkButton(self.verticalLayoutWidget_5)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")

        self.verticalLayout_15.addWidget(self.commandLinkButton_2)

        self.commandLinkButton = QCommandLinkButton(self.verticalLayoutWidget_5)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.verticalLayout_15.addWidget(self.commandLinkButton)

        self.commandLinkButton_4 = QCommandLinkButton(self.verticalLayoutWidget_5)
        self.commandLinkButton_4.setObjectName(u"commandLinkButton_4")

        self.verticalLayout_15.addWidget(self.commandLinkButton_4)


        self.horizontalLayout_28.addWidget(self.groupBox_9)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_43)

        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_social_media_0 = QLabel(self.verticalLayoutWidget)
        self.label_social_media_0.setObjectName(u"label_social_media_0")

        self.horizontalLayout_2.addWidget(self.label_social_media_0)

        self.label_social_media_1 = QLabel(self.verticalLayoutWidget)
        self.label_social_media_1.setObjectName(u"label_social_media_1")

        self.horizontalLayout_2.addWidget(self.label_social_media_1)

        self.label_social_media_2 = QLabel(self.verticalLayoutWidget)
        self.label_social_media_2.setObjectName(u"label_social_media_2")

        self.horizontalLayout_2.addWidget(self.label_social_media_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        # MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QMenuBar(MainWindow)
        # self.menubar.setObjectName(u"menubar")
        # self.menubar.setGeometry(QRect(0, 0, 930, 26))
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName(u"statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EG Antivirus", None))
        self.label_3.setText("")
        self.label_6.setText("")
        self.label_29.setText("")
        self.groupBox_16.setTitle("")
        self.groupBox_17.setTitle("")
        self.groupBox_18.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"StatusImage", None))
        self.label_14.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"StatusText", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Status", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Select Scan Type", None))
        self.groupBox_12.setTitle("")
        self.label_scan_6.setText(QCoreApplication.translate("MainWindow", u"Custom Scan Label", None))
        self.label_scan_7.setText(QCoreApplication.translate("MainWindow", u"\n"
"Custom Scan", None))
        self.groupBox_13.setTitle("")
        self.label_scan_8.setText(QCoreApplication.translate("MainWindow", u"Quick Scan Label", None))
        self.label_scan_9.setText(QCoreApplication.translate("MainWindow", u"\n"
"Quick Scan", None))
        self.groupBox_14.setTitle("")
        self.label_scan_10.setText(QCoreApplication.translate("MainWindow", u"Full Scan Label", None))
        self.label_scan_11.setText(QCoreApplication.translate("MainWindow", u"\n"
"Full Scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Scan", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Real-Time Protection", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Real-Time Protection ON / OFF", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Updates", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Automatic Updates On/Off", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Infected Files", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Report Only", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Remove (Use Carefully)", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Move To Quarantine Folder", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"All Files", None))
        self.label_settings_0.setText(QCoreApplication.translate("MainWindow", u"Do Not Scan Files Larger Than", None))
        self.label_settings_1.setText(QCoreApplication.translate("MainWindow", u"MB", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Do Not Reload Virus Signature DB ( Fast Scan )", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Archive Files", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Extract Files From Archives", None))
        self.label_settings_2.setText(QCoreApplication.translate("MainWindow", u"Do Not Extract More Than", None))
        self.label_settings_3.setText(QCoreApplication.translate("MainWindow", u"MB", None))
        self.label_settings_4.setText(QCoreApplication.translate("MainWindow", u"Do Not Extract More Than", None))
        self.label_settings_5.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.label_settings_6.setText(QCoreApplication.translate("MainWindow", u"Do Not Extract More Than", None))
        self.label_settings_7.setText(QCoreApplication.translate("MainWindow", u"Sub Archives", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.label_settings_8.setText(QCoreApplication.translate("MainWindow", u"Add file extension to include and/or exclude in scan", None))
        self.label_settings_9.setText(QCoreApplication.translate("MainWindow", u"Exclude extension", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_settings_10.setText(QCoreApplication.translate("MainWindow", u"Scan only extension", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.groupBox_11.setTitle("")
        self.checkBox_cleaner_6.setText("")
        self.label_cleaner_6.setText(QCoreApplication.translate("MainWindow", u"Cookies", None))
        self.checkBox_cleaner_4.setText("")
        self.checkBox_cleaner_2.setText("")
        self.label_cleaner_14.setText("")
        self.label_cleaner_13.setText("")
        self.label_cleaner_2.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.checkBox_cleaner_3.setText("")
        self.checkBox_cleaner_7.setText("")
        self.label_cleaner_8.setText(QCoreApplication.translate("MainWindow", u"Recycle Bin Contents", None))
        self.label_cleaner_12.setText("")
        self.label_cleaner_9.setText(QCoreApplication.translate("MainWindow", u"AddressBar History", None))
        self.label_cleaner_4.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.label_cleaner_1.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.label_cleaner_18.setText("")
        self.label_cleaner_10.setText(QCoreApplication.translate("MainWindow", u"Recent Docs History", None))
        self.checkBox_cleaner_1.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label_cleaner_15.setText("")
        self.label_cleaner_19.setText("")
        self.checkBox_cleaner_5.setText("")
        self.label_cleaner_11.setText(QCoreApplication.translate("MainWindow", u"Run History", None))
        self.label_cleaner_5.setText(QCoreApplication.translate("MainWindow", u"Temporary Files/Folders", None))
        self.label_cleaner_17.setText("")
        self.label_cleaner_16.setText("")
        self.checkBox_cleaner_8.setText("")
        self.label_cleaner_3.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
        self.label_cleaner_7.setText(QCoreApplication.translate("MainWindow", u"Browser's Cache And History", None))
        self.label_4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Cleaner", None))
        self.groupBox_10.setTitle("")
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Detected Item", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Action Taken", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Found At Location", None));
        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Current Location", None));
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Clear List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Quarantine", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Any Message? ", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Email Address:-", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Support", None))
        self.groupBox_9.setTitle("")
        self.commandLinkButton_3.setText(QCoreApplication.translate("MainWindow", u"About US", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"About EG Antivirus", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Rate EG Antivirus", None))
        self.commandLinkButton_4.setText(QCoreApplication.translate("MainWindow", u"Please Donate... ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"About", None))
        self.label_social_media_0.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.label_social_media_1.setText(QCoreApplication.translate("MainWindow", u"Twitter", None))
        self.label_social_media_2.setText(QCoreApplication.translate("MainWindow", u"Instagram", None))
        self.label.setText("")
    # retranslateUi


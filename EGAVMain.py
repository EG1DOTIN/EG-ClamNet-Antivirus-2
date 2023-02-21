"""
EGAVMain.py :=> This is the main UI file of EG ClamNet Antivirus
"""

import os
import sys
import time
from json import load as load_json_file, dumps as json_dumps
from platform import system as system_info, release as release_info
from platform import version as version_info, processor as processor_info
from shutil import move as move_file
from webbrowser import open as open_browser

from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QFileDialog
from psutil import virtual_memory as psutil_virtual_memory

from EGAVMsgNPopup import EGAVInfoPopup, EGAVInputPopup, EGAVMessageYN, EGAVMessage
from EGAVResources import EGAVResources, EGAVPaths, EGAVTheme, EGAVStatus, QuickScanPaths
from EGAVScanner import EGAVScanner, ScanType
from EGAVTitleBar import EGAVTitleBar
from config import EGAVLinks, DEBUG_CODE
from custom import email_valid
from custom import get_total_number_of_files, OS, str_list_separation, DiskDrives
from custom import print_v1, get_files_list_from_folder, paths_correction, check_service
from customQt import QtFileDialog, str_item_list_from_listWidget, tableWidget_stretch_header_to_contents
from customQt import QuarantineTableWidgetItemColor, set_foreground_color_toRow_in_tableWidget, set_hand_mouse_pointer
from pyUIClasses.mainwindow import Ui_MainWindow
from singleObj import clamav_commands, clamav_service


def check_egav_installation():
    if not EGAVPaths.getInstalled()['status']:
        msg = EGAVMessageYN(messageText="EGAV is not installed. Would you proceed to install?")
        msg.setModal(True)
        msg.exec()
        if msg.bAccepted == 0 or msg.bAccepted == -1:
            exit(0)
        elif msg.bAccepted == 1:
            # execute SetupEGAV.exe file
            EGAVPaths.execute_file("SetupEGAV")
            exit(0)


def send_support_message(email, msg):
    try:
        from apis import send_message_egav2
        send_message_egav2(email=email, msg=msg)
        success = 1
    except Exception as e:
        print_v1("Error: " + str(e))
        success = 0
    return success


class Main_Window_TAB:
    STATUS = "Status"
    SCAN = "Scan"
    PREFERENCES = "Preferences"
    SETTINGS = "Settings"
    QUARANTINE = "Quarantine"
    SUPPORT = "Support"
    ABOUT = "About"


class EGAVMainWindow(QtWidgets.QWidget):

    def __init__(self):
        # ----------------------------------------------------------- #
        # call base class
        super(EGAVMainWindow, self).__init__()

        if not DEBUG_CODE:
            check_egav_installation()

        # define data
        self.os = OS.get_os_details()
        self.layout = QtWidgets.QVBoxLayout()
        self.title_bar = EGAVTitleBar(self)
        self.__flagPreferencesApply = False
        self.__flagSettingsApply = False
        self.dbObj = clamav_commands.egav_db
        self.status = None
        self.ui = Ui_MainWindow()

        # setup now
        self.setupUi()
        self.resetUi()
        self.setEvents()
        self.initialize()

        # show now
        self.show()  # self.setTrayIcon
        # ----------------------------------------------------------- #

    def applyDatabaseToTabPreferences(self, dbObj_Dict):
        self.ui.checkBox.setCheckState(QtCore.Qt.CheckState.Checked \
                                           if dbObj_Dict["preferences"]["RealTimeProtectionOnOff"] \
                                           else QtCore.Qt.CheckState.Unchecked)
        self.ui.checkBox_2.setCheckState(QtCore.Qt.CheckState.Checked \
                                             if dbObj_Dict["preferences"]["AutomaticUpdatesOnOff"] \
                                             else QtCore.Qt.CheckState.Unchecked)
        self.ui.checkBox_3.setCheckState(QtCore.Qt.CheckState.Checked \
                                             if dbObj_Dict["preferences"]["InfectedFilesNotifications"] \
                                             else QtCore.Qt.CheckState.Unchecked)

        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)

        if dbObj_Dict["preferences"]["InfectedFilesRadioButton"] == 1:
            self.ui.radioButton.setChecked(True)
        elif dbObj_Dict["preferences"]["InfectedFilesRadioButton"] == 2:
            self.ui.radioButton_2.setChecked(True)
        elif dbObj_Dict["preferences"]["InfectedFilesRadioButton"] == 3:
            self.ui.radioButton_3.setChecked(True)

    def applyDatabaseToTabSettings(self, dbObj_Dict):
        self.ui.spinBox.setValue(dbObj_Dict["settings"]["DoNotScanFilesLargerThanMB"])
        self.ui.checkBox_4.setCheckState(QtCore.Qt.CheckState.Checked \
                                             if dbObj_Dict["settings"]["DoNotReloadVirusSignatureDB"] \
                                             else QtCore.Qt.CheckState.Unchecked)
        self.ui.checkBox_5.setCheckState(QtCore.Qt.CheckState.Checked \
                                             if dbObj_Dict["settings"]["ExtractFilesFromArchives"] \
                                             else QtCore.Qt.CheckState.Unchecked)
        self.ui.spinBox_2.setValue(dbObj_Dict["settings"]["DoNotExtractMoreThanMB"])
        self.ui.spinBox_3.setValue(dbObj_Dict["settings"]["DoNotExtractMoreThanFiles"])
        self.ui.spinBox_4.setValue(dbObj_Dict["settings"]["DoNotExtractMoreThanSubArchives"])

        # first clear list
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        # now add items
        self.ui.listWidget.addItems(dbObj_Dict["ExcludeExtension"])
        self.ui.listWidget_2.addItems(dbObj_Dict["ScanOnlyExtension"])

    def preferencesUI_ToDB(self):
        self.dbObj.Preference_RealTimeProtectionOnOff = 1 if self.ui.checkBox.isChecked() else 0
        self.dbObj.Preferences_AutomaticUpdatesOnOff = 1 if self.ui.checkBox_2.isChecked() else 0
        if self.ui.radioButton.isChecked():
            radioButtonSelected = 1
        elif self.ui.radioButton.isChecked():
            radioButtonSelected = 2
        else:
            radioButtonSelected = 3
        self.dbObj.Preferences_InfectedFilesRadioButton = radioButtonSelected
        self.dbObj.Preferences_InfectedFilesNotifications = 1 if self.ui.checkBox_3.isChecked() else 0

    def settingsUI_ToDB(self):
        self.dbObj.Settings_DoNotScanFilesLargerThanMB = self.ui.spinBox.value()
        self.dbObj.Settings_DoNotReloadVirusSignatureDB = 1 if self.ui.checkBox_4.isChecked() else 0
        self.dbObj.Settings_ExtractFilesFromArchives = 1 if self.ui.checkBox_5.isChecked() else 0
        self.dbObj.Settings_DoNotExtractMoreThanMB = self.ui.spinBox_2.value()
        self.dbObj.Settings_DoNotExtractMoreThanFiles = self.ui.spinBox_3.value()
        self.dbObj.Settings_DoNotExtractMoreThanSubArchives = self.ui.spinBox_4.value()
        self.dbObj.Settings_ExcludeExtension = str_item_list_from_listWidget(self.ui.listWidget)
        self.dbObj.Settings_ScanOnlyExtension = str_item_list_from_listWidget(self.ui.listWidget_2)

    def applyDatabaseToUI(self):
        self.applyDatabaseToTabPreferences(dbObj_Dict=self.dbObj.toDict())
        self.applyDatabaseToTabSettings(dbObj_Dict=self.dbObj.toDict())

    def setTrayIcon(self):
        menu = QMenu()
        settingAction = menu.addAction("setting")
        settingAction.triggered.connect(self.setting)
        exitAction = menu.addAction("exit")
        exitAction.triggered.connect(sys.exit)

        icon = QIcon(r"E:\ALL\CODE\PYTHON\pyEGAV\Resources\egav.ico")
        print_v1(os.getcwd() + EGAVPaths.Resources.EGAV_TRAY_ICON)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.show()
        self.tray.setToolTip("unko!")
        self.tray.showMessage("hoge", "moge")
        # self.tray.showMessage("fuga", "moge")
        self.tray.activated.connect(self.onTrayIconClick)
        self.show()

    def closeEvent(self, event):
        # self.hide()
        # event.ignore()
        pass

    def setting(self, event):
        print_v1("settings tray clicked")
        pass

    def onTrayIconClick(self, event):
        if event == QSystemTrayIcon.DoubleClick:
            self.show()

    def setFlagPreferences(self, bFlag):
        if bFlag:
            if not self.__flagPreferencesApply:
                self.__flagPreferencesApply = True
                self.ui.pushButton_18.setEnabled(True)
        else:
            if self.__flagPreferencesApply:
                self.__flagPreferencesApply = False
                self.ui.pushButton_18.setEnabled(False)

    def setFlagSettings(self, bFlag):
        if bFlag:
            if not self.__flagSettingsApply:
                self.__flagSettingsApply = True
                self.ui.pushButton_21.setEnabled(True)
        else:
            if self.__flagSettingsApply:
                self.__flagSettingsApply = False
                self.ui.pushButton_21.setEnabled(False)

    def setupUi(self):
        self.ui.setupUi(self)

    def resetUi(self):
        self.setUi_TitleBar()
        self.setUI_MainWindow()
        self.setUI_TabStatus()
        self.setUI_TabScan()
        self.setUI_TabPreferences()
        self.setUI_TabSettings()
        self.setUI_TabCleaner()
        self.setUI_TabQuarantine()
        self.setUI_TabSupport()
        self.setUI_TabAbout()

    def setUi_TitleBar(self):
        # adding title bar
        self.layout.addWidget(self.title_bar)
        self.layout.addWidget(self.ui.centralwidget)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title_bar.setFixedWidth(self.width())

    def setUI_MainWindow(self):
        self.setStyleSheet(EGAVTheme.MainWindow.style_mainWidget)
        self.ui.label_social_media_0.setStyleSheet(EGAVTheme.MainWindow.style_label_link_facebook)
        self.ui.label_social_media_1.setStyleSheet(EGAVTheme.MainWindow.style_label_link_twitter)
        self.ui.label_social_media_2.setStyleSheet(EGAVTheme.MainWindow.style_label_link_instagram)
        self.ui.label_social_media_0.setMaximumSize(EGAVTheme.MainWindow.size_social_media_link)
        self.ui.label_social_media_1.setMaximumSize(EGAVTheme.MainWindow.size_social_media_link)
        self.ui.label_social_media_2.setMaximumSize(EGAVTheme.MainWindow.size_social_media_link)

        set_hand_mouse_pointer(self.ui.label_social_media_0)
        set_hand_mouse_pointer(self.ui.label_social_media_1)
        set_hand_mouse_pointer(self.ui.label_social_media_2)

        self.ui.label_social_media_0.setText("      ")
        self.ui.label_social_media_1.setText("      ")
        self.ui.label_social_media_2.setText("      ")
        self.ui.centralwidget.setStyleSheet(EGAVTheme.MainWindow.style_widget_with_tab)
        self.ui.tabWidget.setIconSize(EGAVTheme.MainWindow.size_TabWidget)

    def setUI_TabStatus(self):
        self.ui.groupBox_16.setStyleSheet(EGAVTheme.MainWindow.style_groupBox_BorderNone)
        self.ui.groupBox_17.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.groupBox_18.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.setSystemInfo()
        self.ui.label_9.setText("")
        self.ui.label_9.setMinimumSize(EGAVTheme.MainWindow.size_label_status_image)
        self.ui.label_9.setMaximumSize(EGAVTheme.MainWindow.size_label_status_image)
        self.ui.plainTextEdit.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.ui.plainTextEdit.setStyleSheet(EGAVTheme.MainWindow.style_textEdit_os_info)
        set_hand_mouse_pointer(self.ui.label_9)
        self.ui.label_9.setToolTip("""<p style="color:blue;"><b>Click here to check status.</b></p>""")
        self.setStatusAV(status="UPDATED")

    def setStatusAV(self, status):
        self.status = status
        if status == EGAVStatus.STATUS_UPDATED:
            self.ui.label_9.setStyleSheet(EGAVTheme.MainWindow.style_label_image_status_updated)
            self.ui.label_10.setText(EGAVTheme.MainWindow.text_label_status_updated)
            self.ui.label_10.setStyleSheet(EGAVTheme.MainWindow.style_label_status_updated)
        elif status == EGAVStatus.STATUS_NOT_UPDATED:
            self.ui.label_9.setStyleSheet(EGAVTheme.MainWindow.style_label_image_status_not_updated)
            self.ui.label_10.setText(EGAVTheme.MainWindow.text_label_status_not_updated)
            self.ui.label_10.setStyleSheet(EGAVTheme.MainWindow.style_label_status_not_updated)
        elif status == EGAVStatus.STATUS_CRITICAL1:
            self.ui.label_9.setStyleSheet(EGAVTheme.MainWindow.style_label_image_status_critical)
            self.ui.label_10.setText(EGAVTheme.MainWindow.text_label_status_critical1)
            self.ui.label_10.setStyleSheet(EGAVTheme.MainWindow.style_label_status_critical)
        elif status == EGAVStatus.STATUS_CRITICAL2:
            self.ui.label_9.setStyleSheet(EGAVTheme.MainWindow.style_label_image_status_critical)
            self.ui.label_10.setText(EGAVTheme.MainWindow.text_label_status_critical2)
            self.ui.label_10.setStyleSheet(EGAVTheme.MainWindow.style_label_status_critical)
        else:
            pass

    def setSystemInfo(self):
        setTextTheme = lambda value_str, color: EGAVTheme.Html_Text.STYLE_GENERAL(value_str=value_str,
                                                                                  color=color,
                                                                                  font_size=14)
        line_break = EGAVTheme.Html_Text.LINE_BREAK
        color1 = "rgb(150,150,150)"  # "rgb(255,51,52)"
        color2 = "rgb(92, 121, 41)"  # "rgb(220,212,39)"

        OS_STR = setTextTheme("Operating System: ", color1)
        CPU_STR = setTextTheme("CPU: ", color1)
        RAM_STR = setTextTheme("RAM: ", color1)
        os_name = system_info()
        os_release = release_info()
        os_version = version_info()
        os_detail = os_name + " " + os_release + ", " + os_version
        # os_detail = os_detail.replace(",", ", \n" + " " * (len(OS_STR) - 1))
        processor_detail = processor_info()
        # processor_detail = processor_detail.replace(",", ", \n" + " " * (len(CPU_STR) - 1))
        total_ram_size = psutil_virtual_memory().total
        total_ram_size_GB_usable = round(total_ram_size / (1024 * 1024 * 1024), 2)
        total_ram_size_GB = round(total_ram_size_GB_usable)

        all_details = OS_STR + setTextTheme(os_detail, color2) + "\n" + \
                      CPU_STR + setTextTheme(processor_detail, color2) + "\n" + \
                      RAM_STR + setTextTheme(str(total_ram_size_GB) + " GB " + "(" + str(total_ram_size_GB_usable) + \
                                             " GB usable)", color2)
        all_details = all_details.replace("\n", line_break)

        self.ui.plainTextEdit.appendHtml(all_details)

    def setUI_TabScan(self):
        self.ui.groupBox_8.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.groupBox_12.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.groupBox_13.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.groupBox_14.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        set_hand_mouse_pointer(self.ui.groupBox_12)
        set_hand_mouse_pointer(self.ui.groupBox_13)
        set_hand_mouse_pointer(self.ui.groupBox_14)

        self.ui.tabWidget.setTabIcon(0, QIcon(EGAVPaths.Resources.EGAV_ICON_STATUS))
        self.ui.tabWidget.setTabIcon(1, QIcon(EGAVPaths.Resources.EGAV_ICON_SCAN))
        self.ui.tabWidget.setTabIcon(2, QIcon(EGAVPaths.Resources.EGAV_ICON_PREFERENCES))
        self.ui.tabWidget.setTabIcon(3, QIcon(EGAVPaths.Resources.EGAV_ICON_SETTINGS))
        self.ui.tabWidget.setTabIcon(4, QIcon(EGAVPaths.Resources.EGAV_ICON_CLEANER))
        self.ui.tabWidget.setTabIcon(5, QIcon(EGAVPaths.Resources.EGAV_ICON_QUARANTINE))
        self.ui.tabWidget.setTabIcon(6, QIcon(EGAVPaths.Resources.EGAV_ICON_HELP))
        self.ui.tabWidget.setTabIcon(7, QIcon(EGAVPaths.Resources.EGAV_ICON_ABOUT))

        self.ui.label_scan_6.setStyleSheet(EGAVTheme.MainWindow.style_label_image_custom_scan)
        self.ui.label_scan_8.setStyleSheet(EGAVTheme.MainWindow.style_label_image_quick_can)
        self.ui.label_scan_10.setStyleSheet(EGAVTheme.MainWindow.style_label_image_full_scan)

        self.ui.label_scan_6.setMaximumSize(EGAVTheme.MainWindow.size_label_image_scan)
        self.ui.label_scan_8.setMaximumSize(EGAVTheme.MainWindow.size_label_image_scan)
        self.ui.label_scan_10.setMaximumSize(EGAVTheme.MainWindow.size_label_image_scan)

        self.ui.label_scan_6.setText("      ")
        self.ui.label_scan_8.setText("      ")
        self.ui.label_scan_10.setText("      ")

        self.ui.label_scan_7.setStyleSheet(EGAVTheme.MainWindow.style_label_text_scan)
        self.ui.label_scan_9.setStyleSheet(EGAVTheme.MainWindow.style_label_text_scan)
        self.ui.label_scan_11.setStyleSheet(EGAVTheme.MainWindow.style_label_text_scan)

    def setUI_TabPreferences(self):
        self.ui.groupBox.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.groupBox_2.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.groupBox_4.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)

        self.ui.checkBox.setStyleSheet(EGAVTheme.MainWindow.style_checkBox)
        self.ui.checkBox_2.setStyleSheet(EGAVTheme.MainWindow.style_checkBox)
        self.ui.checkBox_3.setStyleSheet(EGAVTheme.MainWindow.style_checkBox)

        self.ui.radioButton.setStyleSheet(EGAVTheme.MainWindow.style_radioButton)
        self.ui.radioButton_2.setStyleSheet(EGAVTheme.MainWindow.style_radioButton)
        self.ui.radioButton_3.setStyleSheet(EGAVTheme.MainWindow.style_radioButton)

        self.ui.pushButton_16.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.pushButton_17.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.pushButton_18.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)

    def setUI_TabSettings(self):
        self.ui.groupBox_3.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.groupBox_5.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.groupBox_6.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)

        self.ui.checkBox_4.setStyleSheet(EGAVTheme.MainWindow.style_checkBox)
        self.ui.checkBox_5.setStyleSheet(EGAVTheme.MainWindow.style_checkBox)

        self.ui.label_settings_0.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_1.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_2.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_3.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_4.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_5.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_6.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_7.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_8.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_9.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_settings_10.setStyleSheet(EGAVTheme.MainWindow.style_label)

        self.ui.pushButton_19.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.pushButton_20.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.pushButton_21.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)

        self.ui.pushButton.setStyleSheet(EGAVTheme.MainWindow.style_pushButton1)
        self.ui.pushButton_2.setStyleSheet(EGAVTheme.MainWindow.style_pushButton1)
        self.ui.pushButton_3.setStyleSheet(EGAVTheme.MainWindow.style_pushButton1)
        self.ui.pushButton_4.setStyleSheet(EGAVTheme.MainWindow.style_pushButton1)
        self.ui.pushButton_5.setStyleSheet(EGAVTheme.MainWindow.style_pushButton1)
        self.ui.pushButton_6.setStyleSheet(EGAVTheme.MainWindow.style_pushButton1)
        self.ui.pushButton_7.setStyleSheet(EGAVTheme.MainWindow.style_pushButton1)
        self.ui.pushButton_8.setStyleSheet(EGAVTheme.MainWindow.style_pushButton1)

        self.ui.spinBox.setStyleSheet(EGAVTheme.MainWindow.style_spinBox)
        self.ui.spinBox_2.setStyleSheet(EGAVTheme.MainWindow.style_spinBox)
        self.ui.spinBox_3.setStyleSheet(EGAVTheme.MainWindow.style_spinBox)
        self.ui.spinBox_4.setStyleSheet(EGAVTheme.MainWindow.style_spinBox)

    def setUI_TabCleaner(self):
        self.ui.groupBox_11.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.label_cleaner_1.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_2.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_3.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_4.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_5.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_6.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_7.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_8.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_9.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_10.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.label_cleaner_11.setStyleSheet(EGAVTheme.MainWindow.style_label)

        self.ui.pushButton_9.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.pushButton_10.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)

    def setUI_TabQuarantine(self):
        self.ui.groupBox_10.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.tableWidget_3.setStyleSheet(EGAVTheme.MainWindow.style_tableWidget)
        self.ui.tableWidget_3.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.pushButton_11.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.pushButton_12.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.pushButton_13.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.pushButton_14.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)

    def setUI_TabSupport(self):
        self.ui.groupBox_7.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.label_28.setStyleSheet(EGAVTheme.MainWindow.style_label)
        self.ui.pushButton_15.setStyleSheet(EGAVTheme.MainWindow.style_pushButton)
        self.ui.lineEdit.setStyleSheet(EGAVTheme.MainWindow.style_lineEdit)
        self.ui.textEdit_2.setStyleSheet(EGAVTheme.MainWindow.style_textEdit)

    def setUI_TabAbout(self):
        self.ui.groupBox_9.setStyleSheet(EGAVTheme.MainWindow.style_groupBox)
        self.ui.commandLinkButton.setStyleSheet(EGAVTheme.MainWindow.style_command_link_button)
        self.ui.commandLinkButton_2.setStyleSheet(EGAVTheme.MainWindow.style_command_link_button)
        self.ui.commandLinkButton_3.setStyleSheet(EGAVTheme.MainWindow.style_command_link_button)
        self.ui.commandLinkButton_4.setStyleSheet(EGAVTheme.MainWindow.style_command_link_button)
        self.ui.commandLinkButton.setText("About EG1.in")
        self.ui.commandLinkButton_2.setText("About EG ClamNet Antivirus")
        self.ui.commandLinkButton_3.setText("Rate EG ClamNet Antivirus")
        self.ui.commandLinkButton_4.setText("Please Support")

    def setEvents(self):
        self.setEvents_MainWindow()
        self.setEvents_TabStatus()
        self.setEvents_TabScan()
        self.setEvents_TabPreferences()
        self.setEvents_TabSettings()
        self.setEvents_TabCleaner()
        self.setEvents_TabQuarantine()
        self.setEvents_TabSupport()
        self.setEvents_TabAbout()

    def insert_data_in_quarantine_table(self, json_file):
        """
        insert virus information into Quarantine table
        :param json_file:
        sample
        {
            "Date": "2022-01-06 23:19:13",
            "Detected Item": "Eicar-Test-Signature",
            "Action Taken": "Action Not Taken",
            "Found At Location": "E:\\clamav-0.104.1\\clam-mew.exe.xor",
            "Status": "Quarantined",
            "Current Location": "C:\\Users\\gauta\\AppData\\Roaming\\EGAV\\Vault\\clam-mew.exe.xor.infected"
        }
        :return: None
        """
        with open(json_file) as f:
            data_json = load_json_file(f)
        rowPosition = self.ui.tableWidget_3.rowCount()
        self.ui.tableWidget_3.insertRow(rowPosition)
        self.ui.tableWidget_3.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(data_json["Date"]))
        self.ui.tableWidget_3.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(data_json["Detected Item"]))
        self.ui.tableWidget_3.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(data_json["Action Taken"]))
        self.ui.tableWidget_3.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(data_json["Found At Location"]))
        self.ui.tableWidget_3.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(data_json["Status"]))
        self.ui.tableWidget_3.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(data_json["Current Location"]))

        if data_json["Action Taken"] == "Action Not Taken" and data_json["Status"] == "Quarantined":
            set_foreground_color_toRow_in_tableWidget(tableWidget=self.ui.tableWidget_3,
                                                      rowIndex=rowPosition,
                                                      color=QuarantineTableWidgetItemColor.ACTION_NOT_TAKEN__QUARANTINED)

        if data_json["Action Taken"] == "Action Not Taken" and data_json["Status"] == "Reported":
            set_foreground_color_toRow_in_tableWidget(tableWidget=self.ui.tableWidget_3,
                                                      rowIndex=rowPosition,
                                                      color=QuarantineTableWidgetItemColor.ACTION_NOT_TAKEN__REPORTED)

        if data_json["Action Taken"] == "Deleted" and data_json["Status"] == "Reported":
            set_foreground_color_toRow_in_tableWidget(tableWidget=self.ui.tableWidget_3,
                                                      rowIndex=rowPosition,
                                                      color=QuarantineTableWidgetItemColor.DELETED__REPORTED)

        if data_json["Action Taken"] == "Deleted" and data_json["Status"] == "Quarantined":
            set_foreground_color_toRow_in_tableWidget(tableWidget=self.ui.tableWidget_3,
                                                      rowIndex=rowPosition,
                                                      color=QuarantineTableWidgetItemColor.DELETED__QUARANTINED)

        if data_json["Action Taken"] == "Deleted" and data_json["Status"] == "Removed":
            set_foreground_color_toRow_in_tableWidget(tableWidget=self.ui.tableWidget_3,
                                                      rowIndex=rowPosition,
                                                      color=QuarantineTableWidgetItemColor.DELETED__REMOVED)

        if data_json["Action Taken"] == "Restored" and data_json["Status"] == "Quarantined":
            set_foreground_color_toRow_in_tableWidget(tableWidget=self.ui.tableWidget_3,
                                                      rowIndex=rowPosition,
                                                      color=QuarantineTableWidgetItemColor.RESTORED__QUARANTINED)

        if data_json["Action Taken"] == "Restored" and data_json["Status"] == "Reported":
            set_foreground_color_toRow_in_tableWidget(tableWidget=self.ui.tableWidget_3,
                                                      rowIndex=rowPosition,
                                                      color=QuarantineTableWidgetItemColor.RESTORED__REPORTED)

    def init_tableWidget_in_quarantine(self):
        files = get_files_list_from_folder(EGAVPaths.QuarantineDir)
        for file in files:
            if os.path.basename(file).endswith(".json"):
                try:
                    self.insert_data_in_quarantine_table(file)
                except Exception as e:
                    print_v1("ERROR: " + e.__str__())

        tableWidget_stretch_header_to_contents(self.ui.tableWidget_3)

    def get_tab_index(self, tab_text):
        for i in range(self.ui.tabWidget.count()):
            if self.ui.tabWidget.tabText(i) == tab_text:
                return i

    def set_current_tab(self, tab_text):
        self.ui.tabWidget.setCurrentIndex(self.get_tab_index(tab_text))

    def set_tab_visible(self, tab_text, visible):
        self.ui.tabWidget.setTabVisible(self.get_tab_index(tab_text), visible)

    def set_update_status(self):
        # if service is stopped:
        # av is in  critical stages
        # return
        if clamav_commands.egav_db.Preference_RealTimeProtectionOnOff == 0:
            self.setStatusAV(status=EGAVStatus.STATUS_CRITICAL1)
        else:
            if clamav_service.isOK():
                if clamav_commands.clamav_paths_and_configs.clamav_db_updated():
                    self.setStatusAV(status=EGAVStatus.STATUS_UPDATED)
                else:
                    self.setStatusAV(status=EGAVStatus.STATUS_NOT_UPDATED)
            else:
                self.setStatusAV(status=EGAVStatus.STATUS_CRITICAL2)

    def initialize(self):
        # apply database to UI
        self.applyDatabaseToUI()

        # set all boolean flags
        self.setFlagPreferences(False)
        self.setFlagSettings(False)

        self.set_update_status()
        self.init_tableWidget_in_quarantine()
        self.set_current_tab(tab_text=Main_Window_TAB.STATUS)
        self.set_tab_visible(tab_text="Cleaner", visible=False)
        # set icon
        icon = QtGui.QIcon(EGAVResources.EGAV_WINDOW_ICON)
        self.setWindowIcon(icon)

    def setEvents_MainWindow(self):
        self.ui.tabWidget.currentChanged.connect(self.on_tab_selection)
        self.setEvents_SocialMediaLabels()

    def setEvents_TabStatus(self):
        self.ui.label_9.mousePressEvent = self.on_press_status_icon

    def on_press_status_icon(self, event):
        if self.status == EGAVStatus.STATUS_CRITICAL1:
            msgYN = EGAVMessageYN("Real-Time Protection is OFF. It is\n"
                                  "strongly recommended to turn it ON.\n"
                                  "Do you want to proceed? ")
            msgYN.setModal(True)
            msgYN.exec()
            if msgYN.bAccepted == 1:
                # run update manually
                print_v1("Turning ON Real-Time Protection.")
                self.dbObj.Preference_RealTimeProtectionOnOff = 1
                self.dbObj.saveToFile()
        elif self.status == EGAVStatus.STATUS_CRITICAL2:
            msgYN = EGAVMessageYN('The Clamd service is not running. It\n'
                                  'is strongly recommended to turn it ON.\n'
                                  'Do you want to fix it ?  ')
            msgYN.setModal(True)
            msgYN.exec()
            if msgYN.bAccepted == 1:
                print_v1('Checking Clamd Service/daemon...')
                if OS.Windows():
                    from runasroot import is_admin
                    if not is_admin():
                        from elevate import elevate
                        self.close()
                        elevate(show_console=False)

                    try:
                        check_service()
                        EGAVMessage.simpleMessage("Please wait for a moment, while\n"
                                                  " ClamAV Services are restarted...")
                        self.close()
                        time.sleep(15)
                        EGAVPaths.execute_file("EGAVMain")
                    except:
                        EGAVMessage.simpleMessage("Either service is not installed correctly or doesn't\n"
                                                  "exist. To fix this issue re-install the EG Antivirus")

                ########################################################################3333
                # change db preference rela time prot on

        else:
            if self.status == EGAVStatus.STATUS_CRITICAL2:
                msg = EGAVMessage("The Clamd service is not running.")
                msg.setModal(True)
                msg.exec()
            else:
                if self.status == EGAVStatus.STATUS_UPDATED:
                    msg = EGAVMessage("The Virus Signature Database is up-to-date.")
                    msg.setModal(True)
                    msg.exec()
                else:
                    msgYN = EGAVMessageYN("The Virus Signature Database is older\n"
                                          "than 5 days. Do you want to update it\n"
                                          "manually?")
                    msgYN.setModal(True)
                    msgYN.exec()
                    if msgYN.bAccepted == 1:
                        # run update manually
                        print("updating VSD...")
                        from ClamAVUpdater import UpdateClamAV
                        updateW = UpdateClamAV()
                        updateW.show()

    def on_tab_selection(self):
        current_selected_tab_index = self.ui.tabWidget.currentIndex()
        current_selected_tab = self.ui.tabWidget.tabText(current_selected_tab_index)
        if current_selected_tab == "Quarantine":
            self.on_select_tab_quarantine()

    def on_select_tab_quarantine(self):
        print_v1("TAB Quarantine Selected")

    def on_label_EG(self, e):
        globalPos = e.globalPosition()
        label_2_lower_size_x = self.ui.label_2.size().width()
        label_2_lower_size_y = self.ui.label_2.size().height()
        globalPos_x = globalPos.x()
        globalPos_y = globalPos.y()
        move_x = globalPos_x + label_2_lower_size_x / 2
        move_y = globalPos_y + label_2_lower_size_y / 2
        popup = EGAVInfoPopup(eg_label_lower_point=QtCore.QPoint(move_x, move_y))
        popup.show()
        print_v1("EG Antivirus popup")

    def setEvents_TabScan(self):
        self.ui.label_scan_6.mousePressEvent = self.on_CustomScan
        self.ui.label_scan_8.mousePressEvent = self.on_QuickScan
        self.ui.label_scan_10.mousePressEvent = self.on_FullScan
        self.ui.label_scan_7.mousePressEvent = self.on_CustomScan
        self.ui.label_scan_9.mousePressEvent = self.on_QuickScan
        self.ui.label_scan_11.mousePressEvent = self.on_FullScan
        self.ui.groupBox_12.mousePressEvent = self.on_CustomScan
        self.ui.groupBox_13.mousePressEvent = self.on_QuickScan
        self.ui.groupBox_14.mousePressEvent = self.on_FullScan

    def setEvents_TabPreferences(self):
        self.ui.checkBox.toggled.connect(self.on_preferences_RealTimeProtectionOnOff)
        self.ui.checkBox_2.toggled.connect(self.on_preferences_AutomaticUpdatesOnOff)
        self.ui.radioButton.clicked.connect(self.on_preferences_InfectedFilesReportOnly)
        self.ui.radioButton_2.clicked.connect(self.on_preferences_InfectedFilesRemove)
        self.ui.radioButton_3.clicked.connect(self.on_preferences_InfectedFilesMove2Quarantine)
        self.ui.checkBox_3.toggled.connect(self.on_preferences_InfectedFilesNotifications)
        self.ui.pushButton_16.clicked.connect(self.on_preferences_button_default)
        self.ui.pushButton_17.clicked.connect(self.on_preferences_button_refresh)
        self.ui.pushButton_18.clicked.connect(self.on_preferences_button_apply)

    def setEvents_TabSettings(self):
        self.ui.spinBox.valueChanged.connect(self.on_settings_DoNotScanFilesLargerThan)
        self.ui.checkBox_4.toggled.connect(self.on_settings_DoNotReloadVirusSignatureDB)
        self.ui.checkBox_5.toggled.connect(self.on_settings_ExtractFilesFromArchives)
        self.ui.spinBox_2.valueChanged.connect(self.on_settings_DoNotExtractMoreThanMB)
        self.ui.spinBox_3.valueChanged.connect(self.on_settings_DoNotExtractMoreThanFiles)
        self.ui.spinBox_4.valueChanged.connect(self.on_settings_DoNotExtractMoreThanSubArchives)
        self.ui.pushButton.clicked.connect(self.on_settings_ExcludeExtensionAdd)
        self.ui.pushButton_2.clicked.connect(self.on_settings_ExcludeExtensionEdit)
        self.ui.pushButton_3.clicked.connect(self.on_settings_ExcludeExtensionDelete)
        self.ui.pushButton_4.clicked.connect(self.on_settings_ExcludeExtensionClear)
        self.ui.pushButton_5.clicked.connect(self.on_settings_ScanOnlyExtensionAdd)
        self.ui.pushButton_6.clicked.connect(self.on_settings_ScanOnlyExtensionEdit)
        self.ui.pushButton_7.clicked.connect(self.on_settings_ScanOnlyExtensionDelete)
        self.ui.pushButton_8.clicked.connect(self.on_settings_ScanOnlyExtensionClear)
        self.ui.pushButton_19.clicked.connect(self.on_settings_button_default)
        self.ui.pushButton_20.clicked.connect(self.on_settings_button_refresh)
        self.ui.pushButton_21.clicked.connect(self.on_settings_button_apply)

    def setEvents_SocialMediaLabels(self):
        print_v1("EVENTS: setEvents_SocialMediaLabels")
        self.ui.label_social_media_0.mousePressEvent = self.on_FacebookLink
        self.ui.label_social_media_1.mousePressEvent = self.on_TwitterLink
        self.ui.label_social_media_2.mousePressEvent = self.on_InstagramLink

    def setEvents_TabCleaner(self):
        print_v1("EVENTS: setEvents_TabCleaner")
        self.ui.pushButton_9.clicked.connect(self.on_cleaner_button_refresh)
        self.ui.pushButton_10.clicked.connect(self.on_cleaner_button_clean)

    def setEvents_TabQuarantine(self):
        print_v1("EVENTS: setEvents_TabQuarantine")
        self.ui.pushButton_11.clicked.connect(self.on_quarantine_button_restore)
        self.ui.pushButton_12.clicked.connect(self.on_quarantine_button_delete)
        self.ui.pushButton_13.clicked.connect(self.on_quarantine_button_delete_all)
        self.ui.pushButton_14.clicked.connect(self.on_quarantine_button_clear_all)

    def setEvents_TabSupport(self):
        print_v1("EVENTS: setEvents_TabSupport")
        self.ui.pushButton_15.clicked.connect(self.on_support_button_send)

    def setEvents_TabAbout(self):
        print_v1("EVENTS: setEvents_TabAbout")
        self.ui.commandLinkButton.clicked.connect(self.on_click_About_EG1)
        self.ui.commandLinkButton_2.clicked.connect(self.on_click_About_EG_Antivirus)
        self.ui.commandLinkButton_3.clicked.connect(self.on_click_Rate_EG_Antivirus)
        self.ui.commandLinkButton_4.clicked.connect(self.on_click_Please_Support)

    def on_click_About_EG1(self):
        print_v1("Link Button Clicked: Current Version")
        self.open_link_in_default_browser(EGAVLinks.EG1_WEBSITE_LINK)

    def on_click_About_EG_Antivirus(self):
        print_v1("Link Button Clicked: About EG Antivirus")
        self.open_link_in_default_browser(EGAVLinks.EGAV_WEBSITE_LINK)

    def on_click_Rate_EG_Antivirus(self):
        print_v1("Link Button Clicked: Rate EG Antivirus")
        self.open_link_in_default_browser(EGAVLinks.EGAV_RATE_LINK)

    def on_click_Please_Support(self):
        print_v1("Link Button Clicked: Please Support")
        self.open_link_in_default_browser(EGAVLinks.EGAV_SUPPORT_LINK)

    def on_support_button_send(self):
        print_v1("Button Clicked: support_button_send")

        # -------------------------------------------------------#
        def showMessage(msg_text=None):
            msg = EGAVMessage(msg_text)
            msg.setModal(True)
            msg.exec()
            if msg.Accepted:
                self.ui.pushButton_15.setEnabled(True)
            return

        # -------------------------------------------------------#

        text_to_send = self.ui.textEdit_2.toPlainText()
        email_user = self.ui.lineEdit.text()

        if email_user == "":
            showMessage("Please enter your email !!")
            return

        if not email_valid(email_user):
            showMessage("Please enter your valid email address !!")
            return

        if text_to_send == "":
            showMessage("Please enter a message !!")
            return

        self.ui.pushButton_15.setEnabled(False)
        # text_to_send = "User Email: " + email_user + "\n\n" + "User Message: " + text_to_send + "\n\n"

        if send_support_message(email_user, text_to_send) == 1:
            showMessage("Message successfully sent, we will \n"
                        "be back ASAP to your given email.")
            self.ui.lineEdit.clear()
            self.ui.textEdit_2.clear()
        else:
            showMessage("Please Check your network and try again.")

        self.ui.pushButton_15.setEnabled(True)

    def on_quarantine_button_restore(self):
        print_v1("Button Clicked: quarantine_button_restore")

        msg = EGAVMessageYN(messageText="It may be a risk to restore infected files. \nDo you really want to restore ?")
        msg.exec_()
        if msg.bAccepted == 0 or msg.bAccepted == -1:
            return
        count_items_in_row = self.ui.tableWidget_3.columnCount()
        items = self.ui.tableWidget_3.selectedItems()
        rows = len(items) // count_items_in_row
        files = []
        for n in range(rows):
            items_nth_row = items[count_items_in_row * n:count_items_in_row * (n + 1)]
            file_path = os.path.splitext(items_nth_row[-1].text())[0]
            files.append(file_path + ".json")

        for file in files:
            if os.path.basename(file).endswith(".json"):
                try:
                    with open(file, "r") as f:
                        data_json = load_json_file(f)
                except Exception as e:
                    print_v1("Error: " + e.__str__())
                    return
                if data_json["Action Taken"] == "Action Not Taken":
                    try:
                        # restore file
                        move_file(src=data_json["Current Location"], dst=data_json["Found At Location"])
                        data_json["Action Taken"] = "Restored"
                        with open(file, "w") as f:
                            f.write(json_dumps(data_json))
                            # json_dump(data_json, f)
                    except Exception as e:
                        print_v1("Error: " + e.__str__())
                        return
                else:
                    pass
            else:
                pass
        self.clear_quarantine_tableWidget()
        self.init_tableWidget_in_quarantine()

    def clear_quarantine_tableWidget(self):
        self.ui.tableWidget_3.clearSpans()
        self.ui.tableWidget_3.setRowCount(0)

    def on_quarantine_button_delete(self):
        print_v1("Button Clicked: quarantine_button_delete")

        count_items_in_row = self.ui.tableWidget_3.columnCount()
        items = self.ui.tableWidget_3.selectedItems()
        rows = len(items) // count_items_in_row
        files = []
        for n in range(rows):
            items_nth_row = items[count_items_in_row * n:count_items_in_row * (n + 1)]
            file_path = os.path.splitext(items_nth_row[-1].text())[0]
            files.append(file_path + ".json")

        for file in files:
            if os.path.basename(file).endswith(".json"):
                try:
                    with open(file, "r") as f:
                        data_json = load_json_file(f)
                except Exception as e:
                    print_v1("Error: " + e.__str__())
                    return
                if data_json["Action Taken"] == "Action Not Taken":
                    try:
                        os.remove(data_json["Current Location"])
                        data_json["Action Taken"] = "Deleted"
                        with open(file, "w") as f:
                            f.write(json_dumps(data_json))
                            # json_dump(data_json, f)
                    except Exception as e:
                        print_v1("Error: " + e.__str__())
                        return
                else:
                    pass
            else:
                pass
        self.clear_quarantine_tableWidget()
        self.init_tableWidget_in_quarantine()

        # count_items_in_row = self.ui.tableWidget_3.columnCount()
        # items = self.ui.tableWidget_3.selectedItems()
        # rows = len(items) // count_items_in_row
        #
        # items_detail = dict()
        #
        # for n in range(rows):
        #     items_nth_row = items[count_items_in_row * n:count_items_in_row * (n + 1)]
        #     items_detail[n] = [item.text() for item in items_nth_row]
        #     try:
        #         # last element of items_nth_row is the path where virus is quarantined
        #         os.remove(items_nth_row[-1].text())
        #         # change "Action Taken" from "Action Not Taken" to "Deleted"
        #         items_nth_row[2].setText("Deleted")
        #         # set color of processed row
        #         for j in range(count_items_in_row):
        #             items_nth_row[j].setForeground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        #     except Exception as e:
        #         print_v1(e)
        #
        # print_v1("Quarantine, Virus Deleted: " + str(items_detail), logs=False)
        # self.ui.tableWidget_3.setFocus()

    def on_quarantine_button_delete_all(self):
        print_v1("Button Clicked: quarantine_button_delete_all")
        files = get_files_list_from_folder(EGAVPaths.QuarantineDir)
        for file in files:
            if os.path.basename(file).endswith(".json"):
                try:
                    with open(file, "r") as f:
                        data_json = load_json_file(f)
                except Exception as e:
                    print_v1("Error: " + e.__str__())
                    return
                if data_json["Action Taken"] == "Action Not Taken":
                    try:
                        os.remove(data_json["Current Location"])
                        data_json["Action Taken"] = "Deleted"
                        with open(file, "w") as f:
                            f.write(json_dumps(data_json))
                            # json_dump(data_json, f)
                    except Exception as e:
                        print_v1("Error: " + e.__str__())
                        return
                else:
                    pass
            else:
                pass
        self.clear_quarantine_tableWidget()
        self.init_tableWidget_in_quarantine()

    def on_quarantine_button_clear_all(self):
        print_v1("Button Clicked: quarantine_button_clear_all")
        n_infected_files = get_total_number_of_files(ext=".infected", walk_dir=EGAVPaths.QuarantineDir)
        if n_infected_files:
            msg = EGAVMessage(messageText="Please delete all infected files first, then click on Clear All.")
            msg.exec_()
            return

        files = get_files_list_from_folder(EGAVPaths.QuarantineDir)
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension == ".json":
                try:
                    os.remove(file)
                except Exception as e:
                    print_v1("Error: " + e.__str__())
            else:
                pass
        self.clear_quarantine_tableWidget()

    def on_cleaner_button_refresh(self):
        print_v1("Button Clicked: cleaner_button_refresh")

    def on_cleaner_button_clean(self):
        print_v1("Button Clicked: cleaner_button_clean")

    def on_settings_DoNotScanFilesLargerThan(self, e):
        self.setFlagSettings(True)
        print_v1("SpinBox Updated: DoNotScanFilesLargerThan")

    def on_settings_DoNotReloadVirusSignatureDB(self, e):
        self.setFlagSettings(True)
        print_v1("CheckBox Clicked: DoNotReloadVirusSignatureDB")

    def on_settings_ExtractFilesFromArchives(self, e):
        self.setFlagSettings(True)
        print_v1("CheckBox Clicked: ExtractFilesFromArchives")

    def on_settings_DoNotExtractMoreThanMB(self, e):
        self.setFlagSettings(True)
        print_v1("SpinBox Updated: DoNotExtractMoreThanMB")

    def on_settings_DoNotExtractMoreThanFiles(self, e):
        self.setFlagSettings(True)
        print_v1("SpinBox Updated: DoNotExtractMoreThanFiles")

    def on_settings_DoNotExtractMoreThanSubArchives(self, e):
        self.setFlagSettings(True)
        print_v1("SpinBox Updated: DoNotExtractMoreThanSubArchives")

    def on_settings_ExcludeExtensionAdd(self, e):
        self.setFlagSettings(True)
        inText = EGAVInputPopup()
        inText.showNormal()
        inText.exec()
        if inText.bAccepted:
            self.ui.listWidget.addItem(inText.inputText)
        print_v1("Button Clicked: SettingsExcludeExtensionAdd")

    def on_settings_ExcludeExtensionEdit(self, e):
        self.setFlagSettings(True)
        item_selected = self.ui.listWidget.item(self.ui.listWidget.currentRow())
        if item_selected is not None:
            editDialog = EGAVInputPopup(editItem=True, itemText=item_selected.text())
            editDialog.showNormal()
            editDialog.exec()
            print_v1("editDialog.bEditItem, " + editDialog.bEditItem.__str__())
            if editDialog.bAccepted:
                item_selected.setText(editDialog.inputText)
                self.ui.listWidget.editItem(item_selected)
        print_v1("Button Clicked: SettingsExcludeExtensionEdit")

    def on_settings_ExcludeExtensionDelete(self, e):
        self.setFlagSettings(True)
        item = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
        item = None
        print_v1("Button Clicked: SettingsExcludeExtensionDelete")

    def on_settings_ExcludeExtensionClear(self, e):
        self.setFlagSettings(True)
        self.ui.listWidget.clear()
        print_v1("Button Clicked: SettingsExcludeExtensionClear")

    def on_settings_ScanOnlyExtensionAdd(self, e):
        self.setFlagSettings(True)
        inText = EGAVInputPopup()
        inText.showNormal()
        inText.exec()
        if inText.bAccepted:
            self.ui.listWidget_2.addItem(inText.inputText)
        print_v1("Button Clicked: SettingsScanOnlyExtensionAdd")

    def on_settings_ScanOnlyExtensionEdit(self, e):
        self.setFlagSettings(True)
        item_selected = self.ui.listWidget_2.item(self.ui.listWidget_2.currentRow())
        if item_selected is not None:
            editDialog = EGAVInputPopup(editItem=True, itemText=item_selected.text())
            editDialog.showNormal()
            editDialog.exec()
            if editDialog.bAccepted:
                item_selected.setText(editDialog.inputText)
                self.ui.listWidget_2.editItem(item_selected)
        print_v1("Button Clicked: SettingsScanOnlyExtensionEdit")

    def on_settings_ScanOnlyExtensionDelete(self, e):
        self.setFlagSettings(True)
        item = self.ui.listWidget_2.takeItem(self.ui.listWidget_2.currentRow())
        item = None
        print_v1("Button Clicked: SettingsScanOnlyExtensionDelete")

    def on_settings_ScanOnlyExtensionClear(self, e):
        self.setFlagSettings(True)
        self.ui.listWidget_2.clear()
        print_v1("Button Clicked: SettingsScanOnlyExtensionClear")

    def on_settings_button_default(self, e):
        print_v1("Button Clicked: preferences_button_default")
        self.applyDatabaseToTabSettings(dbObj_Dict=self.dbObj.toDefaultDBDict())
        self.setFlagSettings(True)

    def on_settings_button_refresh(self, e):
        print_v1("Button Clicked: preferences_button_refresh")
        if self.__flagSettingsApply:
            self.applyDatabaseToTabSettings(dbObj_Dict=self.dbObj.toDict())
            self.setFlagSettings(False)

    def on_settings_button_apply(self, e):
        print_v1("Button Clicked: preferences_button_apply")
        self.settingsUI_ToDB()
        self.dbObj.saveToFile()
        self.setFlagSettings(False)

    def on_preferences_RealTimeProtectionOnOff(self, e):
        self.setFlagPreferences(True)
        print_v1("CheckBox Clicked: real_time_protection_on_off")

    def on_preferences_AutomaticUpdatesOnOff(self, e):
        self.setFlagPreferences(True)
        print_v1("CheckBox Clicked: automatic_updates_on_off")

    def on_preferences_InfectedFilesReportOnly(self, e):
        self.setFlagPreferences(True)
        print_v1("RadioButton Clicked: infected_files_report_only")

    def on_preferences_InfectedFilesRemove(self, e):
        self.setFlagPreferences(True)
        print_v1("RadioButton Clicked: infected_files_remove")

    def on_preferences_InfectedFilesMove2Quarantine(self, e):
        self.setFlagPreferences(True)
        print_v1("RadioButton Clicked: infected_files_move2_quarantine")

    def on_preferences_InfectedFilesNotifications(self, e):
        self.setFlagPreferences(True)
        print_v1("CheckBox Clicked:  infected_files_notifications")

    def on_preferences_button_default(self, e):
        print_v1("Button Clicked: preferences_button_default")
        self.applyDatabaseToTabPreferences(dbObj_Dict=self.dbObj.toDefaultDBDict())
        self.setFlagPreferences(True)

    def on_preferences_button_refresh(self, e):
        print_v1("Button Clicked: preferences_button_refresh")
        if self.__flagPreferencesApply:
            self.applyDatabaseToTabPreferences(dbObj_Dict=self.dbObj.toDict())
            self.setFlagPreferences(False)

    def on_preferences_button_apply(self, e):
        print_v1("Button Clicked: preferences_button_apply")
        self.preferencesUI_ToDB()
        self.dbObj.saveToFile()
        self.setFlagPreferences(False)
        self.set_update_status()

    def get_bClamdFlag(self):
        """bClamdFlag is True only when both clamd service running and DO_NOT_RELOAD_VIRUS_SIGNATURE_DB Option is on"""
        bClamdFlag = self.dbObj.Settings_DoNotReloadVirusSignatureDB and clamav_service.isOK()
        return bClamdFlag

    def on_CustomScan(self, event):
        print_v1("Clicked: CUSTOM SCAN")
        file_open_dialog = QtFileDialog()

        if file_open_dialog.exec_() == QFileDialog.AcceptMode.AcceptOpen:
            files_folders_selected = file_open_dialog.filesSelected()
            files_folders_to_scan = paths_correction(files_folders_selected)
            paths_to_scan = str_list_separation(input_list_str=files_folders_to_scan,
                                                separator=" ", end_quote="\"")
            print_v1(args="Custom SCAN, PATH SCAN - " + paths_to_scan)

            bClamdFlag = self.get_bClamdFlag()
            if len(paths_to_scan) > 3:
                if OS.Windows():
                    paths_to_scan = paths_to_scan.replace("/", "\\")
                    scanner = EGAVScanner(scan_type=ScanType.CUSTOM_SCAN, files_to_scan=paths_to_scan,
                                          bClamd=bClamdFlag)
                    scanner.startScanner()
                    scanner.show()
                elif OS.Linux():
                    scanner = EGAVScanner(scan_type=ScanType.CUSTOM_SCAN, files_to_scan=paths_to_scan,
                                          bClamd=bClamdFlag)
                    scanner.startScanner()
                    scanner.show()
                elif OS.OSX():
                    scanner = EGAVScanner(scan_type=ScanType.CUSTOM_SCAN, files_to_scan=paths_to_scan,
                                          bClamd=bClamdFlag)
                    scanner.startScanner()
                    scanner.show()
                else:
                    exit(-1)
            else:
                pass
        pass

    def on_QuickScan(self, event):
        print_v1("Clicked: QUICK SCAN")

        if OS.Unknown():
            print_v1(args="Critical Error: Unknown Operating System")
            exit(-1)

        bClamdFlag = self.get_bClamdFlag()
        scanner = EGAVScanner(scan_type=ScanType.QUICK_SCAN, files_to_scan=QuickScanPaths.SPACE_SEPARATED_PATHS,
                              bClamd=bClamdFlag)
        scanner.setModal()
        scanner.startScanner()
        scanner.show()

    def on_FullScan(self, event):
        print_v1("Clicked: FULL SCAN")
        if OS.Unknown():
            print_v1(args="Critical Error: Unknown Operating System")
            exit(-1)
        ddList = DiskDrives.getDiskDrivesList()
        dd = str_list_separation(input_list_str=ddList)
        bClamdFlag = self.get_bClamdFlag()
        scanner = EGAVScanner(scan_type=ScanType.FULL_SCAN, files_to_scan=dd,
                              bClamd=bClamdFlag)
        scanner.setModal()
        scanner.startScanner()
        scanner.show()

    @staticmethod
    def open_link_in_default_browser(url):
        open_browser(url=url, new=2)

    def on_FacebookLink(self, event):
        print_v1("Link Clicked: facebook")
        self.open_link_in_default_browser(EGAVLinks.EGAV_FACEBOOK_PAGE_LINK)

    def on_TwitterLink(self, event):
        print_v1("Link Clicked: twitter")
        self.open_link_in_default_browser(EGAVLinks.EGAV_TWITTER_PAGE_LINK)

    def on_InstagramLink(self, event):
        print_v1("Link Clicked: instagram")
        self.open_link_in_default_browser(EGAVLinks.EGAV_INSTAGRAM_PAGE_LINK)


if __name__ == '__main__':
    from main import showEGAVMainWindow
    showEGAVMainWindow()
    pass

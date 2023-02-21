"""
EGAVTray.py :=> This file provides Tray Icon Executable for EG ClamNet Antivirus
"""

import time
from json import dumps as json_dumps
from os import chdir
from threading import Thread

import watchdog.events
import watchdog.observers
# from EGAVMsgNPopup import EGAVMessage
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu

from EGAVResources import EGAVResources, EGAVPaths, EGAVStatus, QuickScanPaths
from custom import get_windows_service, run_command_async_and_print_output
from custom import print_v1, path_correction, OS, DEBUG_CODE
from singleObj import clamav_commands, clamav_service


# make icon tray example and in background this below code run,
# make menu on right click , like open,check for update, exit, double click event etc
# run this file as service always should run
# check for database if realtime flag is on then make scan from clamd



class HandlerForScanning(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.*'],
                                                             ignore_directories=False, case_sensitive=False)

    @staticmethod
    def real_time_scan(event):
        try:
            action = clamav_commands.egav_db.Preferences_InfectedFilesRadioButton
            scan_result = clamav_service.scan_and_get_result(any_file_folder=path_correction(event.src_path),
                                                             cmd='SCAN', action=action)
            scan_result = json_dumps(scan_result)
            print_v1("RealTime Scan: " + scan_result)
        except Exception as e:
            print_v1("Error in Real-Time Scanning: " + e.__str__())
        pass

    def on_created(self, event):
        # print_v1(event)
        HandlerForScanning.real_time_scan(event)

    # Event is created, you can process it now

    def on_modified(self, event):
        # print_v1(event)
        HandlerForScanning.real_time_scan(event)
        pass

    # Event is modified, you can process it now


class HandlerForDBChange(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.txt'],
                                                             ignore_directories=True, case_sensitive=False)
        self.__flag_db_modified = False

    def on_created(self, event):
        # print_v1(event)
        print_v1("Database file created")
        pass

    # Event is created, you can process it now

    def on_modified(self, event):
        # print_v1(event)
        print_v1("Database modified")
        self.set_db_flag(True)
        pass

    def set_db_flag(self, bFlag):
        self.__flag_db_modified = bFlag

    def get_db_flag(self):
        return self.__flag_db_modified


class ThreadRTS(Thread):

    def __init__(self):
        """
        ThreadRTS is class for creating all necessary threads for
        real-time scanning, database file modification events
        """
        super(ThreadRTS, self).__init__()
        self.bStop = None
        self.rts_path1 = QuickScanPaths.DESKTOP_FOLDER
        self.rts_path2 = QuickScanPaths.DOWNLOAD_FOLDER
        self.rts_path3 = QuickScanPaths.DOCUMENTS_FOLDER
        self.rts_path4 = QuickScanPaths.PICTURE_LOCATION
        self.rts_event_handler = None
        self.db_event_handler = None
        self.observer = None

        # just save log paths from service
        from ClamAVResources import log_all_paths_info
        log_all_paths_info("paths_from_service.txt")

    def stop(self):
        """

        :return:
        """
        self.bStop = True

    def run(self):
        """
        :return:
        """
        self.bStop = False
        self.rts_event_handler = HandlerForScanning()
        self.db_event_handler = HandlerForDBChange()
        self.observer = watchdog.observers.Observer()
        self.observer.schedule(self.rts_event_handler, path=self.rts_path1, recursive=True)
        self.observer.schedule(self.rts_event_handler, path=self.rts_path2, recursive=True)
        self.observer.schedule(self.rts_event_handler, path=self.rts_path3, recursive=True)
        self.observer.schedule(self.rts_event_handler, path=self.rts_path4, recursive=True)
        self.observer.schedule(self.db_event_handler, path=EGAVPaths.SettingsDBDir, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
                if self.bStop:
                    raise KeyboardInterrupt
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
        print_v1("Real-Time Scanning terminated successfully")


class EGAVTray:
    def __init__(self):
        """
        this class is for System tray of EG Antivirus
        """
        # variables

        # get os details
        self.os_detail = OS.get_os_details()
        # Create app
        self.app = QtWidgets.QApplication([])
        # Create the icon
        self.icon = QIcon(EGAVResources.EGAV_TRAY_ICON_NOT_UPDATED)
        # Create the tray
        self.tray = QSystemTrayIcon()
        # Create the menu
        self.menu = QMenu()
        # Create menu actions
        self.actionOpen = QAction("Open")
        self.actionCheckStatus = QAction("Refresh Status")
        self.actionCheckUpdate = QAction("Check updates")
        self.actionExit = QAction("Exit")

        # create real-time scanning thread
        self.rts_thread = ThreadRTS()

        # create a timer for notification
        self.timer = QtCore.QTimer()

        self.setupUi()
        self.resetUi()
        self.setEvents()
        self.initialize()
        self.execute()

    def setupUi(self):
        self.app.setQuitOnLastWindowClosed(False)
        pass

    def resetUi(self):
        # set icon in tray

        self.setIcon(self.icon)
        # add menu actions in menu
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionCheckStatus)
        self.menu.addAction(self.actionCheckUpdate)
        self.menu.addAction(self.actionExit)
        # Add the menu to the tray
        self.tray.setContextMenu(self.menu)

        pass

    def setEvents(self):
        # connect slots to the menu click event.
        self.actionOpen.triggered.connect(self.onClickOpen)
        self.actionCheckStatus.triggered.connect(self.onClickRefreshStatus)
        self.actionCheckUpdate.triggered.connect(self.onClickCheckUpdates)
        self.actionExit.triggered.connect(self.onExit)
        # connect slot with notifications event click
        self.tray.messageClicked.connect(self.onClickNotification)
        # connect slot with mouse double click on icon
        # self.tray.activated.connect(self.onClick)
        self.timer.timeout.connect(self.onTimer)
        pass

    def onTimer(self):
        if self.os_detail == "Windows":
            if not DEBUG_CODE:
                winTraySer = get_windows_service("WinSerEGCNTray")
                if (winTraySer is None) or (winTraySer["status"] != "running"):
                    print_v1(args="Error EGAVTray: WinSerEGCNTray Service not running.")
                    self.onExit()
                else:
                    pass
            else:
                pass
        else:
            pass
        if self.rts_thread.db_event_handler.get_db_flag():
            self.rts_thread.db_event_handler.set_db_flag(False)
            self.initialize()
        else:
            time.sleep(0.1)

    def initialize(self):
        clamav_commands.egav_db.loadDatabase()
        if clamav_commands.egav_db.Preference_RealTimeProtectionOnOff == 0:
            self.setStatusCritical1()
        else:
            if clamav_service.isOK():
                if clamav_commands.clamav_paths_and_configs.clamav_db_updated():
                    self.setStatusUpToDate()
                else:
                    self.setStatusNotUpToDate()
            else:
                self.setStatusCritical2()

    def execute(self):
        self.rts_thread.start()
        self.timer.start(100)
        self.app.exec()

    def setIcon(self, icon):
        self.icon = icon
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

    def onClickNotification(self):
        print_v1("Notification Clicked")
        EGAVPaths.execute_file("EGAVMain")

    def onClick(self):
        # if self.tray.ActivationReason == self.tray.DoubleClick:
        #     print_v1("Systray icon double Clicked")
        #     EGAVPaths.execute_file("EGAVMain")
        pass

    def onClickOpen(self):
        print_v1("EGAVTray: Clicked on Open")
        # self.initialize()
        chdir(EGAVResources.EGAV_WORKING_DIR)
        EGAVPaths.execute_file("EGAVMain")

    def onClickCheckUpdates(self):
        print_v1("EGAVTray: Clicked on Check Updates")

    def onClickRefreshStatus(self):
        print_v1("EGAVTray: Clicked on Check Status")
        self.initialize()

    def onExit(self):
        print_v1("EGAVTray: Clicked on Exit")
        self.timer.stop()
        self.rts_thread.stop()
        # time.sleep(0.2)
        self.app.quit()
        if self.os_detail == "Windows":
            if not DEBUG_CODE:
                winTraySer = get_windows_service("WinSerEGCNTray")
                if winTraySer["status"] == "running":
                    run_command_async_and_print_output("sc.exe stop WinSerEGCNTray")
                else:
                    pass
            else:
                pass
        else:
            pass

    def setStatusUpToDate(self):
        self.tray.setToolTip(EGAVStatus.STR_TOOLTIP_UPDATED)
        self.setIcon(QIcon(EGAVResources.EGAV_TRAY_ICON_UPDATED))
        self.tray.showMessage(EGAVStatus.STR_TITLE,
                              EGAVStatus.STR_BALLOON_UPDATED,
                              self.icon
                              )

    def setStatusNotUpToDate(self):
        self.tray.setToolTip(EGAVStatus.STR_TOOLTIP_NOT_UPDATED)
        self.setIcon(QIcon(EGAVResources.EGAV_TRAY_ICON_NOT_UPDATED))
        self.tray.showMessage(EGAVStatus.STR_TITLE,
                              EGAVStatus.STR_BALLOON_NOT_UPDATED,
                              self.icon
                              )

    def setStatusCritical1(self):
        self.tray.setToolTip(EGAVStatus.STR_TOOLTIP_CRITICAL1)
        self.setIcon(QIcon(EGAVResources.EGAV_TRAY_ICON_CRITICAL))
        self.tray.showMessage(EGAVStatus.STR_TITLE,
                              EGAVStatus.STR_BALLOON_CRITICAL1,
                              self.icon
                              )

    def setStatusCritical2(self):
        self.tray.setToolTip(EGAVStatus.STR_TOOLTIP_CRITICAL2)
        self.setIcon(QIcon(EGAVResources.EGAV_TRAY_ICON_CRITICAL))
        self.tray.showMessage(EGAVStatus.STR_TITLE,
                              EGAVStatus.STR_BALLOON_CRITICAL2,
                              self.icon
                              )


if __name__ == '__main__':
    EGAVTray()

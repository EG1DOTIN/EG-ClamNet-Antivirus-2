"""
EGAVScanner.py :=> This file provides GUI for EG ClamNet Antivirus Scanner executable
"""

from config import EXE_SETUP_CLAMAV
from processes import Processes
from os import path, kill
from time import sleep
from json import dumps as json_dumps
from custom import dq, get_time_str, get_time_diff, print_v1, OS, do_nothing
from PySide6 import QtGui, QtCore, QtWidgets
from EGAVResources import EGAVPaths, EGAVResources, EGAVTheme
from pyUIClasses.scanner_window import Ui_Form
from InfoWindow import InfoWin
from datetime import datetime
from singleObj import clamav_service, clamav_commands
from EGAVTitleBar import EGAVTitleBar


class ScanType:
    CUSTOM_SCAN = "Custom Scan"
    QUICK_SCAN = "Quick Scan"
    FULL_SCAN = "Full Scan"
    MEMORY_SCAN = "Memory Scan"


class EGAVScanner(QtWidgets.QWidget):
    def __init__(self, scan_type=ScanType.CUSTOM_SCAN, files_to_scan=None, bClamd=False):
        super(EGAVScanner, self).__init__()

        self.layout = QtWidgets.QVBoxLayout()
        self.title_bar = EGAVTitleBar(self)

        self.p = QtCore.QProcess(self)
        # self.p.setProgram("dirb")
        # self.p.setProcessChannelMode(QtCore.QProcess.MergedChannels)

        self.os = OS.get_os_details()
        self.bClamd = bClamd
        self.scan_type = scan_type
        self.files_to_scan = files_to_scan
        self.virus_count = 0
        self.virus_detail = ''
        self.start_time = datetime.now()
        self.stop_time = None
        self.movie_giff = QtGui.QMovie(EGAVResources.EGAV_SCANNING_IMAGE_GIFF)
        # self.timerScan = QtCore.QTimer()
        self.ui = Ui_Form()

        self.setupUi()
        self.resetUi()
        self.setEvents()

    def startScanner(self):
        self.start_animation()
        cmd_res = self.get_process_cmd()
        if cmd_res["success"]:
            self.start_process(cmd_res["command"])
        else:
            # show message box here with error
            # msg = EGAVMessage(messageText=cmd_res["message"])
            # msg.setModal(True)
            # msg.exec()
            self.process_finished()

    def setModal(self, modal=True):
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal) if modal else do_nothing()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        print_v1(args="close event", logs=False)
        if self.p is not None:
            self.p.kill()
            Processes.kill_process_by_name(proc_name="clamscan.exe")

    def setupUi(self):
        self.ui.setupUi(self)
        pass

    def setUi_TitleBar(self):
        # adding title bar
        self.layout.addWidget(self.title_bar)
        self.layout.addWidget(self.ui.verticalLayoutWidget)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title_bar.setFixedWidth(self.width())

    def resetUi(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setUi_TitleBar()
        self.setStyleSheet(EGAVTheme.ScannerWindow.style_dialog)
        self.ui.label.setText(self.scan_type)
        self.ui.label.setStyleSheet(EGAVTheme.ScannerWindow.style_label_scanType)
        self.ui.label_3.setText("scanning...")
        self.ui.label_3.setStyleSheet(EGAVTheme.ScannerWindow.style_label_scanning_text)
        self.ui.label_5.setText("Infected Files: ")
        self.ui.label_5.setStyleSheet(EGAVTheme.ScannerWindow.style_label_infectedFiles_text)
        self.ui.label_4.setText(str(self.virus_count))
        self.ui.label_4.setStyleSheet(EGAVTheme.ScannerWindow.style_label_infectedFilesNumber_text)
        self.ui.pushButton.setText("Stop")
        self.ui.pushButton.setStyleSheet(EGAVTheme.ScannerWindow.style_stop_button)
        self.setWindowIcon(QtGui.QIcon(EGAVResources.EGAV_WINDOW_ICON))
        # self.setFixedSize(self.size())

        # Loading the GIF
        self.ui.label_2.setMovie(self.movie_giff)
        self.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        pass

    def start_animation(self):
        self.movie_giff.start()

    def stop_animation(self):
        self.movie_giff.stop()

    def setEvents(self):
        self.ui.pushButton.clicked.connect(self.on_button_stop)
        # self.timerScan.timeout.connect(self.timerScanThread)
        pass

    def on_button_stop(self):
        if self.ui.pushButton.text() == "Stop":
            print_v1(args="on_button_stop", logs=False)
            self.close()
        elif self.ui.pushButton.text() == "Scan Result":
            self.show_scan_result()
        elif self.ui.pushButton.text() == "Exit":
            print_v1(args="scanning completed.", logs=False)
            self.close()

    def show_scan_result(self):
        self.hide()
        setTextTheme = EGAVTheme.Html_Text.PARAGRAPH_GENERAL
        line_break = EGAVTheme.Html_Text.LINE_BREAK

        cmd_res = self.get_process_cmd()

        if cmd_res["success"]:
            info = setTextTheme(value_str="Scan Start Time : " + get_time_str(self.start_time),
                                color="white", font_size=14)
            info += setTextTheme(value_str="Scan Stop Time : " + get_time_str(self.stop_time),
                                 color="white", font_size=14)
            info += setTextTheme(value_str="Total Time in Scan : " + get_time_diff(self.start_time, self.stop_time),
                                 color="white", font_size=14)
            info += setTextTheme(value_str="Scan Type: " + self.scan_type,
                                 color="white", font_size=14) + line_break

            info += setTextTheme(value_str="Total Infected Files Found: " + str(self.virus_count),
                                 color="red", font_size=14) + line_break
            if self.virus_count:
                info += setTextTheme(value_str="Infected Files Details: " + line_break + \
                                               self.virus_detail.replace("\r\n", line_break),
                                     color="red", font_size=12)
            iw = InfoWin(parent=self, window_title="EGAV Scanner",
                         info_title="******** Scanning Result ********", info_text=info, custom_title_bar=False)
            iw.exec()
            self.ui.pushButton.setText("Exit")
        else:
            info = setTextTheme(value_str=cmd_res["message"], color="white", font_size=14)
            iw = InfoWin(parent=self, window_title="EGAV Scanner",
                         info_title="******** Scanning Result ********", info_text=info, custom_title_bar=False)
            iw.exec()
            self.ui.pushButton.setText("Exit")

    # def timerScanThread(self):
    #     if self.files_to_scan is None:
    #         self.virus_count += 1
    #         self.ui.label_3.setText("scanning c:\\users\\window.dll " + str(self.virus_count))
    #     else:
    #         self.clamD.scan(self.files_to_scan)
    #         pass

    def message(self, s):
        if clamav_service.isOK():
            print_v1(args=s, logs=False)
            split_lines = s.split("\r\n")

            if len(split_lines) >= 2:
                t = split_lines[-2]
            else:
                t = split_lines[-1]
            # time.sleep(0.01)
            self.ui.label_3.setText(t)

            found_virus = s.count("('FOUND',")
            if found_virus:
                self.virus_detail += s
                self.virus_count += found_virus
                self.ui.label_4.setText(str(self.virus_count))
        else:
            print_v1(args=s, logs=False)
            split_lines = s.split("\n")

            if len(split_lines) >= 2:
                t = split_lines[-2]
            else:
                t = split_lines[-1]
            # time.sleep(0.01)
            self.ui.label_3.setText(t)

            found_virus = s.count("FOUND")
            if found_virus:
                if s.__contains__("FOUND"):
                    for line in split_lines:
                        if line.__contains__("FOUND"):
                            self.virus_detail += line + " \r\n "
                        else:
                            pass
                else:
                    pass
                self.virus_count += found_virus
                self.ui.label_4.setText(str(self.virus_count))

    def get_process_cmd(self, bDistEXE=EXE_SETUP_CLAMAV):
        res = dict()
        action = clamav_commands.egav_db.Preferences_InfectedFilesRadioButton

        if self.bClamd:
            path_option = " -a " + str(action) + " -p "
        else:
            path_option = " -a 0 -P "

        if self.scan_type in [ScanType.QUICK_SCAN, ScanType.CUSTOM_SCAN, ScanType.FULL_SCAN]:
            if self.scan_type == ScanType.FULL_SCAN:
                # in full scan we will not use clamd service it make slow because of file/folder list calculation
                path_option = path_option.replace('-p', '-P')
            if not bDistEXE:
                cmd = EGAVPaths.python_str() + EGAVPaths.file_str("ClamdScanner.py") + path_option + self.files_to_scan
            else:
                cmd = EGAVPaths.file_str("ClamdScanner") + path_option + self.files_to_scan
            msg = self.scan_type
            success = True
        elif self.scan_type == ScanType.MEMORY_SCAN:
            if self.os == "Windows":
                if self.bClamd:
                    if not bDistEXE:
                        cmd = EGAVPaths.python_str() + EGAVPaths.file_str("ClamdScanner.py -a ") + str(action) + " -m"
                    else:
                        cmd = EGAVPaths.file_str("ClamdScanner") + " -a " + str(action) + " -m"
                    msg = "Memory Scan Command for Windows OS only (Clamd Service must be ON)"
                    success = True
                else:
                    cmd = None
                    msg = "Clamd service is not running"
                    success = False
            elif self.os == "Linux":
                cmd = None
                msg = "Memory Scan is available only for Windows"
                success = False
            elif self.os == "MAC":
                cmd = None
                msg = "Memory Scan is available only for Windows"
                success = False
            else:
                cmd = None
                msg = "Unknown OS"
                success = False
        else:
            cmd = None
            msg = "Unknown CMD"
            success = False

        res["command"] = cmd
        res["message"] = msg
        res["success"] = success
        print_v1(args="Scanning command Response: " + json_dumps(res))
        return res

    def start_process(self, cmd):
        # Keep a reference to the QProcess (e.g. on self) while it's running.
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.readyReadStandardError.connect(self.handle_stderr)
        self.p.stateChanged.connect(self.handle_state)
        self.p.finished.connect(self.process_finished)  # Clean up once complete.
        # self.p.start("python3", ['dummy_script.py'])
        # self.p.startDetached(cmd)
        self.start_time = datetime.now()
        self.p.startCommand(cmd)
        print_v1(args="Scanning Process Id: " + str(self.p.processId()))

    def terminate(self):
        if self.p is not None:
            self.p.terminate()

    def kill(self):
        if self.p is not None:
            self.p.terminate()
            self.p.waitForFinished(msecs=2000)
            self.p.kill()
            self.p.waitForFinished(msecs=1000)

    def interrupt(self):
        from signal import CTRL_C_EVENT
        pid = self.p.processId()
        kill(pid, CTRL_C_EVENT)

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QtCore.QProcess.NotRunning: 'Not running',
            QtCore.QProcess.Starting: 'Starting',
            QtCore.QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"Scan: {state_name}")

    def process_finished(self):
        self.message("Finished.")
        self.stop_animation()
        self.ui.pushButton.setText("Scan Result")
        self.stop_time = datetime.now()
        self.p = None


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = EGAVScanner(scan_type="Quick Scan", files_to_scan=r"E:\clamav-0.104.1", bClamd=True)
    print(ex.get_process_cmd())
    ex.startScanner()
    ex.show()
    print_v1(args=ex.get_process_cmd(), logs=False)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    pass

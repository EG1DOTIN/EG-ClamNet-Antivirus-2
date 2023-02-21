"""
main.py :=> this file is used as main file for showing GUI Examples of other files used and
 for converting all Qt ui file into python UI Qt classes
"""

from custom import dq
from EGAVScanner import EGAVScanner
from EGAVMain import EGAVMessageYN, EGAVMessage
from EGAVMain import os, sys, QtWidgets, QtCore, EGAVPaths, EGAVMainWindow, EGAVInfoPopup, EGAVInputPopup


def ui2py(source_ui_file_full_path, target_py_folder_path=EGAVPaths.Resources.EGAV_UI_PY_CLASS_FILES_FOLDER):
    # command usage ->  pyside6-uic "source_file_full_path" -o "target_file_full_path"
    ui_file_name = os.path.basename(source_ui_file_full_path).split(".")[0]
    cmd = "pyside6-uic " + dq + source_ui_file_full_path + dq + " -o " + \
          dq + os.path.join(target_py_folder_path, ui_file_name + ".py") + dq
    # print(cmd)
    os.system(cmd)


def generateUIFiles(uiFiles=None):
    if uiFiles is None:
        ui2py(EGAVPaths.Resources.EGAV_UI_FILE_MAIN_WINDOW)
        ui2py(EGAVPaths.Resources.EGAV_UI_FILE_INFO_POPUP)
        ui2py(EGAVPaths.Resources.EGAV_UI_FILE_SCANNER)
        ui2py(EGAVPaths.Resources.EGAV_UI_FILE_INPUT_TEXT)
        ui2py(EGAVPaths.Resources.EGAV_UI_FILE_MESSAGE_BOX)
        ui2py(EGAVPaths.Resources.EGAV_UI_FILE_MESSAGE_BOX_YN)
        ui2py(EGAVPaths.Resources.EGAV_UI_FILE_LOG_INFO)
        ui2py(EGAVPaths.Resources.EGAV_UI_FILE_SETUP_WINDOW)
        ui2py(EGAVPaths.Resources.EGAV_UI_FILE_TITLE_BAR)
    else:
        for file in uiFiles:
            ui2py(file)



def showEGAVMainWindow():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = EGAVMainWindow()
    sys.exit(app.exec())


def showEGAVInfoPopup():
    app = QtWidgets.QApplication(sys.argv)
    ex = EGAVInfoPopup(QtCore.QPoint(100, 120))
    ex.show()
    sys.exit(app.exec())


def showEGAVInputPopup():
    app = QtWidgets.QApplication(sys.argv)
    ex = EGAVInputPopup(editItem=True)
    ex.show()
    ex.exec()
    print(ex.inputText)
    sys.exit(app.exec())


def showEGAVMessagePopup(yes_no=False):
    app = QtWidgets.QApplication(sys.argv)
    if yes_no:
        ex = EGAVMessageYN()
    else:
        ex = EGAVMessage()
    ex.show()
    sys.exit(app.exec())


def showEGAVScannerWindow():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = EGAVScanner()
    sys.exit(app.exec())


if __name__ == '__main__':
    # test any code here
    pass

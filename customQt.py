"""
customQt.py :=> This file provide custom functions and classes made by using Qt (PySide6 lib)
"""

import os
from PySide6 import QtCore, QtGui, QtWidgets


class QuarantineTableWidgetItemColor:
    ACTION_NOT_TAKEN__QUARANTINED = QtGui.QColor(200, 50, 50)
    ACTION_NOT_TAKEN__REPORTED = QtGui.QColor(255, 0, 0)
    DELETED__REPORTED = QtGui.QColor(200, 100, 0)
    DELETED__QUARANTINED = QtGui.QColor(0, 175, 0)
    DELETED__REMOVED = QtGui.QColor(0, 200, 0)
    RESTORED__QUARANTINED = QtGui.QColor(200, 0, 0)
    RESTORED__REPORTED = QtGui.QColor(235, 20, 50)


def tableWidget_stretch_header_to_contents(tableWidget):
    header = tableWidget.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)


def set_hand_mouse_pointer(qtWidget):
    qtWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


def set_background_color_toRow_in_tableWidget(tableWidget, rowIndex, color):
    for j in range(tableWidget.columnCount()):
        # set background color
        tableWidget.item(rowIndex, j).setBackground(color)
        # set alignment
        tableWidget.item(rowIndex, j).setTextAlignment(QtGui.Qt.AlignCenter)
        # tableWidget.item(rowIndex, j).setTextAlignment(QtGui.Qt.AlignVCenter)
        # tableWidget.item(rowIndex, j).setTextAlignment(QtGui.Qt.AlignHCenter)


def set_foreground_color_toRow_in_tableWidget(tableWidget, rowIndex, color):
    for j in range(tableWidget.columnCount()):
        # set foreground color
        tableWidget.item(rowIndex, j).setForeground(color)
        # set alignment
        tableWidget.item(rowIndex, j).setTextAlignment(QtGui.Qt.AlignCenter)
        # tableWidget.item(rowIndex, j).setTextAlignment(QtGui.Qt.AlignVCenter)
        # tableWidget.item(rowIndex, j).setTextAlignment(QtGui.Qt.AlignHCenter)


def str_item_list_from_listWidget(listWidget):
    count = listWidget.count()
    resList = []
    for i in range(count):
        resList.append(listWidget.item(i).text())
    return resList


class QtFileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args, **kwargs):
        super(QtFileDialog, self).__init__(*args, **kwargs)
        self.selected_files = []
        self.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        self.tree = self.findChild(QtWidgets.QTreeView)

    def accept(self):
        inds = self.tree.selectionModel().selectedIndexes()
        self.selected_files = []
        for i in inds:
            if i.column() == 0:
                self.selected_files.append(os.path.join(str(self.directory().absolutePath()), str(i.data())))
        self.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)
        self.close()

    def filesSelected(self):
        return self.selected_files


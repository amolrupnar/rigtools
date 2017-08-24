# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S:/bsw_programation/01_maya/Pipeline/rigtools/rigtools/ui/aspToolsUI/ui_aspIKOriChange.ui'
#
# Created: Thu Aug 24 16:52:54 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_aspIKOriChangeWindow(object):
    def setupUi(self, aspIKOriChangeWindow):
        aspIKOriChangeWindow.setObjectName("aspIKOriChangeWindow")
        aspIKOriChangeWindow.resize(406, 139)
        self.centralwidget = QtGui.QWidget(aspIKOriChangeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.aspIkOriSet_btn = QtGui.QPushButton(self.centralwidget)
        self.aspIkOriSet_btn.setObjectName("aspIkOriSet_btn")
        self.gridLayout_2.addWidget(self.aspIkOriSet_btn, 2, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.aspIkOriJnt_LE = QtGui.QLineEdit(self.centralwidget)
        self.aspIkOriJnt_LE.setObjectName("aspIkOriJnt_LE")
        self.gridLayout.addWidget(self.aspIkOriJnt_LE, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.aspIkOriCtl_LE = QtGui.QLineEdit(self.centralwidget)
        self.aspIkOriCtl_LE.setObjectName("aspIkOriCtl_LE")
        self.gridLayout.addWidget(self.aspIkOriCtl_LE, 1, 1, 1, 1)
        self.aspIkOriCtlLd_btn = QtGui.QPushButton(self.centralwidget)
        self.aspIkOriCtlLd_btn.setObjectName("aspIkOriCtlLd_btn")
        self.gridLayout.addWidget(self.aspIkOriCtlLd_btn, 1, 2, 1, 1)
        self.aspIkOriJntLd_btn = QtGui.QPushButton(self.centralwidget)
        self.aspIkOriJntLd_btn.setObjectName("aspIkOriJntLd_btn")
        self.gridLayout.addWidget(self.aspIkOriJntLd_btn, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        aspIKOriChangeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(aspIKOriChangeWindow)
        QtCore.QMetaObject.connectSlotsByName(aspIKOriChangeWindow)

    def retranslateUi(self, aspIKOriChangeWindow):
        aspIKOriChangeWindow.setWindowTitle(QtGui.QApplication.translate("aspIKOriChangeWindow", "Advance Skeleton IK Controller Orientation Change", None, QtGui.QApplication.UnicodeUTF8))
        self.aspIkOriSet_btn.setText(QtGui.QApplication.translate("aspIKOriChangeWindow", "Set Orientation as Local", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("aspIKOriChangeWindow", "Controller:-", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("aspIKOriChangeWindow", "Joint:-", None, QtGui.QApplication.UnicodeUTF8))
        self.aspIkOriCtlLd_btn.setText(QtGui.QApplication.translate("aspIKOriChangeWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.aspIkOriJntLd_btn.setText(QtGui.QApplication.translate("aspIKOriChangeWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("aspIKOriChangeWindow", "Get joint for orientation value and load controller to chage orientation", None, QtGui.QApplication.UnicodeUTF8))


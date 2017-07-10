# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\amol\bit_bucket\rigtools\rigtools\ui\aspToolsUI\ui_aspIKOriChange.ui'
#
# Created: Thu Mar 23 12:42:50 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets


class Ui_aspIKOriChangeWindow(object):
    def setupUi(self, aspIKOriChangeWindow):
        aspIKOriChangeWindow.setObjectName("aspIKOriChangeWindow")
        aspIKOriChangeWindow.resize(406, 139)
        self.centralwidget = QtWidgets.QWidget(aspIKOriChangeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.aspIkOriSet_btn = QtWidgets.QPushButton(self.centralwidget)
        self.aspIkOriSet_btn.setObjectName("aspIkOriSet_btn")
        self.gridLayout_2.addWidget(self.aspIkOriSet_btn, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.aspIkOriJnt_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.aspIkOriJnt_LE.setObjectName("aspIkOriJnt_LE")
        self.gridLayout.addWidget(self.aspIkOriJnt_LE, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.aspIkOriCtl_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.aspIkOriCtl_LE.setObjectName("aspIkOriCtl_LE")
        self.gridLayout.addWidget(self.aspIkOriCtl_LE, 1, 1, 1, 1)
        self.aspIkOriCtlLd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.aspIkOriCtlLd_btn.setObjectName("aspIkOriCtlLd_btn")
        self.gridLayout.addWidget(self.aspIkOriCtlLd_btn, 1, 2, 1, 1)
        self.aspIkOriJntLd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.aspIkOriJntLd_btn.setObjectName("aspIkOriJntLd_btn")
        self.gridLayout.addWidget(self.aspIkOriJntLd_btn, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        aspIKOriChangeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(aspIKOriChangeWindow)
        QtCore.QMetaObject.connectSlotsByName(aspIKOriChangeWindow)

    def retranslateUi(self, aspIKOriChangeWindow):
        aspIKOriChangeWindow.setWindowTitle(QtWidgets.QApplication.translate("aspIKOriChangeWindow", "Advance Skeleton IK Controller Orientation Change", None))
        self.aspIkOriSet_btn.setText(QtWidgets.QApplication.translate("aspIKOriChangeWindow", "Set Orientation as Local", None))
        self.label_2.setText(QtWidgets.QApplication.translate("aspIKOriChangeWindow", "Controller:-", None))
        self.label.setText(QtWidgets.QApplication.translate("aspIKOriChangeWindow", "Joint:-", None))
        self.aspIkOriCtlLd_btn.setText(QtWidgets.QApplication.translate("aspIKOriChangeWindow", "<<", None))
        self.aspIkOriJntLd_btn.setText(QtWidgets.QApplication.translate("aspIKOriChangeWindow", "<<", None))
        self.label_3.setText(QtWidgets.QApplication.translate("aspIKOriChangeWindow", "Get joint for orientation value and load controller to chage orientation", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S:/bsw_programation/01_maya/Pipeline/rigtools/rigtools/ui/aspToolsUI/ui_aspFingerAttributes.ui'
#
# Created: Thu Aug 24 16:53:10 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FingerAttributeWindow(object):
    def setupUi(self, FingerAttributeWindow):
        FingerAttributeWindow.setObjectName("FingerAttributeWindow")
        FingerAttributeWindow.resize(593, 324)
        self.centralwidget = QtGui.QWidget(FingerAttributeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.aspFaLoadDriver_btn = QtGui.QPushButton(self.centralwidget)
        self.aspFaLoadDriver_btn.setObjectName("aspFaLoadDriver_btn")
        self.gridLayout.addWidget(self.aspFaLoadDriver_btn, 0, 2, 1, 1)
        self.aspFaDriverControllers_LE = QtGui.QLineEdit(self.centralwidget)
        self.aspFaDriverControllers_LE.setObjectName("aspFaDriverControllers_LE")
        self.gridLayout.addWidget(self.aspFaDriverControllers_LE, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.aspFaFingerControllers_LE = QtGui.QLineEdit(self.centralwidget)
        self.aspFaFingerControllers_LE.setObjectName("aspFaFingerControllers_LE")
        self.gridLayout.addWidget(self.aspFaFingerControllers_LE, 1, 1, 1, 1)
        self.aspFaLoadFingers_btn = QtGui.QPushButton(self.centralwidget)
        self.aspFaLoadFingers_btn.setObjectName("aspFaLoadFingers_btn")
        self.gridLayout.addWidget(self.aspFaLoadFingers_btn, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.aspFaCreate_btn = QtGui.QPushButton(self.centralwidget)
        self.aspFaCreate_btn.setObjectName("aspFaCreate_btn")
        self.gridLayout_2.addWidget(self.aspFaCreate_btn, 4, 0, 1, 1)
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fa_scale_x_rb = QtGui.QRadioButton(self.centralwidget)
        self.fa_scale_x_rb.setObjectName("fa_scale_x_rb")

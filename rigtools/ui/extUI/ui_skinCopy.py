# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\amol\bit_bucket\rigtools\rigtools\ui\extUI\ui_skinCopy.ui'
#
# Created: Thu Mar 23 12:43:07 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_skinCopyWindow(object):
    def setupUi(self, skinCopyWindow):
        skinCopyWindow.setObjectName("skinCopyWindow")
        skinCopyWindow.resize(355, 140)
        self.centralwidget = QtGui.QWidget(skinCopyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.copySkin_btn = QtGui.QPushButton(self.centralwidget)
        self.copySkin_btn.setObjectName("copySkin_btn")
        self.horizontalLayout.addWidget(self.copySkin_btn)
        self.skin_copySkin_btn = QtGui.QPushButton(self.centralwidget)
        self.skin_copySkin_btn.setObjectName("skin_copySkin_btn")
        self.horizontalLayout.addWidget(self.skin_copySkin_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.destMeshLoad_btn = QtGui.QPushButton(self.centralwidget)
        self.destMeshLoad_btn.setObjectName("destMeshLoad_btn")
        self.gridLayout.addWidget(self.destMeshLoad_btn, 1, 2, 1, 1)
        self.sourceMesh_LE = QtGui.QLineEdit(self.centralwidget)
        self.sourceMesh_LE.setObjectName("sourceMesh_LE")
        self.gridLayout.addWidget(self.sourceMesh_LE, 0, 1, 1, 1)
        self.sourceMeshLoad_btn = QtGui.QPushButton(self.centralwidget)
        self.sourceMeshLoad_btn.setObjectName("sourceMeshLoad_btn")
        self.gridLayout.addWidget(self.sourceMeshLoad_btn, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.destMesh_LE = QtGui.QLineEdit(self.centralwidget)
        self.destMesh_LE.setObjectName("destMesh_LE")
        self.gridLayout.addWidget(self.destMesh_LE, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        skinCopyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(skinCopyWindow)
        QtCore.QMetaObject.connectSlotsByName(skinCopyWindow)

    def retranslateUi(self, skinCopyWindow):
        skinCopyWindow.setWindowTitle(
            QtGui.QApplication.translate("skinCopyWindow", "Copy Skin", None, QtGui.QApplication.UnicodeUTF8))
        self.copySkin_btn.setText(
            QtGui.QApplication.translate("skinCopyWindow", "Copy Skin", None, QtGui.QApplication.UnicodeUTF8))
        self.skin_copySkin_btn.setText(
            QtGui.QApplication.translate("skinCopyWindow", "Skin And Copy Skin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("skinCopyWindow", "Destionation Mesh:-", None, QtGui.QApplication.UnicodeUTF8))
        self.destMeshLoad_btn.setText(
            QtGui.QApplication.translate("skinCopyWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.sourceMeshLoad_btn.setText(
            QtGui.QApplication.translate("skinCopyWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("skinCopyWindow", "Source Mesh:-", None, QtGui.QApplication.UnicodeUTF8))

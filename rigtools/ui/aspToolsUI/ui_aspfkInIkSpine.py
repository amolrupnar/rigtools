# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\amol\bit_bucket\rigtools\rigtools\ui\aspToolsUI\ui_aspfkInIkSpine.ui'
#
# Created: Sat Mar 25 12:59:16 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets


class Ui_FkInIkSpineWindow(object):
    def setupUi(self, FkInIkSpineWindow):
        FkInIkSpineWindow.setObjectName("FkInIkSpineWindow")
        FkInIkSpineWindow.resize(483, 244)
        self.centralwidget = QtWidgets.QWidget(FkInIkSpineWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.fkInIkSp_ctlName_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.fkInIkSp_ctlName_LE.setObjectName("fkInIkSp_ctlName_LE")
        self.gridLayout_2.addWidget(self.fkInIkSp_ctlName_LE, 0, 1, 1, 1)
        self.fkInIkSp_ctlNum_spbx = QtWidgets.QSpinBox(self.centralwidget)
        self.fkInIkSp_ctlNum_spbx.setMinimum(4)
        self.fkInIkSp_ctlNum_spbx.setObjectName("fkInIkSp_ctlNum_spbx")
        self.gridLayout_2.addWidget(self.fkInIkSp_ctlNum_spbx, 0, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.fkInIkSp_HipCtls_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fkInIkSp_HipCtls_btn.setObjectName("fkInIkSp_HipCtls_btn")
        self.gridLayout.addWidget(self.fkInIkSp_HipCtls_btn, 2, 2, 1, 1)
        self.fkInIkSp_EndCtl_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fkInIkSp_EndCtl_btn.setObjectName("fkInIkSp_EndCtl_btn")
        self.gridLayout.addWidget(self.fkInIkSp_EndCtl_btn, 1, 2, 1, 1)
        self.fkInIkSp_HipCtls_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.fkInIkSp_HipCtls_LE.setObjectName("fkInIkSp_HipCtls_LE")
        self.gridLayout.addWidget(self.fkInIkSp_HipCtls_LE, 2, 1, 1, 1)
        self.fkInIkSp_StartCtl_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.fkInIkSp_StartCtl_LE.setObjectName("fkInIkSp_StartCtl_LE")
        self.gridLayout.addWidget(self.fkInIkSp_StartCtl_LE, 0, 1, 1, 1)
        self.fkInIkSp_StartCtl_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fkInIkSp_StartCtl_btn.setObjectName("fkInIkSp_StartCtl_btn")
        self.gridLayout.addWidget(self.fkInIkSp_StartCtl_btn, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.fkInIkSp_EndCtl_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.fkInIkSp_EndCtl_LE.setObjectName("fkInIkSp_EndCtl_LE")
        self.gridLayout.addWidget(self.fkInIkSp_EndCtl_LE, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.fkInIkSp_create_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fkInIkSp_create_btn.setObjectName("fkInIkSp_create_btn")
        self.gridLayout_3.addWidget(self.fkInIkSp_create_btn, 2, 0, 1, 1)
        FkInIkSpineWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FkInIkSpineWindow)
        QtCore.QMetaObject.connectSlotsByName(FkInIkSpineWindow)

    def retranslateUi(self, FkInIkSpineWindow):
        FkInIkSpineWindow.setWindowTitle(
            QtWidgets.QApplication.translate("FkInIkSpineWindow", "fk in ik spine", None))
        self.label_2.setText(QtWidgets.QApplication.translate("FkInIkSpineWindow", "Controller Name:-", None))
        self.label_5.setText(QtWidgets.QApplication.translate("FkInIkSpineWindow", "Controller Numbers:-", None))
        self.fkInIkSp_ctlName_LE.setText(
            QtWidgets.QApplication.translate("FkInIkSpineWindow", "Fk_Spine", None))
        self.label_3.setText(QtWidgets.QApplication.translate("FkInIkSpineWindow", "IK End Controller:-", None))
        self.fkInIkSp_HipCtls_btn.setText(
            QtWidgets.QApplication.translate("FkInIkSpineWindow", "<<", None))
        self.fkInIkSp_EndCtl_btn.setText(
            QtWidgets.QApplication.translate("FkInIkSpineWindow", "<<", None))
        self.fkInIkSp_StartCtl_btn.setText(
            QtWidgets.QApplication.translate("FkInIkSpineWindow", "<<", None))
        self.label.setText(QtWidgets.QApplication.translate("FkInIkSpineWindow", "IK Start Controller:-", None))
        self.label_4.setText(QtWidgets.QApplication.translate("FkInIkSpineWindow", "Hip Controllers Group:-", None))
        self.fkInIkSp_create_btn.setText(
            QtWidgets.QApplication.translate("FkInIkSpineWindow", "Create", None))

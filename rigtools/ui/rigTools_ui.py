# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\amol\bit_bucket\rigtools\rigtools\ui\rigTools_ui.ui'
#
# Created: Tue May 02 11:54:54 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(500, 900)
        mainWindow.setMinimumSize(QtCore.QSize(500, 900))
        mainWindow.setMaximumSize(QtCore.QSize(500, 900))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sanity_check_btn = QtGui.QPushButton(self.centralwidget)
        self.sanity_check_btn.setGeometry(QtCore.QRect(20, 20, 75, 25))
        self.sanity_check_btn.setMinimumSize(QtCore.QSize(75, 25))
        self.sanity_check_btn.setMaximumSize(QtCore.QSize(75, 25))
        self.sanity_check_btn.setObjectName("sanity_check_btn")
        self.joint_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.joint_groupBox.setGeometry(QtCore.QRect(20, 60, 460, 241))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.joint_groupBox.sizePolicy().hasHeightForWidth())
        self.joint_groupBox.setSizePolicy(sizePolicy)
        self.joint_groupBox.setObjectName("joint_groupBox")
        self.parent_btn = QtGui.QPushButton(self.joint_groupBox)
        self.parent_btn.setGeometry(QtCore.QRect(10, 56, 75, 23))
        self.parent_btn.setObjectName("parent_btn")
        self.aimCons_groupBox = QtGui.QGroupBox(self.joint_groupBox)
        self.aimCons_groupBox.setGeometry(QtCore.QRect(90, 20, 361, 141))
        self.aimCons_groupBox.setObjectName("aimCons_groupBox")
        self.aim_constraint_btn = QtGui.QPushButton(self.aimCons_groupBox)
        self.aim_constraint_btn.setGeometry(QtCore.QRect(120, 76, 101, 23))
        self.aim_constraint_btn.setObjectName("aim_constraint_btn")
        self.aim_constraint_parent_btn = QtGui.QPushButton(self.aimCons_groupBox)
        self.aim_constraint_parent_btn.setGeometry(QtCore.QRect(230, 76, 121, 23))
        self.aim_constraint_parent_btn.setObjectName("aim_constraint_parent_btn")
        self.orient_chain_btn = QtGui.QPushButton(self.aimCons_groupBox)
        self.orient_chain_btn.setGeometry(QtCore.QRect(10, 76, 101, 23))
        self.orient_chain_btn.setObjectName("orient_chain_btn")
        self.label = QtGui.QLabel(self.aimCons_groupBox)
        self.label.setGeometry(QtCore.QRect(40, 15, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.aimCons_groupBox)
        self.label_2.setGeometry(QtCore.QRect(230, 15, 81, 16))
        self.label_2.setObjectName("label_2")
        self.line = QtGui.QFrame(self.aimCons_groupBox)
        self.line.setGeometry(QtCore.QRect(165, 35, 20, 31))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.none_Orient_btn = QtGui.QPushButton(self.aimCons_groupBox)
        self.none_Orient_btn.setGeometry(QtCore.QRect(120, 110, 101, 23))
        self.none_Orient_btn.setObjectName("none_Orient_btn")
        self.line_2 = QtGui.QFrame(self.aimCons_groupBox)
        self.line_2.setGeometry(QtCore.QRect(10, 95, 341, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtGui.QFrame(self.aimCons_groupBox)
        self.frame.setGeometry(QtCore.QRect(10, 30, 151, 41))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.aimX_rb = QtGui.QRadioButton(self.frame)
        self.aimX_rb.setGeometry(QtCore.QRect(20, 13, 31, 17))
        self.aimX_rb.setChecked(True)
        self.aimX_rb.setObjectName("aimX_rb")
        self.aimY_rb = QtGui.QRadioButton(self.frame)
        self.aimY_rb.setGeometry(QtCore.QRect(60, 13, 31, 17))
        self.aimY_rb.setObjectName("aimY_rb")
        self.aimZ_rb = QtGui.QRadioButton(self.frame)
        self.aimZ_rb.setGeometry(QtCore.QRect(100, 13, 31, 17))
        self.aimZ_rb.setObjectName("aimZ_rb")
        self.frame_2 = QtGui.QFrame(self.aimCons_groupBox)
        self.frame_2.setGeometry(QtCore.QRect(190, 30, 151, 41))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.aimObX_rb = QtGui.QRadioButton(self.frame_2)
        self.aimObX_rb.setGeometry(QtCore.QRect(20, 13, 31, 17))
        self.aimObX_rb.setObjectName("aimObX_rb")
        self.aimObY_rb = QtGui.QRadioButton(self.frame_2)
        self.aimObY_rb.setGeometry(QtCore.QRect(60, 13, 31, 17))
        self.aimObY_rb.setObjectName("aimObY_rb")
        self.aimObZ_rb = QtGui.QRadioButton(self.frame_2)
        self.aimObZ_rb.setGeometry(QtCore.QRect(100, 13, 31, 17))
        self.aimObZ_rb.setChecked(True)
        self.aimObZ_rb.setObjectName("aimObZ_rb")
        self.multipleCons_groupBox = QtGui.QGroupBox(self.joint_groupBox)
        self.multipleCons_groupBox.setGeometry(QtCore.QRect(10, 170, 441, 61))
        self.multipleCons_groupBox.setObjectName("multipleCons_groupBox")
        self.point_constraint_btn = QtGui.QPushButton(self.multipleCons_groupBox)
        self.point_constraint_btn.setGeometry(QtCore.QRect(110, 20, 100, 25))
        self.point_constraint_btn.setObjectName("point_constraint_btn")
        self.orient_constraint_btn = QtGui.QPushButton(self.multipleCons_groupBox)
        self.orient_constraint_btn.setGeometry(QtCore.QRect(220, 20, 100, 25))
        self.orient_constraint_btn.setObjectName("orient_constraint_btn")
        self.parent_constraint_btn = QtGui.QPushButton(self.multipleCons_groupBox)
        self.parent_constraint_btn.setGeometry(QtCore.QRect(330, 20, 100, 25))
        self.parent_constraint_btn.setObjectName("parent_constraint_btn")
        self.maintainOffset_cb = QtGui.QCheckBox(self.multipleCons_groupBox)
        self.maintainOffset_cb.setGeometry(QtCore.QRect(10, 25, 101, 17))
        self.maintainOffset_cb.setChecked(True)
        self.maintainOffset_cb.setObjectName("maintainOffset_cb")
        self.Zero_Out_btn = QtGui.QPushButton(self.joint_groupBox)
        self.Zero_Out_btn.setGeometry(QtCore.QRect(10, 86, 75, 23))
        self.Zero_Out_btn.setObjectName("Zero_Out_btn")
        self.jointSel_btn = QtGui.QPushButton(self.joint_groupBox)
        self.jointSel_btn.setGeometry(QtCore.QRect(10, 26, 75, 23))
        self.jointSel_btn.setObjectName("jointSel_btn")
        self.Select_All_btn = QtGui.QPushButton(self.joint_groupBox)
        self.Select_All_btn.setGeometry(QtCore.QRect(10, 115, 75, 23))
        self.Select_All_btn.setObjectName("Select_All_btn")
        self.Find_Duplicates_btn = QtGui.QPushButton(self.centralwidget)
        self.Find_Duplicates_btn.setGeometry(QtCore.QRect(110, 20, 100, 25))
        self.Find_Duplicates_btn.setMinimumSize(QtCore.QSize(74, 25))
        self.Find_Duplicates_btn.setMaximumSize(QtCore.QSize(100, 25))
        self.Find_Duplicates_btn.setObjectName("Find_Duplicates_btn")
        self.controller_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.controller_groupBox.setGeometry(QtCore.QRect(20, 310, 461, 111))
        self.controller_groupBox.setObjectName("controller_groupBox")
        self.FK_btn = QtGui.QPushButton(self.controller_groupBox)
        self.FK_btn.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.FK_btn.setObjectName("FK_btn")
        self.FK_Proxy_btn = QtGui.QPushButton(self.controller_groupBox)
        self.FK_Proxy_btn.setGeometry(QtCore.QRect(310, 70, 75, 23))
        self.FK_Proxy_btn.setObjectName("FK_Proxy_btn")
        self.label_3 = QtGui.QLabel(self.controller_groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label_3.setObjectName("label_3")
        self.negTrans_cb = QtGui.QCheckBox(self.controller_groupBox)
        self.negTrans_cb.setGeometry(QtCore.QRect(310, 40, 70, 17))
        self.negTrans_cb.setObjectName("negTrans_cb")
        self.ctlAxis_X_rb = QtGui.QRadioButton(self.controller_groupBox)
        self.ctlAxis_X_rb.setGeometry(QtCore.QRect(20, 40, 31, 17))
        self.ctlAxis_X_rb.setChecked(True)
        self.ctlAxis_X_rb.setObjectName("ctlAxis_X_rb")
        self.ctlAxis_Y_rb = QtGui.QRadioButton(self.controller_groupBox)
        self.ctlAxis_Y_rb.setGeometry(QtCore.QRect(60, 40, 31, 17))
        self.ctlAxis_Y_rb.setObjectName("ctlAxis_Y_rb")
        self.ctlAxis_Z_rb = QtGui.QRadioButton(self.controller_groupBox)
        self.ctlAxis_Z_rb.setGeometry(QtCore.QRect(100, 40, 31, 17))
        self.ctlAxis_Z_rb.setObjectName("ctlAxis_Z_rb")
        self.skin_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.skin_groupBox.setGeometry(QtCore.QRect(20, 440, 461, 81))
        self.skin_groupBox.setObjectName("skin_groupBox")
        self.select_Influence_object_btn = QtGui.QPushButton(self.skin_groupBox)
        self.select_Influence_object_btn.setGeometry(QtCore.QRect(10, 20, 131, 23))
        self.select_Influence_object_btn.setObjectName("select_Influence_object_btn")
        self.copySkinOnMultipleObject_btn = QtGui.QPushButton(self.skin_groupBox)
        self.copySkinOnMultipleObject_btn.setGeometry(QtCore.QRect(160, 20, 141, 23))
        self.copySkinOnMultipleObject_btn.setObjectName("copySkinOnMultipleObject_btn")
        self.ShiftShapeConnections_btn = QtGui.QPushButton(self.skin_groupBox)
        self.ShiftShapeConnections_btn.setGeometry(QtCore.QRect(320, 20, 131, 23))
        self.ShiftShapeConnections_btn.setObjectName("ShiftShapeConnections_btn")
        self.Renamer_btn = QtGui.QPushButton(self.centralwidget)
        self.Renamer_btn.setGeometry(QtCore.QRect(230, 20, 100, 25))
        self.Renamer_btn.setMinimumSize(QtCore.QSize(74, 25))
        self.Renamer_btn.setMaximumSize(QtCore.QSize(100, 25))
        self.Renamer_btn.setObjectName("Renamer_btn")
        self.advanceSkeleton_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.advanceSkeleton_groupBox.setGeometry(QtCore.QRect(20, 540, 461, 151))
        self.advanceSkeleton_groupBox.setObjectName("advanceSkeleton_groupBox")
        self.IK_Orient_btn = QtGui.QPushButton(self.advanceSkeleton_groupBox)
        self.IK_Orient_btn.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.IK_Orient_btn.setObjectName("IK_Orient_btn")
        self.FingerSDK_btn = QtGui.QPushButton(self.advanceSkeleton_groupBox)
        self.FingerSDK_btn.setGeometry(QtCore.QRect(110, 30, 75, 23))
        self.FingerSDK_btn.setObjectName("FingerSDK_btn")
        self.FK_in_IKSpine_btn = QtGui.QPushButton(self.advanceSkeleton_groupBox)
        self.FK_in_IKSpine_btn.setGeometry(QtCore.QRect(200, 30, 81, 23))
        self.FK_in_IKSpine_btn.setObjectName("FK_in_IKSpine_btn")
        self.Follow_groupBox = QtGui.QGroupBox(self.advanceSkeleton_groupBox)
        self.Follow_groupBox.setGeometry(QtCore.QRect(20, 70, 421, 61))
        self.Follow_groupBox.setObjectName("Follow_groupBox")
        self.IKArm_btn = QtGui.QPushButton(self.Follow_groupBox)
        self.IKArm_btn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.IKArm_btn.setObjectName("IKArm_btn")
        self.PoleArm_btn = QtGui.QPushButton(self.Follow_groupBox)
        self.PoleArm_btn.setGeometry(QtCore.QRect(120, 20, 75, 23))
        self.PoleArm_btn.setObjectName("PoleArm_btn")
        self.Hide_Extra_Joints_btn = QtGui.QPushButton(self.advanceSkeleton_groupBox)
        self.Hide_Extra_Joints_btn.setGeometry(QtCore.QRect(300, 30, 101, 23))
        self.Hide_Extra_Joints_btn.setObjectName("Hide_Extra_Joints_btn")
        self.otherScript_groupBox = QtGui.QGroupBox(self.centralwidget)
        self.otherScript_groupBox.setGeometry(QtCore.QRect(20, 699, 461, 101))
        self.otherScript_groupBox.setObjectName("otherScript_groupBox")
        self.WireTool_btn = QtGui.QPushButton(self.otherScript_groupBox)
        self.WireTool_btn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.WireTool_btn.setObjectName("WireTool_btn")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionFile = QtGui.QAction(mainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionExit = QtGui.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionFile)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "RigTools MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.sanity_check_btn.setText(QtGui.QApplication.translate("mainWindow", "sanity_check", None, QtGui.QApplication.UnicodeUTF8))
        self.joint_groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Joint", None, QtGui.QApplication.UnicodeUTF8))
        self.parent_btn.setText(QtGui.QApplication.translate("mainWindow", "parent", None, QtGui.QApplication.UnicodeUTF8))
        self.aimCons_groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Aim Constraint And Orient two Joints and Hirarchy", None, QtGui.QApplication.UnicodeUTF8))
        self.aim_constraint_btn.setText(QtGui.QApplication.translate("mainWindow", "aim_constraint", None, QtGui.QApplication.UnicodeUTF8))
        self.aim_constraint_parent_btn.setText(QtGui.QApplication.translate("mainWindow", "aim_constraint_parent", None, QtGui.QApplication.UnicodeUTF8))
        self.orient_chain_btn.setText(QtGui.QApplication.translate("mainWindow", "orient_chain", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mainWindow", "aim axis", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mainWindow", "object up axis", None, QtGui.QApplication.UnicodeUTF8))
        self.none_Orient_btn.setText(QtGui.QApplication.translate("mainWindow", "none_Orient", None, QtGui.QApplication.UnicodeUTF8))
        self.aimX_rb.setText(QtGui.QApplication.translate("mainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.aimY_rb.setText(QtGui.QApplication.translate("mainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.aimZ_rb.setText(QtGui.QApplication.translate("mainWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.aimObX_rb.setText(QtGui.QApplication.translate("mainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.aimObY_rb.setText(QtGui.QApplication.translate("mainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.aimObZ_rb.setText(QtGui.QApplication.translate("mainWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.multipleCons_groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Constraint Multiple Object", None, QtGui.QApplication.UnicodeUTF8))
        self.point_constraint_btn.setText(QtGui.QApplication.translate("mainWindow", "point_constraint", None, QtGui.QApplication.UnicodeUTF8))
        self.orient_constraint_btn.setText(QtGui.QApplication.translate("mainWindow", "orient_constraint", None, QtGui.QApplication.UnicodeUTF8))
        self.parent_constraint_btn.setText(QtGui.QApplication.translate("mainWindow", "parent_constraint", None, QtGui.QApplication.UnicodeUTF8))
        self.maintainOffset_cb.setText(QtGui.QApplication.translate("mainWindow", "Maintain Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.Zero_Out_btn.setText(QtGui.QApplication.translate("mainWindow", "Zero_Out", None, QtGui.QApplication.UnicodeUTF8))
        self.jointSel_btn.setText(QtGui.QApplication.translate("mainWindow", "joint@sel", None, QtGui.QApplication.UnicodeUTF8))
        self.Select_All_btn.setText(QtGui.QApplication.translate("mainWindow", "Select_All", None, QtGui.QApplication.UnicodeUTF8))
        self.Find_Duplicates_btn.setText(QtGui.QApplication.translate("mainWindow", "Find_Duplicates", None, QtGui.QApplication.UnicodeUTF8))
        self.controller_groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.FK_btn.setText(QtGui.QApplication.translate("mainWindow", "FK", None, QtGui.QApplication.UnicodeUTF8))
        self.FK_Proxy_btn.setText(QtGui.QApplication.translate("mainWindow", "FK_Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mainWindow", "axis", None, QtGui.QApplication.UnicodeUTF8))
        self.negTrans_cb.setText(QtGui.QApplication.translate("mainWindow", "Neg Trans", None, QtGui.QApplication.UnicodeUTF8))
        self.ctlAxis_X_rb.setText(QtGui.QApplication.translate("mainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.ctlAxis_Y_rb.setText(QtGui.QApplication.translate("mainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.ctlAxis_Z_rb.setText(QtGui.QApplication.translate("mainWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.skin_groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Skin", None, QtGui.QApplication.UnicodeUTF8))
        self.select_Influence_object_btn.setText(QtGui.QApplication.translate("mainWindow", "select_Influence_object", None, QtGui.QApplication.UnicodeUTF8))
        self.copySkinOnMultipleObject_btn.setText(QtGui.QApplication.translate("mainWindow", "Copy Skin UI", None, QtGui.QApplication.UnicodeUTF8))
        self.ShiftShapeConnections_btn.setText(QtGui.QApplication.translate("mainWindow", "Shift Shape Connections", None, QtGui.QApplication.UnicodeUTF8))
        self.Renamer_btn.setText(QtGui.QApplication.translate("mainWindow", "Renamer", None, QtGui.QApplication.UnicodeUTF8))
        self.advanceSkeleton_groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Advance Skeleton Scripts", None, QtGui.QApplication.UnicodeUTF8))
        self.IK_Orient_btn.setText(QtGui.QApplication.translate("mainWindow", "IK_Orient", None, QtGui.QApplication.UnicodeUTF8))
        self.FingerSDK_btn.setText(QtGui.QApplication.translate("mainWindow", "FingerSDK", None, QtGui.QApplication.UnicodeUTF8))
        self.FK_in_IKSpine_btn.setText(QtGui.QApplication.translate("mainWindow", "FK_in_IKSpine", None, QtGui.QApplication.UnicodeUTF8))
        self.Follow_groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Follow", None, QtGui.QApplication.UnicodeUTF8))
        self.IKArm_btn.setText(QtGui.QApplication.translate("mainWindow", "IKArm", None, QtGui.QApplication.UnicodeUTF8))
        self.PoleArm_btn.setText(QtGui.QApplication.translate("mainWindow", "PoleArm", None, QtGui.QApplication.UnicodeUTF8))
        self.Hide_Extra_Joints_btn.setText(QtGui.QApplication.translate("mainWindow", "Hide_Extra_Joints", None, QtGui.QApplication.UnicodeUTF8))
        self.otherScript_groupBox.setTitle(QtGui.QApplication.translate("mainWindow", "Other Script", None, QtGui.QApplication.UnicodeUTF8))
        self.WireTool_btn.setText(QtGui.QApplication.translate("mainWindow", "WireTool", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("mainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFile.setText(QtGui.QApplication.translate("mainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("mainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))


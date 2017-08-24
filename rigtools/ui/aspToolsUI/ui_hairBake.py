# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S:/bsw_programation/01_maya/Pipeline/rigtools/rigtools/ui/aspToolsUI/ui_hairBake.ui'
#
# Created: Thu Aug 24 16:52:35 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_hairBakeWindow(object):
    def setupUi(self, hairBakeWindow):
        hairBakeWindow.setObjectName("hairBakeWindow")
        hairBakeWindow.resize(456, 392)
        self.centralwidget = QtGui.QWidget(hairBakeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dynParticle_LW = QtGui.QListWidget(self.centralwidget)
        self.dynParticle_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.dynParticle_LW.setObjectName("dynParticle_LW")
        self.gridLayout.addWidget(self.dynParticle_LW, 1, 1, 1, 1)
        self.unbake_btn = QtGui.QPushButton(self.centralwidget)
        self.unbake_btn.setObjectName("unbake_btn")
        self.gridLayout.addWidget(self.unbake_btn, 3, 1, 1, 1)
        self.char_lbl = QtGui.QLabel(self.centralwidget)
        self.char_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.char_lbl.setObjectName("char_lbl")
        self.gridLayout.addWidget(self.char_lbl, 0, 0, 1, 1)
        self.dynPartilce_lbl = QtGui.QLabel(self.centralwidget)
        self.dynPartilce_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.dynPartilce_lbl.setObjectName("dynPartilce_lbl")
        self.gridLayout.addWidget(self.dynPartilce_lbl, 0, 1, 1, 1)
        self.bake_btn = QtGui.QPushButton(self.centralwidget)
        self.bake_btn.setObjectName("bake_btn")
        self.gridLayout.addWidget(self.bake_btn, 3, 0, 1, 1)
        self.characters_LW = QtGui.QListWidget(self.centralwidget)
        self.characters_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.characters_LW.setObjectName("characters_LW")
        self.gridLayout.addWidget(self.characters_LW, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        hairBakeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(hairBakeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        hairBakeWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(hairBakeWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(hairBakeWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), hairBakeWindow.close)
        QtCore.QMetaObject.connectSlotsByName(hairBakeWindow)

    def retranslateUi(self, hairBakeWindow):
        hairBakeWindow.setWindowTitle(QtGui.QApplication.translate("hairBakeWindow", "Hair Bake Unbake Window", None, QtGui.QApplication.UnicodeUTF8))
        self.unbake_btn.setText(QtGui.QApplication.translate("hairBakeWindow", "Unbake", None, QtGui.QApplication.UnicodeUTF8))
        self.char_lbl.setText(QtGui.QApplication.translate("hairBakeWindow", "Characters", None, QtGui.QApplication.UnicodeUTF8))
        self.dynPartilce_lbl.setText(QtGui.QApplication.translate("hairBakeWindow", "Dynamics", None, QtGui.QApplication.UnicodeUTF8))
        self.bake_btn.setText(QtGui.QApplication.translate("hairBakeWindow", "Bake", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("hairBakeWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("hairBakeWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))


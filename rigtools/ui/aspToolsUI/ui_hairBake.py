# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\amol\bit_bucket\rigtools\rigtools\ui\aspToolsUI\ui_hairBake.ui'
#
# Created: Tue May 30 17:47:26 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_hairBakeWindow(object):
    def setupUi(self, hairBakeWindow):
        hairBakeWindow.setObjectName("hairBakeWindow")
        hairBakeWindow.resize(456, 392)
        self.centralwidget = QtWidgets.QWidget(hairBakeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dynParticle_LW = QtWidgets.QListWidget(self.centralwidget)
        self.dynParticle_LW.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.dynParticle_LW.setObjectName("dynParticle_LW")
        self.gridLayout.addWidget(self.dynParticle_LW, 1, 1, 1, 1)
        self.unbake_btn = QtWidgets.QPushButton(self.centralwidget)
        self.unbake_btn.setObjectName("unbake_btn")
        self.gridLayout.addWidget(self.unbake_btn, 3, 1, 1, 1)
        self.char_lbl = QtWidgets.QLabel(self.centralwidget)
        self.char_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.char_lbl.setObjectName("char_lbl")
        self.gridLayout.addWidget(self.char_lbl, 0, 0, 1, 1)
        self.dynPartilce_lbl = QtWidgets.QLabel(self.centralwidget)
        self.dynPartilce_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.dynPartilce_lbl.setObjectName("dynPartilce_lbl")
        self.gridLayout.addWidget(self.dynPartilce_lbl, 0, 1, 1, 1)
        self.bake_btn = QtWidgets.QPushButton(self.centralwidget)
        self.bake_btn.setObjectName("bake_btn")
        self.gridLayout.addWidget(self.bake_btn, 3, 0, 1, 1)
        self.characters_LW = QtWidgets.QListWidget(self.centralwidget)
        self.characters_LW.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.characters_LW.setObjectName("characters_LW")
        self.gridLayout.addWidget(self.characters_LW, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        hairBakeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hairBakeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        hairBakeWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(hairBakeWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(hairBakeWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), hairBakeWindow.close)
        QtCore.QMetaObject.connectSlotsByName(hairBakeWindow)

    def retranslateUi(self, hairBakeWindow):
        hairBakeWindow.setWindowTitle(QtWidgets.QApplication.translate("hairBakeWindow", "Hair Bake Unbake Window", None))
        self.unbake_btn.setText(QtWidgets.QApplication.translate("hairBakeWindow", "Unbake", None))
        self.char_lbl.setText(QtWidgets.QApplication.translate("hairBakeWindow", "Characters", None))
        self.dynPartilce_lbl.setText(QtWidgets.QApplication.translate("hairBakeWindow", "Dynamics", None))
        self.bake_btn.setText(QtWidgets.QApplication.translate("hairBakeWindow", "Bake", None))
        self.menuMenu.setTitle(QtWidgets.QApplication.translate("hairBakeWindow", "Menu", None))
        self.actionExit.setText(QtWidgets.QApplication.translate("hairBakeWindow", "Exit", None))


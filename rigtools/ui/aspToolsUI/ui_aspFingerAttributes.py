# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\amol\bit_bucket\rigtools\rigtools\ui\aspToolsUI\ui_aspFingerAttributes.ui'
#
# Created: Thu Mar 23 12:42:44 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_FingerAttributeWindow(object):
    def setupUi(self, FingerAttributeWindow):
        FingerAttributeWindow.setObjectName("FingerAttributeWindow")
        FingerAttributeWindow.resize(440, 288)
        self.centralwidget = QtGui.QWidget(FingerAttributeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.aspFaTwist_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaTwist_cb.setObjectName("aspFaTwist_cb")
        self.gridLayout_3.addWidget(self.aspFaTwist_cb, 1, 1, 1, 1)
        self.aspFaLean_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaLean_cb.setObjectName("aspFaLean_cb")
        self.gridLayout_3.addWidget(self.aspFaLean_cb, 2, 0, 1, 1)
        self.aspFaScale_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaScale_cb.setObjectName("aspFaScale_cb")
        self.gridLayout_3.addWidget(self.aspFaScale_cb, 2, 1, 1, 1)
        self.aspFaRelax_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaRelax_cb.setObjectName("aspFaRelax_cb")
        self.gridLayout_3.addWidget(self.aspFaRelax_cb, 3, 0, 1, 1)
        self.aspFaScrunch_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaScrunch_cb.setObjectName("aspFaScrunch_cb")
        self.gridLayout_3.addWidget(self.aspFaScrunch_cb, 1, 0, 1, 1)
        self.aspFaFist_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaFist_cb.setObjectName("aspFaFist_cb")
        self.gridLayout_3.addWidget(self.aspFaFist_cb, 4, 0, 1, 1)
        self.aspFaReverse_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaReverse_cb.setObjectName("aspFaReverse_cb")
        self.gridLayout_3.addWidget(self.aspFaReverse_cb, 3, 1, 1, 1)
        self.aspFaCup_cb = QtGui.QCheckBox(self.centralwidget)
        self.aspFaCup_cb.setObjectName("aspFaCup_cb")
        self.gridLayout_3.addWidget(self.aspFaCup_cb, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aspFaAxisX_rb = QtGui.QRadioButton(self.centralwidget)
        self.aspFaAxisX_rb.setChecked(True)
        self.aspFaAxisX_rb.setObjectName("aspFaAxisX_rb")
        self.horizontalLayout.addWidget(self.aspFaAxisX_rb)
        self.aspFaAxisY_rb = QtGui.QRadioButton(self.centralwidget)
        self.aspFaAxisY_rb.setObjectName("aspFaAxisY_rb")
        self.horizontalLayout.addWidget(self.aspFaAxisY_rb)
        self.aspFaAxisZ_rb = QtGui.QRadioButton(self.centralwidget)
        self.aspFaAxisZ_rb.setObjectName("aspFaAxisZ_rb")
        self.horizontalLayout.addWidget(self.aspFaAxisZ_rb)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 2, 1)
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
        FingerAttributeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FingerAttributeWindow)
        QtCore.QMetaObject.connectSlotsByName(FingerAttributeWindow)

    def retranslateUi(self, FingerAttributeWindow):
        FingerAttributeWindow.setWindowTitle(
            QtGui.QApplication.translate("FingerAttributeWindow", "ASP Add Finger Attributes", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("FingerAttributeWindow",
                                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                "p, li { white-space: pre-wrap; }\n"
                                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1) Select Finger Controllers in order like</p>\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">IndexFinger1, IndexFinger2, IndexFinger3</span></p>\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2) on check box for add selected attributes.</p>\n"
                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3) create.</p></body></html>",
                                                                None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaTwist_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Twist", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaLean_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Lean", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaScale_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaRelax_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Relax", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaScrunch_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Scrunch", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaFist_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Fist", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaReverse_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Reverse", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaCup_cb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Cup", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FingerAttributeWindow", "Set Controller Axis:-", None,
                                                        QtGui.QApplication.UnicodeUTF8))
        self.aspFaAxisX_rb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaAxisY_rb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaAxisZ_rb.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.aspFaLoadDriver_btn.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FingerAttributeWindow", "Driver Controller:-", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.aspFaLoadFingers_btn.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FingerAttributeWindow", "Controllers:-", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.aspFaCreate_btn.setText(
            QtGui.QApplication.translate("FingerAttributeWindow", "Create", None, QtGui.QApplication.UnicodeUTF8))

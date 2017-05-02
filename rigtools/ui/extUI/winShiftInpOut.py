from PySide import QtGui

from rigtools import maya_utils
from rigtools.ui import ui_fill
from rigtools.ui.extUI import ui_shiftInpOut
from rigtools.ext import skin, gen
from rigtools.ext import selection


class ShiftInpOutConn(QtGui.QMainWindow, ui_shiftInpOut.Ui_ShiftInpOutConnWindow):
    def __init__(self, prnt):
        super(ShiftInpOutConn, self).__init__(prnt)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.newShapeCreate_btn.clicked.connect(self.createNewShapeConn)
        self.srcInpLd_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.srcInp_LE))
        self.srcOutLd_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.srcOut_LE))
        self.destInpLd_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.destInp_LE))
        self.destOutLd_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.destOut_LE))
        self.shiftConnections_btn.clicked.connect(self.shiftInpOutConn)

    def createNewShapeConn(self):
        parent = selection.getSelection()[0]
        newShapeName = self.newShpName_LE.text()
        gen.createAndParentNewShape(parent, newShapeName)

    def shiftInpOutConn(self):
        sourceInpShp = self.srcInp_LE.text()
        sourceOutShp = self.srcOut_LE.text()
        destInpShp = self.destInp_LE.text()
        destOutShp = self.destOut_LE.text()
        skin.shiftInputOutputConnections(sourceInpShp, sourceOutShp, destInpShp, destOutShp)


def main():
    winClass = ShiftInpOutConn(maya_utils.maya_main_window())
    return winClass.show()

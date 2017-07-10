from PySide2 import QtWidgets

from rigtools.ui import ar_qui
from rigtools.ui import ar_uiFill
from rigtools.ui.extUI import ui_shiftInpOut
from rigtools.ext import ar_skin, ar_gen
from rigtools.ext import ar_selection

reload(ar_qui)
reload(ar_uiFill)
reload(ui_shiftInpOut)
reload(ar_skin)
reload(ar_gen)
reload(ar_selection)


class ShiftInpOutConn(QtWidgets.QMainWindow, ui_shiftInpOut.Ui_ShiftInpOutConnWindow):
    def __init__(self, parent):
        super(ShiftInpOutConn, self).__init__(parent)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.newShapeCreate_btn.clicked.connect(self.createNewShapeConn)
        self.srcInpLd_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.srcInp_LE))
        self.srcOutLd_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.srcOut_LE))
        self.destInpLd_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.destInp_LE))
        self.destOutLd_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.destOut_LE))
        self.shiftConnections_btn.clicked.connect(self.shiftInpOutConn)

    def createNewShapeConn(self):
        parent = ar_selection.ar_getSelection()[0]
        newShapeName = self.newShpName_LE.text()
        ar_gen.ar_createAndParentNewShape(parent, newShapeName)

    def shiftInpOutConn(self):
        sourceInpShp = self.srcInp_LE.text()
        sourceOutShp = self.srcOut_LE.text()
        destInpShp = self.destInp_LE.text()
        destOutShp = self.destOut_LE.text()
        ar_skin.ar_shiftInputOutputConnections(sourceInpShp, sourceOutShp, destInpShp, destOutShp)


def main():
    winClass = ShiftInpOutConn(ar_qui.ar_mayaMainWindow())
    return winClass.show()

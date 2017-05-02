from PySide import QtGui

from rigtools import maya_utils
from rigtools.ui.aspToolsUI import ui_aspfkInIkSpine
from rigtools.ui import ui_fill
from rigtools.aspTools import tools


class FkInIkSpineConn(QtGui.QMainWindow, ui_aspfkInIkSpine.Ui_FkInIkSpineWindow):
    def __init__(self, prnt=None):
        super(FkInIkSpineConn, self).__init__(prnt)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.fkInIkSp_StartCtl_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.fkInIkSp_StartCtl_LE))
        self.fkInIkSp_EndCtl_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.fkInIkSp_EndCtl_LE))
        self.fkInIkSp_HipCtls_btn.clicked.connect(lambda: ui_fill.fillListInLineEdit(self.fkInIkSp_HipCtls_LE))
        self.fkInIkSp_create_btn.clicked.connect(self.asFkInIkSpineConn)

    def asFkInIkSpineConn(self):
        with maya_utils.UndoChunkOpen('FkInIkSpine'):
            startCtl = self.fkInIkSp_StartCtl_LE.text()
            endCtl = self.fkInIkSp_EndCtl_LE.text()
            ctlName = self.fkInIkSp_ctlName_LE.text()
            ctlNumber = self.fkInIkSp_ctlNum_spbx.value()
            hipCtlGrps = ui_fill.extractLineEditList(self.fkInIkSp_HipCtls_LE)
            tools.fkCtlInIkSpine(startCtl, endCtl, hipCtlGrps, ctlName, ctlNumber)


def main():
    winClass = FkInIkSpineConn(maya_utils.maya_main_window())
    return winClass.show()

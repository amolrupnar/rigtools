from PySide import QtGui

from rigtools.ui import ar_qui
from rigtools.ui.aspToolsUI import ui_aspfkInIkSpine
from rigtools.ui import ar_uiFill
from rigtools.aspTools import ar_asTools

reload(ar_qui)
reload(ui_aspfkInIkSpine)
reload(ar_uiFill)
reload(ar_asTools)


class FkInIkSpineConn(QtGui.QMainWindow, ui_aspfkInIkSpine.Ui_FkInIkSpineWindow):
    def __init__(self, parent=None):
        super(FkInIkSpineConn, self).__init__(parent)
        self.setupUi(self)
        self.connections()
        # set check box state command and refresh using on off.
        self.fkInIkSp_hipBase_cBox.stateChanged.connect(self._hipControllerCBox)
        self.fkInIkSp_hipBase_cBox.setChecked(False)
        self.fkInIkSp_hipBase_cBox.setChecked(True)
        self.fkInIkSp_hipBase_cBox.setChecked(False)

    def _hipControllerCBox(self):
        if self.fkInIkSp_hipBase_cBox.isChecked():
            self.label_4.setVisible(True)
            self.fkInIkSp_HipCtls_LE.setVisible(True)
            self.fkInIkSp_HipCtls_btn.setVisible(True)
        else:
            self.label_4.setVisible(False)
            self.fkInIkSp_HipCtls_LE.setVisible(False)
            self.fkInIkSp_HipCtls_btn.setVisible(False)

    def connections(self):
        self.fkInIkSp_StartCtl_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.fkInIkSp_StartCtl_LE))
        self.fkInIkSp_EndCtl_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.fkInIkSp_EndCtl_LE))
        self.fkInIkSp_HipCtls_btn.clicked.connect(lambda: ar_uiFill.ar_fillListInLineEdit(self.fkInIkSp_HipCtls_LE))
        self.fkInIkSp_create_btn.clicked.connect(self.asFkInIkSpineConn)

    def asFkInIkSpineConn(self):
        with ar_qui.ar_undoChunkOpen('FkInIkSpine'):
            startCtl = self.fkInIkSp_StartCtl_LE.text()
            endCtl = self.fkInIkSp_EndCtl_LE.text()
            ctlName = self.fkInIkSp_ctlName_LE.text()
            ctlNumber = self.fkInIkSp_ctlNum_spbx.value()
            hipCtlGrps = ar_uiFill.ar_extractLineEditList(self.fkInIkSp_HipCtls_LE)
            if self.fkInIkSp_hipBase_cBox.isChecked():
                ar_asTools.ar_fkCtlInIkSpine(startCtl, endCtl, ctlName=ctlName, hipCtlGrps=hipCtlGrps, ctlNum=ctlNumber)
            else:
                ar_asTools.ar_fkCtlInIkSpine(startCtl, endCtl, ctlName=ctlName, ctlNum=ctlNumber)


def main():
    winClass = FkInIkSpineConn(ar_qui.ar_mayaMainWindow())
    return winClass.show()

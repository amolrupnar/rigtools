from PySide import QtGui

from rigtools.ui import ar_qui
from rigtools.ui.aspToolsUI import ui_aspIKOriChange
from rigtools.ui import ar_uiFill
from rigtools.aspTools import ar_asTools

reload(ar_qui)
reload(ui_aspIKOriChange)
reload(ar_uiFill)
reload(ar_asTools)


class IkOrientUIConn(QtGui.QMainWindow, ui_aspIKOriChange.Ui_aspIKOriChangeWindow):
    def __init__(self, parent=None):
        super(IkOrientUIConn, self).__init__(parent)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.aspIkOriJntLd_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.aspIkOriJnt_LE))
        self.aspIkOriCtlLd_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.aspIkOriCtl_LE))
        self.aspIkOriSet_btn.clicked.connect(self.asIKCtlOriChangeConn)

    def asIKCtlOriChangeConn(self):
        with ar_qui.ar_undoChunkOpen('Ik Orient Change'):
            jnt = self.aspIkOriJnt_LE.text()
            ctl = self.aspIkOriCtl_LE.text()
            ar_asTools.ar_asIKCtlOriChange(jnt, ctl)


def main():
    winClass = IkOrientUIConn(ar_qui.ar_mayaMainWindow())
    return winClass.show()

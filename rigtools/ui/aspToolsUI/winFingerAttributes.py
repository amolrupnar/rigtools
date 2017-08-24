from PySide import QtGui

from rigtools.ui import ar_qui
from rigtools.ui.aspToolsUI import ui_aspFingerAttributes
from rigtools.ui import ar_uiFill

reload(ui_aspFingerAttributes)


class FingerAttributeConn(QtGui.QMainWindow, ui_aspFingerAttributes.Ui_FingerAttributeWindow):
    def __init__(self, parent=None):
        super(FingerAttributeConn, self).__init__(parent)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.aspFaLoadDriver_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.aspFaDriverControllers_LE))
        self.aspFaLoadFingers_btn.clicked.connect(
            lambda: ar_uiFill.ar_fillListInLineEdit(self.aspFaFingerControllers_LE))

    def asFingerAttributeConn(self):
        with ar_qui.ar_undoChunkOpen('add Finger Attributes'):
            driver = self.aspFaDriverControllers_LE.text()
            controllers = ar_uiFill.ar_extractLineEditList(self.aspFaFingerControllers_LE)
            # TODO: pending ui.


def main():
    winClass = FingerAttributeConn(ar_qui.ar_mayaMainWindow())
    return winClass.show()

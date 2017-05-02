from PySide import QtGui

from rigtools import maya_utils
from rigtools.ui.aspToolsUI import ui_aspFingerAttributes
from rigtools.ui import ui_fill
from rigtools.aspTools import fingers

reload(ui_aspFingerAttributes)


class FingerAttributeConn(QtGui.QMainWindow, ui_aspFingerAttributes.Ui_FingerAttributeWindow):
    def __init__(self, prnt=None):
        super(FingerAttributeConn, self).__init__(prnt)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.aspFaLoadDriver_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.aspFaDriverControllers_LE))
        self.aspFaLoadFingers_btn.clicked.connect(lambda: ui_fill.fillListInLineEdit(self.aspFaFingerControllers_LE))

    def asFingerAttributeConn(self):
        with maya_utils.UndoChunkOpen('add Finger Attributes'):
            driver = self.aspFaDriverControllers_LE.text()
            controllers = ui_fill.extractLineEditList(self.aspFaFingerControllers_LE)


def main():
    winClass = FingerAttributeConn(maya_utils.maya_main_window())
    return winClass.show()

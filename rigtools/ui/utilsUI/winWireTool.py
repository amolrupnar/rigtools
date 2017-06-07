from PySide import QtGui
from rigtools.ui.utilsUI import ui_wireTool
from rigtools.utils import wireTool
from rigtools import maya_utils
from rigtools.ui import ui_fill
from rigtools.utils import deformerUtils

reload(ui_wireTool)
reload(wireTool)
reload(maya_utils)
reload(ui_fill)
reload(deformerUtils)


class WireTool(QtGui.QMainWindow, ui_wireTool.Ui_wireToolWindow):
    def __init__(self, parent):
        super(WireTool, self).__init__(parent)
        self.setupUi(self)
        # default off user defined orientation sample.
        self.orientSample_btn.setVisible(False)
        self.orientSample_LE.setVisible(False)
        self.label_3.setVisible(False)
        self.orientSample_cb.stateChanged.connect(self.orientSampleStatus)
        # fill line edits.
        self.curve_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.curve_LE))
        self.geo_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.geo_LE))
        self.orientSample_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.orientSample_LE))
        self.deoformer_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.deoformer_LE))
        # connection to create button.
        self.create_btn.clicked.connect(self._createWireTool)
        self.clean_btn.clicked.connect(self._cleanSetMembership)

    def orientSampleStatus(self):
        self.orientSample_btn.setVisible(self.orientSample_cb.isChecked())
        self.orientSample_LE.setVisible(self.orientSample_cb.isChecked())
        self.label_3.setVisible(self.orientSample_cb.isChecked())

    def _createWireTool(self):
        with maya_utils.UndoChunkOpen('WireTool'):
            crv = self.curve_LE.text()
            geo = self.geo_LE.text()
            if self.orientSample_LE.text():
                wireTool.addWireTool(str(crv), str(geo), orientSample=str(self.orientSample_LE.text()))
            else:
                wireTool.addWireTool(str(crv), str(geo))

    def _cleanSetMembership(self):
        deformerName = self.deoformer_LE.text()
        deformerUtils.removeFromDeformerInvertedVertex(str(deformerName))


def main():
    winClass = WireTool(maya_utils.maya_main_window())
    winClass.show()

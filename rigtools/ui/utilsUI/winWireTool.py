from PySide import QtGui

from rigtools.ui import ar_qui
from rigtools.ui.utilsUI import ui_wireTool
from rigtools.utils import ar_wireTool
from rigtools.ui import ar_uiFill
from rigtools.utils import ar_deformer

reload(ar_qui)
reload(ui_wireTool)
reload(ar_wireTool)
reload(ar_uiFill)
reload(ar_deformer)


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
        self.curve_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.curve_LE))
        self.geo_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.geo_LE))
        self.orientSample_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.orientSample_LE))
        self.deoformer_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.deoformer_LE))
        # connection to create button.
        self.create_btn.clicked.connect(self._createWireTool)
        self.clean_btn.clicked.connect(self._cleanSetMembership)

    def orientSampleStatus(self):
        self.orientSample_btn.setVisible(self.orientSample_cb.isChecked())
        self.orientSample_LE.setVisible(self.orientSample_cb.isChecked())
        self.label_3.setVisible(self.orientSample_cb.isChecked())

    def _createWireTool(self):
        with ar_qui.ar_undoChunkOpen('WireTool'):
            crv = self.curve_LE.text()
            geo = self.geo_LE.text()
            if self.orientSample_LE.text():
                ar_wireTool.ar_addWireTool(str(crv), str(geo), orientSample=str(self.orientSample_LE.text()))
            else:
                ar_wireTool.ar_addWireTool(str(crv), str(geo))

    def _cleanSetMembership(self):
        deformerName = self.deoformer_LE.text()
        ar_deformer.ar_removeFromDeformerInvertedVertex(str(deformerName))


def main():
    winClass = WireTool(ar_qui.ar_mayaMainWindow())
    winClass.show()

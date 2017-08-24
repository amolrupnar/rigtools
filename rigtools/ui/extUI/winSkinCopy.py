from PySide import QtGui

from rigtools.ui import ar_qui
from rigtools.ui import ar_uiFill
from rigtools.ui.extUI import ui_skinCopy
from rigtools.ext import ar_skin

reload(ar_qui)
reload(ar_uiFill)
reload(ui_skinCopy)
reload(ar_skin)


class SkinCopyUIConn(QtGui.QMainWindow, ui_skinCopy.Ui_skinCopyWindow):
    def __init__(self, parent=None):
        super(SkinCopyUIConn, self).__init__(parent)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.sourceMeshLoad_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.sourceMesh_LE))
        self.destMeshLoad_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.destMesh_LE))
        self.copySkin_btn.clicked.connect(self.skinCopyConn)
        self.skin_copySkin_btn.clicked.connect(self.skinAndCopySkin)

    def skinCopyConn(self):
        with ar_qui.ar_undoChunkOpen('skin copy'):
            source = self.sourceMesh_LE.text()
            destination = self.destMesh_LE.text()
            ar_skin.ar_copySkinOnMultiObjects(source, [destination])

    def skinAndCopySkin(self):
        with ar_qui.ar_undoChunkOpen('skin and copy skin'):
            source = self.sourceMesh_LE.text()
            destination = self.destMesh_LE.text()
            ar_skin.ar_skinAndCopySkin(source, destination)


def main():
    winClass = SkinCopyUIConn(ar_qui.ar_mayaMainWindow())
    return winClass.show()

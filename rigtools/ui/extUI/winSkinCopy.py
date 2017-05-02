from PySide import QtGui

from rigtools import maya_utils
from rigtools.ui import ui_fill
from rigtools.ui.extUI import ui_skinCopy
from rigtools.ext import skin


class SkinCopyUIConn(QtGui.QMainWindow, ui_skinCopy.Ui_skinCopyWindow):
    def __init__(self, prnt=None):
        super(SkinCopyUIConn, self).__init__(prnt)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.sourceMeshLoad_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.sourceMesh_LE))
        self.destMeshLoad_btn.clicked.connect(lambda: ui_fill.fillLineEdit(self.destMesh_LE))
        self.copySkin_btn.clicked.connect(self.skinCopyConn)
        self.skin_copySkin_btn.clicked.connect(self.skinAndCopySkin)

    def skinCopyConn(self):
        with maya_utils.UndoChunkOpen('skin copy'):
            source = self.sourceMesh_LE.text()
            destination = self.destMesh_LE.text()
            skin.copySkinOnMultiObjects(source, [destination])

    def skinAndCopySkin(self):
        with maya_utils.UndoChunkOpen('skin and copy skin'):
            source = self.sourceMesh_LE.text()
            destination = self.destMesh_LE.text()
            skin.skinAndCopySkin([source], destination)


def main():
    winClass = SkinCopyUIConn(maya_utils.maya_main_window())
    return winClass.show()

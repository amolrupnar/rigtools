import pymel.core as pm
from PySide2 import QtWidgets, QtGui

from rigtools.ui import ar_qui
from rigtools.ui.aspToolsUI import ui_hairBake
from rigtools.utils import ar_bake

reload(ar_qui)
reload(ui_hairBake)
reload(ar_bake)


class HairBakeUnbake(QtWidgets.QMainWindow, ui_hairBake.Ui_hairBakeWindow):
    def __init__(self, parent):
        super(HairBakeUnbake, self).__init__(parent)
        self.setupUi(self)
        self.connections()

    def connections(self):
        # add all Characters in list widget.
        characters = []
        for each in pm.listReferences():
            characterName = each.namespace + ':' + each.path.split('/')[-1].split('.')[0]
            characters.append(characterName)
        if characters:
            self.characters_LW.addItems(characters)
        # button connections.
        self.characters_LW.itemSelectionChanged.connect(self.fillDynListWidget)
        self.bake_btn.clicked.connect(self.bakeHair)
        self.unbake_btn.clicked.connect(self.unbakeHair)

    def checkBake(self):
        for index in xrange(self.dynParticle_LW.count()):
            a = str(self.dynParticle_LW.item(index).text())
            namespace = str(a.split(':')[0])
            dynaName = str(a.split(':')[1])
            ikHandleTransform = pm.PyNode(namespace + ':DynIKHandledyn' + dynaName)
            if not ikHandleTransform.ikBlend.get():
                self.dynParticle_LW.item(index).setForeground((QtGui.QColor(255, 0, 0)))
            else:
                self.dynParticle_LW.item(index).setForeground((QtGui.QColor(255, 255, 255)))
        self.dynParticle_LW.clearSelection()

    def fillDynListWidget(self):
        self.dynParticle_LW.clear()
        # get all selected characters from ui.
        for eachChar in self.characters_LW.selectedItems():
            char = eachChar.text()
            namespace = char.split(':')[0]
            dynIkHandles = pm.ls(namespace + ':DynIKHandledyn*', type='ikHandle')
            dynIks = []
            for each in dynIkHandles:
                dynIks.append(str(each).replace('DynIKHandledyn', ''))
            self.dynParticle_LW.addItems(dynIks)
        self.checkBake()

    def bakeHair(self):
        bakeIkList = []
        bakeParticleList = []
        for each in self.dynParticle_LW.selectedItems():
            namespace = str(each.text().split(':')[0])
            dynaName = str(each.text().split(':')[1])
            ikHandleTransform = pm.PyNode(namespace + ':DynIKHandledyn' + dynaName)
            particleTransform = pm.PyNode(namespace + ':DynParticledyn' + dynaName)
            particleShape = particleTransform.getShape()
            bakeIkList.extend([ikHandleTransform])
            bakeParticleList.extend([particleShape])
        if not bakeIkList:
            raise RuntimeError('No Selection found in hair bake window,')
        ar_bake.ar_bakeIkJoints(bakeIkList, particleShps=bakeParticleList)
        self.checkBake()

    def unbakeHair(self):
        unBakeIkList = []
        unBakeParticleList = []
        for each in self.dynParticle_LW.selectedItems():
            namespace = str(each.text().split(':')[0])
            dynaName = str(each.text().split(':')[1])
            ikHandleTransform = pm.PyNode(namespace + ':DynIKHandledyn' + dynaName)
            particleTransform = pm.PyNode(namespace + ':DynParticledyn' + dynaName)
            particleShape = particleTransform.getShape()
            unBakeIkList.extend([ikHandleTransform])
            unBakeParticleList.extend([particleShape])
        if not unBakeIkList:
            raise RuntimeError('No Selection found in hair bake window,')
        ar_bake.ar_unBakeIkJoints(unBakeIkList, particleShps=unBakeParticleList)
        self.checkBake()


def main():
    winClass = HairBakeUnbake(ar_qui.ar_mayaMainWindow())
    return winClass.show()

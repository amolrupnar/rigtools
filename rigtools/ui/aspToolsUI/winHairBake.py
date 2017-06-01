import pymel.core as pm
from PySide import QtGui
from rigtools.ui.aspToolsUI import ui_hairBake
from rigtools import maya_utils
from rigtools.utils import bake

reload(ui_hairBake)
reload(bake)


class HairBakeUnbake(QtGui.QMainWindow, ui_hairBake.Ui_hairBakeWindow):
    def __init__(self, prnt):
        super(HairBakeUnbake, self).__init__(prnt)
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

    def colorChanger(self):
        print 11111111111
        sItems = self.dynParticle_LW.selectedItems()
        # print sItems
        for each in sItems:
            print each
            each.setForeground((QtGui.QColor(255, 0, 0)))

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
        bake.bakeIkJoints(bakeIkList, particleShps=bakeParticleList)

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
        bake.unBakeIkJoints(unBakeIkList, particleShps=unBakeParticleList)


def main():
    winClass = HairBakeUnbake(maya_utils.maya_main_window())
    return winClass.show()

import pymel.core as pm
from PySide import QtGui
from rigtools.ui.aspToolsUI import ui_hairBake
from rigtools import maya_utils
from rigtools.aspTools import dyna

reload(ui_hairBake)
reload(dyna)


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

    def fillDynListWidget(self):
        self.dynParticle_LW.clear()
        # get all selected characters from ui.
        for eachChar in self.characters_LW.selectedItems():
            char = eachChar.text()
            namespace = char.split(':')[0]
            dynCrvs = pm.ls(namespace + ':DynIKCurveSoftdyn*', type='nurbsCurve')
            dynParticles = []
            for each in dynCrvs:
                dynParent = each.getParent()
                dynParticles.append(str(dynParent).replace('DynIKCurveSoftdyn', ''))
            self.dynParticle_LW.addItems(dynParticles)

    def bakeHair(self):
        bakeList = []
        for each in self.dynParticle_LW.selectedItems():
            namespace = str(each.text().split(':')[0])
            curveName = str(each.text().split(':')[1])
            curveTransform = pm.PyNode(namespace + ':DynIKCurveSoftdyn' + curveName)
            curveShape = curveTransform.getShape()
            bakeList.extend([curveShape])
        if not bakeList:
            raise RuntimeError('No Selection found in hair bake window,')
        dyna.bakeHair(dynCrvs=bakeList)

    def unbakeHair(self):
        unbakeList = []
        for each in self.dynParticle_LW.selectedItems():
            # x = str(each.text())
            namespace = each.text().split(':')[0]
            dynCrvs = pm.ls(str(namespace) + ':DynIKCurveSoftdyn*', type='nurbsCurve')
            unbakeList.extend(dynCrvs)
        if not unbakeList:
            raise RuntimeError('No Selection found in hair bake window,')
        dyna.unBakeHair(dynCrvs=unbakeList)


def main():
    winClass = HairBakeUnbake(maya_utils.maya_main_window())
    return winClass.show()

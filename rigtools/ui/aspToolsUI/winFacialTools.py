import pymel.core as pm
from PySide2 import QtWidgets
import os

from rigtools.ui import ar_qui
from rigtools.ui.aspToolsUI import ui_facial_tools
from rigtools.ui import ar_uiFill
from rigtools.aspTools import ar_asFacialTools

reload(ar_qui)
reload(ui_facial_tools)
reload(ar_qui)
reload(ar_asFacialTools)

setupPathRoot = r'\\stor\Data\python_packages\RIG_DATA'


class FacialTools(QtWidgets.QMainWindow, ui_facial_tools.Ui_FacialToolsWindow):
    def __init__(self, parent=None):
        super(FacialTools, self).__init__(parent)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.faceGeo_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.faceGeo_LE))
        self.faceGeoMainRig_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.faceGeoMainRig_LE))
        self.faceGeoTopGroup_btn.clicked.connect(lambda: ar_uiFill.ar_fillLineEdit(self.faceGeoTopGroup_LE))
        self.refresh_btn.clicked.connect(self.refreshServerFiles)
        self.export_btn.clicked.connect(self.export)
        self.import_btn.clicked.connect(self.importFile)
        self.connect_btn.clicked.connect(self.connectSetup)
        # add projects in combo box.
        projects = os.listdir(setupPathRoot)
        projects.sort()
        self.project_comboBox.addItems(projects)
        self.refreshServerFiles()
        self.characters_LW.clicked.connect(self.fillSetupLW)
        self.project_comboBox.currentIndexChanged.connect(self.refreshServerFiles)

    def refreshServerFiles(self):
        project = self.project_comboBox.currentText()
        characters = os.listdir(setupPathRoot + '\\' + project)
        self.characters_LW.clear()
        self.expSetups_LW.clear()
        self.characters_LW.addItems(characters)

    def fillSetupLW(self):
        project = self.project_comboBox.currentText()
        character = self.characters_LW.currentItem().text()
        charPath = setupPathRoot + '\\' + project + '\\' + character
        self.expSetups_LW.clear()
        self.expSetups_LW.addItems(os.listdir(charPath))

    def export(self):
        if self.lip_rb.isChecked():
            self.exportLip()
        else:
            self.exportEyeBrow()

    def exportLip(self):
        face_geo = self.faceGeo_LE.text()
        face_geo_top_group = self.faceGeoTopGroup_LE.text()
        namespaces = self.namespaces_LE.text()
        project = self.project_comboBox.currentText()
        char = self.charName_LE.text()
        path = setupPathRoot + '\\' + project + '\\' + char + '\\Lip.ma'
        lipExpClass = ar_asFacialTools.Ar_LipSetup(face_geo=face_geo, face_geo_top_node=face_geo_top_group,
                                                   namespaceName=namespaces, exportFile=True, path=path)
        lipExpClass.exportLipSetup()

    def exportEyeBrow(self):
        face_geo = self.faceGeo_LE.text()
        project = self.project_comboBox.currentText()
        char = self.charName_LE.text()
        path = setupPathRoot + '\\' + project + '\\' + char + '\\EyeBrow.ma'
        ar_asFacialTools.ar_browExport(face_geo, exportFile=True, path=path)

    def importFile(self):
        namespaces = self.namespaces_LE.text()
        project = self.project_comboBox.currentText()
        char = self.characters_LW.currentItem().text()
        setup = self.expSetups_LW.currentItem().text()
        path = setupPathRoot + '\\' + project + '\\' + char + '\\' + setup
        if not os.path.exists(path):
            raise RuntimeError('{0} path is dose not exist'.format(self.path))
        pm.importFile(path, type="mayaAscii", pr=True, namespace=namespaces[:-1], mergeNamespacesOnClash=False)

    def connectSetup(self):
        face_geo = self.faceGeo_LE.text()
        face_geo_top_group = self.faceGeoTopGroup_LE.text()
        face_geo_main_rig = self.faceGeoMainRig_LE.text()
        namespaces = self.namespaces_LE.text()
        setup = self.expSetups_LW.currentItem().text()
        if setup == 'Lip.ma':
            lipImpClass = ar_asFacialTools.Ar_LipSetup(face_geo=face_geo_main_rig, face_geo_top_node=face_geo_top_group,
                                                       namespaceName=namespaces)
            lipImpClass.connectLipSetup()
        else:
            ar_asFacialTools.ar_browConnect(face_geo, face_geo_top_group, face_geo_main_rig, namespacesName=namespaces)


def main():
    winClass = FacialTools(ar_qui.ar_mayaMainWindow())
    return winClass.show()

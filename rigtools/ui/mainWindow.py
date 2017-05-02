from PySide import QtGui

from rigtools.ext import gen
from rigtools.ui import rigTools_ui
from rigtools.ui.aspToolsUI import winIkOriChange
from rigtools.ui.aspToolsUI import winFkInIkSpine
from rigtools.ui.aspToolsUI import winFingerAttributes
from rigtools.ui.extUI import extConn
from rigtools.ui.utilsUI import utilsConn
from rigtools import maya_utils
from rigtools.ui.extUI import winSkinCopy
from rigtools.aspTools import tools
from rigtools.ui.extUI import winShiftInpOut
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

reload(gen)
reload(rigTools_ui)
reload(winIkOriChange)
reload(winFkInIkSpine)
reload(utilsConn)
reload(extConn)
reload(maya_utils)
reload(winSkinCopy)
reload(winFingerAttributes)


class RigToolsUIConn(MayaQWidgetDockableMixin, QtGui.QMainWindow, rigTools_ui.Ui_mainWindow):
    def __init__(self, prnt=None):
        super(RigToolsUIConn, self).__init__(prnt)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.jointSel_btn.clicked.connect(utilsConn.jointsOnSelectionConn)
        self.parent_btn.clicked.connect(extConn.parentHirarchyConn)
        self.Zero_Out_btn.clicked.connect(extConn.zeroOutConn)
        self.Select_All_btn.clicked.connect(extConn.selectAllConn)
        self.orient_chain_btn.clicked.connect(lambda: utilsConn.orientChainConn(self))
        self.aim_constraint_btn.clicked.connect(lambda: utilsConn.aimConstraintConn(self))
        self.aim_constraint_parent_btn.clicked.connect(lambda: utilsConn.aimConstraintParentConn(self))
        self.none_Orient_btn.clicked.connect(utilsConn.noneOrientConn)
        self.point_constraint_btn.clicked.connect(lambda: utilsConn.multiPointConstraintConn(self))
        self.orient_constraint_btn.clicked.connect(lambda: utilsConn.multiOrientConstraintConn(self))
        self.parent_constraint_btn.clicked.connect(lambda: utilsConn.multiParentConstraintConn(self))
        self.FK_btn.clicked.connect(lambda: utilsConn.fkchainConn(self))
        self.Find_Duplicates_btn.clicked.connect(gen.findDuplicates)
        self.select_Influence_object_btn.clicked.connect(extConn.selectInfluenceObjConn)
        self.copySkinOnMultipleObject_btn.clicked.connect(winSkinCopy.main)
        self.ShiftShapeConnections_btn.clicked.connect(winShiftInpOut.main)
        self.IK_Orient_btn.clicked.connect(winIkOriChange.main)
        self.Hide_Extra_Joints_btn.clicked.connect(tools.changeDrawStyleOfExtraJoints)
        self.FK_in_IKSpine_btn.clicked.connect(winFkInIkSpine.main)
        self.FingerSDK_btn.clicked.connect(winFingerAttributes.main)


def main():
    winClass = RigToolsUIConn(maya_utils.maya_main_window())
    return winClass.show(dockable=True)

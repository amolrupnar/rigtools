from PySide import QtGui

from rigtools.ui import ar_qui
from rigtools.ext import ar_gen
from rigtools.ui import rigTools_ui
from rigtools.ui.aspToolsUI import winIkOriChange
from rigtools.ui.aspToolsUI import winFkInIkSpine
from rigtools.ui.aspToolsUI import winFingerAttributes
from rigtools.ui.extUI import extConn
from rigtools.ui.utilsUI import utilsConn
from rigtools.ui.utilsUI import winWireTool
from rigtools.ui.extUI import winSkinCopy
from rigtools.aspTools import ar_asTools
from rigtools.ui.extUI import winShiftInpOut

reload(ar_qui)
reload(ar_gen)
reload(rigTools_ui)
reload(winIkOriChange)
reload(winFkInIkSpine)
reload(winFingerAttributes)
reload(extConn)
reload(utilsConn)
reload(winWireTool)
reload(winSkinCopy)
reload(ar_asTools)
reload(winShiftInpOut)


class RigToolsUIConn(QtGui.QMainWindow, rigTools_ui.Ui_rtMainWindow):
    def __init__(self, parent=None):
        super(RigToolsUIConn, self).__init__(parent)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.matchPosition_btn.clicked.connect(extConn.matchPositionConn)
        self.matchOrientation_btn.clicked.connect(extConn.matchOrientationConn)
        self.matchBoth_btn.clicked.connect(extConn.matchPositionOrientation)
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
        self.FK_btn.clicked.connect(lambda: utilsConn.fkChainConn(self))
        self.Find_Duplicates_btn.clicked.connect(ar_gen.ar_findDuplicates)
        self.select_Influence_object_btn.clicked.connect(extConn.selectInfluenceObjConn)
        self.copySkinOnMultipleObject_btn.clicked.connect(winSkinCopy.main)
        self.ShiftShapeConnections_btn.clicked.connect(winShiftInpOut.main)
        self.IK_Orient_btn.clicked.connect(winIkOriChange.main)
        self.Hide_Extra_Joints_btn.clicked.connect(ar_asTools.ar_changeDrawStyleOfExtraJoints)
        self.FK_in_IKSpine_btn.clicked.connect(winFkInIkSpine.main)
        self.FingerSDK_btn.clicked.connect(winFingerAttributes.main)
        self.WireTool_btn.clicked.connect(winWireTool.main)
        # color btn connections.
        self.noneColor_btn.setStyleSheet("background-color:rgb(0,0,102)")
        self.noneColor_btn.clicked.connect(lambda: ar_gen.ar_overrideColor(0, offOver=True))
        self.blueColor_btn.setStyleSheet("background-color:rgb(0,0,255)")
        self.blueColor_btn.clicked.connect(lambda: ar_gen.ar_overrideColor(6))
        self.redColor_btn.setStyleSheet("background-color:rgb(255,0,0)")
        self.redColor_btn.clicked.connect(lambda: ar_gen.ar_overrideColor(13))
        self.greenColor_btn.setStyleSheet("background-color:rgb(0,255,0)")
        self.greenColor_btn.clicked.connect(lambda: ar_gen.ar_overrideColor(14))
        self.SkyBlueColor_btn.setStyleSheet("background-color:rgb(0,255,255)")
        self.SkyBlueColor_btn.clicked.connect(lambda: ar_gen.ar_overrideColor(18))
        self.yellowColor_btn.setStyleSheet("background-color:rgb(255,255,0)")
        self.yellowColor_btn.clicked.connect(lambda: ar_gen.ar_overrideColor(17))
        # controller add connection.
        self.circleCtl_btn.clicked.connect(lambda: extConn.controllerConn('circle', self))
        self.cubeCtl_btn.clicked.connect(lambda: extConn.controllerConn('cube', self))
        self.sphereCtl_btn.clicked.connect(lambda: extConn.controllerConn('sphere', self))
        self.diamondCtl_btn.clicked.connect(lambda: extConn.controllerConn('diamond', self))
        self.coneCtl_btn.clicked.connect(lambda: extConn.controllerConn('cone', self))
        self.arrrowBallCtl_btn.clicked.connect(lambda: extConn.controllerConn('arrowBall', self))
        self.arrow1Ctl_btn.clicked.connect(lambda: extConn.controllerConn('arrow1', self))
        self.arrow4Ctl_btn.clicked.connect(lambda: extConn.controllerConn('arrow4', self))


def main():
    winClass = RigToolsUIConn(ar_qui.ar_mayaMainWindow())
    return winClass.show()

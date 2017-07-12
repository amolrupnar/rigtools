from maya import cmds as cmds
import maya.mel as mel
import pymel.core as pm

from rigtools.ui import ar_qui
from rigtools.ext import ar_gen, ar_selection, ar_skin, ar_controllers

reload(ar_qui)
reload(ar_gen)
reload(ar_selection)
reload(ar_skin)
reload(ar_controllers)


# --------------------------------------------------------------
# -------------------------- gen -------------------------------
# --------------------------------------------------------------
def findDuplicatesConn():
    """
    @ findDuplicates UI connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('jointsOnSelection'):
        ar_gen.ar_findDuplicates()


def zeroOutConn():
    """
    @ zeroOut UI connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('zeroOut'):
        sel = cmds.ls(sl=True)
        ar_gen.ar_zeroOut(sel)


def parentHirarchyConn():
    """
    @ parentHierarchy UI connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('parentHirarchy'):
        sel = cmds.ls(sl=True)
        ar_gen.ar_parentHirarchy(sel)


# --------------------------------------------------------------
# ----------------------- selection ----------------------------
# --------------------------------------------------------------
def selectAllConn():
    """
    @ selectAll UI connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('selectAll'):
        ar_selection.ar_selectAll()


# --------------------------------------------------------------
# ------------------------- skin -------------------------------
# --------------------------------------------------------------
def selectInfluenceObjConn():
    """
    @ getInfluenceJoint UI Connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('selectInfluenceObj'):
        sel = cmds.ls(sl=True)
        if sel:
            infObj = ar_skin.ar_getInfluenceJoint(sel)
            cmds.select(infObj, r=True)
            ar_qui.ar_displayMessage('success', '%s influence objects is selected..' % len(infObj))
        else:
            ar_qui.ar_displayMessage('warning', 'your selection is empty')


def shiftInputOutputConnectionsConn():
    """
    @ shiftInputOutputConnections UI connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('shiftInputOutputConnections'):
        sourceInp = cmds.textField('srcInp_LE', q=True, tx=True)
        sourceOut = cmds.textField('srcOut_LE', q=True, tx=True)
        destInp = cmds.textField('destInp_LE', q=True, tx=True)
        destOut = cmds.textField('destOut_LE', q=True, tx=True)
        ar_skin.ar_shiftInputOutputConnections(sourceInp, sourceOut, destInp, destOut)


def matchPositionConn():
    """
    @ match position connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('Match Position'):
        ar_gen.ar_matchPosition()


def matchOrientationConn():
    """
    @ match orientation connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('Match Orientation'):
        ar_gen.ar_matchOrientation()


def matchPositionOrientation():
    """
    @ match orientation and position connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('Match Position and Orientation'):
        ar_gen.ar_matchPositionOrientation()


# --------------------------------------------------------------
# ----------------------- controller ---------------------------
# --------------------------------------------------------------
def controllerConn(ctlType, passUI):
    with ar_qui.ar_undoChunkOpen('controller maker'):
        myObj = pm.ls(sl=True)
        pm.select(cl=True)
        ctl = ar_controllers.Ar_CtlShapes('controller')
        ctlTyp = {'cube': ctl.ar_cubeCtl, 'sphere': ctl.ar_sphereCtl, 'diamond': ctl.ar_diamondCtl,
                  'cone': ctl.ar_coneCtl,
                  'arrowBall': ctl.ar_arrowBallCtl, 'arrow1': ctl.ar_arrow1Ctl, 'arrow4': ctl.ar_arrow4Ctl,
                  'circle': ctl.ar_circleCtl}
        newCtl = ctlTyp[ctlType]()
        if myObj:
            ar_gen.ar_matchPositionOrientation(sel=[newCtl, myObj[0]])
        if passUI.shapeReplace_cb.isChecked():
            if not myObj:
                ar_qui.ar_displayMessage('error', 'please select object to replace the shape.')
                return False
            oldShape = myObj[0].getShape()
            if oldShape:
                oldShapeName = oldShape.name()
                pm.delete(oldShape)
            else:
                oldShapeName = myObj[0] + 'Shape'
            newShape = newCtl.getShape()
            pm.select(myObj[0], r=True)
            mel.eval("parent -r -s " + newShape)
            newShape.rename(oldShapeName)
            pm.delete(newCtl)
            pm.select(myObj[0])
            return True
        return False

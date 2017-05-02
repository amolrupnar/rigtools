import maya.cmds as cmds

from rigtools import maya_utils
from rigtools.utils import fk
from rigtools.utils import constraint
from rigtools.utils import joint


# --------------------------------------------------------------
# ------------------- constraint -------------------------------
# --------------------------------------------------------------
def aimConstraintConn(passUI):
    """
    aimConstraint UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('aimConstraint'):
        aimAxis = str()
        objectUpAxis = str()
        aimValue = list()
        objValue = list()
        # radio checks.
        if passUI.aimX_rb.isChecked():
            aimAxis = 'X'
        if passUI.aimY_rb.isChecked():
            aimAxis = 'Y'
        if passUI.aimZ_rb.isChecked():
            aimAxis = 'Z'
        if passUI.aimObX_rb.isChecked():
            objectUpAxis = 'X'
        if passUI.aimObY_rb.isChecked():
            objectUpAxis = 'Y'
        if passUI.aimObZ_rb.isChecked():
            objectUpAxis = 'Z'
        if aimAxis == 'X':
            aimValue = [1, 0, 0]
        if aimAxis == 'Y':
            aimValue = [0, 1, 0]
        if aimAxis == 'Z':
            aimValue = [0, 0, 1]
        if objectUpAxis == 'X':
            objValue = [1, 0, 0]
        if objectUpAxis == 'Y':
            objValue = [0, 1, 0]
        if objectUpAxis == 'Z':
            objValue = [0, 0, 1]
        sel = cmds.ls(sl=True)
        constraint.aimConstraint(aimValue, objValue, sel)


def aimConstraintParentConn(passUI):
    """
    aimConstraintParent UI connections.
    :return: connection
    """
    with maya_utils.UndoChunkOpen('aimConstraintParent'):
        aimAxis = str()
        objectUpAxis = str()
        aimValue = list()
        objValue = list()
        # radio checks.
        if passUI.aimX_rb.isChecked():
            aimAxis = 'X'
        if passUI.aimY_rb.isChecked():
            aimAxis = 'Y'
        if passUI.aimZ_rb.isChecked():
            aimAxis = 'Z'
        if passUI.aimObX_rb.isChecked():
            objectUpAxis = 'X'
        if passUI.aimObY_rb.isChecked():
            objectUpAxis = 'Y'
        if passUI.aimObZ_rb.isChecked():
            objectUpAxis = 'Z'
        if aimAxis == 'X':
            aimValue = [1, 0, 0]
        if aimAxis == 'Y':
            aimValue = [0, 1, 0]
        if aimAxis == 'Z':
            aimValue = [0, 0, 1]
        if objectUpAxis == 'X':
            objValue = [1, 0, 0]
        if objectUpAxis == 'Y':
            objValue = [0, 1, 0]
        if objectUpAxis == 'Z':
            objValue = [0, 0, 1]
        sel = cmds.ls(sl=True, type='joint')
        constraint.aimConstraintParent(aimValue, objValue, sel)


def multiPointConstraintConn(passUI):
    """
    mutiPointConstraint UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('multiPointConstraint'):
        sel = cmds.ls(sl=True)
        offset = passUI.maintainOffset_cb.isChecked()
        constraint.multiPointConstraint(offset, sel)


def multiOrientConstraintConn(passUI):
    """
    multiOrientConstraint UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('multiOrientConstraint'):
        sel = cmds.ls(sl=True)
        offset = passUI.maintainOffset_cb.isChecked()
        constraint.multiOrientConstraint(offset, sel)


def multiParentConstraintConn(passUI):
    """
    multiParentConstraint UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('multiParentConstraint'):
        sel = cmds.ls(sl=True)
        offset = passUI.maintainOffset_cb.isChecked()
        constraint.multiParentConstraint(offset, sel)


# --------------------------------------------------------------
# -------------------------- fk --------------------------------
# --------------------------------------------------------------
def fkchainConn(passUI):
    """
    fkchain UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('multiParentConstraint'):
        # get axis from ui
        axis = list()
        if passUI.ctlAxis_X_rb.isChecked():
            axis = [1, 0, 0]
        if passUI.ctlAxis_Y_rb.isChecked():
            axis = [0, 1, 0]
        if passUI.ctlAxis_Z_rb.isChecked():
            axis = [0, 0, 1]
        fk.fkchain(axis)


# --------------------------------------------------------------
# ------------------------ joint -------------------------------
# --------------------------------------------------------------
def jointsOnSelectionConn():
    """
    jointsOnSelection UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('jointsOnSelection'):
        sel = cmds.ls(sl=True)
        joint.jointsOnSelection(sel)


def noneOrientConn():
    """
    noneOrient UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('noneOrient'):
        sel = cmds.ls(sl=True)
        joint.noneOrient(sel)


def orientChainConn(passUI):
    """
    orientChain UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('orient chain'):
        aimAxis = str()
        objectUpAxis = str()
        aimValue = list()
        objValue = list()
        if passUI.aimX_rb.isChecked():
            aimAxis = 'X'
        if passUI.aimY_rb.isChecked():
            aimAxis = 'Y'
        if passUI.aimZ_rb.isChecked():
            aimAxis = 'Z'
        if passUI.aimObX_rb.isChecked():
            objectUpAxis = 'X'
        if passUI.aimObY_rb.isChecked():
            objectUpAxis = 'Y'
        if passUI.aimObZ_rb.isChecked():
            objectUpAxis = 'Z'
        if aimAxis == 'X':
            aimValue = [1, 0, 0]
        if aimAxis == 'Y':
            aimValue = [0, 1, 0]
        if aimAxis == 'Z':
            aimValue = [0, 0, 1]
        if objectUpAxis == 'X':
            objValue = [1, 0, 0]
        if objectUpAxis == 'Y':
            objValue = [0, 1, 0]
        if objectUpAxis == 'Z':
            objValue = [0, 0, 1]
        sel = cmds.ls(sl=True, type='joint')
        joint.orientChain(aimValue, objValue, sel)

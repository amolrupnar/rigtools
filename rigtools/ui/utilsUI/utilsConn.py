import maya.cmds as cmds

from rigtools.ui import ar_qui
from rigtools.utils import ar_fk
from rigtools.utils import ar_constraint
from rigtools.utils import ar_joint

reload(ar_qui)
reload(ar_fk)
reload(ar_constraint)
reload(ar_joint)


# --------------------------------------------------------------
# ------------------- constraint -------------------------------
# --------------------------------------------------------------
def aimConstraintConn(passUI):
    """
    @ aimConstraint UI connections.
    Args:
        passUI: 

    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('aimConstraint'):
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
        ar_constraint.ar_aimConstraint(aimValue, objValue, sel)


def aimConstraintParentConn(passUI):
    """
    @ aimConstraintParent UI connections.
    Args:
        passUI: 

    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('aimConstraintParent'):
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
        ar_constraint.ar_aimConstraintParent(aimValue, objValue, sel)


def multiPointConstraintConn(passUI):
    """
    @ multiPointConstraint UI connections.
    Args:
        passUI: 

    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('multiPointConstraint'):
        sel = cmds.ls(sl=True)
        offset = passUI.maintainOffset_cb.isChecked()
        ar_constraint.ar_multiPointConstraint(offset, sel)


def multiOrientConstraintConn(passUI):
    """
    @ multiOrientConstraint UI connections.
    Args:
        passUI: 

    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('multiOrientConstraint'):
        sel = cmds.ls(sl=True)
        offset = passUI.maintainOffset_cb.isChecked()
        ar_constraint.ar_multiOrientConstraint(offset, sel)


def multiParentConstraintConn(passUI):
    """
    @ multiParentConstraint UI connections.
    Args:
        passUI: 

    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('multiParentConstraint'):
        sel = cmds.ls(sl=True)
        offset = passUI.maintainOffset_cb.isChecked()
        ar_constraint.ar_multiParentConstraint(offset, sel)


# --------------------------------------------------------------
# -------------------------- fk --------------------------------
# --------------------------------------------------------------
def fkChainConn(passUI):
    """
    fkChain UI connections.
    Args:
        passUI: 

    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('multiParentConstraint'):
        # get axis from ui
        axis = list()
        if passUI.ctlAxis_X_rb.isChecked():
            axis = [1, 0, 0]
        if passUI.ctlAxis_Y_rb.isChecked():
            axis = [0, 1, 0]
        if passUI.ctlAxis_Z_rb.isChecked():
            axis = [0, 0, 1]
        ar_fk.ar_addFk(axis)


# --------------------------------------------------------------
# ------------------------ joint -------------------------------
# --------------------------------------------------------------
def jointsOnSelectionConn():
    """
    @ jointsOnSelection UI connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('jointsOnSelection'):
        sel = cmds.ls(sl=True)
        ar_joint.ar_jointsOnSelection(sel)


def noneOrientConn():
    """
    @ noneOrient UI connections.
    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('noneOrient'):
        sel = cmds.ls(sl=True)
        ar_joint.ar_noneOrient(sel)


def orientChainConn(passUI):
    """
    @ orientChain UI connections.
    Args:
        passUI: 

    Returns:
            none.
    """
    with ar_qui.ar_undoChunkOpen('orient chain'):
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
        ar_joint.ar_orientChain(aimValue, objValue, sel)

from maya import cmds as cmds

from rigtools.ui import ar_qui
from rigtools.ext import ar_gen, ar_selection, ar_skin

reload(ar_qui)
reload(ar_gen)
reload(ar_selection)
reload(ar_skin)


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

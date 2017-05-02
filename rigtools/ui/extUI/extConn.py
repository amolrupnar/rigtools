from maya import cmds as cmds

from rigtools.ext import gen, selection, skin
from rigtools import maya_utils


# --------------------------------------------------------------
# -------------------------- gen -------------------------------
# --------------------------------------------------------------
def findDuplicatesConn():
    """
    findDuplicates UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('jointsOnSelection'):
        gen.findDuplicates()


def zeroOutConn():
    """
    zeroOut UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('zeroOut'):
        sel = cmds.ls(sl=True)
        gen.zeroOut(sel)


def parentHirarchyConn():
    """
    parentHierarchy UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('parentHirarchy'):
        sel = cmds.ls(sl=True)
        gen.parentHirarchy(sel)


# --------------------------------------------------------------
# ----------------------- selection ----------------------------
# --------------------------------------------------------------
def selectAllConn():
    """
    selectAll UI connections.
    :return: ui connections
    """
    with maya_utils.UndoChunkOpen('selectAll'):
        selection.selectAll()


# --------------------------------------------------------------
# ------------------------- skin -------------------------------
# --------------------------------------------------------------
def selectInfluenceObjConn():
    """
    getInfluenceJoint UI Connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('selectInfluenceObj'):
        sel = cmds.ls(sl=True)
        if sel:
            infObj = skin.getInfluenceJoint(sel)
            cmds.select(infObj, r=True)
            print('%s influence objects is selected..' % len(infObj)),
        else:
            cmds.warning('your selection is empty')


def shiftInputOutputConnectionsConn():
    """
    shiftInputOutputConnections UI connections.
    :return: ui connection
    """
    with maya_utils.UndoChunkOpen('shiftInputOutputConnections'):
        sourceInp = cmds.textField('srcInp_LE', q=True, tx=True)
        sourceOut = cmds.textField('srcOut_LE', q=True, tx=True)
        destInp = cmds.textField('destInp_LE', q=True, tx=True)
        destOut = cmds.textField('destOut_LE', q=True, tx=True)
        skin.shiftInputOutputConnections(sourceInp, sourceOut, destInp, destOut)

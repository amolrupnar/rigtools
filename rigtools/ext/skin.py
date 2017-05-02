import pymel.core as pm
import maya.cmds as cmds


def getInfluenceJoint(sel=None):
    """
    select influence objects from selected skinned object.
    :param sel: list (selection)
    :return:
    """
    if not sel:
        sel = pm.ls(sl=True)
    if len(sel) == 1:
        skc = list()
        [skc.append(str(each)) for each in pm.listHistory(sel[0], pdo=True) if each.nodeType() == 'skinCluster']
        if len(skc) == 1:
            infObj = cmds.skinCluster(skc[0], q=True, inf=True)
            return infObj
        else:
            raise RuntimeError('selected object has found multiple skin clusters...')
    else:
        pm.warning('Please select one skinned object...')
        return False


def copySkinOnMultiObjects(source, target):
    """
    copy skin weight from source object to selected objects.
    :param source: str (skinned source object)
    :param target: list (object has to be copying)
    :return: skin weight copy.
    """
    if not target:
        pm.warning('Please specify target objects to copy skin weight')
        return False
    for each in target:
        cmds.copySkinWeights(source, each, nm=True, sa='closestPoint', ia='oneToOne')


def skinAndCopySkin(source, target):
    """
    get influence objects from source and apply new skin cluster.
    and copy skin weight from source to destination object.
    :param source: list
    :param target: str
    :return: skinCluster.
    """
    jnt = getInfluenceJoint(source)
    cmds.skinCluster(jnt, target, tsb=True, bm=0, sm=0, nw=1, wd=0)
    copySkinOnMultiObjects(source, [target])
    return True


def shiftInputOutputConnections(sourceInp, sourceOut, destInp, destOut):
    """
    get connections from source and connect with destination.
    :param sourceInp: string
    :param sourceOut: string
    :param destInp: string
    :param destOut: string
    :return: connections
    """
    sourceInp = pm.PyNode(sourceInp)
    sourceOut = pm.PyNode(sourceOut)
    destInp = pm.PyNode(destInp)
    destOut = pm.PyNode(destOut)
    # set intermediate objects.
    destInp.setIntermediateObject(False)
    destOut.setIntermediateObject(True)
    # output connection.
    outConn = pm.connectionInfo(sourceOut + '.worldMesh[0]', dfs=True)
    pm.connectAttr(destOut + '.worldMesh[0]', outConn[0], f=True)
    # input connection.
    inpConn = pm.connectionInfo(sourceInp + '.inMesh', sfd=True)
    pm.connectAttr(inpConn, destInp + '.inMesh', f=True)

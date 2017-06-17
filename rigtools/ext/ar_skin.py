import pymel.core as pm
import maya.cmds as cmds

from rigtools.utils import ar_mesure
from rigtools.ui import ar_qui

reload(ar_mesure)
reload(ar_qui)


def ar_getInfluenceJoint(sel=None):
    """
    @ select influence objects from selected skinned object.
    Args:
        sel (list): single object but in list. 

    Returns:
            infObj.
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
            ar_qui.ar_displayMessage('error', 'selected object has found multiple skin clusters...')
            return False
    else:
        ar_qui.ar_displayMessage('warning', 'Please select one skinned object...')
        return False


def ar_copySkinOnMultiObjects(source, target):
    """
    @ copy skin weight from source object to selected objects.
    Args:
        source (str): skinned source object.
        target (list): object has to be copy.

    Returns:
            bool.
    """
    if not target:
        ar_qui.ar_displayMessage('warning', 'Please specify target objects to copy skin weight')
        return False
    for each in target:
        cmds.copySkinWeights(source, each, nm=True, sa='closestPoint', ia='oneToOne')
    return True


def ar_skinAndCopySkin(source, target):
    """
    @ get influence objects from source and apply new skin cluster.
    Args:
        source (str): skinned objects.
        target (str): target non skinned object.

    Returns:
            bool.
    """
    jnt = ar_getInfluenceJoint([source])
    cmds.skinCluster(jnt, target, tsb=True, bm=0, sm=0, nw=1, wd=0)
    ar_copySkinOnMultiObjects(source, [target])
    return True


def ar_shiftInputOutputConnections(sourceInp, sourceOut, destInp, destOut):
    """
    @ get connections from source and connect with destination.
    Args:
        sourceInp (str): source input shape.
        sourceOut (str): source output shape.
        destInp (str): destination input shape.
        destOut (str): destination output shape.

    Returns:
            bool.
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
    return True


def ar_addSkinProxyCylinder(startJoint, endJoint):
    """
    @ add proxy geometries for skin according to start and end joint.
    Args:
        startJoint (str): start joint.
        endJoint (str): end joint.

    Returns:
            cageGeo, grp
    """
    startJoint = pm.PyNode(startJoint)
    endJoint = pm.PyNode(endJoint)
    pm.select(cl=True)
    # basic queries.
    totHeight = ar_mesure.ar_getDistanceBetweenTwoObjects(startJoint, endJoint)
    chain = []
    testJoint = startJoint
    chain.append(startJoint)
    breakJoint = ''
    while not breakJoint:
        child = pm.listRelatives(testJoint, c=True, typ='joint')[0]
        if str(child) == str(endJoint):
            chain.append(child)
            break
        chain.append(child)
        testJoint = child
    subHeight = len(chain) - 1
    cageGeo = pm.modeling.polyCylinder(h=totHeight, sc=0, sh=subHeight, ch=False, n=startJoint + '_SkinProxyGeo')
    grp = pm.createNode('transform', n=cageGeo[0] + '_grp')
    pm.parent(cageGeo, grp)
    pm.delete(pm.pointConstraint(startJoint, endJoint, grp, mo=False))
    pm.delete(pm.orientConstraint(startJoint, grp, mo=False))
    cageGeo[0].rz.set(90)
    cageGeo[0].t.lock()
    cageGeo[0].r.lock()
    cageGeo[0].s.lock()
    faceCount = pm.modeling.polyEvaluate(cageGeo[0], f=True)
    pm.delete(cageGeo[0].f[faceCount - 1])
    pm.delete(cageGeo[0].f[faceCount - 2])
    # TODO: get shape in geometry mode.
    return cageGeo, grp

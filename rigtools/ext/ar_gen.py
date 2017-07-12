import pymel.core as pm
import maya.cmds as cmds

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_findDuplicates():
    """
    @ brief Check for nodes with duplicate name and add them to errors node.
    Returns:
            bool.
    """
    duplicateNames = list()
    for node in pm.ls():
        if "|" in str(node):
            if not node.isInstanced():
                duplicateNames.append(str(node))
            else:
                if len(pm.ls(node)) > 1:
                    duplicateNames.append(str(node))
    if not duplicateNames:
        ar_qui.ar_displayMessage('success', 'No duplicates in scene...')
        return True
    pm.select(cl=True)
    if pm.objExists('SET_duplicate_names'):
        pm.delete('SET_duplicate_names')
    pm.sets(n='SET_duplicate_names', em=True).union(duplicateNames)
    ar_qui.ar_displayMessage('success',
                             '%s duplicate objects has been found and put in the "SET_duplicate_names".' % len(
                                 duplicateNames)),
    return False


def ar_createAndParentNewShape(parent, newShapeName):
    """
    @ create new shape from parent add it on as shape parent with parent.
    Args:
        parent (str): duplicate this object and parent duplicated shape with this.
        newShapeName (str): new shape name.

    Returns:
            newShape.
    """
    parent = pm.PyNode(parent)
    dupParent = pm.duplicate(parent, rr=True)
    newShape = dupParent[0].getShapes()[0]
    newShape.rename(newShapeName)
    pm.parent(newShape, parent, r=True, s=True)
    pm.delete(dupParent)
    newShape.setIntermediateObject(False)
    return str(newShape)


def ar_identifyInpOutShapes(source):
    """
    @ identify shapes who has inputs and output connection.
    Args:
        source (str): transform of object.

    Returns:
            inpShape, outShape.
    """
    # get inputs from source.
    source = pm.PyNode(source)
    inpShape = str()
    outShape = str()
    sourceShapes = source.getShapes()
    if len(sourceShapes) == 2:
        for each in sourceShapes:
            if each.isIntermediateObject():
                outShape = each
            else:
                inpShape = each
    else:
        ar_qui.ar_displayMessage('warning', 'source mesh has more than two shapes or only one shape...')
        return False
    return str(inpShape), str(outShape)


def ar_parentHirarchy(sel=None):
    """
    @ parent objects using selection order.
    Args:
        sel (list): object order like child to parent.

    Returns:
            bool.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if len(sel) < 2:
        ar_qui.ar_displayMessage('warning', 'Please select two or more item...')
    else:
        for i in range(len(sel) - 1):
            cmds.parent(sel[i], sel[i + 1])
        cmds.select(sel[len(sel) - 1])
    return True


def ar_zeroOut(sel=None):
    """
    @ zeroOut all the selected objects.
    Args:
        sel (list): objects for zero out.

    Returns:
            groups.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        ar_qui.ar_displayMessage('warning', 'Please select at least on object...')
    else:
        groups = list()
        for i in range(len(sel)):
            name = sel[i] + 'ZERO'
            if cmds.objExists(name):
                ar_qui.ar_displayMessage('error', '%s is already exist please rename it and zeroOut again..' % name)
                return False
            else:
                grp = cmds.group(em=True, w=True, n=name)
                par = cmds.listRelatives(sel[i], p=True)
                cmds.delete(cmds.parentConstraint(sel[i], grp))
                cmds.parent(sel[i], grp)
                if not par:
                    pass
                else:
                    cmds.parent(grp, par[0])
            groups.append(grp)
        return groups


def ar_matchPosition(sel=None):
    """
    @ match position tool.
    Args:
        sel (list): object list.

    Returns:
            bool.
    """
    if not sel:
        sel = pm.ls(sl=True)
    if len(sel) == 2:
        pm.delete(pm.pointConstraint(sel[1], sel[0]))
    else:
        raise RuntimeError('Please select two objects only.')
    return True


def ar_matchOrientation(sel=None):
    """
    @ match orientation tool.
    Args:
        sel (list): object list.

    Returns:
            bool.
    """
    if not sel:
        sel = pm.ls(sl=True)
    if len(sel) == 2:
        pm.delete(pm.orientConstraint(sel[1], sel[0]))
    else:
        raise RuntimeError('Please select two objects only.')
    return True


def ar_matchPositionOrientation(sel=None):
    """
    @ match position and orientation tool.
    Args:
        sel (list): object list.

    Returns:
            bool.
    """
    if not sel:
        sel = pm.ls(sl=True)
    if len(sel) == 2:
        pm.delete(pm.parentConstraint(sel[1], sel[0]))
    else:
        raise RuntimeError('Please select two objects only.')
    return True


def ar_overrideColor(clrIndex, sel=None, offOver=None):
    """
    @ override display color of sel.
    Args:
        clrIndex (int): maya drawing override color index.
        sel (str): objects.
        offOver (bool): off drawing override.

    Returns:
            bool.
    """
    if not sel:
        sel = pm.ls(sl=True)
    for each in sel:
        if offOver:
            pm.setAttr(each + '.overrideEnabled', 0)
        else:
            pm.setAttr(each + '.overrideEnabled', 1)
        pm.setAttr(each + '.overrideColor', clrIndex)
    return True

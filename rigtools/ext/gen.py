import pymel.core as pm
import maya.cmds as cmds


def findDuplicates():
    """@brief Check for nodes with duplicate name and add them to errors node.
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
        print ('No duplicates in scene...'),
        return True
    pm.select(cl=True)
    if pm.objExists('SET_duplicate_names'):
        pm.delete('SET_duplicate_names')
    pm.sets(n='SET_duplicate_names', em=True).union(duplicateNames)
    print ('%s duplicate objects has been found and put in the "SET_duplicate_names".' % len(duplicateNames)),
    return False


def createAndParentNewShape(parent, newShapeName):
    """
    create new shape from parent add it on as shape parent with parent.
    :param parent: string
    :param newShapeName: string
    :return: newShape
    """
    parent = pm.PyNode(parent)
    dupParent = pm.duplicate(parent, rr=True)
    newShape = dupParent[0].getShapes()[0]
    newShape.rename(newShapeName)
    pm.parent(newShape, parent, r=True, s=True)
    pm.delete(dupParent)
    newShape.setIntermediateObject(False)
    return str(newShape)


def identifyInpOutShapes(source):
    """
    identify shapes who has inputs and output connection.
    :param source: string
    :return: inputShape and output shape.
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
        pm.warning('source mesh has more than two shapes or only one shape...')
        return False
    return str(inpShape), str(outShape)


def parentHirarchy(sel=None):
    """
    parent objects using selection order.
    parent selection needs to be in children to parent.
    :param sel: list
    :return: parented chain
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if len(sel) < 2:
        cmds.warning('Please select two or more item...')
    else:
        for i in range(len(sel) - 1):
            cmds.parent(sel[i], sel[i + 1])
        cmds.select(sel[len(sel) - 1])


def zeroOut(sel=None):
    """
    zeroOut all the selected objects.
    :param sel: list
    :return: upper group
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning('Please select at least on object...')
    else:
        for i in range(len(sel)):
            name = sel[i] + 'ZERO'
            if cmds.objExists(name):
                raise RuntimeError('%s is already exist please rename it and run zeroOut again...' % name)
            else:
                grp = cmds.group(em=True, w=True, n=name)
                par = cmds.listRelatives(sel[i], p=True)
                cmds.delete(cmds.parentConstraint(sel[i], grp))
                cmds.parent(sel[i], grp)
                if not par:
                    pass
                else:
                    cmds.parent(grp, par[0])

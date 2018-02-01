import pymel.core as pm

from rigtools.ui import ar_qui
from rigtools.utils import ar_find

reload(ar_qui)
reload(ar_find)


def ar_addBlendShape(source, target, value=0):
    """
    @ add blendshape in target.
    Args:
        source (str, PyNode):  transform of source geometry.
        target (str, PyNode): transform of target geometry.
        value (float): addBlendShapeValue

    Returns:
            face_blend.
    """
    source = pm.PyNode(source)
    target = pm.PyNode(target)
    # get existing blendshape if exist.
    blendShape = []
    allHist = target.history(pdo=True)
    for each in allHist:
        if each.nodeType() == 'blendShape':
            blendShape.append(each)
    # add blendshape.
    if not blendShape:
        face_blend = pm.blendShape(source, target, foc=True, n='BS_' + target)[0]
        weightCount = face_blend.getWeightCount()
        face_blend.setWeight(weightCount - 1, value)
    elif len(blendShape) == 1:
        face_blend = blendShape[0]
        weightCount = face_blend.getWeightCount()
        pm.blendShape(face_blend, edit=True, t=(target, weightCount + 1, source, 1.0))
        face_blend.setWeight(weightCount + 1, value)
    else:
        ar_qui.ar_displayMessage('error', 'geometry have more than one blenshapes found...')
        return False
    return face_blend


def ar_mirrorShapeUsingWrap(baseGeo, editedGeo, newShapeName='newShape', axis='sx'):
    """
    @ mirror blendshape using wrap deformer.
    Args:
        baseGeo (str, PyNode): base geometry transform.
        editedGeo (str, PyNode): edited shape transform.
        newShapeName (str, PyNode): new geometry name.
        axis (str): axis example like 'sx'.

    Returns:
            newShape.
    """
    # convert inputs in PyNode.
    baseGeo = pm.PyNode(baseGeo)
    editedGeo = pm.PyNode(editedGeo)
    # create new shapes
    newShape = baseGeo.duplicate(rr=True, n=newShapeName)[0]
    tempBase = baseGeo.duplicate(rr=True, n='tempBaseForAddBlendshape')[0]
    tempBlendshape = ar_addBlendShape(editedGeo, tempBase, value=0)
    pm.setAttr(tempBase + '.' + axis, -1)
    pm.select(newShape, tempBase, r=True)
    pm.runtime.CreateWrap()
    weightCount = tempBlendshape.getWeightCount()
    tempBlendshape.setWeight(weightCount - 1, 1)
    pm.select(newShape, r=True)
    pm.runtime.DeleteHistory(newShape)
    pm.delete(str(tempBase) + 'Base')
    pm.delete(tempBase)
    return newShape


def ar_bakeShapeUsingWrap(baseGeo, newGeo):
    """
    @ bake blendshape using wrap deformer.
    Args:
        baseGeo (str, PyNode): base geometry transform.
        newGeo (str, PyNode): edited shape transform.

    Returns:
            newShape.
    """
    oldGeo = pm.PyNode(baseGeo)
    newGeo = pm.PyNode(newGeo)
    # find blendshape node.
    bShpNode = ar_find.ar_findInputNodeType(oldGeo, 'blendShape')[0]
    bShpNode = pm.PyNode(bShpNode)
    # set all weight at zero.
    for i in range(bShpNode.getWeightCount()):
        bShpNode.setWeight(i, 0)
    # create targets.
    for each in pm.listAttr(bShpNode + '*.w', k=True, m=True):
        # duplicate new geometry.
        dupNewGeo = pm.duplicate(newGeo, rr=True, n=each)[0]
        pm.select(dupNewGeo, oldGeo)
        pm.runtime.CreateWrap()
        # on blendShape.
        pm.setAttr(bShpNode + '.' + each, 1)
        pm.runtime.DeleteHistory(dupNewGeo)
        pm.delete(oldGeo + 'Base')
        pm.setAttr(bShpNode + '.' + each, 0)
        ar_qui.ar_displayMessage('success', '% shape created' % each)


def ar_bakeShapeWithIbUsingWrap(baseGeo, newGeo, addShape=None):
    """
    @ bake blendshape with in-between shapes using wrap deformer .
    Args:
        baseGeo (str, PyNode): base geometry transform.
        newGeo (str, PyNode): edited shape transform.
        addShape (bool): if shape want to add then pass True.

    Returns:
            newShapes.
    """
    oldGeo = pm.PyNode(baseGeo)
    newGeo = pm.PyNode(newGeo)
    # find blendshape node.
    bShpNode = ar_find.ar_findInputNodeType(oldGeo, 'blendShape')[0]
    bShpNode = pm.PyNode(bShpNode)
    # set all weight at zero.
    for i in range(bShpNode.getWeightCount()):
        bShpNode.setWeight(i, 0)
    # blendshape in-between information.
    blendValueInfo = ar_getBlendshapeIbInfo(bShpNode)
    # create targets.
    newShapes = list()
    for each in pm.listAttr(bShpNode + '*.w', k=True, m=True):
        if len(blendValueInfo[each]) != 1:
            for x in blendValueInfo[each]:
                if x != 1:
                    # duplicate new geometry.
                    dupNewGeo = pm.duplicate(newGeo, rr=True, n=each + '__ib__' + str(x).split('.')[1])[0]
                    pm.select(dupNewGeo, oldGeo)
                    pm.runtime.CreateWrap()
                    # on blendShape.
                    pm.setAttr(bShpNode + '.' + each, x)
                    pm.runtime.DeleteHistory(dupNewGeo)
                    pm.delete(oldGeo + 'Base')
                    pm.setAttr(bShpNode + '.' + each, 0)
                    newShapes.append(dupNewGeo)
                    ar_qui.ar_displayMessage('success', '% shape created' % each)
                else:
                    # duplicate new geometry.
                    dupNewGeo = pm.duplicate(newGeo, rr=True, n=each)[0]
                    pm.select(dupNewGeo, oldGeo)
                    pm.runtime.CreateWrap()
                    # on blendShape.
                    pm.setAttr(bShpNode + '.' + each, 1)
                    pm.runtime.DeleteHistory(dupNewGeo)
                    pm.delete(oldGeo + 'Base')
                    pm.setAttr(bShpNode + '.' + each, 0)
                    newShapes.append(dupNewGeo)
                    ar_qui.ar_displayMessage('success', '% shape created' % each)
        else:
            # duplicate new geometry.
            dupNewGeo = pm.duplicate(newGeo, rr=True, n=each)[0]
            pm.select(dupNewGeo, oldGeo)
            pm.runtime.CreateWrap()
            # on blendShape.
            pm.setAttr(bShpNode + '.' + each, 1)
            pm.runtime.DeleteHistory(dupNewGeo)
            pm.delete(oldGeo + 'Base')
            pm.setAttr(bShpNode + '.' + each, 0)
            newShapes.append(dupNewGeo)
            ar_qui.ar_displayMessage('success', '% shape created' % each)
    # add blendshape if bool is true.
    if addShape:
        # create blendshapes.
        for each in newShapes:
            if each.find('__ib__') == -1:
                ar_addBlendShape(each, newGeo)
        # find in-between shapes.
        allInbetweenShapes = []
        for each in newShapes:
            if each.find('__ib__') != -1:
                allInbetweenShapes.append(each)
        # apply in-between shapes.
        for each in allInbetweenShapes:
            splitValue = len(each.split('__ib__')[1]) + 6
            shapeBaseName = each[:-splitValue]
            shapeVal = float(str('.' + each.split('__ib__')[1]))
            newBsNode = ar_find.ar_findInputNodeType(newGeo, 'blendShape')[0]
            shapeIndex = pm.listAttr(newBsNode + '*.w', k=True, m=True).index(shapeBaseName) + 1
            pm.blendShape(newBsNode, edit=True, ib=True, t=(newGeo, shapeIndex, each, shapeVal))


def ar_getBlendshapeWeightNames(blendshapeNode):
    """
    @ get blendshape weight names from blendshape node.
    Args:
        blendshapeNode (str, PyNode): blendshape node.

    Returns:
            blendshape list (list).
    """
    blendshapeNode = pm.PyNode(blendshapeNode)
    return pm.listAttr(blendshapeNode + '*.w', k=True, m=True)


def ar_getBlendshapeIbInfo(bShpNode):
    """
    @ get blendshape and its in-between shape information from connections.
    Args:
        bShpNode (str, PyNode): blendshape node name.

    Returns:
            blendshape information (dict).
    """
    iTg = '%s.inputTarget[0]' % bShpNode
    iTi = '.inputTargetItem'
    dicCrGrp = {}
    allCrName = pm.listAttr(bShpNode + '.weight', m=True)
    allCrGrp = pm.getAttr(bShpNode + '.weight', mi=True)
    for nm in allCrName:
        dicCrGrp[nm] = allCrGrp[allCrName.index(nm)]
    # get blendshape information with in-between.
    dicCrGrpItem = {}
    for crName in dicCrGrp.keys():
        iTgGr = '.inputTargetGroup[%s]' % dicCrGrp[crName]
        grpItem = pm.getAttr(iTg + iTgGr + iTi, mi=True)
        if grpItem is None:
            pm.getAttr(iTg + iTgGr + '.inputTargetItem[6000].inputGeomTarget')
            pm.getAttr(iTg + iTgGr + '.inputTargetItem[6000].inputPointsTarget')
            pm.getAttr(iTg + iTgGr + '.inputTargetItem[6000].inputComponentsTarget')
            grpItem = [6000]
            dicCrGrpItem[crName] = (dicCrGrp[crName], grpItem)
        dicCrGrpItem[crName] = (dicCrGrp[crName], grpItem)
    # rearrange dictionary.
    blendshapeInfoDict = {}
    for each in dicCrGrpItem.keys():
        newValues = list()
        for x in dicCrGrpItem[each][1]:
            if x == 6000:
                newValues.append(1)
            else:
                newValues.append(float('0.{}'.format(x - 5000)))
        blendshapeInfoDict[each] = sorted(newValues)
    return blendshapeInfoDict

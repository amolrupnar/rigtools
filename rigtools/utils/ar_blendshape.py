import pymel.core as pm

from rigtools.ui import ar_qui
from rigtools.utils import ar_find

reload(ar_qui)
reload(ar_find)


def ar_addBlendShape(source, target, value=0):
    """
    @ add blendshape in target.
    Args:
        source (str):  transform of source geometry.
        target (str): transform of target geometry.
        value (float): addBlendShapeValue

    Returns:
            face_blend.
    """
    source = pm.PyNode(source)
    target = pm.PyNode(target)
    # get existing blendshape if exist.
    blendshapes = []
    allHist = target.history(pdo=True)
    for each in allHist:
        if each.nodeType() == 'blendShape':
            blendshapes.append(each)
    # add blendshape.
    if not blendshapes:
        face_blend = pm.blendShape(source, target, foc=True, n='BS_' + target)[0]
        weightCount = face_blend.getWeightCount()
        face_blend.setWeight(weightCount - 1, value)
    elif len(blendshapes) == 1:
        face_blend = blendshapes[0]
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
        baseGeo (str): base geometry transform.
        editedGeo (str): edited shape transform.
        newShapeName (str): new geometry name.
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
        baseGeo (str): base geometry transform.
        newGeo (str): edited shape transform.

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

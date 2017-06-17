import pymel.core as pm

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_addBlendShape(source, target):
    """
    @ add blendshape in target.
    Args:
        source (str):  transform of source geometry.
        target (str): transform of target geometry.

    Returns:
            bool.
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
        blendNode = pm.blendShape(source, target, foc=True, n='BS_' + target)[0]
        weightCount = blendNode.listAttr(m=True, k=True)
        for each in weightCount:
            pm.setAttr(each, 1)
    elif len(blendshapes) == 1:
        face_blend = blendshapes[0]
        weightCount = face_blend.getWeightCount()
        pm.blendShape(face_blend, edit=True, t=(target, weightCount + 1, source, 1.0))
        face_blend.setWeight(weightCount + 1, 1)
    else:
        ar_qui.ar_displayMessage('error', 'geometry have more than one blenshapes found...')
        return False
    return True

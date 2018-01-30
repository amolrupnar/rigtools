import pymel.core as pm


def ar_findInputNodeType(obj, nodeType):
    """
    @ return node name of node type of object.
    Args:
        obj (str, PyNode): object which you return node name.
        nodeType (str): nodeType ('blendshape').

    Returns:
            nodeName.
    """
    obj = pm.PyNode(obj)
    nodeName = list()
    [nodeName.append(str(each)) for each in pm.listHistory(obj, pdo=True) if each.nodeType() == nodeType]
    if nodeName:
        return nodeName
    return False

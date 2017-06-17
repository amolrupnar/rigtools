from maya import OpenMaya as om
from pymel import core as pm


def ar_distanceCompareBetweenTwoObjects(objA, objB):
    """
    @ get xform of two objects and minus its and get return.
    Args:
        objA (str): first object.
        objB (str): second object.

    Returns:
            posX, posY, posZ
    """
    obj1 = pm.PyNode(objA)
    obj2 = pm.PyNode(objB)
    obj1Pos = pm.xform(obj1, q=True, ws=True, t=True)
    obj2Pos = pm.xform(obj2, q=True, ws=True, t=True)

    posX = obj1Pos[0] - obj2Pos[0]
    posY = obj1Pos[1] - obj2Pos[1]
    posZ = obj1Pos[2] - obj2Pos[2]
    return posX, posY, posZ


def ar_getLength(valX, valY, valZ):
    """
    @ get vector length using open maya MVector.
    Args:
        valX (float): x axis value.
        valY (float): y axis value.
        valZ (float): z axis value.

    Returns:
            distance.length
    """
    distance = om.MVector(valX, valY, valZ)
    return distance.length()


def ar_getDistanceBetweenTwoObjects(obj1, obj2):
    """
    @ get distance between two objects.
    Args:
        obj1 (str): first object.
        obj2 (str): second object.

    Returns:
            length.
    """
    valX, valY, valZ = ar_distanceCompareBetweenTwoObjects(obj1, obj2)
    return ar_getLength(valX, valY, valZ)

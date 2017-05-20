from maya import OpenMaya as om
from pymel import core as pm


def distanceCompareBetweenTwoObjects(objA, objB):
    """
    get xform of two objects and minus its and get return.
    :param objA: string
    :param objB: string
    :return: positions (x,y,z)
    """
    obj1 = pm.PyNode(objA)
    obj2 = pm.PyNode(objB)
    obj1Pos = pm.xform(obj1, q=True, ws=True, t=True)
    obj2Pos = pm.xform(obj2, q=True, ws=True, t=True)

    posA = obj1Pos[0] - obj2Pos[0]
    posB = obj1Pos[1] - obj2Pos[1]
    posC = obj1Pos[2] - obj2Pos[2]
    return posA, posB, posC


def getLength(valX, valY, valZ):
    """
    get length
    :param valX: float
    :param valY: float
    :param valZ: float
    :return: length (float)
    """
    distance = om.MVector(valX, valY, valZ)
    return distance.length()


def getDistanceBetweenTwoObjects(obj1, obj2):
    valX, valY, valZ = distanceCompareBetweenTwoObjects(obj1, obj2)
    return getLength(valX, valY, valZ)

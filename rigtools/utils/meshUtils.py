import maya.OpenMaya as OpenMaya
import pymel.core as pm


def getClosestVertex(geo, obj):
    """
    get closest vertex of obj
    :param geo: string
    :param obj: string
    :return: closestVert
    """
    geo = pm.PyNode(geo)
    obj = pm.PyNode(obj)
    pos = obj.getRotatePivot(space='world')
    # nodeDagPath = OpenMaya.MDagPath()
    try:
        selectionList = OpenMaya.MSelectionList()
        selectionList.add(geo.name())
        nodeDagPath = OpenMaya.MDagPath()
        selectionList.getDagPath(0, nodeDagPath)
    except:
        raise RuntimeError('OpenMaya.MDagPath() failed on %s' % geo.name())
    nodeDagPath = OpenMaya.MDagPath()
    mfnMesh = OpenMaya.MFnMesh(nodeDagPath)

    pointA = OpenMaya.MPoint(pos.x, pos.y, pos.z)
    pointB = OpenMaya.MPoint()

    space = OpenMaya.MSpace.kWorld

    util = OpenMaya.MScriptUtil()
    util.createFromInt(0)
    idPointer = util.asIntPtr()

    mfnMesh.getClosestPoint(pointA, pointB, space, idPointer)
    idx = OpenMaya.MScriptUtil(idPointer).asInt()

    faceVerts = [geo.vtx[i] for i in geo.f[idx].getVertices()]
    closestVert = None
    minLength = None
    for v in faceVerts:
        thisLength = (pos - v.getPosition(space='world')).length()
        if minLength is None or thisLength < minLength:
            minLength = thisLength
            closestVert = v
    return closestVert

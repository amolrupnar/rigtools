import pymel.core as pm


def transferRivet(source, dest):
    """
    transfer loft CurceFromMeshEdge connection from source to destination geometry.
    :param source: string (shape node)
    :param dest: string (shape node)
    :return: crvFrmMshEdg
    """
    source = pm.PyNode(source)
    dest = pm.PyNode(dest)
    allConnections = source.connections()
    crvFrmMshEdg = list()
    for each in allConnections:
        if each.nodeType() == 'curveFromMeshEdge':
            crvFrmMshEdg.append(each)

    for each in crvFrmMshEdg:
        # noinspection PyTypeChecker
        pm.connectAttr('{0}.worldMesh[0]'.format(dest), '{0}.inputMesh'.format(each), f=True)
    return crvFrmMshEdg

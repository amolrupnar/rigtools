import pymel.core as pm

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_transferRivet(source, dest):
    """
    @ transfer loft CurveFromMeshEdge connection from source to destination geometry.
    Args:
        source (str): source shape node.
        dest (str): destination shape node.

    Returns:
            crvFrmMshEdg.
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
    ar_qui.ar_displayMessage('success', 'all rivet transfer done.')
    return crvFrmMshEdg

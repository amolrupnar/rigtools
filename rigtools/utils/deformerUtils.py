import pymel.core as pm


def removeFromDeformerInvertedVertex(deformer, sel=None):
    """
    invert(all vertex - sel vertex) your selected vertex and remove from deformer set.
    :param deformer: string
    :param sel: list
    :return: None
    """
    deformerNd = pm.PyNode(deformer)
    if not sel:
        sel = pm.ls(sl=True, fl=True)
    # query geometry from selection.
    geo = pm.ls(sel[0], o=True)[0]
    deformerSet = deformerNd.deformerSet()
    allVert = pm.ls(geo + '.vtx[*]', fl=True)
    unwantedVert = list(set(allVert) - set(sel))
    # remove from deformer set.
    pm.sets(deformerSet, rm=unwantedVert)
    print ('selected vertex is only affect with %s deformer.' % deformer),

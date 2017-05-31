import pymel.core as pm
from rigtools.utils import bake


def bakeHair(dynCrvs=None):
    """
    bake hair dynamics.
    :param dynCrvs: list (list)
    :return: bake hair curves.
    """
    if not dynCrvs:
        # Query all dynamic curve using specific name.
        dynCrvs = pm.ls("*DynIKCurveSoftdyn*", "*:DynIKCurveSoftdyn*", "DynIKCurveSoftdyn*", type='nurbsCurve')
    else:
        # convert list into PyNode.
        dynCrvs = [pm.PyNode(x) for x in dynCrvs]
    # query playback options.
    minFrame = pm.playbackOptions(q=True, min=True)
    maxFrame = pm.playbackOptions(q=True, max=True)
    astFrame = pm.playbackOptions(q=True, ast=True)
    crtFrame = pm.currentTime(q=True)
    # set playback options -50 frames from current time.
    pm.playbackOptions(e=True, ps=0, mps=1)
    pm.playbackOptions(min=minFrame - 50, ast=astFrame - 50)
    pm.currentTime(minFrame - 50)
    # set all particle start time -50 from current time.
    # allParticles = pm.ls(type='particle')
    # for each in allParticles:
    #     each.startFrame.set(minFrame - 50)
    for each in dynCrvs:
        particleShape = each.getParent().getChildren(ad=True, type='particle')[0]
        particleShape.startFrame.set(minFrame - 50)
    # bake animation curve.
    bake.bakeCurveAnim(dynCrvs, minFrame - 50, maxFrame)
    # off dynamics.
    for each in dynCrvs:
        # get children particle.
        particleShape = each.getParent().getChildren(ad=True, type='particle')[0]
        particleShape.isDynamic.set(0)
    # apply default values.
    pm.playbackOptions(min=minFrame, ast=astFrame)
    pm.currentTime(crtFrame, e=True)


def unBakeHair(dynCrvs=None):
    """
    unbake hair dynamics and on particle dynamics.
    :param dynCrvs: list
    :return: unbake hair dynamic.
    """
    if not dynCrvs:
        dynCrvs = pm.ls("*DynIKCurveSoftdyn*", "*:DynIKCurveSoftdyn*", "DynIKCurveSoftdyn*", type='nurbsCurve')
    else:
        # convert list into PyNode.
        dynCrvs = [pm.PyNode(x) for x in dynCrvs]
    for each in dynCrvs:
        particleShape = each.getParent().getChildren(ad=True, type='particle')[0]
        if not pm.isConnected(particleShape.targetGeometry, each.create):
            particleShape.targetGeometry.connect(each.create, f=True)
        if len(each.listConnections(type='animCurve')):
            pm.delete(each.listConnections(type='animCurve'))
        # get spans.
        spans = pm.getAttr(each.spans)
        degrees = each.degree()
        totalCvs = spans + degrees
        for i in range(totalCvs):
            pm.setAttr(str(each) + '.cv[' + str(i) + ']', [0, 0, 0])
        # dynamics on
        particleShape.isDynamic.set(1)

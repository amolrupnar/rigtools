import pymel.core as pm


def ar_bakeIkJoints(ikHandles, startFrame=None, endFrame=None, particleShps=None):
    """
    @ bake ik joints (using query ik handle joint list).
    Args:
        ikHandles (list): list of ik handle which will bake.
        startFrame (float): start frame (if not provide query from timeline).
        endFrame (float): end frame (if not provide query from timeline).
        particleShps (list): particle list if using particle on curve.

    Returns:
            bool.
    """
    # convert arguments into PyNode.
    ikHandles = [pm.PyNode(x) for x in ikHandles]
    # Query ik Handle related joints.
    joints = [pm.ikHandle(x, q=True, jl=True) for x in ikHandles]
    if not startFrame:
        # query playback options.
        startFrame = pm.playbackOptions(q=True, min=True)
        endFrame = pm.playbackOptions(q=True, max=True)
        # set playback options -50 frames from current time.
        pm.playbackOptions(e=True, ps=0, mps=1)
        pm.currentTime(startFrame - 50)
    # animation start time and current time query and set it to -50.
    astFrame = pm.playbackOptions(q=True, ast=True)
    crtFrame = pm.currentTime(q=True)
    pm.playbackOptions(min=startFrame - 50, ast=astFrame - 50)
    # if particle shapes is passed.
    if particleShps:
        particleShps = [pm.PyNode(x) for x in particleShps]
        # set particle start frame at -50 from current time.
        for each in particleShps:
            each.startFrame.set(startFrame - 50)
    # bake simulation.
    pm.bakeResults(joints, sm=True, t=str(startFrame) + ':' + str(endFrame), sb=1, dic=1, pok=1, sac=False, cp=False,
                   s=False)
    # off dynamics if particle argument is passed.
    if particleShps:
        [x.isDynamic.set(0) for x in particleShps]
    # apply default values.
    pm.playbackOptions(min=startFrame, ast=astFrame)
    pm.currentTime(crtFrame, e=True)
    return True


def ar_unBakeIkJoints(ikHandles, particleShps=None):
    """
    @ unbake ik joints (query ik handle joint list)
    Args:
        ikHandles (list): ik handles which has to be unbake.
        particleShps: particle shapes which has to be on dynamics after the unbake.

    Returns:
            bool.
    """
    # convert arguments into PyNode.
    ikHandles = [pm.PyNode(x) for x in ikHandles]
    # Query ik Handle related joints.
    joints = [pm.ikHandle(x, q=True, jl=True) for x in ikHandles]
    if particleShps:
        particleShps = [pm.PyNode(x) for x in particleShps]
    # delete animation curves on all joints.
    pm.delete(pm.listConnections(joints, type='animCurve'))
    # on ik blend on all joints related ik Handles.
    [pm.listConnections(x, type='ikHandle')[0].ikBlend.set(1) for x in joints]
    if particleShps:
        [x.isDynamic.set(1) for x in particleShps]
    return True


def ar_bakeCurveAnim(curve, startTime, endTime):
    """
    @ bake curve cv animation.
    Args:
        curve (list): list of curves.
        startTime (float): start time.
        endTime (float): end time.

    Returns:
            bool.
    """
    pm.bakeResults(curve, sm=True, t=str(startTime) + ':' + str(endTime), sb=1, dic=0, pok=0, sac=False, cp=True,
                   s=False)
    return True

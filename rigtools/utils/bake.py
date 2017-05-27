import pymel.core as pm


# query all particles.
def bakeCurveAnim(curve, startTime, endTime):
    """
    bake curve cv animation.
    :param curve: list (list of curves)
    :param startTime: float
    :param endTime: float
    :return: animation bake.
    """
    pm.bakeResults(curve, sm=True, t=str(startTime) + ':' + str(endTime), sb=1, dic=0, pok=0, sac=False, cp=True,
                   s=False)

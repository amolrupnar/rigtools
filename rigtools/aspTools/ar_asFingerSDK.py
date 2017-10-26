import pymel.core as pm


def ar_asAddFingerFistAndRelaxGroupsOnControllers():
    """
    @ add two upper groups on finger controllers.
    Returns:
            fingerUpperGroups (None).
    """
    # add groups
    fingCtrls = ['FKMiddleFinger1_L', 'FKMiddleFinger2_L', 'FKMiddleFinger3_L', 'FKThumbFinger1_L',
                 'FKThumbFinger2_L', 'FKThumbFinger3_L', 'FKIndexFinger1_L', 'FKIndexFinger2_L', 'FKIndexFinger3_L',
                 'FKPinkyFinger1_L', 'FKPinkyFinger2_L', 'FKPinkyFinger3_L', 'FKRingFinger1_L', 'FKRingFinger2_L',
                 'FKRingFinger3_L', 'FKMiddleFinger1_R', 'FKMiddleFinger2_R', 'FKMiddleFinger3_R', 'FKThumbFinger1_R',
                 'FKThumbFinger2_R', 'FKThumbFinger3_R', 'FKIndexFinger1_R', 'FKIndexFinger2_R', 'FKIndexFinger3_R',
                 'FKPinkyFinger1_R', 'FKPinkyFinger2_R', 'FKPinkyFinger3_R', 'FKRingFinger1_R', 'FKRingFinger2_R',
                 'FKRingFinger3_R', 'FKCup_L', 'FKCup_R']
    fingerUpperGroups = list()
    for each in fingCtrls:
        fingerController = pm.PyNode(each)
        pm.select(cl=True)
        # make a groups.
        fistGroup = pm.createNode('transform', n='FKFistExtra' + fingerController[2:], ss=True)
        relaxGroup = pm.createNode('transform', n='FKRelaxExtra' + fingerController[2:], ss=True)
        fingerUpperGroups.append(fistGroup)
        fingerUpperGroups.append(relaxGroup)
        # set rotate order.
        if not fingerController.startswith('FKCup_'):
            fistGroup.rotateOrder.set(5)
            relaxGroup.rotateOrder.set(5)
        # parent fist group.
        pm.parent(fistGroup, fingerController.getParent())
        fistGroup.t.set([0, 0, 0])
        fistGroup.r.set([0, 0, 0])
        pm.parent(fingerController, fistGroup)
        # parent relax group.
        pm.parent(relaxGroup, fingerController.getParent())
        relaxGroup.t.set([0, 0, 0])
        relaxGroup.r.set([0, 0, 0])
        pm.parent(fingerController, relaxGroup)
    return fingerUpperGroups


def ar_asFistKeyConnection():
    """
    @ select fist animCurves and then run this function it will connect keys with finger fist attribute and controllers.
    Returns:
            None.
    """
    # connect keys with finger controller.
    sel = pm.ls(sl=True)

    for each in sel:
        groupName = ''
        for i in range(len(each.split('_')) - 1):
            groupName += each.split('_')[i] + '_'
        groupName = 'FKFistExtra' + groupName[2:-1]
        each.output.connect(groupName + '.' + each.split('_')[-1])
    # connect main finger controller fist attribute to keys inputs.
    # select all keys and then run.
    for each in sel:
        if each.split('_')[-2] == 'L':
            fist = pm.PyNode('Fingers_L')
            fist.fist.connect(each + '.input')
        if each.split('_')[-2] == 'R':
            fist = pm.PyNode('Fingers_R')
            fist.fist.connect(each + '.input')
        each.rename('FKFistExtra' + each[2:])


def ar_asRelaxKeyConnection():
    """
    @ select relax anim curve and run function it will connect keys with relax attribute on finger controller.
    Returns:
            None.
    """
    # connect keys with finger controller.
    sel = pm.ls(sl=True)

    for each in sel:
        groupName = ''
        for i in range(len(each.split('_')) - 1):
            groupName += each.split('_')[i] + '_'
        groupName = 'FKRelaxExtra' + groupName[2:-1]
        each.output.connect(groupName + '.' + each.split('_')[-1])
    # connect main finger controller relax attribute to keys inputs.
    # select all keys and then run.
    for each in sel:
        if each.split('_')[-2] == 'L':
            relax = pm.PyNode('Fingers_L')
            relax.relax.connect(each + '.input')
        if each.split('_')[-2] == 'R':
            relax = pm.PyNode('Fingers_R')
            relax.relax.connect(each + '.input')
        each.rename('FKRelaxExtra' + each[2:])

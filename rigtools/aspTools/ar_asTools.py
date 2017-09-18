from maya import cmds as cmds
from pymel import core as pm

from rigtools.utils import ar_constraint
from rigtools.utils import ar_mesure
from rigtools.ui import ar_qui
from rigtools.ext import ar_gen

reload(ar_constraint)
reload(ar_mesure)
reload(ar_qui)
reload(ar_gen)


def ar_asIKCtlOriChange(joint, controller):
    """
    @ change ik controller orientation as local (getting joint orientation for reference).
    Args:
        joint (str): this parameter is use only for orientation reference.
        controller (str): ik controller.

    Returns:
            controller.
    """
    cmds.select(cl=True)
    tempLoc = cmds.spaceLocator()
    tempLoc1 = cmds.spaceLocator()
    cmds.select(cl=True)
    cmds.delete(cmds.parentConstraint(joint, tempLoc))
    cmds.delete(cmds.parentConstraint(joint, tempLoc1))
    cmds.parent(tempLoc, 'IKOffset' + controller[2:])
    listParents = cmds.listRelatives(controller, c=True)
    for i in range(1, len(listParents)):
        cmds.parent(listParents[i], tempLoc[0])
    cmds.delete(cmds.parentConstraint(tempLoc1, 'IKExtra' + controller[2:]))
    for i in range(1, len(listParents)):
        cmds.parent(listParents[i], controller)
    cmds.delete(tempLoc, tempLoc1)
    cmds.select(cl=True)

    # Add Hand Ik Extra Group Rotation value In Build Pose.
    GetAttrs = cmds.getAttr('buildPose.udAttr')
    qExtra = cmds.xform('IKExtra' + controller[2:], q=True, os=True, ro=True)
    newAttrs = GetAttrs.replace('xform -os -t 0 0 0 -ro 0 0 0 %s;' % ('IKExtra' + controller[2:]),
                                'xform -os -t 0 0 0 -ro %f %f %f %s;' % (
                                    qExtra[0], qExtra[1], qExtra[2], 'IKExtra' + controller[2:]))
    cmds.setAttr('buildPose.udAttr', newAttrs, type="string")
    cmds.select(controller, r=True)
    ar_qui.ar_displayMessage('success', '{0} orientation changed... '.format(controller))
    return controller


def ar_changeDrawStyleOfExtraJoints():
    """
    @ none draw style of unused joints in asp rig tool.
    Returns:
            unusedJoints.
    """
    with ar_qui.ar_undoChunkOpen('hide extra joints'):
        unusedJoints = cmds.ls('FKX*', 'IKX*', 'FKOffset*', type='joint')
        for each in unusedJoints:
            cmds.setAttr(each + '.drawStyle', 2)
        return unusedJoints


def ar_fkCtlInIkSpine(startCtl, endCtl, hipCtlGrps, ctlName='Fk_Spine', ctlNum=4):
    """
    @ create fk controllers in advance skeleton ik spine setup.
    Args:
        startCtl (str): bottom ik controller.
        endCtl (str): top ik controller.
        hipCtlGrps (list): list of hip offset group os controllers.
        ctlName (string): controller name for fk spine.
        ctlNum (int): number of controller to add.

    Returns:
            ctrls.
    """
    loc = []
    for i in range(ctlNum + 1):
        newLoc = pm.spaceLocator(p=[0, 0, 0])
        loc.append(newLoc)

    # get length between start ctl and end ctl.
    pos = ar_mesure.ar_distanceCompareBetweenTwoObjects(startCtl, endCtl)
    length = ar_mesure.ar_getLength(pos[0], pos[1], pos[2])
    dividedLength = length / ctlNum

    for i in range(len(loc)):
        if i == 0:
            pm.delete(pm.parentConstraint(startCtl, loc[i]))
            ar_constraint.ar_aimConstraint([1, 0, 0], [0, 0, 1], [endCtl, str(loc[i])], freeze=False)
        else:
            setValX = dividedLength
            pm.parent(loc[i], loc[i - 1])
            loc[i].t.set(setValX, 0, 0)
            loc[i].r.set(0, 0, 0)
            setValX += dividedLength

    # create controllers.
    ctrls = []
    ctrlGrps = []
    ctrlGrpFollows = []
    for i in range(len(loc[:-1])):
        ctr = pm.modeling.circle(n=ctlName + str(i + 1), nrx=0, nry=1, nrz=0, ch=False)
        ctrls.append(ctr[0])
        ctrGrpExtra = pm.group(em=True, n=ctlName + str(i + 1) + '_Extra')
        ctrGrp = pm.group(em=True, n=ctlName + str(i + 1) + '_Grp')
        ctrlGrps.append(ctrGrp)
        ctrGrpFollow = pm.group(em=True, n=ctlName + str(i + 1) + '_Grp' + '_Follow')
        ctrlGrpFollows.append(ctrGrpFollow)
        pm.parent(ctr[0], ctrGrpExtra)
        pm.parent(ctrGrpExtra, ctrGrp)
        pm.parent(ctrGrp, ctrGrpFollow)
        pm.delete(pm.pointConstraint(loc[i], ctrGrpFollow))

    for i in range(2, len(ctrlGrpFollows)):
        pm.parentConstraint(ctrls[i - 1], ctrlGrpFollows[i], mo=True)

    # To put New controller in their corresponding Grp.
    pm.parentConstraint(ctrls[-1], 'IKOffset' + endCtl[2:], mo=True)
    pm.parentConstraint(ctrls[0], hipCtlGrps[0], mo=True)
    pm.parentConstraint(ctrls[0], hipCtlGrps[1], mo=True)
    pm.parentConstraint(startCtl, ctrlGrps[0])

    for each in range(len(ctrlGrpFollows)):
        pm.parent(ctrlGrpFollows[each], 'IKRootConstraint')
        pm.connectAttr('FKIKSpine_M.FKIKBlend', ctrlGrpFollows[each] + '.visibility')

    pm.parentConstraint('HipSwinger_M', 'IKOffset' + startCtl[2:], mo=True)
    pm.delete(loc)
    return ctrls


def ar_ikFootRollReOrient(ctl, ctlOffGrp, orientSample, rotateAxis='.rz', reverseConnections=False):
    """
    @ reorient ik roll controllers using re parenting.
    Args:
        ctl (str): controller.
        ctlOffGrp (str): controller offset group.
        orientSample (str): orient sample.
        rotateAxis (str): rotate axis with "." in prefix.
        reverseConnections (bool): bool.

    Returns:
            bool.
    """
    ctl = pm.PyNode(ctl)
    ctlOffGrp = pm.PyNode(ctlOffGrp)
    orientSample = pm.PyNode(orientSample)
    # offsetGroup changes.
    pm.select(cl=True)
    jt = pm.joint(n=ctlOffGrp[:-2] + 'Extra' + ctlOffGrp[-2:])
    pm.select(cl=True)
    jtTemp = pm.joint(n=ctlOffGrp + 'ConnTemp')
    pm.delete(pm.parentConstraint(orientSample, jt))
    parentGrp = ctlOffGrp.getParent()
    pm.parent(jt, parentGrp)
    pm.makeIdentity(jt, apply=True, t=1, r=1, s=1, n=0, pn=1)
    # query connection.
    connections = pm.connectionInfo(ctlOffGrp.rx, sfd=True)
    # attach connection.
    pm.connectAttr(connections, jtTemp + rotateAxis)
    pm.disconnectAttr(connections, ctlOffGrp.rx)
    # parent.
    children = ctlOffGrp.getChildren()
    pm.parent(children, jt)
    jtNewName = str(ctlOffGrp)
    pm.delete(ctlOffGrp)
    jt.rename(jtNewName)
    if reverseConnections:
        mdn = pm.createNode('multiplyDivide', n='multiplyDivideReverse' + jt)
        mdn.input2X.set(-1)
        pm.connectAttr(connections, mdn.input1X)
        mdn.outputX.connect(jt + rotateAxis)
        connName = pm.PyNode(connections.split('.')[0])
        if type(connName) == pm.nodetypes.UnitConversion:
            connName.conversionFactor.set(1)
    else:
        pm.connectAttr(connections, jt + rotateAxis)
    # delete tempJoint.
    pm.delete(jtTemp)
    # rotate controller group.
    children = ctl.getChildren()
    filtChildren = []
    for each in children:
        print each
        if type(each) == pm.nodetypes.NurbsCurve:
            pass
        elif each.rx.isConnected() or each.ry.isConnected() or each.rz.isConnected():
            pm.select(cl=True)
            newGroup = pm.createNode('transform', n=each + '_Freezed', ss=True)
            pm.delete(pm.parentConstraint(each, newGroup))
            pm.parent(newGroup, ctl)
            pm.parent(each, newGroup)
            filtChildren.append(newGroup)
        else:
            filtChildren.append(each)
    pm.parent(filtChildren, w=True)
    offChild = jt.getChildren()
    for each in offChild:
        each.r.set([0, 0, 0])
    pm.parent(filtChildren, ctl)
    return True


def ar_ikFootLiftToeReOrient(ctlOffGrp, orientSample, rotateAxis='.rz', reverseConnections=False):
    """
    @ re orient ikLiftToe controllers.
    Args:
        ctlOffGrp (str): controller offset group.
        orientSample (str): orientation sample.
        rotateAxis (str): rotation axis with "." in prefix.
        reverseConnections: bool

    Returns:
            bool.
    """
    ctlOffGrp = pm.PyNode(ctlOffGrp)
    orientSample = pm.PyNode(orientSample)
    # offsetGroup changes.
    pm.select(cl=True)
    jt = pm.joint(n=ctlOffGrp[:-2] + 'Extra' + ctlOffGrp[-2:])
    pm.select(cl=True)
    jtTemp = pm.joint(n=ctlOffGrp + 'ConnTemp')
    pm.delete(pm.parentConstraint(orientSample, jt))
    parentGrp = ctlOffGrp.getParent()
    pm.parent(jt, parentGrp)
    pm.makeIdentity(jt, apply=True, t=1, r=1, s=1, n=0, pn=1)
    # query connection.
    connections = pm.connectionInfo(ctlOffGrp.rx, sfd=True)
    # attach connection.
    pm.connectAttr(connections, jtTemp + rotateAxis)
    pm.disconnectAttr(connections, ctlOffGrp.rx)
    # parent.
    child = ctlOffGrp.getChildren()
    pm.parent(child, jt)
    jtNewName = str(ctlOffGrp)
    pm.delete(ctlOffGrp)
    jt.rename(jtNewName)
    if reverseConnections:
        mdn = pm.createNode('multiplyDivide', n='multiplyDivideReverse' + jt)
        mdn.input2X.set(-1)
        pm.connectAttr(connections, mdn.input1X)
        mdn.outputX.connect(jt + rotateAxis)
        connName = pm.PyNode(connections.split('.')[0])
        if type(connName) == pm.nodetypes.UnitConversion:
            connName.conversionFactor.set(1)
    else:
        pm.connectAttr(connections, jt + rotateAxis)
    # delete tempJoint.
    pm.delete(jtTemp)


def ar_addPlacementController():
    """
    @ add placement Controller in asp rig.
    Returns:
            controller.
    """
    if not pm.objExists('Group'):
        ar_qui.ar_displayMessage('error', 'Group Not Found..')
        return False
    if not pm.objExists('Main'):
        ar_qui.ar_displayMessage('error', 'Main Controller not Found..')
        return False
    mainCtl = pm.PyNode('Main')
    ctl = pm.modeling.circle(nr=[0, 1, 0], r=1, ch=False, n='Placement_C')[0]
    allCvs = pm.ls(mainCtl + '.cv[*]', fl=True)
    for i, each in enumerate(allCvs):
        pm.setAttr(ctl + '.cv[' + str(i) + '].xValue', pm.xform(each, q=True, ws=True, t=True)[0])
        pm.setAttr(ctl + '.cv[' + str(i) + '].yValue', pm.xform(each, q=True, ws=True, t=True)[1])
        pm.setAttr(ctl + '.cv[' + str(i) + '].zValue', pm.xform(each, q=True, ws=True, t=True)[2])
    ctl.s.set(1.2, 1.2, 1.2)
    pm.makeIdentity(ctl, apply=True, t=1, r=1, s=1, n=0, pn=1)
    # parenting.
    pm.parent(ctl, 'Group')
    pm.parent(mainCtl, ctl)
    ar_gen.ar_overrideColor(15, sel=[ctl])
    pm.select(cl=True)
    return ctl

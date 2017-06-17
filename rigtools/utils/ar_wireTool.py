import pymel.core as pm

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_addWireTool(curve, mesh, orientSample=None):
    """
    @ add wire from curve and add controller on each cv.
    Args:
        curve (str): wire curve.
        mesh (str): geometry.
        orientSample (str): sub controller orient aim point.

    Returns:
            bool.
    """
    # convert parameters into PyNode.
    curve = pm.PyNode(curve)
    mesh = pm.PyNode(mesh)
    curveUpperGroup = curve.getParent()
    if not curveUpperGroup:
        ar_qui.ar_displayMessage('error', 'Please create upperGroup on the "%s".' % curve)
        return False
    curveShape = curve.getShape()
    if not curveShape:
        ar_qui.ar_displayMessage('error', '"%s" has no shape.' % curve)
        return False

    # press tab from down line.
    cvs = pm.ls(curve + '.cv[*]', fl=True)
    cls = None
    if not orientSample:
        cls = pm.cluster(cvs, n=curve + '_Cluster')
        orientSample = cls[1]
    # create root group.
    rootGrp = pm.createNode('transform', n='Wire_' + curve + '_RootGrp', ss=True)
    controllersGrp = pm.createNode('transform', n=curve + '_Ctrl_Grp', ss=True)
    jointsGrp = pm.createNode('transform', n=curve + '_Joints_Grp', ss=True)
    pm.parent(controllersGrp, jointsGrp, rootGrp)
    pm.select(cl=True)
    # create main Controller.
    mainCtrl = curve.duplicate(n=curve + '_MainCtrl')[0]
    mainCtrl.v.unlock()
    mainCtrl.v.set(1)
    # hide default curve.
    curve.v.unlock()
    curve.v.set(0)
    curve.v.lock()
    pm.parent(mainCtrl, w=True)
    mainCtrlExtraGrp = pm.createNode('transform', n=curve + '_MainCtrl_ExtraGrp')
    mainCtrlOffsetGrp = pm.createNode('transform', n=curve + '_MainCtrl_OffsetGrp')
    pm.parent(mainCtrlExtraGrp, mainCtrlOffsetGrp)
    pm.delete(pm.parentConstraint(curveUpperGroup, mainCtrlOffsetGrp))
    pm.parent(mainCtrl, mainCtrlExtraGrp)
    # assign pivot and freeze transform main curve.
    pivPos = pm.xform(mainCtrlExtraGrp, q=True, ws=True, piv=True)[:3]
    pm.xform(mainCtrl, ws=True, piv=pivPos)
    pm.makeIdentity(mainCtrl, apply=True, t=1, r=1, s=1, n=0, pn=1)
    mainCtrl.setAttr('v', l=True, cb=False, k=False)
    # visibility attributes.
    pm.addAttr(mainCtrl, longName='visAttrs', at='enum', en='=====', k=True)
    mainCtrl.visAttrs.lock()
    pm.addAttr(mainCtrl, ln='clusterVis', at='bool', k=True)
    pm.addAttr(mainCtrl, ln='jointsVis', at='bool', k=True)
    pm.addAttr(mainCtrl, ln='subCtrlVis', at='bool', k=True, dv=True)
    # wire attributes.
    pm.addAttr(mainCtrl, ln='wireAttrs', at='enum', en='=====', k=True)
    mainCtrl.wireAttrs.lock()
    pm.addAttr(mainCtrl, ln='envelope', at='double', min=0, max=1, dv=1, k=True)
    pm.addAttr(mainCtrl, ln='dropoffDistance', at='double', min=0, dv=1, k=True)
    # -----------------------
    # create joints on each cv.
    joints = []
    for i, cv in enumerate(cvs):
        pm.select(cl=True)
        pos = pm.xform(cv, q=True, ws=True, t=True)
        jnt = pm.joint(p=pos, n=curve + '_' + str(i) + '_jt')
        joints.append(jnt)
        mainCtrl.jointsVis.connect(jnt.v)

    # x axis orient in center and create cluster and parent.
    for i in range(len(joints)):
        if i != len(cvs) - 1:
            pm.delete(
                pm.aimConstraint(orientSample, joints[i], o=[0, 0, 0], w=True, aim=[1, 0, 0], u=[0, 0, 1], wut="object",
                                 wuo=joints[i + 1]))
        else:
            pm.delete(
                pm.aimConstraint(orientSample, joints[i], o=[0, 0, 0], w=True, aim=[1, 0, 0], u=[0, 0, 1], wut="object",
                                 wuo=joints[0]))
        pm.makeIdentity(joints[i], a=True, t=1, r=1, s=1, n=0, pn=1)
        cvCls = pm.cluster(cvs[i], en=1, n=joints[i][:-2] + 'Cls')
        pm.parent(cvCls[1], joints[i])
        mainCtrl.clusterVis.connect(cvCls[1].v, f=True)
    if cls:
        pm.delete(cls)
    # create controllers.
    for i in range(len(joints)):
        # create sub controller.
        controller = pm.modeling.curve(d=1,
                                       p=[[-0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [-0.5, -0.5, 0.5],
                                          [-0.5, -0.5, -0.5],
                                          [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5], [0.5, -0.5, -0.5], [0.5, -0.5, 0.5],
                                          [0.5, 0.5, 0.5], [0.5, 0.5, -0.5], [0.5, -0.5, -0.5],
                                          [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [-0.5, 0.5, 0.5],
                                          [-0.5, 0.5, -0.5]],
                                       k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                                       n=joints[i] + '_CTRL')
        extraGroup = pm.createNode('transform', n=joints[i] + '_CTRL_ExtraGrp', ss=True)
        offsetGroup = pm.createNode('transform', n=joints[i] + '_CTRL_OffsetGrp', ss=True)
        # lock and hide unwanted attributes.
        mainCtrl.subCtrlVis.connect(offsetGroup.v)
        # controller.r.lock()
        controller.setAttr('rx', l=True, cb=False, k=False)
        controller.setAttr('ry', l=True, cb=False, k=False)
        controller.setAttr('rz', l=True, cb=False, k=False)
        controller.setAttr('sx', l=True, cb=False, k=False)
        controller.setAttr('sy', l=True, cb=False, k=False)
        controller.setAttr('sz', l=True, cb=False, k=False)
        controller.setAttr('v', l=True, cb=False, k=False)
        pm.parent(controller, extraGroup)
        pm.parent(extraGroup, offsetGroup)
        pm.delete(pm.parentConstraint(joints[i], offsetGroup))
        pm.parent(offsetGroup, mainCtrl)
        pm.parentConstraint(controller, joints[i])

    # parent all joints in joints grp.
    pm.parent(joints, jointsGrp)
    pm.parent(mainCtrlOffsetGrp, controllersGrp)
    # add Wire Tool on mesh.
    wireDeformer = pm.wire(mesh, gw=False, en=1.0, ce=0.0, li=0.0, w=curve, n='wire_' + curve)
    # connect wire attributes on main controller.
    mainCtrl.envelope.connect(wireDeformer[0].envelope, f=True)
    mainCtrl.dropoffDistance.connect(wireDeformer[0].dropoffDistance[0], f=True)
    ar_qui.ar_displayMessage('success', 'wire tool added successfully.')
    return True

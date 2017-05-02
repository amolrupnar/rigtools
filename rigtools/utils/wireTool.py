import maya.cmds as cmds


def jointCreate(curve, mesh):
    """
    create wire and add controllers
    :param curve: string
    :param mesh: string
    :return: wire
    """
    # get all curve.
    crv = cmds.listRelatives(curve, c=True, typ='nurbsCurve')
    if crv:
        cvs = cmds.ls(curve + '.cv[*]', fl=True)
        cls = cmds.cluster(cvs, n=curve + '_Cluster')
        # create root group.
        rootGrp = cmds.createNode('transform', n='Wire_' + curve + '_RootGrp')
        controllersGrp = cmds.createNode('transform', n=curve + '_Ctrl_Grp')
        jointsGrp = cmds.createNode('transform', n=curve + '_Joints_Grp')
        cmds.parent(controllersGrp, jointsGrp, rootGrp)
        cmds.select(cl=True)

        # create main controller.
        mainCtrl = cmds.circle(s=len(cvs), ch=False, n=curve + '_MainCtrl')
        mainCtrlExtraGrp = cmds.createNode('transform', n=curve + '_MainCtrl_ExtraGrp')
        mainCtrlOffsetGrp = cmds.createNode('transform', n=curve + '_MainCtrl_OffsetGrp')
        cmds.parent(mainCtrl[0], mainCtrlExtraGrp)
        cmds.parent(mainCtrlExtraGrp, mainCtrlOffsetGrp)
        cmds.delete(cmds.parentConstraint(curve, mainCtrlOffsetGrp))
        # xform all cvs on wire curve position.
        for i in range(len(cvs)):
            wPos = cmds.xform(cvs[i], q=True, ws=True, t=True)
            cmds.xform('%s_MainCtrl.cv[%d]' % (curve, i), ws=True, t=wPos)
        # add attributes on main controller.
        cmds.setAttr(mainCtrl[0] + '.v', l=True, k=False, cb=False)
        # visibility attributes.
        cmds.addAttr(mainCtrl[0], ln='visAttrs', at='enum', en='=====', k=True)
        cmds.setAttr(mainCtrl[0] + '.visAttrs', l=True)
        cmds.addAttr(mainCtrl[0], ln='clusterVis', at='bool', k=True)
        cmds.addAttr(mainCtrl[0], ln='jointsVis', at='bool', k=True)
        cmds.addAttr(mainCtrl[0], ln='subCtrlVis', at='bool', k=True)
        # wire attributes.
        cmds.addAttr(mainCtrl[0], ln='wireAttrs', at='enum', en='=====', k=True)
        cmds.setAttr(mainCtrl[0] + '.wireAttrs', l=True)
        cmds.addAttr(mainCtrl[0], ln='envelope', at='double', min=0, max=1, dv=1, k=True)
        cmds.addAttr(mainCtrl[0], ln='dropoffDistance', at='double', min=0, dv=1, k=True)
        # -----------------------
        # create joints on each cv.
        joints = []
        for i, ch in enumerate(cvs):
            cmds.select(cl=True)
            pos = cmds.xform(ch, q=True, ws=True, t=True)
            jnt = cmds.joint(p=pos, n=curve + '_' + str(i) + '_jt')
            joints.append(jnt)
            cmds.connectAttr(mainCtrl[0] + '.jointsVis', jnt + '.v', f=True)
        # x axis orient in center and create cluster and parent.
        for i in range(len(joints)):
            if i != len(cvs) - 1:
                cmds.delete(
                    cmds.aimConstraint(cls[1], joints[i], o=[0, 0, 0], w=True, aim=[1, 0, 0], u=[0, 0, 1], wut="object",
                                       wuo=joints[i + 1]))
                cmds.makeIdentity(joints[i], a=True, t=1, r=1, s=1, n=0, pn=1)
                cvCls = cmds.cluster(cvs[i], en=1, n=joints[i][:-2] + 'Cls')
                cmds.parent(cvCls[1], joints[i])
                cmds.connectAttr(mainCtrl[0] + '.clusterVis', cvCls[1] + '.v', f=True)
            else:
                cmds.delete(
                    cmds.aimConstraint(cls[1], joints[i], o=[0, 0, 0], w=True, aim=[1, 0, 0], u=[0, 0, 1], wut="object",
                                       wuo=joints[0]))
                cmds.makeIdentity(joints[i], a=True, t=1, r=1, s=1, n=0, pn=1)
                cvCls = cmds.cluster(cvs[i], en=1, n=joints[i][:-2] + 'Cls')
                cmds.parent(cvCls[1], joints[i])
                cmds.connectAttr(mainCtrl[0] + '.clusterVis', cvCls[1] + '.v', f=True)
        # delete cluster.
        cmds.delete(cls)
        # create controllers.
        for i in range(len(joints)):
            # create sub controllers.
            controller = cmds.curve(d=1, p=[[-0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [-0.5, -0.5, 0.5],
                                            [-0.5, -0.5, -0.5],
                                            [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5], [0.5, -0.5, -0.5], [0.5, -0.5, 0.5],
                                            [0.5, 0.5, 0.5], [0.5, 0.5, -0.5], [0.5, -0.5, -0.5],
                                            [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [-0.5, 0.5, 0.5], [-0.5, 0.5, -0.5]],
                                    k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], n=joints[i] + '_CTRL')
            # get controller shape and rename.
            shape = cmds.listRelatives(controller, s=True)
            cmds.rename(shape[0], controller + 'Shape')
            extraGroup = cmds.createNode('transform', n=joints[i] + '_CTRL_ExtraGrp')
            offsetGroup = cmds.createNode('transform', n=joints[i] + '_CTRL_OffsetGrp')
            cmds.parent(controller, extraGroup)
            cmds.parent(extraGroup, offsetGroup)
            cmds.delete(cmds.parentConstraint(joints[i], offsetGroup))
            cmds.parent(offsetGroup, mainCtrl[0])
            cmds.parentConstraint(controller, joints[i])
        # parent all joints in joints grp.
        cmds.parent(joints, jointsGrp)
        cmds.parent(mainCtrlOffsetGrp, controllersGrp)
        # add Wire Tool on mesh.
        wireDeformer = cmds.wire(mesh, gw=False, en=1.0, ce=0.0, li=0.0, w=curve, n='wire_' + curve)
        # connect wire attributes on main controller.
        cmds.connectAttr(mainCtrl[0] + '.envelope', wireDeformer[0] + '.envelope', f=True)
        cmds.connectAttr(mainCtrl[0] + '.dropoffDistance', wireDeformer[0] + '.dropoffDistance[0]', f=True)

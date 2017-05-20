import maya.cmds as cmds


def stretch():
    setupName = 'Nose'
    sel = cmds.ls(sl=True)
    chain = cmds.ls(sel[0], dag=True, typ='joint')
    IKSpine = cmds.ikHandle(sj=chain[0], ee=chain[len(chain) - 1], sol='ikSplineSolver')
    # rename
    cmds.rename(IKSpine[0], 'IKSplineHandle_' + setupName)
    cmds.rename(IKSpine[1], 'IKSplineEff_' + setupName)
    cmds.rename(IKSpine[2], 'IKSplineCurve_' + setupName)
    # create new joints.
    cmds.select(cl=True)
    bindStartJt = cmds.joint(n='JtCrvBind01')
    cmds.select(cl=True)
    bindEndJt = cmds.joint(n='JtCrvBind02')
    cmds.delete(cmds.parentConstraint(chain[0], bindStartJt))
    cmds.delete(cmds.parentConstraint(chain[len(chain) - 1], bindEndJt))

    cmds.skinCluster(bindStartJt, bindEndJt, 'IKSplineCurve_' + setupName, bm=0, sm=0, nw=1, wd=0, mi=2)
    ctlStart = cmds.circle(nr=[1, 0, 0], n='Toony' + setupName + '01_CTRL', ch=False)
    extraGrp = cmds.createNode('transform', n='Toony' + setupName + '01ExtraGrp')
    offGrp = cmds.createNode('transform', n='Toony' + setupName + '01OffsetGrp')
    cmds.parent(ctlStart[0], extraGrp)
    cmds.parent(extraGrp, offGrp)
    cmds.delete(cmds.parentConstraint(bindStartJt, offGrp))
    # endJOint
    ctlEnd = cmds.circle(nr=[1, 0, 0], n='Toony' + setupName + '02_CTRL', ch=False)
    extraGrpEnd = cmds.createNode('transform', n='Toony' + setupName + '02ExtraGrp')
    offGrpEnd = cmds.createNode('transform', n='Toony' + setupName + '02OffsetGrp')
    cmds.parent(ctlEnd[0], extraGrpEnd)
    cmds.parent(extraGrpEnd, offGrpEnd)
    cmds.delete(cmds.parentConstraint(bindEndJt, offGrpEnd))
    # parent constraint wiht bind joints.
    cmds.parentConstraint(ctlStart[0], bindStartJt)
    cmds.parentConstraint(ctlEnd[0], bindEndJt)
    # Create connection with node basis.
    crvInfo = cmds.createNode('curveInfo', n='curveInfo_Toony' + setupName)
    shpCrv = cmds.listRelatives('IKSplineCurve_' + setupName, s=True)
    cmds.connectAttr(shpCrv[0] + '.worldSpace[0]', crvInfo + '.inputCurve', f=True)
    mdnForSX = cmds.createNode('multiplyDivide', n='multiplyDivide_Toony' + setupName + '_ScaleX')
    mdnForPW = cmds.createNode('multiplyDivide', n='multiplyDivide_Toony' + setupName + '_Power')
    mdnForYZ = cmds.createNode('multiplyDivide', n='multiplyDivide_Toony' + setupName + '_ScaleYZ')
    cmds.setAttr(mdnForSX + '.operation', 2)
    cmds.setAttr(mdnForPW + '.operation', 3)
    cmds.setAttr(mdnForYZ + '.operation', 2)
    # connections.
    cmds.connectAttr(crvInfo + '.arcLength', mdnForSX + '.input1X', f=True)
    cmds.setAttr(mdnForSX + '.input2X', cmds.getAttr(mdnForSX + '.input1X'))
    scaledJoint = chain[:-1]
    for each in scaledJoint:
        cmds.connectAttr(mdnForSX + '.outputX', each + '.sx', f=True)
    # power connections.
    cmds.connectAttr(mdnForSX + '.outputX', mdnForPW + '.input1X', f=True)
    cmds.setAttr(mdnForPW + '.input2X', 0.5)
    cmds.connectAttr(mdnForPW + '.outputX', mdnForYZ + '.input2X', f=True)
    cmds.setAttr(mdnForYZ + '.input1X', 1)
    for each in scaledJoint:
        cmds.connectAttr(mdnForYZ + '.outputX', each + '.sy')
        cmds.connectAttr(mdnForYZ + '.outputX', each + '.sz')

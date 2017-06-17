from maya import cmds as cmds

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_addFk(axis, sel=None):
    """
    @ create fk controller chain on selected joint.
    Args:
        axis (list): axis example [1,0,0].
        sel (list): joints.

    Returns:
            controller.
    """
    # get selection.
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        ar_qui.ar_displayMessage('warning', 'Please select at least one joint.')
        return False
    for x in range(len(sel)):
        chain = cmds.ls(sel[x], dag=True, typ='joint')
        controller = []
        for i in range(len(chain)):
            if i != len(chain) - 1:
                cmds.select(cl=True)
                offGrp = cmds.joint(n='FKOffset' + chain[i])
                grp = cmds.group(n='FKExtra' + chain[i], em=True)
                ctrl = cmds.circle(ch=False, n='FK' + chain[i], nr=axis)
                cmds.select(cl=True)
                fkxGrp = cmds.joint(n='FKX' + chain[i])
                cmds.parent(ctrl[0], grp)
                cmds.parent(fkxGrp, ctrl[0])
                cmds.parent(grp, offGrp)
                cmds.delete(cmds.parentConstraint(chain[i], offGrp))
                cmds.makeIdentity(offGrp, a=True, t=1, r=1, s=1, n=0, pn=1)
                cmds.parentConstraint(fkxGrp, chain[i])
                controller.append(fkxGrp)
                if i != 0:
                    cmds.parent(offGrp, controller[i - 1])
            else:
                cmds.select(cl=True)
                fkxGrp = cmds.joint(n='FKX' + chain[i])
                cmds.delete(cmds.parentConstraint(chain[i], fkxGrp))
                cmds.parent(fkxGrp, controller[i - 1])
                cmds.parentConstraint(fkxGrp, chain[i])
        ar_qui.ar_displayMessage('success', 'done add fk controllers.')
        return controller


def ar_addFkProxy(axis, sel=None):
    """
    create fk proxy setup. will add it soon.
    :param axis: list ([1,0,0])
    :param sel: list (joint)
    :return: fkproxy chain
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        ar_qui.ar_displayMessage('success', 'No selections is present.')
    ar_qui.ar_displayMessage('success', '%s this tool will be coming soon...' % axis)
    # TODO: need to add fk proxy rig on existing or new.

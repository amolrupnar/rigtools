from maya import cmds as cmds

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_aimConstraintParent(aimValue, objValue, sel=None, freeze=True):
    """
    @ do create aimConstraint according to ui based axis and delete constraint,
    @ then parent first selected object and freeze transformation.
    Args:
        aimValue (list): [1,0,0]
        objValue (list): [1,0,0]
        sel (list): two objects selection order is aimObject and then main object.
        freeze (bool): maintain offset set to on or off.

    Returns:
            bool.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if len(sel) != 2:
        ar_qui.ar_displayMessage('error', 'please select two objects...')
        return False
    cmds.select(cl=True)
    # create locator and snap on selection one.
    loc = cmds.spaceLocator(n='TempLocatorForObjectUpOrientation')
    cmds.delete(cmds.parentConstraint(sel[1], loc[0]))
    if objValue == [1, 0, 0]:
        cmds.move(3, 0, 0, loc[0], r=True, os=True, wd=True)
    if objValue == [0, 1, 0]:
        cmds.move(0, 3, 0, loc[0], r=True, os=True, wd=True)
    if objValue == [0, 0, 1]:
        cmds.move(0, 0, 3, loc[0], r=True, os=True, wd=True)
    cmds.delete(cmds.aimConstraint(sel[0], sel[1], o=[0, 0, 0], w=True, aim=aimValue, u=objValue,
                                   wut="object", wuo=loc[0]))
    # parent joint.
    cmds.parent(sel[0], sel[1])
    if freeze:
        cmds.makeIdentity(sel[1], a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.setAttr(sel[0] + '.jointOrientX', 0)
    cmds.setAttr(sel[0] + '.jointOrientY', 0)
    cmds.setAttr(sel[0] + '.jointOrientZ', 0)
    # delete locator.
    cmds.delete(loc[0])
    cmds.select(sel[1])
    ar_qui.ar_displayMessage('success', 'constraint done')
    return True


def ar_aimConstraint(aimValue, objValue, sel=None, freeze=True):
    """
    @ do create aim constraint according to ui based axis and delete constraint,
    @ and freeze transform second selected joint.
    Args:
        aimValue (list): [1,0,0]
        objValue (list): [1,0,0]
        sel (list): two objects selection order is aimObject and then main object.
        freeze (bool): maintain offset set to on or off.

    Returns:
            bool.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if len(sel) != 2:
        ar_qui.ar_displayMessage('error', 'please select two objects...')
        return False
    cmds.select(cl=True)
    # create locator and snap on selection one.
    loc = cmds.spaceLocator(n='TempLocatorForObjectUpOrientation')
    cmds.delete(cmds.parentConstraint(sel[1], loc[0]))
    if objValue == [1, 0, 0]:
        cmds.move(3, 0, 0, loc[0], r=True, os=True, wd=True)
    if objValue == [0, 1, 0]:
        cmds.move(0, 3, 0, loc[0], r=True, os=True, wd=True)
    if objValue == [0, 0, 1]:
        cmds.move(0, 0, 3, loc[0], r=True, os=True, wd=True)
    cmds.delete(cmds.aimConstraint(sel[0], sel[1], o=[0, 0, 0], w=True, aim=aimValue, u=objValue,
                                   wut="object", wuo=loc[0]))
    if freeze:
        cmds.makeIdentity(sel[1], a=True, t=1, r=1, s=1, n=0, pn=1)
    # delete locator.
    cmds.delete(loc[0])
    cmds.select(sel[1])
    ar_qui.ar_displayMessage('success', 'constraint done')
    return True


def ar_multiPointConstraint(maintainOffset, sel=None):
    """
    @ point constraint all selected item with last selected object.
    Args:
        maintainOffset (bool): set maintain offset on or off.
        sel (list): objects has to be constraint.

    Returns:
            bool.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        ar_qui.ar_displayMessage('warning', 'no objects selected...')
        return False
    if maintainOffset:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.pointConstraint(parentObj, sel[i], mo=True)
    else:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.pointConstraint(parentObj, sel[i])
    ar_qui.ar_displayMessage('success', 'constraint done')
    return True


def ar_multiOrientConstraint(maintainOffset, sel=None):
    """
    @ orient constraint all selected item with last selected object.
    Args:
        maintainOffset (bool): set maintain offset on or off.
        sel (list): objects has to be constraint.

    Returns:
            bool.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        ar_qui.ar_displayMessage('warning', 'no objects selected...')
        return False
    if maintainOffset:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.orientConstraint(parentObj, sel[i], mo=True)
    else:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.orientConstraint(parentObj, sel[i])
    return True


def ar_multiParentConstraint(maintainOffset, sel=None):
    """
    @ parent constraint all selected item with last selected object.
    Args:
        maintainOffset (bool): set maintain offset on or off.
        sel (list): objects has to be constraint.

    Returns:
            bool.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        ar_qui.ar_displayMessage('warning', 'no objects selected...')
        return False
    if maintainOffset:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.parentConstraint(parentObj, sel[i], mo=True)
    else:
        for i in range(len(sel) - 1):
            parentObj = sel[len(sel) - 1]
            cmds.parentConstraint(parentObj, sel[i])
    return True

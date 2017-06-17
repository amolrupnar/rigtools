from maya import cmds as cmds
from pymel import core as pm

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_addFingerAttributes(drivers):
    """
    @ add finger extra attribute on Finger main controller.
    Args:
        drivers (list): driver controllers.

    Returns:
            bool.
    """
    attributes = ['_Scrunch', '_Twist', '_Lean', '_Scale']
    fingerBranch = ['Index', 'Middle', 'Ring', 'Pinky', 'Thumb']
    dispAttr = '_'
    for i in range(len(drivers)):
        for x in range(len(attributes)):
            cmds.addAttr(drivers[i], ln=dispAttr, at="enum", en=attributes[x][1:], k=True)
            cmds.setAttr(drivers[i] + '.' + dispAttr, l=True)
            for z in range(len(fingerBranch)):
                cmds.addAttr(drivers[i], ln=fingerBranch[z] + attributes[x], at="double", k=True)
            dispAttr += '_'
    return True


def ar_addScrunch(attribute, controllers, axis='ry'):
    """
    @ add scrunch connections on controllers upper group.
    Args:
        attribute (str): attribute with object name.
        controllers (list): list of one finger controllers in order of start to end.
        axis (str): sample of axis, 'rx' or 'ry' or 'rz'.

    Returns:
            bool.
    """
    for a in range(len(controllers)):
        controllers[a] = pm.PyNode(controllers[a])
        if a == 0:
            pma = pm.createNode('plusMinusAverage', ss=True, n='pma_' + controllers[a])
            pm.connectAttr(attribute, pma + '.input1D[0]', f=True)
            md = pm.createNode('multiplyDivide', ss=True, n='md_' + controllers[a])
            pm.connectAttr(pma + '.output1D', md + '.input1X', f=True)
            cmds.setAttr(md + '.input2X', -1)
            parentGrp = controllers[a].getParent()
            pm.connectAttr(md + '.outputX', parentGrp + '.' + axis, f=True)
        else:
            pma = pm.createNode('plusMinusAverage', ss=True, n='pma_' + controllers[a])
            pm.connectAttr(attribute, pma + '.input1D[0]', f=True)
            parentGrp = controllers[a].getParent()
            pm.connectAttr(pma + '.output1D', parentGrp + '.' + axis, f=True)
    ar_qui.ar_displayMessage('success', '---- "%s" ----    connections done.....' % attribute)
    return True


def ar_addFingerAttributeConnections(attribute, controllers, axis='rx'):
    """
    @ add twist connections on controllers upper group.
    Args:
        attribute (str): attribute with object name.
        controllers (list): list of one finger controllers in order of start to end.
        axis (str): sample of axis, 'rx' or 'ry' or 'rz'.

    Returns:
            bool.
    """
    for a in range(len(controllers)):
        controllers[a] = pm.PyNode(controllers[a])
        parentGrp = controllers[a].getParent()
        pm.connectAttr(attribute, parentGrp + "." + axis)
    ar_qui.ar_displayMessage('success', '---- "%s" ----    connections done.....' % attribute)
    return True

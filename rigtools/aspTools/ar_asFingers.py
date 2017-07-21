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
    attributes = ['Scrunch', 'Twist', 'Lean', 'Scale']
    fingerBranch = ['index', 'middle', 'ring', 'pinky', 'thumb']
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
        # if connection is in translate and translate is in minus then add multiply divide,
        # and reverse its connections.
        if axis.startswith('t'):
            offGroup = pm.PyNode('FKOffset' + controllers[a][2:])
            if offGroup.tx.get() < 0:
                mdnNode = pm.createNode('multiplyDivide', ss=True, n='mdn_' + controllers[a] + '_Reverse')
                pm.connectAttr(attribute, mdnNode + '.input1X')
                pm.connectAttr(mdnNode + '.outputX', parentGrp + "." + axis)
                mdnNode.input2X.set(-1)
        else:
            pm.connectAttr(attribute, parentGrp + "." + axis)
    ar_qui.ar_displayMessage('success', '---- "%s" ----    connections done.....' % attribute)
    return True


def ar_addAllAttrsInFingerDriverController():
    """
    @ add all attributes in basic main finger controllers.
    Returns:
            bool.
    """
    fingerCtlsL = {
        'index': ['FKIndexFinger1_L', 'FKIndexFinger2_L', 'FKIndexFinger3_L'],
        'middle': ['FKMiddleFinger1_L', 'FKMiddleFinger2_L', 'FKMiddleFinger3_L'],
        'ring': ['FKRingFinger1_L', 'FKRingFinger2_L', 'FKRingFinger3_L'],
        'pinky': ['FKPinkyFinger1_L', 'FKPinkyFinger2_L', 'FKPinkyFinger3_L'],
        'thumb': ['FKThumbFinger1_L', 'FKThumbFinger2_L', 'FKThumbFinger3_L']
    }
    fingerCtlsR = {
        'index': ['FKIndexFinger1_R', 'FKIndexFinger2_R', 'FKIndexFinger3_R'],
        'middle': ['FKMiddleFinger1_R', 'FKMiddleFinger2_R', 'FKMiddleFinger3_R'],
        'ring': ['FKRingFinger1_R', 'FKRingFinger2_R', 'FKRingFinger3_R'],
        'pinky': ['FKPinkyFinger1_R', 'FKPinkyFinger2_R', 'FKPinkyFinger3_R'],
        'thumb': ['FKThumbFinger1_R', 'FKThumbFinger2_R', 'FKThumbFinger3_R']
    }
    # make a new dictionary with main finger controllers.
    mainCtls = {'Fingers_L': fingerCtlsL, 'Fingers_R': fingerCtlsR}
    for w in mainCtls.keys():
        pm.addAttr(w, ln='pose', at="enum", en='pose', k=True)
        pm.setAttr(w + '.pose', l=True)
        pm.addAttr(w, ln='fist', at='double', min=0, max=10, dv=0, k=True)
        pm.addAttr(w, ln='relax', at='double', min=-10, max=10, dv=0, k=True)
        ar_addFingerAttributes([w])
        for x in mainCtls[w].keys():
            ar_addScrunch(w + '.' + x + 'Scrunch', mainCtls[w][x])
            ar_addFingerAttributeConnections(w + '.' + x + 'Lean', mainCtls[w][x], axis='rz')
            ar_addFingerAttributeConnections(w + '.' + x + 'Twist', mainCtls[w][x])
            ar_addFingerAttributeConnections(w + '.' + x + 'Scale', mainCtls[w][x], axis='tx')
    return True

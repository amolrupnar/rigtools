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
        pm.connectAttr(attribute, parentGrp + "." + axis)
    ar_qui.ar_displayMessage('success', '---- "%s" ----    connections done.....' % attribute)
    return True


def ar_addAllAttrsInFingerDriverController():
    """
    @ add all attributes in basic main finger controllers.
    Returns:
            bool.
    """
    # add pose attributes.
    pm.addAttr('Fingers_L', ln='pose', at="enum", en='pose', k=True)
    pm.setAttr('Fingers_L.pose', l=True)
    pm.addAttr('Fingers_L', ln='fist', at='double', min=0, max=10, dv=0, k=True)
    pm.addAttr('Fingers_L', ln='relax', at='double', min=-10, max=10, dv=0, k=True)

    pm.addAttr('Fingers_R', ln='pose', at="enum", en='pose', k=True)
    pm.setAttr('Fingers_R.pose', l=True)
    pm.addAttr('Fingers_R', ln='fist', at='double', min=0, max=10, dv=0, k=True)
    pm.addAttr('Fingers_R', ln='relax', at='double', min=-10, max=10, dv=0, k=True)
    # add individual finger attributes.
    ar_addFingerAttributes(['Fingers_L', 'Fingers_R'])

    # left index attributes.
    indexCtlList = ['FKIndexFinger1_L', 'FKIndexFinger2_L', 'FKIndexFinger3_L']
    ar_addScrunch('Fingers_L.indexScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.indexTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.indexLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_L.indexScale', indexCtlList, axis='tx')

    # left middle attributes.
    indexCtlList = ['FKMiddleFinger1_L', 'FKMiddleFinger2_L', 'FKMiddleFinger3_L']
    ar_addScrunch('Fingers_L.middleScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.middleTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.middleLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_L.middleScale', indexCtlList, axis='tx')

    # left ring attributes.
    indexCtlList = ['FKRingFinger1_L', 'FKRingFinger2_L', 'FKRingFinger3_L']
    ar_addScrunch('Fingers_L.ringScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.ringTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.ringLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_L.ringScale', indexCtlList, axis='tx')

    # left pinky attributes.
    indexCtlList = ['FKPinkyFinger1_L', 'FKPinkyFinger2_L', 'FKPinkyFinger3_L']
    ar_addScrunch('Fingers_L.pinkyScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.pinkyTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.pinkyLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_L.pinkyScale', indexCtlList, axis='tx')

    # left thumb attributes.
    indexCtlList = ['FKThumbFinger1_L', 'FKThumbFinger2_L', 'FKThumbFinger3_L']
    ar_addScrunch('Fingers_L.thumbScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.thumbTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_L.thumbLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_L.thumbScale', indexCtlList, axis='tx')
    # ----------------------------------------------------------------------------------
    # right hand
    # ----------------------------------------------------------------------------------
    # right index attributes.
    indexCtlList = ['FKIndexFinger1_R', 'FKIndexFinger2_R', 'FKIndexFinger3_R']
    ar_addScrunch('Fingers_R.indexScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.indexTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.indexLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_R.indexScale', indexCtlList, axis='tx')

    # right middle attributes.
    indexCtlList = ['FKMiddleFinger1_R', 'FKMiddleFinger2_R', 'FKMiddleFinger3_R']
    ar_addScrunch('Fingers_R.middleScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.middleTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.middleLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_R.middleScale', indexCtlList, axis='tx')

    # right ring attributes.
    indexCtlList = ['FKRingFinger1_R', 'FKRingFinger2_R', 'FKRingFinger3_R']
    ar_addScrunch('Fingers_R.ringScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.ringTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.ringLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_R.ringScale', indexCtlList, axis='tx')

    # right pinky attributes.
    indexCtlList = ['FKPinkyFinger1_R', 'FKPinkyFinger2_R', 'FKPinkyFinger3_R']
    ar_addScrunch('Fingers_R.pinkyScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.pinkyTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.pinkyLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_R.pinkyScale', indexCtlList, axis='tx')

    # right thumb attributes.
    indexCtlList = ['FKThumbFinger1_R', 'FKThumbFinger2_R', 'FKThumbFinger3_R']
    ar_addScrunch('Fingers_R.thumbScrunch', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.thumbTwist', indexCtlList)
    ar_addFingerAttributeConnections('Fingers_R.thumbLean', indexCtlList, axis='rz')
    ar_addFingerAttributeConnections('Fingers_R.thumbScale', indexCtlList, axis='tx')

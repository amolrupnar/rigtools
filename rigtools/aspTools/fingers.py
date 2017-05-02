from maya import cmds as cmds
from pymel import core as pm


def rt_addFingerAttributes(drivers):
    """
    add finger extra attribute on Finger main controller.
    :param drivers: list
    :return: fingers connnections
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


def rt_addScrunch(attribute, controllers, axis='ry'):
    """
    add scrunch connections on controllers upper group.
    :param attribute: string
    :param controllers: list
    :param axis: string ('rx' or 'ry' or 'rz')
    :return: connections.
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
    print ('---- "%s" ----    connections done.....' % attribute),


def rt_addFingerAttributeConnections(attribute, controllers, axis='rx'):
    """
    add twist connections on controllers upper group.
    :param attribute: string
    :param controllers: list
    :param axis: string ('rx' or 'ry' or 'rz' or 'tx' or 'ty' or 'tz')
    :return: connections.
    """
    for a in range(len(controllers)):
        controllers[a] = pm.PyNode(controllers[a])
        parentGrp = controllers[a].getParent()
        pm.connectAttr(attribute, parentGrp + "." + axis)
    print ('---- "%s" ----    connections done.....' % attribute),

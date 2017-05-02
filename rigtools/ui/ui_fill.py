import pymel.core as pm
import maya.cmds as cmds


def fillLineEdit(lineEdit, sel=None):
    """
    add selection in window line edit.
    :param lineEdit: string
    :param sel: list
    :return: line edit fill
    """
    if not sel:
        sel = pm.ls(sl=True)
    if not sel:
        raise RuntimeError('Please select only one object')
    elif len(sel) > 1:
        raise RuntimeError('more than one objects selected.')
    lineEdit.setText(str(sel[0]))


def fillListInLineEdit(lineEdit, sel=None):
    """
    add selection list in line edit.
    :param lineEdit: string
    :param sel: list
    :return: line edit fill
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        raise RuntimeError('Please select only one object')
    lineText = ",".join(sel)
    lineEdit.setText(lineText)


def extractLineEditList(lineEdit):
    """
    convert string to list.
    :param lineEdit: string
    :return: objList
    """
    strObj = lineEdit.text()
    objList = strObj.split(',')
    return objList

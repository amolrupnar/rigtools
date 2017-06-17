import pymel.core as pm
import maya.cmds as cmds

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_fillLineEdit(lineEdit, sel=None):
    """
    @ add selection in window line edit.
    Args:
        lineEdit (str): line edit name.
        sel (list): object has to be add in line edit.

    Returns:
            bool.
    """
    if not sel:
        sel = pm.ls(sl=True)
    if not sel:
        ar_qui.ar_displayMessage('error', 'Please select only one object')
        return False
    elif len(sel) > 1:
        ar_qui.ar_displayMessage('error', 'more than one objects selected.')
        return False
    lineEdit.setText(str(sel[0]))
    return True


def ar_fillListInLineEdit(lineEdit, sel=None):
    """
    @ add selection list in line edit.
    Args:
        lineEdit (str): line edit name.
        sel (list): object has to be add in line edit.

    Returns:
            bool.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        ar_qui.ar_displayMessage('error', 'Please select only one object')
        return False
    lineText = ",".join(sel)
    lineEdit.setText(lineText)
    return True


def ar_extractLineEditList(lineEdit):
    """
    @ extract multiple objects from line edit and return it to list.
    Args:
        lineEdit (str): line edit name.

    Returns:
            objList.
    """
    strObj = lineEdit.text()
    objList = strObj.split(',')
    return objList

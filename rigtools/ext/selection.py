import pymel.core as pm
import maya.cmds as cmds


def getSelection(sel=None):
    """
    get selection from maya
    :param sel: list (get selection)
    :return: selection
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning('Selection is empty please select something...')
        return False
    return sel


def getHighlightedAttribute(sel=None):
    """
    get channel box highlighted attribute
    :param sel: list (selection)
    :return: channel attribute
    """
    if not sel:
        sel = pm.ls(sl=True)
    if len(sel) != 1:
        pm.warning('Please select only one object')
        return False
    # get highlighted attribute from channel box.
    channel = pm.windows.channelBox('mainChannelBox', q=True, sma=True)
    if not channel or len(channel) != 1:
        pm.warning('Please select one attribute to load...')
        return False
    return channel[0]


def selectAll():
    """
    select hierarchy of all selected objects.
    :return: hierarchy
    """
    cmds.select(hi=True)

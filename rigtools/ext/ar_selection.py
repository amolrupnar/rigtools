import pymel.core as pm
import maya.cmds as cmds

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_getSelection(sel=None):
    """
    @ get selection from maya.
    Args:
        sel (list): selection list from maya.

    Returns:
            sel.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        ar_qui.ar_displayMessage('warning', 'Selection is empty please select something...')
        return False
    return sel


def ar_getHighlightedAttribute(sel=None):
    """
    @ get channel box highlighted attribute.
    Args:
        sel (list): attribute selection.

    Returns:
            selected channel.
    """
    if not sel:
        sel = pm.ls(sl=True)
    if len(sel) != 1:
        ar_qui.ar_displayMessage('warning', 'Please select only one object')
        return False
    # get highlighted attribute from channel box.
    channel = pm.windows.channelBox('mainChannelBox', q=True, sma=True)
    if not channel or len(channel) != 1:
        ar_qui.ar_displayMessage('warning', 'Please select one attribute to load...')
        return False
    return channel[0]


def ar_selectAll():
    """
    @ select hierarchy of all selected objects.
    Returns:
            selection.
    """
    return cmds.select(hi=True)

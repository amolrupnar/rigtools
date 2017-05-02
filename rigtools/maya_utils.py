from PySide import QtGui
from maya import OpenMayaUI as omui
from pymel import core as pm
from shiboken import wrapInstance


class UndoChunkOpen(object):
    def __init__(self, chunkName=''):
        self._name = chunkName

    def __enter__(self):
        pm.undoInfo(chunkName=self._name, openChunk=True)

    def __exit__(self, *_):
        pm.undoInfo(chunkName=self._name, closeChunk=True)


def maya_main_window():
    """
    This is to get the maya window QT pointer.
    :return:
    :rtype:
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)

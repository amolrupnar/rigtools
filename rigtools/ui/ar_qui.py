import pymel.core as pm
import maya.OpenMayaUI as omui
from PySide import QtGui
from shiboken import wrapInstance


class ar_undoChunkOpen(object):
    def __init__(self, chunkName=''):
        self._name = chunkName

    def __enter__(self):
        pm.undoInfo(chunkName=self._name, openChunk=True)

    def __exit__(self, *_):
        pm.undoInfo(chunkName=self._name, closeChunk=True)


def ar_mayaMainWindow():
    """
    This is to get the maya window QT pointer.
    :return:
    :rtype:
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)


def ar_displayMessage(status, message):
    """
    display message with different color in maya according to status.
    :param status: string
    :param message: string
    :return: message
    """
    # exit if this function run in batch mode.
    if pm.about(batch=True):
        return False
    # Base color    Text Color.
    statusColors = {
        'error': ((255, 40, 20), (0, 0, 0)),
        'warning': ((255, 177, 86), (0, 0, 0)),
        'success': ((140, 230, 140), (0, 0, 0))}
    # commandLine1 will be unique in maya in all cases.
    commandLinePtr = omui.MQtUtil.findControl('commandLine1')
    commandLine = wrapInstance(long(commandLinePtr), QtGui.QWidget)
    # get result Line.
    resultLine = commandLine.findChildren(QtGui.QLineEdit)[0]
    palette = resultLine.palette()
    palette.setBrush(QtGui.QPalette.Base, QtGui.QColor(*statusColors[status][0]))
    palette.setColor(QtGui.QPalette.Text, QtGui.QColor(*statusColors[status][1]))
    resultLine.setPalette(palette)
    resultLine.setText('[ ' + status + ' ] ' + message)
    pm.refresh()


def ar_displayDialogue(status, message, detailMessage=None):
    """
    create qt QMessageBox according to status.
    :param status: string
    :param message: string
    :param detailMessage: string
    :return: None
    """
    # exit if this function run in batch mode.
    if pm.about(batch=True):
        return False
    # set icon according to status mode.
    if status == 'warning':
        statusIcon = QtGui.QMessageBox.Warning
    elif status == 'error':
        statusIcon = QtGui.QMessageBox.Critical
    else:
        statusIcon = QtGui.QMessageBox.NoIcon
    # create QMessageBox.
    msgBox = QtGui.QMessageBox(ar_mayaMainWindow())
    msgBox.setIcon(statusIcon)
    msgBox.setText(status)
    msgBox.setInformativeText(message)
    msgBox.setWindowTitle(status)
    # set additional text.
    if detailMessage:
        msgBox.setDetailedText("The details are as follows:\n" + detailMessage)
    else:
        msgBox.setDetailedText("The details are as follows:")
    msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
    msgBox.exec_()

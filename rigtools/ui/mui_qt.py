import pymel.core as pm
import maya.OpenMayaUI as omui
from PySide import QtGui, QtCore
from shiboken import wrapInstance


def displayMsg(status, message):
    """
    display message with different color in maya according to status.
    :param status: string
    :param message: string
    :return: message
    """
    #              Base color    Text Color.
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
    resultLine.setText('[ '+status+' ] '+message)
    pm.refresh()

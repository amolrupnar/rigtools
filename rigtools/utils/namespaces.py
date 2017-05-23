import pymel.core as pm


def removeNamespace(namespaceName):
    """
    remove namespace.
    :param namespaceName: string (namespace like 'XYZ')
    :return: none
    """
    allNameSpaces = pm.listNamespaces()
    for each in allNameSpaces:
        if each == ':' + namespaceName:
            pm.namespace(rm=each[1:], mnr=True)

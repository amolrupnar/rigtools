import pymel.core as pm

from rigtools.ui import ar_qui

reload(ar_qui)


def ar_removeNamespace(namespaceName):
    """
    @ remove namespace of passed argument.
    Args:
        namespaceName (str): namespace without colon ex (MSH).

    Returns:
            bool.
    """
    allNameSpaces = pm.listNamespaces()
    for each in allNameSpaces:
        if each == ':' + namespaceName:
            pm.namespace(rm=each[1:], mnr=True)
    ar_qui.ar_displayMessage('success', 'namespace successfully removed.')
    return True

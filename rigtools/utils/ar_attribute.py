import pymel.core as pm


def ar_addFloatAttributes(mainObj, attributeNames):
    """
    @ add attributes (float type and min=0, max=1), on the objects and set it to f
    Args:
        mainObj (str): object name where attributes will be add.
        attributeNames (list): list of attribute names.

    Returns:
            attributes  (list).
    """
    mainObj = pm.PyNode(mainObj)
    addedAttributes = list()
    for each in attributeNames:
        mainObj.addAttr(each, at='double', min=0, max=1, dv=0, k=True)
        addedAttributes.append(mainObj.name() + '.' + each)
    return addedAttributes

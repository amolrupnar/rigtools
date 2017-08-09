import pymel.core as pm


def ar_connectSameAttributes(srcAttrList, destAttrList):
    """
    @ connect attribute list 1 to attribute list 2,
    same attribute matching with attrList2.
    Args:
        srcAttrList (list): source attribute list.
        destAttrList (list): destination attribute list.

    Returns:
            connections (dict).
    """
    filtSrcAttr = list()
    filtDestAttr = list()
    for x in srcAttrList:
        filtSrcAttr.append(x.split('.')[-1])
    for x in destAttrList:
        filtDestAttr.append(x.split('.')[-1])
    # if attribute match connect it.
    matchedObjects = list(set(filtSrcAttr) & set(filtDestAttr))
    for each in matchedObjects:
        # pm.connectAttr(each.split('.')[0]+each,)
        print 11111111111111
        # TODO: pending after that.
    print matchedObjects
    return filtSrcAttr, filtDestAttr

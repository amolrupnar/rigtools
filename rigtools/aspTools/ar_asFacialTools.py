import pymel.core as pm
import maya.mel as mel
import os
import tempfile

from rigtools.utils import ar_blendshape
from rigtools.utils import ar_namespaces
from rigtools.utils import ar_rivet
from rigtools.ui import ar_qui

reload(ar_blendshape)
reload(ar_namespaces)
reload(ar_rivet)
reload(ar_qui)


def _hierarchyChecker(namespaceName):
    """
    @ check the hierarchy for ar_facialTools.
    Args:
        namespaceName (str): add namespace with colon. 

    Returns:
            bool.
    """
    groups = ['FaceGroup', 'FaceMotionSystem', 'FaceDeformationSystem', 'FaceMotionFollowHead', 'ControlsSetup',
              'RegionDeformations']
    existed = []
    notExisted = []
    for each in groups:
        if pm.objExists(each):
            existed.append(each)
        else:
            notExisted.append(each)

    if not notExisted:
        if len(existed) == len(groups):
            # parent all objects in groups.
            pm.parent(namespaceName + 'FKOffsetLips_M', 'FaceMotionFollowHead')
            pm.parent(namespaceName + 'Brs', namespaceName + 'Lip_Controllers', 'ControlsSetup')
            pm.parent(namespaceName + 'ClusterSetup', namespaceName + 'LipSetup', 'FaceMotionSystem')
            pm.parent(namespaceName + 'LipRegion', namespaceName + 'LipsRegion', 'RegionDeformations')
            pm.parent(namespaceName + 'faceHeadJoint', 'FaceDeformationSystem')
            pm.delete(namespaceName + 'FaceGroup')
            ar_namespaces.ar_removeNamespace(namespaceName)
            pm.orientConstraint('Head_M', 'Brs', mo=True)
            ret = True
        else:
            ar_qui.ar_displayMessage('warning',
                                     'default hierarchy is exist but not proper, please undo step and match hierarchy.')
            ret = False
    else:
        if len(notExisted) == len(groups):
            pm.parent(namespaceName + 'FaceGroup', 'Rig')
            ar_namespaces.ar_removeNamespace(namespaceName)
            pm.orientConstraint('Head_M', 'Brs', mo=True)
            pm.orientConstraint('Head_M', 'FaceMotionFollowHead', mo=True)
            ret = True
        else:
            ar_qui.ar_displayMessage('warning',
                                     'default hierarchy is exist but not proper, please undo step and match hierarchy.')
            ret = False
    if ret:
        if pm.objExists('Main'):
            pm.connectAttr('Main.s', 'Brs.s', f=True)
        else:
            pm.connectAttr('Main_CTRL.s', 'Brs.s', f=True)
        pm.setAttr('FaceDeformationSystem.v', 0)
        pm.setAttr('FaceDeformationSystem.v', l=True)
        return True
    else:
        return False


class Ar_LipSetup(object):
    def __init__(self, face_geo=None, face_geo_top_node=None, namespaceName='XXX:', exportFile=False, path=None):
        """
        @ export and import only Lip rig part from asp face rig.
        Args:
            face_geo (str): face geometry.
            face_geo_top_node (str): top group of face geometry.
            namespaceName (str): namespace with colon.
            exportFile (bool): want to export file or not.
            path (str): path for the export or import file.
        """
        if not face_geo:
            self.face_geo = None
        else:
            self.face_geo = pm.PyNode(face_geo)
        if not face_geo_top_node:
            self.face_geo_top_node = None
        else:
            self.face_geo_top_node = face_geo_top_node
        self.namespaceName = namespaceName
        self.lipCtrlGrps = ['upperLip3Attach_L', 'upperLip3Attach_R', 'lowerLip3Attach_L', 'lowerLip3Attach_R',
                            'upperLip5Attach_R', 'lowerLip5Attach_R', 'upperLip5Attach_L', 'lowerLip5Attach_L',
                            'Lip6Attach_L', 'Lip6Attach_R', 'lowerLip0Attach_M', 'upperLip0Attach_M']
        self.deleteObjArray = ['FaceGroup', 'Head_M', 'Main', 'faceLid', 'Jaw_M', 'FaceUpperRegion_M',
                               'FaceLowerRegion_M']
        self.lip_geos = ['LipRegion', 'LipsRegion']
        self.exportFile = exportFile
        if not path:
            tempDir = tempfile.gettempdir()
            self.path = tempDir + '\\TempLipSetup.ma'
        else:
            if not os.path.isdir(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            self.path = path

    def exportLipSetup(self):
        # create groups.
        lipControllersGrp = pm.createNode('transform', n='Lip_Controllers')
        clusterSetup = pm.createNode('transform', n='NewClusterSetup')
        pm.parent('LipRegion', 'LipsRegion', 'FKOffsetLips_M', 'LipSetup', 'Brs', 'faceHeadJoint', self.lipCtrlGrps,
                  w=True)
        pm.parent(self.lipCtrlGrps, lipControllersGrp)
        # get all rivets and connect with "lipRegion" geometry.
        # all connected with "curveFromMeshEdge" node type.
        for each in self.lipCtrlGrps:
            allHist = pm.listHistory(each, pdo=True)
            for hist in allHist:
                if hist.nodeType() == 'pointOnCurveInfo':
                    clusterCurve = hist.inputCurve.connections()[0]
                    pm.parent(clusterCurve, clusterSetup)
                    crvFrmMshEdg = hist.inputCurve.connections()[0].create.connections()[0]
                    lipRegionShape = pm.listRelatives('LipRegion', s=True, ni=True)[0]
                    lipRegionShape.worldMesh[0].connect(crvFrmMshEdg.inputMesh, f=True)

        # create dummy head and main.
        pm.delete('Brs_orientConstraint1', 'FaceAllSet', 'FaceControlSet', 'MainAndHeadScaleMultiplyDivide',
                  self.deleteObjArray, self.face_geo_top_node)
        # Brs scale set to 1.
        pm.setAttr('Brs.sx', 1)
        pm.setAttr('Brs.sy', 1)
        pm.setAttr('Brs.sz', 1)
        # create Hierarchy.
        faceGroup = pm.createNode('transform', n='FaceGroup')
        faceMotionSystem = pm.createNode('transform', n='FaceMotionSystem')
        faceMotionFollowHead = pm.createNode('transform', n='FaceMotionFollowHead')
        controlsSetup = pm.createNode('transform', n='ControlsSetup')
        faceDeformationSystem = pm.createNode('transform', n='FaceDeformationSystem')
        regionDeformation = pm.createNode('transform', n='RegionDeformations')
        pm.parent(faceMotionSystem, faceDeformationSystem, faceGroup)
        pm.parent(faceMotionFollowHead, controlsSetup, clusterSetup, 'LipSetup', faceMotionSystem)
        pm.parent(regionDeformation, 'faceHeadJoint', faceDeformationSystem)
        pm.parent('Brs', lipControllersGrp, controlsSetup)
        pm.parent('FKOffsetLips_M', faceMotionFollowHead)
        pm.parent('LipRegion', 'LipsRegion', regionDeformation)
        clusterSetup.rename('ClusterSetup')
        mel.eval("MLdeleteUnused")
        if self.exportFile:
            pm.system.exportAll(self.path, force=True, type="mayaAscii", pr=True)
        ar_qui.ar_displayMessage('success', 'export lip setup')

    def connectLipSetup(self):
        if not _hierarchyChecker(self.namespaceName):
            pm.windows.confirmDialog(title='Hierarchy Error',
                                     message='Hierarchy has some error please\nplease opens script editor for details.',
                                     button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            ar_qui.ar_displayDialogue('error', 'Hierarchy is not proper.')
            ar_qui.ar_displayMessage('error', 'Hierarchy is not proper.')
            return False
        # connect all rivet to "self.face_geo" geometry.
        for each in self.lipCtrlGrps:
            allHist = pm.listHistory(each, pdo=True)
            for hist in allHist:
                if hist.nodeType() == 'pointOnCurveInfo':
                    crvFrmMshEdg = hist.inputCurve.connections()[0].create.connections()[0]
                    self.face_geo.worldMesh[0].connect(crvFrmMshEdg.inputMesh, f=True)
        # add blendshape.
        for each in self.lip_geos:
            ar_blendshape.ar_addBlendShape(each, self.face_geo)


def ar_browExport(face_geo, exportFile=False, path=None):
    """
    @ export brow rig from asp face rig.
    Args:
        face_geo (str): face geometry.
        exportFile (bool): want to export the file or not.
        path (str): path for export file.

    Returns:
            bool.
    """
    # path queries.
    if not path:
        tempDir = tempfile.gettempdir()
        path = tempDir + '/tempLipSetup.ma'
    else:
        if not os.path.isdir(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
    # convert into pyobject.
    face_geo = pm.PyNode(face_geo)
    # arrays
    ctlOffsetGroups = ['browInnerAttach_R', 'browOuterAttach_R', 'browInnerAttach_L', 'browOuterAttach_L',
                       'browHalfAttach_R', 'browHalfAttach_L']
    browCurves = ['browInnerCurve_R', 'browHalfCurve_R', 'browOuterCurve_R', 'browInnerCurve_L',
                  'browHalfCurve_L', 'browOuterCurve_L']
    deleteArray = ['FaceGroup', 'FaceUpper_M', 'FaceLower_M', 'FaceAllSet', 'FaceControlSet']
    # check parenting.
    parent = face_geo.getParent()
    if not parent:
        ar_qui.ar_displayDialogue('error', (str(face_geo), 'Has no top group.'))
        ar_qui.ar_displayMessage('error', (str(face_geo), 'Has no top group.'))
        return False
    # delete blendshape node.
    blendshapeNode = []
    hist = face_geo.listHistory()
    for each in hist:
        if type(each) == pm.nodetypes.BlendShape:
            blendshapeNode.append(each)
    if len(blendshapeNode) != 1:
        ar_qui.ar_displayDialogue('error', 'blendshape node is more than one or not exist.')
        ar_qui.ar_displayMessage('error', 'blendshape node is more than one or not exist.')
        return False
    else:
        pm.delete(blendshapeNode[0])

    # unparent offset groups
    pm.parent(ctlOffsetGroups, w=True)
    brow_Controllers = pm.createNode('transform', n='Brow_Controllers')
    ctlCurveMainGroup = pm.createNode('transform', n='ctlCurveMainGroup')
    pm.parent(ctlOffsetGroups, brow_Controllers)
    pm.parent(browCurves, ctlCurveMainGroup)
    pm.parent('Brs', 'FaceDeformationFollowHead', w=True)
    # delete extra nodes.
    pm.delete(deleteArray)
    # export setup.
    if exportFile:
        pm.system.exportAll(path, force=True, type="mayaAscii", pr=True)
    ar_qui.ar_displayMessage('success', 'brow export done.')
    return True


def ar_browConnect(face_geo, face_geo_top_node, face_geo_main, namespacesName='XXX:'):
    """
    @ import brow rig and attach with rig.
    Args:
        face_geo (str): geometry from imported file.
        face_geo_top_node (str): upper group of face geometry.
        face_geo_main (str): face geometry of main rig.
        namespacesName (str): namespace with colon.

    Returns:
            bool.
    """
    face_geo = pm.PyNode(namespacesName + face_geo)
    face_geo_top_node = pm.PyNode(namespacesName + face_geo_top_node)
    face_geo_main = pm.PyNode(face_geo_main)
    # import eyebrow setup.
    ctlOffsetGroups = ['browInnerAttach_R', 'browOuterAttach_R', 'browInnerAttach_L', 'browOuterAttach_L',
                       'browHalfAttach_R', 'browHalfAttach_L']
    # for import
    pm.parent(namespacesName + 'Brow_Controllers', 'ControlsSetup')
    # parent Rivet Curves.
    crvs = pm.listRelatives(namespacesName + 'ctlCurveMainGroup', c=True)
    pm.parent(crvs, 'ClusterSetup')
    # connection with old Brs.
    for each in ctlOffsetGroups:
        pm.connectAttr('Brs.r', namespacesName + each + '.r', f=True)
        pm.connectAttr('Brs.s', namespacesName + each + '.s', f=True)
    # parent face motion follow head.
    childs = pm.listRelatives(namespacesName + 'FaceDeformationFollowHead', c=True)
    filtChilds = []
    for each in childs:
        if type(each) == pm.nodetypes.PointConstraint:
            pass
        elif type(each) == pm.nodetypes.OrientConstraint:
            pass
        else:
            filtChilds.append(each)
    pm.parent(filtChilds, 'FaceDeformationFollowHead')
    # delete unwanted.
    deleteArray = ['Main', 'ctlCurveMainGroup', 'Brs', 'FaceDeformationFollowHead']
    for each in deleteArray:
        pm.delete(namespacesName + each)
    # make hierarchy.
    eyeBrowExtraSystem = pm.createNode('transform', n='EyeBrowExtraSystem')
    pm.parent(face_geo, namespacesName + 'Head_M', eyeBrowExtraSystem)
    pm.delete(face_geo_top_node)
    face_geo.rename('BrowRigBlendshape_geo')
    ar_blendshape.ar_addBlendShape(face_geo, face_geo_main)
    # transfer rivet.
    shapes = face_geo.listRelatives(s=True)
    for each in shapes:
        if not each.isIntermediate():
            ar_rivet.ar_transferRivet(each, face_geo_main)
    ar_namespaces.ar_removeNamespace(namespacesName[:-1])
    # lock and parent eyeBrowExtraSystem.
    eyeBrowExtraSystem.v.set(0)
    eyeBrowExtraSystem.v.lock()
    if not pm.objExists('ExtraSystem'):
        pm.createNode('transform', n='ExtraSystem')
    pm.parent(eyeBrowExtraSystem, 'ExtraSystem')
    ar_qui.ar_displayMessage('success', 'brow connection is done....')
    return True

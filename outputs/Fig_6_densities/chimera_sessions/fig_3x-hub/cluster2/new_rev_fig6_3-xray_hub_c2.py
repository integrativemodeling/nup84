import cPickle, base64
try:
	from SimpleSession.versions.v62 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 9, 39760])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v62 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwBOfYdVCWJhbGxTY2FsZXEDSwBOfYdVCXBvaW50U2l6ZXEESwBOfYdVBWNvbG9ycQVLAE59h1UKcmliYm9uVHlwZXEGSwBOfYdVCnN0aWNrU2NhbGVxB0sATn2HVQxhcm9tYXRpY01vZGVxCEsATn2HVQp2ZHdEZW5zaXR5cQlLAE59h1UGaGlkZGVucQpLAE59h1UNYXJvbWF0aWNDb2xvcnELSwBOfYdVD3JpYmJvblNtb290aGluZ3EMSwBOfYdVCWF1dG9jaGFpbnENSwBOfYdVCG9wdGlvbmFscQ59VQ9sb3dlckNhc2VDaGFpbnNxD0sATn2HVQlsaW5lV2lkdGhxEEsATn2HVQ9yZXNpZHVlTGFiZWxQb3NxEUsATn2HVQRuYW1lcRJLAE59h1UPYXJvbWF0aWNEaXNwbGF5cRNLAE59h1UPcmliYm9uU3RpZmZuZXNzcRRLAE59h1UKcGRiSGVhZGVyc3EVXVUDaWRzcRZLAE59h1UOc3VyZmFjZU9wYWNpdHlxF0sATn2HVRBhcm9tYXRpY0xpbmVUeXBlcRhLAE59h1UUcmliYm9uSGlkZXNNYWluY2hhaW5xGUsATn2HVQdkaXNwbGF5cRpLAE59h3Uu'))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksATn2HVQtmaWxsRGlzcGxheXEDSwBOfYdVBG5hbWVxBEsATn2HVQVjaGFpbnEFSwBOfYdVDnJpYmJvbkRyYXdNb2RlcQZLAE59h1UCc3NxB0sATn2HVQhtb2xlY3VsZXEISwBOfYdVC3JpYmJvbkNvbG9ycQlLAE59h1UFbGFiZWxxCksATn2HVQpsYWJlbENvbG9ycQtLAE59h1UIZmlsbE1vZGVxDEsATn2HVQVpc0hldHENSwBOfYdVC2xhYmVsT2Zmc2V0cQ5LAE59h1UIcG9zaXRpb25xD11VDXJpYmJvbkRpc3BsYXlxEEsATn2HVQhvcHRpb25hbHERfVUEc3NJZHESSwBOfYd1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQdyZXNpZHVlcQJLAE59h1UIdmR3Q29sb3JxA0sATn2HVQRuYW1lcQRLAE59h1UDdmR3cQVLAE59h1UOc3VyZmFjZURpc3BsYXlxBksATn2HVQVjb2xvcnEHSwBOfYdVCWlkYXRtVHlwZXEISwBOfYdVBmFsdExvY3EJSwBOfYdVBWxhYmVscQpLAE59h1UOc3VyZmFjZU9wYWNpdHlxC0sATn2HVQdlbGVtZW50cQxLAE59h1UKbGFiZWxDb2xvcnENSwBOfYdVDHN1cmZhY2VDb2xvcnEOSwBOfYdVD3N1cmZhY2VDYXRlZ29yeXEPSwBOfYdVBnJhZGl1c3EQSwBOfYdVCmNvb3JkSW5kZXhxEV1VC2xhYmVsT2Zmc2V0cRJLAE59h1USbWluaW11bUxhYmVsUmFkaXVzcRNLAE59h1UIZHJhd01vZGVxFEsATn2HVQhvcHRpb25hbHEVfXEWVQxzZXJpYWxOdW1iZXJxF4iIXYdzVQdkaXNwbGF5cRhLAE59h3Uu'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECSwBOfYdVBWF0b21zcQNdVQVsYWJlbHEESwBOfYdVCGhhbGZib25kcQVLAE59h1UGcmFkaXVzcQZLAE59h1ULbGFiZWxPZmZzZXRxB0sATn2HVQhkcmF3TW9kZXEISwBOfYdVCG9wdGlvbmFscQl9VQdkaXNwbGF5cQpLAE59h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('gAJ9cQEu'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), 'gold': ((1, 0.843137, 0), 1, u'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), 'Rf': ((0.8, 0, 0.34902), 1, u'default'), 'Ra': ((0, 0.490196, 0), 1, u'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), 'Be': ((0.760784, 1, 0), 1, u'default'), 'Ba': ((0, 0.788235, 0), 1, u'default'), 'Bh': ((0.878431, 0, 0.219608), 1, u'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), 'brown': ((0.647059, 0.164706, 0.164706), 1, u'default'), 'H': ((1, 1, 1), 1, u'default'), 'P': ((1, 0.501961, 0), 1, u'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), 'Gd': ((0.270588, 1, 0.780392), 1, u'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), 'Pr': ((0.85098, 1, 0.780392), 1, u'default'),
'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), 'Pu': ((0, 0.419608, 1), 1, u'default'), 'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), 'Pa': ((0, 0.631373, 1), 1, u'default'), 'Pd': ((0, 0.411765, 0.521569), 1, u'default'), 'Cd': ((1, 0.85098, 0.560784), 1, u'default'), 'Po': ((0.670588, 0.360784, 0), 1, u'default'), 'Pm': ((0.639216, 1, 0.780392), 1, u'default'), 'Hs': ((0.901961, 0, 0.180392), 1, u'default'), 'Ho': ((0, 1, 0.611765), 1, u'default'), 'Hf': ((0.301961, 0.760784, 1), 1, u'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), 'He': ((0.85098, 1, 1), 1, u'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), 'Mg': ((0.541176, 1, 0), 1, u'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), 'O': ((1, 0.0509804, 0.0509804), 1, u'default'), 'Mt': ((0.921569, 0, 0.14902), 1, u'default'), 'S': ((1, 1, 0.188235), 1, u'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'),
'Eu': ((0.380392, 1, 0.780392), 1, u'default'), 'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), 'Er': ((0, 0.901961, 0.458824), 1, u'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), 'Nd': ((0.780392, 1, 0.780392), 1, u'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), 'Np': ((0, 0.501961, 1), 1, u'default'), 'Fr': ((0.258824, 0, 0.4), 1, u'default'), 'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), 'B': ((1, 0.709804, 0.709804), 1, u'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), 'Sr': ((0, 1, 0), 1, u'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), 'Sm': ((0.560784, 1, 0.780392), 1, u'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, u'default'),
'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), 'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), 'Sg': ((0.85098, 0, 0.270588), 1, u'default'), 'Se': ((1, 0.631373, 0), 1, u'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), 'Ca': ((0.239216, 1, 0), 1, u'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), 'Ce': ((1, 1, 0.780392), 1, u'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), 'Tm': ((0, 0.831373, 0.321569), 1, u'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), 'La': ((0.439216, 0.831373, 1), 1, u'default'), 'Li': ((0.8, 0.501961, 1), 1, u'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), 'Lu': ((0, 0.670588, 0.141176), 1, u'default'), 'Lr': ((0.780392, 0, 0.4), 1, u'default'), 'Th': ((0, 0.729412, 1), 1, u'default'), 'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'),
'Te': ((0.831373, 0.478431, 0), 1, u'default'), 'Tb': ((0.188235, 1, 0.780392), 1, u'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), 'Ta': ((0.301961, 0.65098, 1), 1, u'default'), 'Yb': ((0, 0.74902, 0.219608), 1, u'default'), 'Db': ((0.819608, 0, 0.309804), 1, u'default'), 'Dy': ((0.121569, 1, 0.780392), 1, u'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), 'I': ((0.580392, 0, 0.580392), 1, u'default'), 'U': ((0, 0.560784, 1), 1, u'default'), 'Y': ((0.580392, 1, 1), 1, u'default'), 'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), 'Au': ((1, 0.819608, 0.137255), 1, u'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), 'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 0, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 2, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (3, (u'green', (0, 1, 0, 1)), {(u'', (1, 1, 1, 1)): [1], (u'', (1, 0.270588, 0, 1)): [0]})
	viewerInfo = {'cameraAttrs': {'center': (-13.438102722168, -26.141986846924, -82.401504516602), 'fieldOfView': 12.198317351596, 'nearFar': (23.397581375342, -211.10630370798), 'ortho': False, 'eyeSeparation': 50.8, 'focal': -82.401504516602}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': True, 'showShadows': False, 'viewSize': 114.33205999895, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 1.5, 'singleLayerTransparency': True, 'shadowTextureSize': 4096, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.8, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 2, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': 1}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v62 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {'session-start': (0.8, 114.33205999895, (-13.438102722168, -26.141986846924, -82.401504516602), (27.382496647003, -214.59240753452), -82.401504516602, {(9, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582)), (0, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582)), (7, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582)), (3, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582)), (8, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582)), (6, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582)), (2, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582)), (5, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582)), (1, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582)), (4, 0): ((-42.274742647716764, -79.28096336763366, -126.74891550758952), (0.8581557987488271, 0.24430532572775668, -0.451534641965395, 148.64615591164582))}, {(6, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (3, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (0, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (5, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (2, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (9, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (7, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (4, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (1, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0), (8, 0, 'Volume'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, False, 5.0)}, 4, (-23.83985474367006, -25.700333022792066, -93.60495544376052), False, 12.198317351596)}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = [('4times', [[1, 1], [3.6, 1], [3.6, 1], [1.8, 0.25, 0.25, 0.25], [0.9, 0.25]]), ('licorice', [[0.35, 0.35], [0.35, 0.35], [0.35, 0.35], [0.35, 0.35, 0.35, 0.35], [0.35, 0.35]]), ('FAT', [[0.75, 0.75], [2.7, 0.75], [2.7, 0.75], [5.4, 0.75, 0.75, 0.75], [2.7, 0.75]])]
	userXSections = []
	userResidueClasses = []
	residueData = []
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDVUMY3VzdG9tX3NjZW5lcQ5VBG1vZGVxD1UGbGluZWFycRB1YlUIa2V5ZnJhbWVxEWgFKYFxEn1xEyhoCEsUaAlLAWgKXXEUaAxhaA1VCGtleWZyYW1lcRVoD2gQdWJVBXNjZW5lcRZoBSmBcRd9cRgoaAhLAWgJSwFoCl1xGWgMYWgNVQVzY2VuZXEaaA9oEHVidWIu'
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.3574067443365933, 0.6604015517481455, -0.6604015517481456), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.3574067443365933, 0.6604015517481455, 0.6604015517481456), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.2505628070857316, 0.2505628070857316, 0.9351131265310294), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Nup85.dx',
       'path': '3-xray_Nup85.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.9, 0.75, 0.6, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 38, 46, 55, ),
          [ 2, 2, 2, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 38, 46, 55, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 0,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 1,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.0129,
         },
        'representation': 'surface',
        'session_volume_id': 'S\x0b7cW_CTIS{ \x0c%Ag2?`Gus4 Gg*1=` I',
        'solid_brightness_factor': 1.0,
        'solid_colors': (
          ( 0.0, 0.16666666666666674, 0.33333333333333337, 1, ),
          ( 0.0, 0.16666666666666674, 0.33333333333333337, 1, ),
          ( 0.0, 0.16666666666666674, 0.33333333333333337, 1, ),
          ( 1.0, 0.8333333333333333, 0.6666666666666666, 1, ),
          ( 1.0, 0.8333333333333333, 0.6666666666666666, 1, ),
          ( 1.0, 0.8333333333333333, 0.6666666666666666, 1, ),
         ),
        'solid_levels': (
          ( 0.0, 1, ),
          ( 0.0, 0.99, ),
          ( 0, 0, ),
          ( 0, 0, ),
          ( 0.028524863976985216, 0.99, ),
          ( 0.07449690252542496, 1, ),
         ),
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 1.0, 0.843137, 0.0, 1.0, ),
         ],
        'surface_levels': [ 0.00818, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 7,
          'name': u'3-xray_Nup85.dx',
          'osl_identifier': u'#7',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Seh1.dx',
       'path': '3-xray_Seh1.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.8, 0.8, 0.6, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 38, 36, 33, ),
          [ 2, 2, 2, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 38, 36, 33, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 0,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 1,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.00622,
         },
        'representation': 'surface',
        'session_volume_id': 'vX\rTw<B,&3bjKR~lAmJ>Rg FA"C]{31w',
        'solid_brightness_factor': 1.0,
        'solid_colors': (
          ( 0.0, 0.0, 0.2500000000000001, 1, ),
          ( 0.0, 0.0, 0.2500000000000001, 1, ),
          ( 0.0, 0.0, 0.2500000000000001, 1, ),
          ( 1.0, 1.0, 0.7499999999999999, 1, ),
          ( 1.0, 1.0, 0.7499999999999999, 1, ),
          ( 1.0, 1.0, 0.7499999999999999, 1, ),
         ),
        'solid_levels': (
          ( 0.0, 1, ),
          ( 0.0, 0.99, ),
          ( 0, 0, ),
          ( 0, 0, ),
          ( 0.028157767094671726, 0.99, ),
          ( 0.05272990092635155, 1, ),
         ),
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.11764705882352941, 0.5647058823529412, 1.0, 1.0, ),
         ],
        'surface_levels': [ 0.0106, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 9,
          'name': u'3-xray_Seh1.dx',
          'osl_identifier': u'#9',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Nup120.dx',
       'path': '3-xray_Nup120.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 1, 1, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 59, 57, 55, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 59, 57, 55, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': False,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': True,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': 'OS\tm\r#~?H\x0blm&%-d@ LT]L!\n7i*5\r)Xg',
        'solid_brightness_factor': 1,
        'solid_colors': [ ],
        'solid_levels': [ ],
        'solid_model': None,
        'surface_brightness_factor': 1,
        'surface_colors': [ ],
        'surface_levels': [ ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': False,
          'id': 1,
          'name': u'3-xray_Nup120.dx',
          'osl_identifier': u'#1',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Sec13.dx',
       'path': '3-xray_Sec13.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.6, 0.75, 0.9, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 27, 29, 28, ),
          [ 2, 2, 2, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 27, 29, 28, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 0,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 1,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.00303,
         },
        'representation': 'surface',
        'session_volume_id': 'lu#fUJAy{F+\tOY!75\nY\'2OR3sL~2\x0b{"U',
        'solid_brightness_factor': 1.0,
        'solid_colors': (
          ( 0.33333333333333337, 0.16666666666666674, 0.0, 1, ),
          ( 0.33333333333333337, 0.16666666666666674, 0.0, 1, ),
          ( 0.33333333333333337, 0.16666666666666674, 0.0, 1, ),
          ( 0.6666666666666666, 0.8333333333333333, 1.0, 1, ),
          ( 0.6666666666666666, 0.8333333333333333, 1.0, 1, ),
          ( 0.6666666666666666, 0.8333333333333333, 1.0, 1, ),
         ),
        'solid_levels': (
          ( 0.0, 1, ),
          ( 0.0, 0.99, ),
          ( 0, 0, ),
          ( 0, 0, ),
          ( 0.053778223163634536, 0.99, ),
          ( 0.08219199627637863, 1, ),
         ),
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.647059, 0.164706, 0.164706, 1.0, ),
         ],
        'surface_levels': [ 0.0112, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 8,
          'name': u'3-xray_Sec13.dx',
          'osl_identifier': u'#8',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Nup145c-CTD.dx',
       'path': '3-xray_Nup145c-CTD.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 0.7, 1, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 25, 20, 23, ),
          [ 2, 2, 2, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 25, 20, 23, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 0,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 1,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.00165,
         },
        'representation': 'surface',
        'session_volume_id': 'Pc_r}MEoJv\r,er4Lx?9dH3k}->z%Q v#',
        'solid_brightness_factor': 1.0,
        'solid_colors': (
          ( 0.30000000000000004, 0.30000000000000004, 0, 1, ),
          ( 0.30000000000000004, 0.30000000000000004, 0, 1, ),
          ( 0.30000000000000004, 0.30000000000000004, 0, 1, ),
          ( 0.7, 0.7, 1, 1, ),
          ( 0.7, 0.7, 1, 1, ),
          ( 0.7, 0.7, 1, 1, ),
         ),
        'solid_levels': (
          ( 0.0, 1, ),
          ( 0.0, 0.99, ),
          ( 0, 0, ),
          ( 0, 0, ),
          ( 0.0009033964018221013, 0.99, ),
          ( 0.0018261499935761094, 1, ),
         ),
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.745, 0.745, 0.745, 1.0, ),
         ],
        'surface_levels': [ 0.00032, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 3,
          'name': u'3-xray_Nup145c-CTD.dx',
          'osl_identifier': u'#3',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Nup145c-NTD.dx',
       'path': '3-xray_Nup145c-NTD.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 1, 0.7, 1, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 22, 25, 18, ),
          [ 2, 2, 2, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 22, 25, 18, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 0,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 1,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.0015,
         },
        'representation': 'surface',
        'session_volume_id': 'VSHP:i]|m\\\x0cSK L/RB,70]Y}O/Y^Vc<^',
        'solid_brightness_factor': 1.0,
        'solid_colors': (
          ( 0, 0.30000000000000004, 0, 1, ),
          ( 0, 0.30000000000000004, 0, 1, ),
          ( 0, 0.30000000000000004, 0, 1, ),
          ( 1, 0.7, 1, 1, ),
          ( 1, 0.7, 1, 1, ),
          ( 1, 0.7, 1, 1, ),
         ),
        'solid_levels': (
          ( 0.0, 1, ),
          ( 0.0, 0.99, ),
          ( 0, 0, ),
          ( 0, 0, ),
          ( 0.0007066483051283285, 0.99, ),
          ( 0.0025668300222605467, 1, ),
         ),
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.745, 0.745, 0.745, 1.0, ),
         ],
        'surface_levels': [ 0.00043, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 4,
          'name': u'3-xray_Nup145c-NTD.dx',
          'osl_identifier': u'#4',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Nup84.dx',
       'path': '3-xray_Nup84.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 1, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 58, 70, 59, ),
          ( 1, 1, 1, ),
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 58, 70, 59, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': False,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': True,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': 'nX1jX=V@Q\\v3Nn\x0c>+#<L8v94U\nz6I#IQ',
        'solid_brightness_factor': 1,
        'solid_colors': [ ],
        'solid_levels': [ ],
        'solid_model': None,
        'surface_brightness_factor': 1,
        'surface_colors': [ ],
        'surface_levels': [ ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': False,
          'id': 6,
          'name': u'3-xray_Nup84.dx',
          'osl_identifier': u'#6',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Nup145c-middle.dx',
       'path': '3-xray_Nup145c-middle.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 1, 0.7, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 37, 37, 37, ),
          [ 2, 2, 2, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 37, 37, 37, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 0,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 1,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.00661,
         },
        'representation': 'surface',
        'session_volume_id': '`{p)9B>\nH\r}z3R``%$ BfRij\rwVK6RKm',
        'solid_brightness_factor': 1.0,
        'solid_colors': (
          ( 0, 0.30000000000000004, 0.30000000000000004, 1, ),
          ( 0, 0.30000000000000004, 0.30000000000000004, 1, ),
          ( 0, 0.30000000000000004, 0.30000000000000004, 1, ),
          ( 1, 0.7, 0.7, 1, ),
          ( 1, 0.7, 0.7, 1, ),
          ( 1, 0.7, 0.7, 1, ),
         ),
        'solid_levels': (
          ( 0.0, 1, ),
          ( 0.0, 0.99, ),
          ( 0, 0, ),
          ( 0, 0, ),
          ( 0.0355587700098753, 0.99, ),
          ( 0.07072149962186813, 1, ),
         ),
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.745, 0.745, 0.745, 1.0, ),
         ],
        'surface_levels': [ 0.01, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 5,
          'name': u'3-xray_Nup145c-middle.dx',
          'osl_identifier': u'#5',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Nup133.dx',
       'path': '3-xray_Nup133.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 1, 1, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 113, 102, 95, ),
          [ 2, 2, 2, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 113, 102, 95, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': False,
          'cap_faces': False,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': True,
          'dim_transparent_voxels': True,
          'flip_normals': True,
          'limit_voxel_count': True,
          'line_thickness': 1.0,
          'linear_interpolation': True,
          'maximum_intensity_projection': False,
          'mesh_lighting': True,
          'minimal_texture_memory': False,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': False,
          'smooth_lines': False,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': True,
          'subdivide_surface': False,
          'subdivision_levels': 1,
          'surface_smoothing': False,
          'two_sided_lighting': True,
          'version': 1,
          'voxel_limit': 1.0,
         },
        'representation': 'surface',
        'session_volume_id': '8s!-<`+B[#)FEr>$~VF6R%n_7"o+U\tI.',
        'solid_brightness_factor': 1,
        'solid_colors': [ ],
        'solid_levels': [ ],
        'solid_model': None,
        'surface_brightness_factor': 1,
        'surface_colors': [ ],
        'surface_levels': [ ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': False,
          'id': 2,
          'name': u'3-xray_Nup133.dx',
          'osl_identifier': u'#2',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0,
        'version': 6,
       },
      ],
     ),
     (
      {
       'available_subsamplings': {},
       'cell_angles': ( 90, 90, 90, ),
       'class': 'Data_State',
       'file_type': 'apbs',
       'grid_id': '',
       'name': '3-xray_Nup120-CTD.dx',
       'path': '3-xray_Nup120-CTD.dx',
       'rotation': (
         ( 1, 0, 0, ),
         ( 0, 1, 0, ),
         ( 0, 0, 1, ),
        ),
       'symmetries': ( ),
       'version': 6,
       'xyz_origin': None,
       'xyz_step': None,
      },
      [
       {
        'class': 'Volume_State',
        'default_rgba': ( 0.7, 0.7, 0.7, 1, ),
        'region': (
          ( 0, 0, 0, ),
          ( 44, 40, 41, ),
          [ 2, 2, 2, ],
         ),
        'region_list': {
          'class': 'Region_List_State',
          'current_index': 0,
          'named_regions': [ ],
          'region_list': [
            (
             ( 0, 0, 0, ),
             ( 44, 40, 41, ),
            ),
           ],
          'version': 1,
         },
        'rendering_options': {
          'box_faces': False,
          'bt_correction': 0,
          'cap_faces': 0,
          'class': 'Rendering_Options_State',
          'color_mode': 'auto8',
          'dim_transparency': 1,
          'dim_transparent_voxels': 1,
          'flip_normals': 1,
          'limit_voxel_count': 1,
          'line_thickness': 1.0,
          'linear_interpolation': 1,
          'maximum_intensity_projection': 0,
          'mesh_lighting': 1,
          'minimal_texture_memory': 0,
          'orthoplane_positions': ( 0, 0, 0, ),
          'orthoplanes_shown': ( False, False, False, ),
          'outline_box_linewidth': 1.0,
          'outline_box_rgb': ( 1.0, 1.0, 1.0, ),
          'projection_mode': 'auto',
          'show_outline_box': 0,
          'smooth_lines': 0,
          'smoothing_factor': 0.3,
          'smoothing_iterations': 2,
          'square_mesh': 1,
          'subdivide_surface': 0,
          'subdivision_levels': 1,
          'surface_smoothing': 0,
          'two_sided_lighting': 1,
          'version': 1,
          'voxel_limit': 0.00977,
         },
        'representation': 'surface',
        'session_volume_id': 'L\r)8[S+,b) I#O{X&Je"Ce|C|VX&fofM',
        'solid_brightness_factor': 1.0,
        'solid_colors': (
          ( 0.0, 0.0, 0.0, 1, ),
          ( 0.0, 0.0, 0.0, 1, ),
          ( 0.0, 0.0, 0.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
          ( 1.0, 1.0, 1.0, 1, ),
         ),
        'solid_levels': (
          ( 0.0, 1, ),
          ( 0.0, 0.99, ),
          ( 0, 0, ),
          ( 0, 0, ),
          ( 0.015726568356901408, 0.99, ),
          ( 0.051010601222515106, 1, ),
         ),
        'solid_model': None,
        'surface_brightness_factor': 1.0,
        'surface_colors': [
          ( 0.13333333333333333, 0.5450980392156862, 0.13333333333333333, 1.0, ),
         ],
        'surface_levels': [ 0.00778, ],
        'surface_model': {
          'active': True,
          'class': 'Model_State',
          'clip_plane_normal': ( 0.0, 0.0, -1.0, ),
          'clip_plane_origin': ( 0.0, 0.0, 0.0, ),
          'clip_thickness': 5.0,
          'display': True,
          'id': 0,
          'name': u'3-xray_Nup120-CTD.dx',
          'osl_identifier': u'#0',
          'silhouette': True,
          'subid': 0,
          'use_clip_plane': False,
          'use_clip_thickness': False,
          'version': 5,
          'xform': {
            'class': 'Xform_State',
            'rotation_angle': 148.64615591164582,
            'rotation_axis': ( 0.8581557987488271, 0.24430532572775668, -0.451534641965395, ),
            'translation': ( -42.274742647716764, -79.28096336763366, -126.74891550758952, ),
            'version': 1,
           },
         },
        'transparency_depth': 0.5,
        'transparency_factor': 0.0,
        'version': 6,
       },
      ],
     ),
    ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')


def restore_volume_dialog():
 volume_dialog_state = \
  {
   'adjust_camera': 0,
   'auto_show_subregion': 0,
   'box_padding': '0',
   'class': 'Volume_Dialog_State',
   'data_cache_size': '512',
   'focus_volume': 'VSHP:i]|m\\\x0cSK L/RB,70]Y}O/Y^Vc<^',
   'geometry': u'417x478+497+538',
   'histogram_active_order': [ 2, 1, 0, ],
   'histogram_volumes': [ 'lu#fUJAy{F+\tOY!75\nY\'2OR3sL~2\x0b{"U', 'Pc_r}MEoJv\r,er4Lx?9dH3k}->z%Q v#', 'VSHP:i]|m\\\x0cSK L/RB,70]Y}O/Y^Vc<^', ],
   'immediate_update': 1,
   'initial_colors': (
     ( 0.7, 0.7, 0.7, 1, ),
     ( 1, 1, 0.7, 1, ),
     ( 0.7, 1, 1, 1, ),
     ( 0.7, 0.7, 1, 1, ),
     ( 1, 0.7, 1, 1, ),
     ( 1, 0.7, 0.7, 1, ),
     ( 0.7, 1, 0.7, 1, ),
     ( 0.9, 0.75, 0.6, 1, ),
     ( 0.6, 0.75, 0.9, 1, ),
     ( 0.8, 0.8, 0.6, 1, ),
    ),
   'is_visible': True,
   'max_histograms': '3',
   'representation': 'surface',
   'selectable_subregions': 0,
   'show_on_open': 1,
   'show_plane': 1,
   'shown_panels': [ 'Threshold and Color', 'Brightness and Transparency', 'Display style', ],
   'subregion_button': 'middle',
   'use_initial_colors': 1,
   'version': 12,
   'voxel_limit_for_open': '256',
   'voxel_limit_for_plane': '256',
   'zone_radius': 2.0,
  }
 from VolumeViewer import session
 session.restore_volume_dialog_state(volume_dialog_state)

try:
  restore_volume_dialog()
except:
  reportRestoreError('Error restoring volume dialog')


def restore_surface_color_mapping():
 try:
  surface_color_state = \
   {
    'class': 'Surface_Colorings_State',
    'coloring_table': {},
    'geometry': None,
    'is_visible': False,
    'version': 2,
   }
  import SurfaceColor.session
  SurfaceColor.session.restore_surface_color_state(surface_color_state)
 except:
  reportRestoreError('Error restoring surface color mapping')

registerAfterModelsCB(restore_surface_color_mapping)


def restoreRemainder():
	from SimpleSession.versions.v62 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (513, 418)
	xformMap = {}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v62 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v62 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')


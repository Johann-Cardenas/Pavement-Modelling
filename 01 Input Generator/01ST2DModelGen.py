#Loading Modulus...
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

#==============================================================================
# MODEL DEFINITION
#==============================================================================

# [MODEL DIMENSIONS]

Height=2500.0  #Unit: mm
Width=2500.0   #Unit: mm  

# [LAYER PROPERTIES]

# Layer O1: Wearing Course
h1=25.0      #Unit: mm
E1=3300.0    #Unit: MPa
v1=0.35      #Unit: --

# Layer O2: Binder Course
h2=37.5      #Unit: mm
E2=2000.0    #Unit: MPa
v2=0.35     #Unit: --

# Layer O3: Base Layer
h3=62.5     #Unit: mm
E3=1250.0    #Unit: MPa
v3=0.35     #Unit: --

# Layer O4: Sub-Base Layer
h4=150.0     #Unit: mm
E4=220.0     #Unit: MPa
v4=0.30      #Unit: --

# Layer O5: Subgrade
h5=Height-h1-h2-h3-h4      #Unit: mm
E5=70.0                    #Unit: MPa
v5=0.30                    #Unit: --

# [LOADING]
UPress=0.69      #Unit: MPa
Radius=100.0     #Unit: mm

# [MESHING]

# [Horizontal Bias]

# Left Side 
MinLS=5.0     #Unit: mm
MaxLS=10.0     #Unit: mm

# Right Side
MinRS=10.0     #Unit: mm
MaxRS=100.0     #Unit: mm

# [Vertical Bias]

# Wearing Course
MinWC=5.0     #Unit: mm
MaxWC=5.0     #Unit: mm

# Binder Course
MinBC=5.0     #Unit: mm
MaxBC=5.0     #Unit: mm

# Base Layer
MinBL=5.0     #Unit: mm
MaxBL=5.0     #Unit: mm

# Sub-Base Layer
MinSBL=5.0     #Unit: mm
MaxSBL=10.0     #Unit: mm

# Subgrade
MinSUB=10.0     #Unit: mm
MaxSUB=100.0     #Unit: mm


#==============================================================================
# PART DEFINITION
#==============================================================================

# [WEARING COURSE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=Width)
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    viewStyle=AXISYM)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -Height/2), point2=(0.0, Height/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(Width, -h1))
mdb.models['Model-1'].Part(dimensionality=AXISYMMETRIC, name='Wearing Course', 
    type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Wearing Course'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])

# [Wearing Course] Defining partition <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=125, name='__profile__', 
    sheetSize=2*Width, transform=
    mdb.models['Model-1'].parts['Wearing Course'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Wearing Course'].faces.findAt((
    2*Width/3, -h1/3, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(Width/2, -h1/2, 0.0)))
mdb.models['Model-1'].parts['Wearing Course'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, Height), 
    point2=(0.0, -Height))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1/2), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ), textPoint=(0.0, Height), value=Radius)
mdb.models['Model-1'].parts['Wearing Course'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Wearing Course'].faces.findAt(((2*Width/3, 
    -h1/3, 0.0), )), sketch=
    mdb.models['Model-1'].sketches['__profile__'])


# [BINDER COURSE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=Width)
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    viewStyle=AXISYM)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -Height/2), point2=(0.0, Height/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, -h1), 
    point2=(Width, -h1-h2))
mdb.models['Model-1'].Part(dimensionality=AXISYMMETRIC, name='Binder Course', 
    type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Binder Course'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])

# [Binder Course] Defining partition <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=125, name='__profile__', 
    sheetSize=2*Width, transform=
    mdb.models['Model-1'].parts['Binder Course'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Binder Course'].faces.findAt((
    2*Width/3, -h1-h2/3, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(Width/2, -h1-h2/2, 0.0)))
mdb.models['Model-1'].parts['Binder Course'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, Height), 
    point2=(0.0, -Height))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1-h2/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1-h2/2), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ), textPoint=(0.0, Height), value=Radius)
mdb.models['Model-1'].parts['Binder Course'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Binder Course'].faces.findAt(((2*Width/3, 
    -h1-h2/3, 0.0), )), sketch=
    mdb.models['Model-1'].sketches['__profile__'])


# [BASE LAYER] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=Width)
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    viewStyle=AXISYM)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -Height/2), point2=(0.0, Height/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, -h1-h2), 
    point2=(Width, -h1-h2-h3))
mdb.models['Model-1'].Part(dimensionality=AXISYMMETRIC, name='Base Layer', 
    type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Base Layer'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])

# [Base Layer] Defining partition <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=125, name='__profile__', 
    sheetSize=2*Width, transform=
    mdb.models['Model-1'].parts['Base Layer'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Base Layer'].faces.findAt((
    2*Width/3, -h1-h2-h3/3, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(Width/2, -h1-h2-h3/2, 0.0)))
mdb.models['Model-1'].parts['Base Layer'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, Height), 
    point2=(0.0, -Height))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1-h2-h3/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1-h2-h3/2), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ), textPoint=(0.0, Height), value=Radius)
mdb.models['Model-1'].parts['Base Layer'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Base Layer'].faces.findAt(((2*Width/3, 
    -h1-h2-h3/3, 0.0), )), sketch=
    mdb.models['Model-1'].sketches['__profile__'])


# [SUB-BASE LAYER] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=Width)
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    viewStyle=AXISYM)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -Height/2), point2=(0.0, Height/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, -h1-h2-h3), 
    point2=(Width, -h1-h2-h3-h4))
mdb.models['Model-1'].Part(dimensionality=AXISYMMETRIC, name='Sub-Base Layer', 
    type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Sub-Base Layer'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])

# [Sub-Base Layer] Defining partition <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=125, name='__profile__', 
    sheetSize=2*Width, transform=
    mdb.models['Model-1'].parts['Sub-Base Layer'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Sub-Base Layer'].faces.findAt((
    2*Width/3, -h1-h2-h3-h4/3, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(Width/2, -h1-h2-h3-h4/2, 0.0)))
mdb.models['Model-1'].parts['Sub-Base Layer'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, Height), 
    point2=(0.0, -Height))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1-h2-h3-h4/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1-h2-h3-h4/2), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ), textPoint=(0.0, Height), value=Radius)
mdb.models['Model-1'].parts['Sub-Base Layer'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Sub-Base Layer'].faces.findAt(((2*Width/3, 
    -h1-h2-h3-h4/3, 0.0), )), sketch=
    mdb.models['Model-1'].sketches['__profile__'])


# [SUBGRADE] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=Width)
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    viewStyle=AXISYM)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -Height/2), point2=(0.0, Height/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 0.0), 
    ))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, -h1-h2-h3-h4), 
    point2=(Width, -Height))
mdb.models['Model-1'].Part(dimensionality=AXISYMMETRIC, name='Subgrade', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Subgrade'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])

# [Subgrade Layer] Defining partition <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=125, name='__profile__', 
    sheetSize=2*Width, transform=
    mdb.models['Model-1'].parts['Subgrade'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Subgrade'].faces.findAt((
    2*Width/3, -h1-h2-h3-h4-h5/3, 0.0), (0.0, 0.0, 1.0)), sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, origin=(Width/2, -h1-h2-h3-h4-h5/2, 0.0)))
mdb.models['Model-1'].parts['Subgrade'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, Height), 
    point2=(0.0, -Height))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1-h2-h3-h4-h5/2))
mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0))
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((-Width/2, 
    -h1-h2-h3-h4-h5/2), ), entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry.findAt((0.0, 
    0.0), ), textPoint=(0.0, Height), value=Radius)
mdb.models['Model-1'].parts['Subgrade'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Subgrade'].faces.findAt(((2*Width/3, 
    -h1-h2-h3-h4-h5/3, 0.0), )), sketch=
    mdb.models['Model-1'].sketches['__profile__'])


#==============================================================================
# MATERIAL DEFINITION
#==============================================================================

# [Wearing Course] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].Material(name='MAT_Wearing Course')
mdb.models['Model-1'].materials['MAT_Wearing Course'].Elastic(table=((E1, 
    v1), ))

# [Binder Course] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].Material(name='MAT_Binder Course')
mdb.models['Model-1'].materials['MAT_Binder Course'].Elastic(table=((E2, 
    v2), ))

# [Base Layer] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].Material(name='MAT_Base Layer')
mdb.models['Model-1'].materials['MAT_Base Layer'].Elastic(table=((E3, 
    v3), ))

# [Sub-Base Layer] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].Material(name='MAT_Sub-Base Layer')
mdb.models['Model-1'].materials['MAT_Sub-Base Layer'].Elastic(table=((E4, 
    v4), ))

# [Subgrade] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].Material(name='MAT_Subgrade')
mdb.models['Model-1'].materials['MAT_Subgrade'].Elastic(table=((E5, v5), ))

#==============================================================================
# SECTION DEFINITION
#==============================================================================

# [Wearing Course] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].HomogeneousSolidSection(material='MAT_Wearing Course', 
    name='SECTION_Wearing Course', thickness=None)

# [Binder Course] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].HomogeneousSolidSection(material='MAT_Binder Course', 
    name='SECTION_Binder Course', thickness=None)

# [Base Layer] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].HomogeneousSolidSection(material='MAT_Base Layer', name=
    'SECTION_Base Layer', thickness=None)

# [Sub-Base Layer] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].HomogeneousSolidSection(material='MAT_Sub-Base Layer', 
    name='SECTION_Sub-Base Layer', thickness=None)

# [Subgrade] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].HomogeneousSolidSection(material='MAT_Subgrade', name=
    'SECTION_Subgrade', thickness=None)


#==============================================================================
# SECTION ASSIGNMENT
#==============================================================================

# [Wearing Course] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].parts['Wearing Course'].Set(faces=
    mdb.models['Model-1'].parts['Wearing Course'].faces.findAt(((Radius/2, 
    -h1/2, 0.0), ), ((Width/2, -h1/2, 0.0), ), ), name=
    'REG_Wearing Course')
mdb.models['Model-1'].parts['Wearing Course'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Wearing Course'].sets['REG_Wearing Course'], 
    sectionName='SECTION_Wearing Course', thicknessAssignment=FROM_SECTION)

# [Binder Course] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].parts['Binder Course'].Set(faces=
    mdb.models['Model-1'].parts['Binder Course'].faces.findAt(((Radius/2, 
    -h1-h2/2, 0.0), ), ((Width/2, -h1-h2/2, 0.0), ), ), name=
    'REG_Binder Course')
mdb.models['Model-1'].parts['Binder Course'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Binder Course'].sets['REG_Binder Course'], 
    sectionName='SECTION_Binder Course', thicknessAssignment=FROM_SECTION)


# [Base Layer] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].parts['Base Layer'].Set(faces=
    mdb.models['Model-1'].parts['Base Layer'].faces.findAt(((Radius/2, 
    -h1-h2-h3/2, 0.0), ), ((Width/2, -h1-h2-h3/2, 0.0), ), ), name=
    'REG_Base Layer')
mdb.models['Model-1'].parts['Base Layer'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Base Layer'].sets['REG_Base Layer'], 
    sectionName='SECTION_Base Layer', thicknessAssignment=FROM_SECTION)


# [Sub-Base Layer] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].parts['Sub-Base Layer'].Set(faces=
    mdb.models['Model-1'].parts['Sub-Base Layer'].faces.findAt(((Radius/2, 
    -h1-h2-h3-h4/2, 0.0), ), ((Width/2, -h1-h2-h3-h4/2, 0.0), ), ), name=
    'REG_Sub-Base Layer')
mdb.models['Model-1'].parts['Sub-Base Layer'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Sub-Base Layer'].sets['REG_Sub-Base Layer'], 
    sectionName='SECTION_Sub-Base Layer', thicknessAssignment=FROM_SECTION)


# [Subgrade] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].parts['Subgrade'].Set(faces=
    mdb.models['Model-1'].parts['Subgrade'].faces.findAt(((Radius/2, 
    -h1-h2-h3-h4-h5/2, 0.0), ), ((Width/2, -h1-h2-h3-h4-h5/2, 0.0), ), ), name=
    'REG_Subgrade')
mdb.models['Model-1'].parts['Subgrade'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Subgrade'].sets['REG_Subgrade'], 
    sectionName='SECTION_Subgrade', thicknessAssignment=FROM_SECTION)

#==============================================================================
# INSTANCE DEFINITION
#==============================================================================

mdb.models['Model-1'].rootAssembly.DatumCsysByThreePoints(coordSysType=
    CYLINDRICAL, origin=(0.0, 0.0, 0.0), point1=(1.0, 0.0, 0.0), point2=(0.0, 
    0.0, -1.0))

mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name=
    'Wearing Course-1', part=mdb.models['Model-1'].parts['Wearing Course'])

mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name=
    'Binder Course-1', part=mdb.models['Model-1'].parts['Binder Course'])

mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='Base Layer-1', 
    part=mdb.models['Model-1'].parts['Base Layer'])

mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name=
    'Sub-Base Layer-1', part=mdb.models['Model-1'].parts['Sub-Base Layer'])

mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='Subgrade-1', 
    part=mdb.models['Model-1'].parts['Subgrade'])

#==============================================================================
# STEP DEFINITION
#==============================================================================

mdb.models['Model-1'].StaticStep(initialInc=0.1, name='Tire Loading', previous=
    'Initial')

#==============================================================================
# LOAD DEFINITION
#==============================================================================

mdb.models['Model-1'].rootAssembly.Surface(name='Tire Contact Area', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Radius/2, 0.0, 0.0), )))
mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='Tire Loading', 
    distributionType=UNIFORM, field='', magnitude=UPress, name='Tire Pressure', 
    region=mdb.models['Model-1'].rootAssembly.surfaces['Tire Contact Area'])


#==============================================================================
# MESH DEFINITION 
#==============================================================================

# [Setting Mesh Control]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].rootAssembly.setMeshControls(elemShape=QUAD, regions=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].faces.findAt(
    ((Radius/2, -h1/2, 0.0), (0.0, 0.0, 1.0)), ((Width/2, -h1/2, 0.0),
    (0.0, 0.0, 1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].faces.findAt(
    ((Radius/2, -h1-h2/2, 0.0), (0.0, 0.0, 1.0)), ((Width/2, -h1-h2/2, 0.0), 
    (0.0, 0.0, 1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].faces.findAt(
    ((Radius/2, -h1-h2-h3/2, 0.0), (0.0, 0.0, 1.0)), ((Width/2, -h1-h2-h3/2, 0.0),
    (0.0, 0.0, 1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].faces.findAt(
    ((Radius/2, -h1-h2-h3-h4/2, 0.0), (0.0, 0.0, 1.0)), ((Width/2, -h1-h2-h3-h4/2, 0.0), 
    (0.0, 0.0, 1.0)), )+\
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].faces.findAt(
    ((Radius/2, -h1-h2-h3-h4-h5/2, 0.0), (0.0, 0.0, 1.0)), ((Width/2, -h1-h2-h3-h4-h5/2, 0.0), 
    (0.0, 0.0, 1.0)), ), technique=STRUCTURED)


# [Seeding Part Instance] - Single Bias <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# [Left Side ] 
mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
    constraint=FINER, end1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Radius/2, -h1, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Radius/2, -h1-h2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Radius/2, -h1-h2-h3, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Radius/2, -h1-h2-h3-h4, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(((
    Radius/2, -h1-h2-h3-h4-h5, 0.0), ), ), end2Edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Radius/2, 0.0, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Radius/2, -h1, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Radius/2, -h1-h2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Radius/2, -h1-h2-h3, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(((
    Radius/2, -h1-h2-h3-h4, 0.0), ), ), maxSize=MaxLS, minSize=MinLS)


# [Right Side ] 
mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
    constraint=FINER, end1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Width/2, -h1, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Width/2, -h1-h2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Width/2, -h1-h2-h3, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Width/2, -h1-h2-h3-h4, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(((
    Width/2, -h1-h2-h3-h4-h5, 0.0), ), ), end2Edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Width/2, 0.0, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Width/2, -h1, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Width/2, -h1-h2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Width/2, -h1-h2-h3, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(((
    Width/2, -h1-h2-h3-h4, 0.0), ), ), maxSize=MaxRS, minSize=MinRS)


# [Wearing Course] 
mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
    constraint=FINER, end1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Radius, -h1/2, 0.0), ), ((0.0, -h1/2, 0.0), ), ), end2Edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Width, -h1/2, 0.0), )), maxSize=MaxWC, minSize=MinWC)

# [Binder Course] 
mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
    constraint=FINER, end1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Radius, -h1-h2/2, 0.0), ), ((0.0, -h1-h2/2, 0.0), ), ), end2Edges=
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Width, -h1-h2/2, 0.0), )), maxSize=MaxBC, minSize=MinBC)


mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
    constraint=FINER, end1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Radius, -h1-h2/2, 0.0), ), ((0.0, -h1-h2/2, 0.0), ), ), end2Edges=
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Width, -h1-h2/2, 0.0), )), maxSize=MaxBC, minSize=MinBC)

# [Base Layer] 
mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
    constraint=FINER, end1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Radius, -h1-h2-h3/2, 0.0), ), ((0.0, -h1-h2-h3/2, 0.0), ), ), end2Edges=
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Width, -h1-h2-h3/2, 0.0), )), maxSize=MaxBL, minSize=MinBL)

mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
    constraint=FINER, end1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Radius, -h1-h2-h3/2, 0.0), ), ((0.0, -h1-h2-h3/2, 0.0), ), ), end2Edges=
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Width, -h1-h2-h3/2, 0.0), )), maxSize=MaxBL, minSize=MinBL)

# [Sub-Base Layer] 
mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
    constraint=FINER, end1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Radius, -h1-h2-h3-h4/2, 0.0), ), ((0.0, -h1-h2-h3-h4/2, 0.0), ), ), end2Edges=
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Width, -h1-h2-h3-h4/2, 0.0), )), maxSize=MaxSBL, minSize=MinSBL)

# [Subgrade Layer] 
mdb.models['Model-1'].rootAssembly.seedEdgeByBias(biasMethod=SINGLE, 
    constraint=FINER, end1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(((
    Radius, -h1-h2-h3-h4-h5/2, 0.0), ), ((0.0, -h1-h2-h3-h4-h5/2, 0.0), ), ), end2Edges=
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(((
    Width, -h1-h2-h3-h4-h5/2, 0.0), )), maxSize=MaxSUB, minSize=MinSUB)


# [Meshing Part Instance] - Single Bias <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1']))


#==============================================================================
# BOUNDARY CONDITIONS (Supports)
#==============================================================================

# [Left Edge Boundary Conditions (Restriction in X)] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((0.0, -h1/2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((0.0, -h1-h2/2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (0.0, -h1-h2-h3/2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((0.0, -h1-h2-h3-h4/2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(((
    0.0, -h1-h2-h3-h4-h5/2, 0.0), ), ), name='SET_BC_Left Edge')

mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='BC_Left Edge'
    , region=mdb.models['Model-1'].rootAssembly.sets['SET_BC_Left Edge'], u1=
    SET, u2=UNSET, ur3=UNSET)

# [Rigth Edge Boundary Conditions (Restriction in X)] <<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Width, -h1/2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Width, -h1-h2/2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Width, -h1-h2-h3/2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Width, -h1-h2-h3-h4/2, 0.0), ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(((
    Width, -h1-h2-h3-h4-h5/2, 0.0), ), ), name='SET_BC_Right Edge')

mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
    'BC_Right Edge', region=
    mdb.models['Model-1'].rootAssembly.sets['SET_BC_Right Edge'], u1=SET, u2=
    UNSET, ur3=UNSET)

# [Bottom Edge Boundary Conditions (Restriction in X and Y)] <<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(
    ((Radius/2, -Height, 0.0), ),((Width/2, -Height, 0.0), ), ), name='SET_BC_Bottom Edge')
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
    'BC_Bottom Edge', region=
    mdb.models['Model-1'].rootAssembly.sets['SET_BC_Bottom Edge'], u1=SET, u2=
    SET, ur3=UNSET)

#==============================================================================
# INTERACTION DEFINITION
#==============================================================================

# [Surface Definition] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].rootAssembly.Surface(name='SBE_Wearing Course', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Radius/2, -h1, 0.0), ), ((Width/2, -h1, 0.0), ), ))

mdb.models['Model-1'].rootAssembly.Surface(name='STE_Binder Course', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Radius/2, -h1, 0.0), ), ((Width/2, -h1, 0.0), ), ))

mdb.models['Model-1'].rootAssembly.Surface(name='SBE_Binder Course', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Radius/2, -h1-h2, 0.0), ), ((Width/2, -h1-h2, 0.0), ), ))

mdb.models['Model-1'].rootAssembly.Surface(name='STE_Base Layer', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Radius/2, -h1-h2, 0.0), ), ((Width/2, -h1-h2, 0.0), ), ))

mdb.models['Model-1'].rootAssembly.Surface(name='SBE_Base Layer', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt((
    (Radius/2, -h1-h2-h3, 0.0), ), ((Width/2, -h1-h2-h3, 0.0), ), ))

mdb.models['Model-1'].rootAssembly.Surface(name='STE_Sub-Base Layer', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Radius/2, -h1-h2-h3, 0.0), ), ((Width/2, -h1-h2-h3, 0.0), ), ))

mdb.models['Model-1'].rootAssembly.Surface(name='SBE_Sub-Base Layer', 
    side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Radius/2, -h1-h2-h3-h4, 0.0), ), ((Width/2, -h1-h2-h3-h4, 0.0), ), ))

mdb.models['Model-1'].rootAssembly.Surface(name='STE_Subgrade', side1Edges=
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(((
    Radius/2, -h1-h2-h3-h4, 0.0), ), ((Width/2, -h1-h2-h3-h4, 0.0), ), ))


# [Interaction Property Definition] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.models['Model-1'].ContactProperty('IP_Wearing Course-Binder Course')
mdb.models['Model-1'].interactionProperties['IP_Wearing Course-Binder Course'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.3, ), ), temperatureDependency=OFF)
mdb.models['Model-1'].interactionProperties['IP_Wearing Course-Binder Course'].NormalBehavior(
    allowSeparation=OFF, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)


mdb.models['Model-1'].InteractionProperty(name='IP_Binder Course-Base Layer', 
    objectToCopy=
    mdb.models['Model-1'].interactionProperties['IP_Wearing Course-Binder Course'])

mdb.models['Model-1'].InteractionProperty(name='IP_Base Layer-Sub-Base Layer', 
    objectToCopy=
    mdb.models['Model-1'].interactionProperties['IP_Binder Course-Base Layer'])

mdb.models['Model-1'].InteractionProperty(name='IP_Sub-Base Layer-Subgrade', 
    objectToCopy=
    mdb.models['Model-1'].interactionProperties['IP_Base Layer-Sub-Base Layer'])


# [Edge Set Definition] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Wearing Course-1'].edges.findAt(
    ((Radius/2, -h1, 0.0), ), ((Width/2, -h1, 0.0), ), ), name=
    'GSBE_Wearing Course')

mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Radius/2, -h1, 0.0), ), ((Width/2, -h1, 0.0), ), ), name=
    'GSTE_Binder Course')

mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Binder Course-1'].edges.findAt(
    ((Radius/2, -h1-h2, 0.0), ), ((Width/2, -h1-h2, 0.0), ), ), name=
    'GSBE_Binder Course')

mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt(
    ((Radius/2, -h1-h2, 0.0), ), ((Width/2, -h1-h2, 0.0), ), ), name=
    'GSTE_Base Layer')

mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Base Layer-1'].edges.findAt(
    ((Radius/2, -h1-h2-h3, 0.0), ), ((Width/2, -h1-h2-h3, 0.0), ), ), name=
    'GSBE_Base Layer')

mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Radius/2, -h1-h2-h3, 0.0), ), ((Width/2, -h1-h2-h3, 0.0), ), ), name=
    'GSTE_Sub-Base Layer')

mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Sub-Base Layer-1'].edges.findAt(
    ((Radius/2, -h1-h2-h3-h4, 0.0), ), ((Width/2, -h1-h2-h3-h4, 0.0), ), ), name=
    'GSBE_Sub-Base Layer')

mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Subgrade-1'].edges.findAt(
    ((Radius/2, -h1-h2-h3-h4, 0.0), ), ((Width/2, -h1-h2-h3-h4, 0.0), ), ), name=
    'GSTE_Subgrade')

# [Interaction Property Assignment] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# [Wearing Course - Binder Course] 
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=SET, adjustSet=
    mdb.models['Model-1'].rootAssembly.sets['GSBE_Wearing Course'], 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty=
    'IP_Wearing Course-Binder Course', master=
    mdb.models['Model-1'].rootAssembly.surfaces['SBE_Wearing Course'], name=
    'INT_Wearing Course - Binder Course', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['STE_Binder Course'], sliding=
    FINITE, thickness=ON, tied=OFF)

# [Binder Course - Base Layer] 
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=SET, adjustSet=
    mdb.models['Model-1'].rootAssembly.sets['GSBE_Binder Course'], 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IP_Binder Course-Base Layer', 
    master=mdb.models['Model-1'].rootAssembly.surfaces['SBE_Binder Course'], 
    name='INT_Binder Course - Base Layer', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['STE_Base Layer'], sliding=
    FINITE, thickness=ON, tied=OFF)

# [Base Layer - Sub-Base Layer] 
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=SET, adjustSet=
    mdb.models['Model-1'].rootAssembly.sets['GSBE_Base Layer'], 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IP_Base Layer-Sub-Base Layer', 
    master=mdb.models['Model-1'].rootAssembly.surfaces['SBE_Base Layer'], name=
    'INT_Base Layer - Sub-Base Layer', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['STE_Sub-Base Layer'], sliding=
    FINITE, thickness=ON, tied=OFF)


# [Sub-Base Layer - Subgrade] 
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=SET, adjustSet=
    mdb.models['Model-1'].rootAssembly.sets['GSBE_Sub-Base Layer'], 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='IP_Sub-Base Layer-Subgrade', 
    master=mdb.models['Model-1'].rootAssembly.surfaces['SBE_Sub-Base Layer'], 
    name='INT_Sub-Base Layer - Subgrade', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['STE_Subgrade'], sliding=FINITE
    , thickness=ON, tied=OFF)

#==============================================================================
# JOB DEFINITION
#==============================================================================

# [Creating a New Job] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)


# [Submitting Job] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1'].waitForCompletion()


#==============================================================================
# OUTPUT
#==============================================================================

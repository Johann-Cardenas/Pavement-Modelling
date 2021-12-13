
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=210.96875, 
    height=132.701400756836)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
#: Executing "onCaeStartup()" in the site directory ...

session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)""")

o3 = session.openOdb(
    name='D:/02 Academic Content/03 UIUC/01 Research Projects/02 Abaqus Training/00 Scripts/01 Extracting Data/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()

a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)

odb = session.odbs['D:/02 Academic Content/03 UIUC/01 Research Projects/02 Abaqus Training/00 Scripts/01 Extracting Data/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8001.5, 
    farPlane=11998.5, width=1613.8, height=720.599, viewOffsetX=-745.889, 
    viewOffsetY=820.142)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )

#==============================================================================
# DEFINING A PATH ALONG THE LEFT EDGE
#==============================================================================
session.Path(name='Path-1', type=NODE_LIST, expression=(('Wearing Course-1', (
    3, )), ('SUBGRADE-1', (4, ))))
pth = session.paths['Path-1']


#==============================================================================
# GENERATE XY DATA FROM PATH
#==============================================================================
session.XYDataFromPath(name='S22 Stress', path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)

#==============================================================================
# VERTICAL STRESS (S22) PLOT AND EXPORT AS .PNG FILE
#==============================================================================

odb = session.odbs['D:/02 Academic Content/03 UIUC/01 Research Projects/02 Abaqus Training/00 Scripts/01 Extracting Data/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8001.5, 
    farPlane=11998.5, width=1613.8, height=720.599, viewOffsetX=-745.889, 
    viewOffsetY=820.142)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.printToFile(fileName='PNG S22 2D Model', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))


#==============================================================================
# PLOT (S22) GRAPH AND EXPORT AS .PNG FILE
#==============================================================================
odb = session.odbs['D:/02 Academic Content/03 UIUC/01 Research Projects/02 Abaqus Training/00 Scripts/01 Extracting Data/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=8001.5, 
    farPlane=11998.5, width=1613.8, height=720.599, viewOffsetX=-745.889, 
    viewOffsetY=820.142)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']

xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.printToFile(fileName='S22 Graph', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))

#==============================================================================
# EXPORTING FILE CONTAINING X AND Y DATA
#==============================================================================
x0 = session.xyDataObjects['S22 Stress']
session.writeXYReport(fileName='S22 DATA.txt', appendMode=OFF, xyData=(x0, ))




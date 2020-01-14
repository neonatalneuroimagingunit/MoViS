# written by Matteo Caffini
# 26-May-2016
# contact: matteo.caffini@unitn.it

import numpy as np
from psychopy import visual, core, event, info
from scipy.integrate import cumtrapz
from scipy.interpolate import interp1d

# Monitor parameters
monitor_width = 1920
monitor_height = 1080
monitor_frame_rate = 30 # crucial!

# Stimulus parameters (timing)
crossing_time = 6 # time for crossing, one-way, in seconds
Nframes = monitor_frame_rate*crossing_time

# Stimulus parameters (trajectory)
Ax = 17 # percentage, reference frame left-bottom
Ay = 88 # percentage, reference frame left-bottom
Bx = 50 # percentage, reference frame left-bottom
By = 16 # percentage, reference frame left-bottom
Cx = 83 # percentage, reference frame left-bottom
Cy = 88 # percentage, reference frame left-bottom

# Stimulus parameters (shape)
shape_size = 228 #blob width (in pixel units, equals 6.3 cm on 1920x1080 BENQ screen)

# Create blob shape
width = 1
height = 0.5873
R = height/2

xc1 = -width/2+R+R/height # you don't wanna ask, it works
yc1 = 0
xc2 = width/2-R+R/height
yc2 = 0

ang = np.arange(np.pi/2, 3*np.pi/2, 0.1)
xp1 = xc1 + R*np.cos(ang)
yp1 = yc1 + R*np.sin(ang)
ang = np.arange(3*np.pi/2, 5*np.pi/2, 0.1)
xp2 = xc2 + R*np.cos(ang)
yp2 = yc2 + R*np.sin(ang)

xp = np.concatenate((xp1, xp2), axis=0)
yp = np.concatenate((yp1, yp2), axis=0)

vertices = np.stack((xp, yp), axis=1)

# Create bighead L shape
width = 1
height = 0.3174
R = height/2

xc1 = -width/2+R+R/height # you don't wanna ask, it works
yc1 = 0
xc2 = width/2-R+R/height
yc2 = 0

ang = np.arange(np.pi/2, 3*np.pi/2, 0.1)
xp1 = xc1 + R*np.cos(ang)
yp1 = yc1 + R*np.sin(ang)
ang = np.arange(3*np.pi/2, 5*np.pi/2, 0.1)
xp2 = xc2 + R*np.cos(ang)
yp2 = yc2 + R*np.sin(ang)

xp = np.concatenate((xp1, xp2), axis=0)
yp = np.concatenate((yp1, yp2), axis=0)

height = 0.5873
R = height/2
xc3 = width/2-R+R/height
yc3 = 0
ang = np.arange(0, 2*np.pi, 0.1)
xp3 = xc3 + R*np.cos(ang)
yp3 = yc3 + R*np.sin(ang)

vertices_bighead_L_1 = np.stack((xp, yp), axis=1)
vertices_bighead_L_2 = np.stack((xp3, yp3), axis=1)

# Create bighead R shape
width = 1
height = 0.3174
R = height/2

xc1 = -width/2+R+R/height # you don't wanna ask, it works
yc1 = 0
xc2 = width/2-R+R/height
yc2 = 0

ang = np.arange(np.pi/2, 3*np.pi/2, 0.1)
xp1 = xc1 + R*np.cos(ang)
yp1 = yc1 + R*np.sin(ang)
ang = np.arange(3*np.pi/2, 5*np.pi/2, 0.1)
xp2 = xc2 + R*np.cos(ang)
yp2 = yc2 + R*np.sin(ang)

xp = np.concatenate((xp1, xp2), axis=0)
yp = np.concatenate((yp1, yp2), axis=0)

height = 0.5873
R = height/2
xc3 = -width/2+R+R/height
yc3 = 0
ang = np.arange(0, 2*np.pi, 0.1)
xp3 = xc3 + R*np.cos(ang)
yp3 = yc3 + R*np.sin(ang)

vertices_bighead_R_1 = np.stack((xp, yp), axis=1)
vertices_bighead_R_2 = np.stack((xp3, yp3), axis=1)

# Create bigbelly shape
width = 1
height = 0.3174
R = height/2

xc1 = -width/2+R+R/height # you don't wanna ask, it works
yc1 = 0
xc2 = width/2-R+R/height
yc2 = 0

ang = np.arange(np.pi/2, 3*np.pi/2, 0.1)
xp1 = xc1 + R*np.cos(ang)
yp1 = yc1 + R*np.sin(ang)
ang = np.arange(3*np.pi/2, 5*np.pi/2, 0.1)
xp2 = xc2 + R*np.cos(ang)
yp2 = yc2 + R*np.sin(ang)

xp = np.concatenate((xp1, xp2), axis=0)
yp = np.concatenate((yp1, yp2), axis=0)

height = 0.5873
R = height/2
xc3 = 0
yc3 = 0
ang = np.arange(0, 2*np.pi, 0.1)
xp3 = xc3 + R*np.cos(ang)
yp3 = yc3 + R*np.sin(ang)

vertices_bigbelly_1 = np.stack((xp, yp), axis=1)
vertices_bigbelly_2 = np.stack((xp3, yp3), axis=1)

# Create X shape
xXshape = np.array([4, 1, 2, 5, 8, 9, 6, 9, 8, 5, 2, 1]) + 2
yXshape = np.array([0, -3, -4, -1, -4, -3, 0, 3, 4, 1, 4, 3])

#r = np.sqrt(1**2+7**2)
#theta = np.arctan(1/7)
#xXshape = np.array([r*np.cos(theta), 1, r*np.cos(np.pi/2-theta), r*np.cos(np.pi/2+theta), -1, r*np.cos(np.pi-theta), r*np.cos(np.pi+theta), -1, r*np.cos(3*np.pi/2-theta), r*np.cos(3*np.pi/2+theta), 1, r*np.cos(-theta)]) + 10
#yXshape = np.array([r*np.sin(theta), 1, r*np.sin(np.pi/2-theta), r*np.sin(np.pi/2+theta), 1, r*np.sin(np.pi-theta), r*np.sin(np.pi+theta), -1, r*np.sin(3*np.pi/2-theta), r*np.sin(3*np.pi/2+theta), -1, r*np.sin(-theta)])

vertices_Xshape_head = np.stack((xXshape, yXshape), axis=1)
vertices_Xshape_tail = np.stack((-xXshape, yXshape), axis=1)

# Create C shape
#xCshape = np.array([ 1, 9, 9, 2, 2, 9, 9, 1]) + 2
#yCshape = np.array([-3, -3, -2, -2, 2, 2, 3, 3])
#vertices_Cshape_head = np.stack((xCshape, yCshape), axis=1)
#vertices_Cshape_tail = np.stack((-xCshape, yCshape), axis=1)

#xc = np.array([0, 2*np.sqrt(18)-1, 2*np.sqrt(18)-1, np.sqrt(2), np.sqrt(2), 2*np.sqrt(18)-1, 2*np.sqrt(18)-1, 0])+1
#yc = np.array([-3*np.sqrt(2)/2-1, -3*np.sqrt(2)/2-1, -np.sqrt(2)/2-1, -np.sqrt(2)/2-1, np.sqrt(2)/2+1, np.sqrt(2)/2+1, 3*np.sqrt(2)/2+1, 3*np.sqrt(2)/2+1])
xc_1 = np.array([0, 0, np.sqrt(2), np.sqrt(2)])+1
yc_1 = np.array([3*np.sqrt(2)/2, -3*np.sqrt(2)/2, -3*np.sqrt(2)/2, 3*np.sqrt(2)/2])
xc_2 = np.array([np.sqrt(2), np.sqrt(2), 2*np.sqrt(18), 2*np.sqrt(18)])
yc_2 = np.array([3*np.sqrt(2)/2, np.sqrt(2)/2, np.sqrt(2)/2, 3*np.sqrt(2)/2])
xc_3 = np.array([np.sqrt(2), np.sqrt(2), 2*np.sqrt(18), 2*np.sqrt(18)])
yc_3 = -np.array([3*np.sqrt(2)/2, np.sqrt(2)/2, np.sqrt(2)/2, 3*np.sqrt(2)/2])
vertices_Cshape_head_1 = np.stack((xc_1, yc_1), axis=1)
vertices_Cshape_tail_1 = np.stack((-xc_1, yc_1), axis=1)
vertices_Cshape_head_2 = np.stack((xc_2, yc_2), axis=1)
vertices_Cshape_tail_2 = np.stack((-xc_2, yc_2), axis=1)
vertices_Cshape_head_3 = np.stack((xc_3, yc_3), axis=1)
vertices_Cshape_tail_3 = np.stack((-xc_3, yc_3), axis=1)

xe_1 = np.array([0, 0, 2*np.sqrt(18)+np.sqrt(2)/2, 2*np.sqrt(18)+np.sqrt(2)/2])+2
ye_1 = np.array([3*np.sqrt(2)/2, np.sqrt(2)/2, np.sqrt(2)/2, 3*np.sqrt(2)/2])+1
xe_2 = np.array([0, 0, 2*np.sqrt(18)+np.sqrt(2)/2, 2*np.sqrt(18)+np.sqrt(2)/2])+2
ye_2 = -np.array([3*np.sqrt(2)/2, np.sqrt(2)/2, np.sqrt(2)/2, 3*np.sqrt(2)/2])-1
vertices_equalshape_head_1 = np.stack((xe_1, ye_1), axis=1)
vertices_equalshape_tail_1 = np.stack((-xe_1, ye_1), axis=1)
vertices_equalshape_head_2 = np.stack((xe_2, ye_2), axis=1)
vertices_equalshape_tail_2 = np.stack((-xe_2, ye_2), axis=1)

#xx = np.array([2, 2, 6, 6, 8, 8, 12, 12, 8, 8, 6, 6, 2])
#yx = np.array([1, -1, -1, -5, -5, -1, -1, 1, 1, 5, 5, 1, 1])
#vertices_Xshape_head = np.stack((xx, yx), axis=1)
#vertices_Xshape_tail = np.stack((-xx, yx), axis=1)

# Change units to pixels and reference frame to center
Ax_pix = monitor_width*(Ax-50)/100
Ay_pix = monitor_height*(Ay-50)/100
Bx_pix = monitor_width*(Bx-50)/100
By_pix = monitor_height*(By-50)/100
Cx_pix = monitor_width*(Cx-50)/100
Cy_pix = monitor_height*(Cy-50)/100

# Create windows
win_1 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=0, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=[0,0,0])
win_2 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=1, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=[0,0,0])

keys = event.BuilderKeyResponse()

# Create shapes
dot_1 = visual.Circle(win=win_1, name='dot1', units='pix',
    radius=10, edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor='blue', lineColorSpace='rgb255',
    fillColor='blue', fillColorSpace='rgb255',
    opacity=1,interpolate=True)
dot_2 = visual.Circle(win=win_2, name='dot2', units='pix',
    radius=10, edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor='blue', lineColorSpace='rgb255',
    fillColor='blue', fillColorSpace='rgb255',
    opacity=1,interpolate=True)

blob_1 = visual.ShapeStim(win=win_1, name='blob_1', units='pix',
    vertices=vertices,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
blob_2= visual.ShapeStim(win=win_2, name='blob_2', units='pix',
    vertices=vertices,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)

bighead_L_1_1 = visual.ShapeStim(win=win_1, name='bighead_L', units='pix',
    vertices=vertices_bighead_L_1,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
bighead_L_1_2= visual.ShapeStim(win=win_1, name='bighead_L', units='pix',
    vertices=vertices_bighead_L_2,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
bighead_L_2_1 = visual.ShapeStim(win=win_2, name='bighead_L', units='pix',
    vertices=vertices_bighead_L_1,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
bighead_L_2_2= visual.ShapeStim(win=win_2, name='bighead_L', units='pix',
    vertices=vertices_bighead_L_2,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)

bighead_R_1_1 = visual.ShapeStim(win=win_1, name='bighead_L', units='pix',
    vertices=vertices_bighead_R_1,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
bighead_R_1_2= visual.ShapeStim(win=win_1, name='bighead_L', units='pix',
    vertices=vertices_bighead_R_2,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
bighead_R_2_1 = visual.ShapeStim(win=win_2, name='bighead_L', units='pix',
    vertices=vertices_bighead_R_1,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
bighead_R_2_2= visual.ShapeStim(win=win_2, name='bighead_L', units='pix',
    vertices=vertices_bighead_R_2,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)

bigbelly_1_1 = visual.ShapeStim(win=win_1, name='bighead_L', units='pix',
    vertices=vertices_bigbelly_1,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
bigbelly_1_2= visual.ShapeStim(win=win_1, name='bighead_L', units='pix',
    vertices=vertices_bigbelly_2,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
bigbelly_2_1 = visual.ShapeStim(win=win_2, name='bighead_L', units='pix',
    vertices=vertices_bigbelly_1,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
bigbelly_2_2= visual.ShapeStim(win=win_2, name='bighead_L', units='pix',
    vertices=vertices_bigbelly_2,
    ori=0, pos=(0,0), size=shape_size,
    lineWidth=1, lineColor='red', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)

Xshape_1_head = visual.ShapeStim(win=win_1, name='Xshape_1', units='pix',
    vertices=vertices_Xshape_head,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Xshape_1_tail = visual.ShapeStim(win=win_1, name='Xshape_1', units='pix',
    vertices=vertices_Xshape_tail,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Xshape_2_head = visual.ShapeStim(win=win_2, name='Xshape_2', units='pix',
    vertices=vertices_Xshape_head,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Xshape_2_tail = visual.ShapeStim(win=win_2, name='Xshape_2', units='pix',
    vertices=vertices_Xshape_tail,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)

Cshape_1_head_1 = visual.ShapeStim(win=win_1, name='Cshape_1', units='pix',
    vertices=vertices_Cshape_head_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_1_head_2 = visual.ShapeStim(win=win_1, name='Cshape_1', units='pix',
    vertices=vertices_Cshape_head_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_1_head_3 = visual.ShapeStim(win=win_1, name='Cshape_1', units='pix',
    vertices=vertices_Cshape_head_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_1_tail_1 = visual.ShapeStim(win=win_1, name='Cshape_1', units='pix',
    vertices=vertices_Cshape_tail_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_1_tail_2 = visual.ShapeStim(win=win_1, name='Cshape_1', units='pix',
    vertices=vertices_Cshape_tail_2,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_1_tail_3 = visual.ShapeStim(win=win_1, name='Cshape_1', units='pix',
    vertices=vertices_Cshape_tail_3,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_2_head_1 = visual.ShapeStim(win=win_2, name='Cshape_2', units='pix',
    vertices=vertices_Cshape_head_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_2_head_2 = visual.ShapeStim(win=win_2, name='Cshape_2', units='pix',
    vertices=vertices_Cshape_head_2,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_2_head_3 = visual.ShapeStim(win=win_2, name='Cshape_2', units='pix',
    vertices=vertices_Cshape_head_3,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_2_tail_1 = visual.ShapeStim(win=win_2, name='Cshape_2', units='pix',
    vertices=vertices_Cshape_tail_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_2_tail_2 = visual.ShapeStim(win=win_2, name='Cshape_2', units='pix',
    vertices=vertices_Cshape_tail_2,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
Cshape_2_tail_3 = visual.ShapeStim(win=win_2, name='Cshape_2', units='pix',
    vertices=vertices_Cshape_tail_3,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)

equalshape_1_head_1 = visual.ShapeStim(win=win_1, name='equalshape_1', units='pix',
    vertices=vertices_equalshape_head_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
equalshape_1_head_2 = visual.ShapeStim(win=win_1, name='equalshape_1', units='pix',
    vertices=vertices_equalshape_head_2,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
equalshape_1_tail_1 = visual.ShapeStim(win=win_1, name='equalshape_1', units='pix',
    vertices=vertices_equalshape_tail_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
equalshape_1_tail_2 = visual.ShapeStim(win=win_1, name='equalshape_1', units='pix',
    vertices=vertices_equalshape_tail_2,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
equalshape_2_head_1 = visual.ShapeStim(win=win_2, name='equalshape_2', units='pix',
    vertices=vertices_equalshape_head_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
equalshape_2_head_2 = visual.ShapeStim(win=win_2, name='equalshape_2', units='pix',
    vertices=vertices_equalshape_head_2,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
equalshape_2_tail_1 = visual.ShapeStim(win=win_2, name='equalshape_2', units='pix',
    vertices=vertices_equalshape_tail_1,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)
equalshape_2_tail_2 = visual.ShapeStim(win=win_2, name='equalshape_2', units='pix',
    vertices=vertices_equalshape_tail_2,
    ori=0, pos=(0,0), size=8,
    lineWidth=1, lineColor='white', lineColorSpace='rgb255',
    fillColor='white', fillColorSpace='rgb255',
    opacity=1.0, interpolate=True)

rect_L1 = visual.Rect(win=win_1, name='rect_L1', units='pix',
    width=23*monitor_width/100, height=monitor_height,
    ori=0, pos=(-38.5*monitor_width/100,0),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb255',
    fillColor='grey', fillColorSpace='rgb255',
    opacity=1,interpolate=True)
rect_R1 = visual.Rect(win=win_1, name='rect_R1', units='pix',
    width=23*monitor_width/100, height=monitor_height,
    ori=0, pos=(+38.5*monitor_width/100,0),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb255',
    fillColor='grey', fillColorSpace='rgb255',
    opacity=1,interpolate=True)
rect_L2 = visual.Rect(win=win_2, name='rect_L2', units='pix',
    width=23*monitor_width/100, height=monitor_height,
    ori=0, pos=(-38.5*monitor_width/100,0),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb255',
    fillColor='grey', fillColorSpace='rgb255',
    opacity=1,interpolate=True)
rect_R2 = visual.Rect(win=win_2, name='rect_R2', units='pix',
    width=23*monitor_width/100, height=monitor_height,
    ori=0, pos=(+38.5*monitor_width/100,0),
    lineWidth=1, lineColor='grey', lineColorSpace='rgb255',
    fillColor='grey', fillColorSpace='rgb255',
    opacity=1,interpolate=True)

# Calculate coefficients of a parabolic trajectory given three points
x = np.array([Ax_pix, Bx_pix, Cx_pix])
y = np.array([Ay_pix, By_pix, Cy_pix])
z = np.polyfit(x, y, 2)

# Parametrize trajectory and then transform to instrinsic coordinates
t = np.linspace(Ax_pix, Cx_pix, Nframes)

x = t
y = z[0]*x**2+z[1]*x+z[2]

dxdt = np.diff(x)
first = np.insert(dxdt,0, dxdt[0])
last = np.insert(dxdt,-1, dxdt[-1])
dxdt = (first+last)/2;

dydt = np.diff(y)
first = np.insert(dydt,0, dydt[0])
last = np.insert(dydt,-1, dydt[-1])
dydt = (first+last)/2;

s = cumtrapz(np.sqrt(dxdt**2+dydt**2), initial=0)

s0 = s[0]
L = s[-1]
N = np.size(s)
f = interp1d(s, t)

sq = np.linspace(s0, L, N) # equally spaced indices
tnew = f(sq)
xnew = tnew
ynew = z[0]*xnew**2+z[1]*xnew+z[2]

while True:
    # Animate one way...
    for frameN in range(0, Nframes, 1):
        blob_1.pos = (xnew[frameN], ynew[frameN])
        blob_2.pos = (xnew[frameN], ynew[frameN])
        bighead_L_1_1.pos = (xnew[frameN], ynew[frameN])
        bighead_L_1_2.pos = (xnew[frameN], ynew[frameN])
        bighead_L_2_1.pos = (xnew[frameN], ynew[frameN])
        bighead_L_2_2.pos = (xnew[frameN], ynew[frameN])
        bighead_R_1_1.pos = (xnew[frameN], ynew[frameN])
        bighead_R_1_2.pos = (xnew[frameN], ynew[frameN])
        bighead_R_2_1.pos = (xnew[frameN], ynew[frameN])
        bighead_R_2_2.pos = (xnew[frameN], ynew[frameN])
        bigbelly_1_1.pos = (xnew[frameN], ynew[frameN])
        bigbelly_1_2.pos = (xnew[frameN], ynew[frameN])
        bigbelly_2_1.pos = (xnew[frameN], ynew[frameN])
        bigbelly_2_2.pos = (xnew[frameN], ynew[frameN])
        Xshape_1_head.pos = (xnew[frameN], ynew[frameN])
        Xshape_1_tail.pos = (xnew[frameN], ynew[frameN])
        Xshape_2_head.pos = (xnew[frameN], ynew[frameN])
        Xshape_2_tail.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_head_1.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_head_2.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_head_3.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_tail_1.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_tail_2.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_tail_3.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_head_1.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_head_2.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_head_3.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_tail_1.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_tail_2.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_tail_3.pos = (xnew[frameN], ynew[frameN])
        equalshape_1_head_1.pos = (xnew[frameN], ynew[frameN])
        equalshape_1_head_2.pos = (xnew[frameN], ynew[frameN])
        equalshape_1_tail_1.pos = (xnew[frameN], ynew[frameN])
        equalshape_1_tail_2.pos = (xnew[frameN], ynew[frameN])
        equalshape_2_head_1.pos = (xnew[frameN], ynew[frameN])
        equalshape_2_head_2.pos = (xnew[frameN], ynew[frameN])
        equalshape_2_tail_1.pos = (xnew[frameN], ynew[frameN])
        equalshape_2_tail_2.pos = (xnew[frameN], ynew[frameN])

    
        if frameN == 0:
            initial_angle = np.degrees(np.arctan(-(ynew[frameN]-ynew[frameN-1])/(xnew[frameN]-xnew[frameN-1])))
        else:
            angle = np.degrees(np.arctan(-(ynew[frameN]-ynew[frameN-1])/(xnew[frameN]-xnew[frameN-1])))-90 # change this angle to tilt object from tangent trajectory for one way
            blob_1.ori = angle
            blob_2.ori = angle
            bighead_L_1_1.ori = angle
            bighead_L_1_2.ori = angle
            bighead_L_2_1.ori = angle
            bighead_L_2_2.ori = angle
            bighead_R_1_1.ori = angle
            bighead_R_1_2.ori = angle
            bighead_R_2_1.ori = angle
            bighead_R_2_2.ori = angle
            bigbelly_1_1.ori = angle
            bigbelly_1_2.ori = angle
            bigbelly_2_1.ori = angle
            bigbelly_2_2.ori = angle
            Xshape_1_head.ori = angle
            Xshape_1_tail.ori = angle
            Xshape_2_head.ori = angle
            Xshape_2_tail.ori = angle
            Cshape_1_head_1.ori = angle
            Cshape_1_head_2.ori = angle
            Cshape_1_head_3.ori = angle
            Cshape_1_tail_1.ori = angle
            Cshape_1_tail_2.ori = angle
            Cshape_1_tail_3.ori = angle
            Cshape_2_head_1.ori = angle
            Cshape_2_head_2.ori = angle
            Cshape_2_head_3.ori = angle
            Cshape_2_tail_1.ori = angle
            Cshape_2_tail_2.ori = angle
            Cshape_2_tail_3.ori = angle
            equalshape_1_head_1.ori = angle
            equalshape_1_head_2.ori = angle
            equalshape_1_tail_1.ori = angle
            equalshape_1_tail_2.ori = angle
            equalshape_2_head_1.ori = angle
            equalshape_2_head_2.ori = angle
            equalshape_2_tail_1.ori = angle
            equalshape_2_tail_2.ori = angle
        
        # Monitor 1
        #blob_1.draw()
        #bighead_L_1_1.draw()
        #bighead_L_1_2.draw()
        #bighead_R_1_1.draw()
        #bighead_R_1_2.draw()
        bigbelly_1_1.draw()
        bigbelly_1_2.draw()
        #Xshape_1_head.draw()
        #Xshape_1_tail.draw()
        #Cshape_1_head_1.draw()
        #Cshape_1_head_2.draw()
        #Cshape_1_head_3.draw()
        #Cshape_1_tail_1.draw()
        #Cshape_1_tail_2.draw()
        #Cshape_1_tail_3.draw()
        #equalshape_1_head_1.draw()
        #equalshape_1_head_2.draw()
        #equalshape_1_tail_1.draw()
        #equalshape_1_tail_2.draw()
        
        # Monitor 2
        #blob_2.draw()
        #bighead_L_2_1.draw()
        #bighead_L_2_2.draw()
        #bighead_R_2_1.draw()
        #bighead_R_2_2.draw()
        bigbelly_2_1.draw()
        bigbelly_2_2.draw()
        #Xshape_2_head.draw()
        #Xshape_2_tail.draw()
        #Cshape_2_head_1.draw()
        #Cshape_2_head_2.draw()
        #Cshape_2_head_3.draw()
        #Cshape_2_tail_1.draw()
        #Cshape_2_tail_2.draw()
        #Cshape_2_tail_3.draw()
        #equalshape_2_head_1.draw()
        #equalshape_2_head_2.draw()
        #equalshape_2_tail_1.draw()
        #equalshape_2_tail_2.draw()
        
        # Frame
        rect_L1.draw()
        rect_R1.draw()
        rect_L2.draw()
        rect_R2.draw()
        
        win_1.flip()
        win_2.flip()
        
        if event.getKeys(keyList=["escape"]):
            win_1.close()
            win_2.close()
            core.quit()
    
    # ...and the way back.
    for frameN in range(Nframes-1, 0, -1):
        blob_1.pos = (xnew[frameN], ynew[frameN])
        blob_2.pos = (xnew[frameN], ynew[frameN])
        bighead_L_1_1.pos = (xnew[frameN], ynew[frameN])
        bighead_L_1_2.pos = (xnew[frameN], ynew[frameN])
        bighead_L_2_1.pos = (xnew[frameN], ynew[frameN])
        bighead_L_2_2.pos = (xnew[frameN], ynew[frameN])
        bighead_R_1_1.pos = (xnew[frameN], ynew[frameN])
        bighead_R_1_2.pos = (xnew[frameN], ynew[frameN])
        bighead_R_2_1.pos = (xnew[frameN], ynew[frameN])
        bighead_R_2_2.pos = (xnew[frameN], ynew[frameN])
        bigbelly_1_1.pos = (xnew[frameN], ynew[frameN])
        bigbelly_1_2.pos = (xnew[frameN], ynew[frameN])
        bigbelly_2_1.pos = (xnew[frameN], ynew[frameN])
        bigbelly_2_2.pos = (xnew[frameN], ynew[frameN])
        Xshape_1_head.pos = (xnew[frameN], ynew[frameN])
        Xshape_1_tail.pos = (xnew[frameN], ynew[frameN])
        Xshape_2_head.pos = (xnew[frameN], ynew[frameN])
        Xshape_2_tail.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_head_1.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_head_2.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_head_3.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_tail_1.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_tail_2.pos = (xnew[frameN], ynew[frameN])
        Cshape_1_tail_3.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_head_1.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_head_2.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_head_3.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_tail_1.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_tail_2.pos = (xnew[frameN], ynew[frameN])
        Cshape_2_tail_3.pos = (xnew[frameN], ynew[frameN])
        equalshape_1_head_1.pos = (xnew[frameN], ynew[frameN])
        equalshape_1_head_2.pos = (xnew[frameN], ynew[frameN])
        equalshape_1_tail_1.pos = (xnew[frameN], ynew[frameN])
        equalshape_1_tail_2.pos = (xnew[frameN], ynew[frameN])
        equalshape_2_head_1.pos = (xnew[frameN], ynew[frameN])
        equalshape_2_head_2.pos = (xnew[frameN], ynew[frameN])
        equalshape_2_tail_1.pos = (xnew[frameN], ynew[frameN])
        equalshape_2_tail_2.pos = (xnew[frameN], ynew[frameN])

    
        if frameN == 0:
            initial_angle = np.degrees(np.arctan(-(ynew[frameN]-ynew[frameN-1])/(xnew[frameN]-xnew[frameN-1])))
        else:
            angle = np.degrees(np.arctan(-(ynew[frameN]-ynew[frameN-1])/(xnew[frameN]-xnew[frameN-1])))+90 # change this angle to tilt object from tangent trajectory for way back
            blob_1.ori = angle
            blob_2.ori = angle
            bighead_L_1_1.ori = angle
            bighead_L_1_2.ori = angle
            bighead_L_2_1.ori = angle
            bighead_L_2_2.ori = angle
            bighead_R_1_1.ori = angle
            bighead_R_1_2.ori = angle
            bighead_R_2_1.ori = angle
            bighead_R_2_2.ori = angle
            bigbelly_1_1.ori = angle
            bigbelly_1_2.ori = angle
            bigbelly_2_1.ori = angle
            bigbelly_2_2.ori = angle
            Xshape_1_head.ori = angle
            Xshape_1_tail.ori = angle
            Xshape_2_head.ori = angle
            Xshape_2_tail.ori = angle
            Cshape_1_head_1.ori = angle
            Cshape_1_head_2.ori = angle
            Cshape_1_head_3.ori = angle
            Cshape_1_tail_1.ori = angle
            Cshape_1_tail_2.ori = angle
            Cshape_1_tail_3.ori = angle
            Cshape_2_head_1.ori = angle
            Cshape_2_head_2.ori = angle
            Cshape_2_head_3.ori = angle
            Cshape_2_tail_1.ori = angle
            Cshape_2_tail_2.ori = angle
            Cshape_2_tail_3.ori = angle
            equalshape_1_head_1.ori = angle
            equalshape_1_head_2.ori = angle
            equalshape_1_tail_1.ori = angle
            equalshape_1_tail_2.ori = angle
            equalshape_2_head_1.ori = angle
            equalshape_2_head_2.ori = angle
            equalshape_2_tail_1.ori = angle
            equalshape_2_tail_2.ori = angle
        
        # Monitor 1
        #blob_1.draw()
        #bighead_L_1_1.draw()
        #bighead_L_1_2.draw()
        #bighead_R_1_1.draw()
        #bighead_R_1_2.draw()
        bigbelly_1_1.draw()
        bigbelly_1_2.draw()
        #Xshape_1_head.draw()
        #Xshape_1_tail.draw()
        #Cshape_1_head_1.draw()
        #Cshape_1_head_2.draw()
        #Cshape_1_head_3.draw()
        #Cshape_1_tail_1.draw()
        #Cshape_1_tail_2.draw()
        #Cshape_1_tail_3.draw()
        #equalshape_1_head_1.draw()
        #equalshape_1_head_2.draw()
        #equalshape_1_tail_1.draw()
        #equalshape_1_tail_2.draw()
        
        # Monitor 2
        #blob_2.draw()
        #bighead_L_2_1.draw()
        #bighead_L_2_2.draw()
        #bighead_R_2_1.draw()
        #bighead_R_2_2.draw()
        bigbelly_2_1.draw()
        bigbelly_2_2.draw()
        #Xshape_2_head.draw()
        #Xshape_2_tail.draw()
        #Cshape_2_head_1.draw()
        #Cshape_2_head_2.draw()
        #Cshape_2_head_3.draw()
        #Cshape_2_tail_1.draw()
        #Cshape_2_tail_2.draw()
        #Cshape_2_tail_3.draw()
        #equalshape_2_head_1.draw()
        #equalshape_2_head_2.draw()
        #equalshape_2_tail_1.draw()
        #equalshape_2_tail_2.draw()
        
        # Frame
        rect_L1.draw()
        rect_R1.draw()
        rect_L2.draw()
        rect_R2.draw()
        
        win_1.flip()
        win_2.flip()
        
        if event.getKeys(keyList=["escape"]):
            win_1.close()
            win_2.close()
            core.quit()
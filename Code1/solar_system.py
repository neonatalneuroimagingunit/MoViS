# -*- coding: utf-8 -*-
"""
@script: This script presents 6 vs. 3 orbiting circles and controls for total circles area and orbit time
@author: Matteo Caffini
@date: 11-Dec-2017
@institution: CIMeC - University of Trento
@contact: matteo.caffini@unitn.it
"""

import numpy as np
from psychopy import visual, core, event, info

# Monitor parameters
monitor_width = 1920
monitor_height = 1200
monitor_frame_rate = 60 # check monitor frame rate

# Colors
background_color = [0,0,0]       # RGB triplet, limits [0,255]
foreground_color = [0,255,0] # RGB triplet, limits [0,255]

# Stimuli parameters (timing)
orbit1_time = 2 # in seconds
orbit2_time = 3 # in seconds

orbit1_time_1 = orbit1_time   # time for orbiting, in seconds
orbit1_start_1 = 0 # starting angle in degrees (zero at 3 o'clock)
orbit1_time_2 = orbit1_time   # time for orbiting, in seconds
orbit1_start_2 = 0 # starting angle in degrees (zero at 3 o'clock)
orbit1_time_3 = orbit1_time   # time for orbiting, in seconds
orbit1_start_3 = 0 # starting angle in degrees (zero at 3 o'clock)
orbit1_time_4 = orbit1_time   # time for orbiting, in seconds
orbit1_start_4 = 0 # starting angle in degrees (zero at 3 o'clock)
orbit1_time_5 = orbit1_time   # time for orbiting, in seconds
orbit1_start_5 = 0 # starting angle in degrees (zero at 3 o'clock)
orbit1_time_6 = orbit1_time   # time for orbiting, in seconds
orbit1_start_6 = 0 # starting angle in degrees (zero at 3 o'clock)

orbit2_time_1 = orbit2_time   # time for orbiting, in seconds
orbit2_start_1 = 0 # starting angle in degrees (zero at 3 o'clock)
orbit2_time_2 = orbit2_time   # time for orbiting, in seconds
orbit2_start_2 = 0 # starting angle in degrees (zero at 3 o'clock)
orbit2_time_3 = orbit2_time   # time for orbiting, in seconds
orbit2_start_3 = 0 # starting angle in degrees (zero at 3 o'clock)

# Stimuli parameters (shape)
total_area1 = 1000 # total area (px^2)
total_area2 = 1000 # total area (px^2)

# Stimuli parameters (trajectory)
p1_1 = np.array([0.1, 0.1]) # orbit size (% of monitor width, % of monitor height)
p2_1 = np.array([0.4, 0.2]) # orbit size (% of monitor width, % of monitor height)
p3_1 = np.array([0.3, 0.2]) # orbit size (% of monitor width, % of monitor height)
p4_1 = np.array([0.3, 0.3]) # orbit size (% of monitor width, % of monitor height)
p5_1 = np.array([0.4, 0.2]) # orbit size (% of monitor width, % of monitor height)
p6_1 = np.array([0.1, 0.05]) # orbit size (% of monitor width, % of monitor height)

p1_2 = np.array([0.3, 0.4]) # orbit size (% of monitor width, % of monitor height)
p2_2 = np.array([0.5, 0.7]) # orbit size (% of monitor width, % of monitor height)
p3_2 = np.array([0.7, 0.2]) # orbit size (% of monitor width, % of monitor height)

#---------- DO NOT CHANGE FROM NOW ON ----------#

# Compute stimuli areas
min_area1 = total_area1/10 # min area
max_area1 = total_area1/2 # max area
min_area2 = total_area2/10 # min area
max_area2 = total_area2/2 # max area

# get n random areas with given total area
areas1 = np.zeros(6)
for ii in np.arange(6):
    #partial_sum = radii.sum()
    areas1[ii] = np.random.randint(min_area1, max_area1)

areas1 = total_area1*areas1/areas1.sum()
#areas1.sort()
areas1 = areas1[::-1]
radii1 = np.sqrt(areas1/np.pi)
check_tot_area1 = areas1.sum()

# get n random areas with given total area
areas2 = np.zeros(3)
for ii in np.arange(3):
    #partial_sum = radii.sum()
    areas2[ii] = np.random.randint(min_area2, max_area2)

areas2 = total_area2*areas2/areas2.sum()
#areas2.sort()
areas2 = areas2[::-1]
radii2 = np.sqrt(areas2/np.pi)
check_tot_area2 = areas2.sum()

# Compute elliptical trajectory and other useful parameters
Nframes = monitor_frame_rate*orbit1_time*orbit2_time

orbit1_start_1_rad = orbit1_start_1*np.pi/180
a1_1 = monitor_width*p1_1[0]/2
b1_1 = monitor_height*p1_1[1]/2
t1_1 = np.linspace(orbit1_start_1_rad, orbit1_start_1_rad+2*np.pi*orbit2_time, Nframes)
x1_1 = a1_1*np.cos(t1_1)
y1_1 = b1_1*np.sin(t1_1)
orbit1_start_2_rad = orbit1_start_2*np.pi/180
a2_1 = monitor_width*p2_1[0]/2
b2_1 = monitor_height*p2_1[1]/2
t2_1 = np.linspace(orbit1_start_2_rad, orbit1_start_2_rad+2*np.pi*orbit2_time, Nframes)
x2_1 = a2_1*np.cos(t2_1)
y2_1 = b2_1*np.sin(t2_1)
orbit1_start_3_rad = orbit1_start_3*np.pi/180
a3_1 = monitor_width*p3_1[0]/2
b3_1 = monitor_height*p3_1[1]/2
t3_1 = np.linspace(orbit1_start_3_rad, orbit1_start_3_rad+2*np.pi*orbit2_time, Nframes)
x3_1 = a3_1*np.cos(t3_1)
y3_1 = b3_1*np.sin(t3_1)
orbit1_start_4_rad = orbit1_start_4*np.pi/180
a4_1 = monitor_width*p4_1[0]/2
b4_1 = monitor_height*p4_1[1]/2
t4_1 = np.linspace(orbit1_start_4_rad, orbit1_start_4_rad+2*np.pi*orbit2_time, Nframes)
x4_1 = a4_1*np.cos(t4_1)
y4_1 = b4_1*np.sin(t4_1)
orbit1_start_5_rad = orbit1_start_5*np.pi/180
a5_1 = monitor_width*p5_1[0]/2
b5_1 = monitor_height*p5_1[1]/2
t5_1 = np.linspace(orbit1_start_5_rad, orbit1_start_5_rad+2*np.pi*orbit2_time, Nframes)
x5_1 = a5_1*np.cos(t5_1)
y5_1 = b5_1*np.sin(t5_1)
orbit1_start_6_rad = orbit1_start_6*np.pi/180
a6_1 = monitor_width*p6_1[0]/2
b6_1 = monitor_height*p6_1[1]/2
t6_1 = np.linspace(orbit1_start_6_rad, orbit1_start_6_rad+2*np.pi*orbit2_time, Nframes)
x6_1 = a6_1*np.cos(t6_1)
y6_1 = b6_1*np.sin(t6_1)

orbit2_start_1_rad = orbit2_start_1*np.pi/180
a1_2 = monitor_width*p1_2[0]/2
b1_2 = monitor_height*p1_2[1]/2
t1_2 = np.linspace(orbit2_start_1_rad, orbit2_start_1_rad+2*np.pi*orbit1_time, Nframes)
x1_2 = a1_2*np.cos(t1_2)
y1_2 = b1_2*np.sin(t1_2)
orbit2_start_2_rad = orbit2_start_2*np.pi/180
a2_2 = monitor_width*p2_2[0]/2
b2_2 = monitor_height*p2_2[1]/2
t2_2 = np.linspace(orbit2_start_2_rad, orbit2_start_2_rad+2*np.pi*orbit1_time, Nframes)
x2_2 = a2_2*np.cos(t2_2)
y2_2 = b2_2*np.sin(t2_2)
orbit2_start_3_rad = orbit2_start_3*np.pi/180
a3_2 = monitor_width*p3_2[0]/2
b3_2 = monitor_height*p3_2[1]/2
t3_2 = np.linspace(orbit2_start_3_rad, orbit2_start_3_rad+2*np.pi*orbit1_time, Nframes)
x3_2 = a3_2*np.cos(t3_2)
y3_2 = b3_2*np.sin(t3_2)

# Create windows
win_1 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=0, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=background_color)
win_2 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=1, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=background_color)

keys = event.BuilderKeyResponse()

# Create shapes
dot1_1= visual.Circle(win=win_1, name='dot1', units='pix',
    radius=radii1[0], edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=foreground_color, lineColorSpace='rgb255',
    fillColor=foreground_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True)

dot2_1 = visual.Circle(win=win_1, name='dot1', units='pix',
    radius=radii1[1], edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=foreground_color, lineColorSpace='rgb255',
    fillColor=foreground_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True)
    
dot3_1 = visual.Circle(win=win_1, name='dot1', units='pix',
    radius=radii1[2], edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=foreground_color, lineColorSpace='rgb255',
    fillColor=foreground_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True)

dot4_1 = visual.Circle(win=win_1, name='dot1', units='pix',
    radius=radii1[3], edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=foreground_color, lineColorSpace='rgb255',
    fillColor=foreground_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True)

dot5_1 = visual.Circle(win=win_1, name='dot1', units='pix',
    radius=radii1[4], edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=foreground_color, lineColorSpace='rgb255',
    fillColor=foreground_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True)

dot6_1 = visual.Circle(win=win_1, name='dot1', units='pix',
    radius=radii1[5], edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=foreground_color, lineColorSpace='rgb255',
    fillColor=foreground_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True)

dot1_2 = visual.Circle(win=win_2, name='dot2', units='pix',
    radius=radii2[0], edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=foreground_color, lineColorSpace='rgb255',
    fillColor=foreground_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True)

dot2_2 = visual.Circle(win=win_2, name='dot2', units='pix',
    radius=radii2[1], edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=foreground_color, lineColorSpace='rgb255',
    fillColor=foreground_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True)

dot3_2 = visual.Circle(win=win_2, name='dot2', units='pix',
    radius=radii2[2], edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor=foreground_color, lineColorSpace='rgb255',
    fillColor=foreground_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True)

while True:
    # Animate one way...
    for frameN in range(0, Nframes, 1):
        dot1_1.pos = (x1_1[frameN], y1_1[frameN])
        dot2_1.pos = (x2_1[frameN], y2_1[frameN])
        dot3_1.pos = (x3_1[frameN], y3_1[frameN])
        dot4_1.pos = (x4_1[frameN], y4_1[frameN])
        dot5_1.pos = (x5_1[frameN], y5_1[frameN])
        dot6_1.pos = (x6_1[frameN], y6_1[frameN])
        
        dot1_2.pos = (x1_2[frameN], y1_2[frameN])
        dot2_2.pos = (x2_2[frameN], y2_2[frameN])
        dot3_2.pos = (x3_2[frameN], y3_2[frameN])
        
        # Monitor 1
        dot1_1.draw()
        dot2_1.draw()
        dot3_1.draw()
        dot4_1.draw()
        dot5_1.draw()
        dot6_1.draw()
        
        # Monitor 2
        dot1_2.draw()
        dot2_2.draw()
        dot3_2.draw()
        
        win_1.flip()
        win_2.flip()
        
        if event.getKeys(keyList=["escape"]):
            win_1.close()
            win_2.close()
            core.quit()
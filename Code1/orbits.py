# This script presents a number of orbiting circles and controls for total area and number of circles
# written by Matteo Caffini
# 11-Dec-2017
# contact: matteo.caffini@unitn.it

import numpy as np
from psychopy import visual, core, event, info
import random

# Monitor parameters
monitor_width = 1920
monitor_height = 1080
monitor_frame_rate = 60 # check monitor frame rate

# Colors
background_color = [255,255,0] # RGB triplet, limits [0,255]

# Stimulus parameters (timing)
orbit_time = 5 # time for orbiting, in seconds

p1 = np.array([0.5, 0.4, 0.8]) # orbit width (% of monitor width)
p2 = np.array([0.5, 0.4, 0.8])   # orbit height (% of monitor height)

#---------- DO NOT CHANGE FROM NOW ON ----------#

# Compute elliptical trajectory and other useful parameters
Nframes = monitor_frame_rate*orbit_time
#a = monitor_width*p1/2
#b = monitor_height*p2/2
#t = np.linspace(0, 2*np.pi, Nframes)
#x = np.zeros([3,Nframes]);
#y = np.zeros([3,Nframes]);
#for i in range(a.shape[0]):
#    x[i,:] = a[i]*np.cos(t)
#    y[i,:] = b[i]*np.sin(t)

n_dots = 3
dot_xys = []
dot_xys_frames = []

for n in range(Nframes):
    for dot in range(n_dots):
    
        dot_x = random.uniform(-200, 200)
        dot_y = random.uniform(-200, 200)
    
        dot_xys.append([dot_x, dot_y])
    dot_xys_frames.append(dot_xys)

# Create windows
win_1 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=0, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=background_color)

keys = event.BuilderKeyResponse()

# Create shapes

dots = visual.ElementArrayStim(win=win_1, nElements=3)

while True:
    # Animate one way...
    for frameN in range(0, Nframes, 1):
        dots.xys = dot_xys_frames[frameN]
        dots.draw()
        win_1.flip()
        if event.getKeys(keyList=["escape"]):
            win_1.close()
            core.quit()
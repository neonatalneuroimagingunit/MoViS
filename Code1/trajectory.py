# written by Matteo Caffini
# CIMeC University of Trento
# 11-Feb-2018
# Contact: matteo.caffini@unitn.it

from psychopy import visual, core, event, info, gui
import numpy as np

# Monitor parameters
monitor_width = 1920
monitor_height = 1200
monitor_frame_rate = 60 # crucial!
monitor_dpi = 102.46
background_color = [255,255,255]

# Ball parameters
ball_color = [0,0,0]
ball_size = 0.2 # radius in cm

# Trajectory parameters
width_scaling_factor = 1
height_scaling_factor = 1
#height_scaling_factor = width_scaling_factor*(monitor_width/monitor_height)  # uncomment this for squared trajectory
fps = 1

###########################################################################################
#                                                                                         #
###########################################################################################
# This sets the ball size
inch2cm = 2.54
ball_size = ball_size/inch2cm*monitor_dpi

# This calculates the trajectory (Lissajous curve)
steps = 200     # quantization of curve
t = np.linspace(0, 2*np.pi, steps);
x = np.cos(3*t) * width_scaling_factor*monitor_width/2;
y = np.sin(2*t) * height_scaling_factor*monitor_height/2;

# This enables the use of the keyboard during the stimuli presentation
keys = event.BuilderKeyResponse()

# This creates the windows where you draw your stimuli
window_1 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=0, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=background_color)

# This creates a shape with specific features (color, dimensions, ...)
ball = visual.Circle(win=window_1,
    units='pix',
    edges=100,
    ori=0,
    pos=(0,0),
    radius = ball_size,
    lineWidth=1,
    lineColorSpace='rgb255',
    fillColorSpace='rgb255',
    lineColor= ball_color,
    fillColor= ball_color,
    opacity=1,
    interpolate=True,
    autoDraw = True)
    

while True:
    for i in range(x.shape[0]):
        ball.pos = (x[i],y[i])
        ball.draw()
        window_1.flip()
        core.wait(1/fps)
        if event.getKeys(keyList=["escape"]):
            window_1.close()
            core.quit()
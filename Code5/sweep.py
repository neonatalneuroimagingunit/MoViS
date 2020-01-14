# written by Matteo Caffini
# 11-Apr-2017
# contact: matteo.caffini@unitn.it

from psychopy import visual, core, event, info
import numpy as np

# Monitor parameters
monitor_width = 1980
monitor_height = 1200
monitor_frame_rate = 60 # crucial!

# Stimulus parameters (time)
crossing_time = 5 # time for crossing, one-way, in seconds
Nframes = monitor_frame_rate*crossing_time

# Stimulus parameters (initial and final position)
initial_x = -monitor_width/2
initial_y = -monitor_height/2
final_x = monitor_width/2
final_y = monitor_height/2

# Stimulus parameters (delta x and delta y)
increment_x = monitor_width/Nframes
increment_y = monitor_height/Nframes

# This enables the use of the keyboard during the stimuli presentation
keys = event.BuilderKeyResponse()

# This creates the windows where you draw your stimuli
window_1 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=0, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=[0,0,0])

# This creates a shape with specific features (color, dimensions, ...)
ball = visual.Circle(win=window_1, name='ball', units='pix',
    radius=50, edges=32,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor='blue', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = True)

# Compute the xy coordinates for the position of the center of mass of the shape
xnew = np.linspace(initial_x, final_x, Nframes)
ynew = np.linspace(initial_y, final_y, Nframes)

# This loops over the frames (and this is the reason why using the true frame rate is crucial) and draws the shape in the correct position
while True: # use this to go on forever and be doomed for eternity
#for aa in range(N_repetitions)  # use this and substitute N_repetitions with the desired number
    # Animate one way...
    for frameN in range(0, Nframes, 1):
        ball.pos = (xnew[frameN], ynew[frameN])
        ball.draw()
        window_1.flip()
        if event.getKeys(keyList=["escape"]):
            window_1.close()
            core.quit()
    # ...and the way back
    for frameN in range(Nframes-1, 0, -1):
        ball.pos = (xnew[frameN], ynew[frameN])
        ball.draw()
        window_1.flip()
        if event.getKeys(keyList=["escape"]):
            window_1.close()

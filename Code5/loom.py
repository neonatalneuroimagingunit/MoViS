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
looming_time = 5 # time for looming, (one-way, in seconds)
Nframes = monitor_frame_rate*looming_time

# Stimulus parameters (initial and final radii)
initial_radius = 50
final_radius = 500

# This enables the use of the keyboard during the stimuli presentation
keys = event.BuilderKeyResponse()

# This creates the windows where you draw your stimuli
window_1 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=0, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=[0,0,0])

# This creates a shape with specific features (color, dimensions, ...)
ball = visual.Circle(win=window_1, name='ball', units='pix',
    radius=50, edges=100,
    ori=0, pos=(0,0),
    lineWidth=1, lineColor='blue', lineColorSpace='rgb255',
    fillColor='red', fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = True)

# Compute the radii
radius_new = np.linspace(initial_radius, final_radius, Nframes)

# This loops over the frames (and this is the reason why using the true frame rate is crucial) and draws the shape with the correct radius
while True: # use this to go on forever and be doomed for eternity
#for aa in range(N_repetitions)  # use this and substitute N_repetitions with the desired number
    # Animate one way...
    for frameN in range(0, Nframes, 1):
        ball.radius = radius_new[frameN]
        ball.draw()
        window_1.flip()
        if event.getKeys(keyList=["escape"]):
            window_1.close()
            core.quit()
    core.wait(2) # use this if you want your stimulus to stay unchanged for 2 seconds
    
    # use those 4 lines if you want a black screen
    ball.radius = 0
    ball.draw()
    window_1.flip()
    core.wait(2) # 2 seconds long black screen
    
    # ...and the way back
    for frameN in range(Nframes-1, 0, -1):
        ball.radius = radius_new[frameN]
        ball.draw()
        window_1.flip()
        if event.getKeys(keyList=["escape"]):
            window_1.close()
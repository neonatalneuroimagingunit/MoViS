# written by Matteo Caffini
# 12-Jul-2018
# contact: matteo.caffini@unitn.it

from psychopy import visual, core, event, info
import numpy as np

# Monitor parameters
monitor_width = 1920
monitor_height = 1200
monitor_frame_rate = 60 # crucial for timing!
monitor_dpi = 96        # crucial for size!

# Stimulus parameters
initial_size = 2 # initial size in cm
final_size = 10  # final size in cm
looming_time = 2 # time for looming, (one-way, in seconds) 
total_duration = 10 # in minutes, will be then rounded to the closest multiple of stimulus+ISI+stimulus+ISI
shape_color_1 = 'grey'
shape_color_2 = 'red'
background_color_1 = 'black'
background_color_2 = 'black'

# Compute derived parameters
Nframes = monitor_frame_rate*looming_time
initial_size_px = initial_size*monitor_dpi/2.54
final_size_px = final_size*monitor_dpi/2.54
size_new = np.linspace(initial_size_px, final_size_px, Nframes)

# This creates the sequence of shapes
Npairs = np.int(np.round(total_duration*60/4))
temp_sequence_1 = np.random.randint(1,4,Npairs)
sequence_1_1 = np.zeros(Npairs, dtype=int)
sequence_1_2 = np.zeros(Npairs, dtype=int)
temp_sequence_2 = np.random.randint(1,7,10*Npairs)

selection = np.ones(len(temp_sequence_2), dtype=bool)
selection[1:] = temp_sequence_2[1:] != temp_sequence_2[:-1]
temp_sequence_2 = temp_sequence_2[selection]
temp_sequence_2 = temp_sequence_2[:2*Npairs]

sequence_2_1 = temp_sequence_2[0::2]
sequence_2_2 = temp_sequence_2[1::2]

for i in np.arange(Npairs):
    if temp_sequence_1[i] == 1:
        sequence_1_1[i] = 1
        sequence_1_2[i] = 2
    elif temp_sequence_1[i] == 2:
        sequence_1_1[i] = 3
        sequence_1_2[i] = 4
    elif temp_sequence_1[i] == 3:
        sequence_1_1[i] = 5
        sequence_1_2[i] = 6

# This enables the use of the keyboard during the stimuli presentation
keys = event.BuilderKeyResponse()

# This creates the windows where you draw your stimuli
window_1 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=0, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=background_color_1)
window_2 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=1, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=background_color_2)

# This creates the coordinates for the X shape
x = np.array([1,2,2,1, 2, 2, 1, 0,-1,-2,-2,-1,-2,-2,-1,0])
y = np.array([2,2,1,0,-1,-2,-2,-1,-2,-2,-1,0,1,2,2,1])
xshape_vertices = np.stack((x, y), axis=1)/4

# This creates the coordinates for the T shape
x = np.array([2,2,0.5,0.5,-0.5,-0.5,-2,-2])
y = np.array([2,1,1,-2,-2,1,1,2])
tshape_vertices = np.stack((x, y), axis=1)/4

# This creates the coordinates for the papillon
x = np.array([2,2,0,-2,-2,0])
y = np.array([2,-2,-1,-2,2,1])
papillon_vertices = np.stack((x, y), axis=1)/4

# This creates the shapes with specific features (color, dimensions, ...)
square = visual.Polygon(win=window_1, name='square', units='pix',
    edges=4,
    ori=45, pos=(0,0), size=initial_size_px,
    lineWidth=1, lineColorSpace='rgb255', fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

xshape = visual.ShapeStim(win=window_1, name='xshape', units='pix',
    vertices=xshape_vertices,
    ori=0, pos=(0,0), size=initial_size_px,
    lineWidth=1, lineColorSpace='rgb255', fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

ball = visual.Circle(win=window_1, name='ball', units='pix',
    edges=100,
    ori=0, pos=(0,0), size=initial_size_px, 
    lineWidth=1, lineColorSpace='rgb255', fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

triangle = visual.Polygon(win=window_1, name='triangle', units='pix',
    edges=3,
    ori=0, pos=(0,0), size=initial_size_px,
    lineWidth=1, lineColorSpace='rgb255', fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

tshape = visual.ShapeStim(win=window_1, name='tshape', units='pix',
    vertices=tshape_vertices,
    ori=0, pos=(0,0), size=initial_size_px,
    lineWidth=1, lineColorSpace='rgb255', fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)
    
papillon = visual.ShapeStim(win=window_1, name='papillon', units='pix',
    vertices=papillon_vertices,
    ori=0, pos=(0,0), size=initial_size_px,
    lineWidth=1,lineColorSpace='rgb255', fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

for aa in range(Npairs):
    
    for frameN in range(0, Nframes, 1):
        # Display 1
        if sequence_1_1[aa] == 1:
            square.win = window_1
            square.lineColor = shape_color_1
            square.fillColor = shape_color_1
            square.size = size_new[frameN]
            square.draw()
            window_1.flip()
        if sequence_1_1[aa] == 2:
            xshape.win = window_1
            xshape.lineColor = shape_color_1
            xshape.fillColor = shape_color_1
            xshape.size = size_new[frameN]
            xshape.draw()
            window_1.flip()
        if sequence_1_1[aa] == 3:
            ball.win = window_1
            ball.lineColor = shape_color_1
            ball.fillColor = shape_color_1
            ball.size = size_new[frameN]
            ball.draw()
            window_1.flip()
        if sequence_1_1[aa] == 4:
            triangle.win = window_1
            triangle.lineColor = shape_color_1
            triangle.fillColor = shape_color_1
            triangle.size = size_new[frameN]
            triangle.draw()
            window_1.flip()
        if sequence_1_1[aa] == 5:
            tshape.win = window_1
            tshape.lineColor = shape_color_1
            tshape.fillColor = shape_color_1
            tshape.size = size_new[frameN]
            tshape.draw()
            window_1.flip()
        if sequence_1_1[aa] == 6:
            papillon.win = window_1
            papillon.lineColor = shape_color_1
            papillon.fillColor = shape_color_1
            papillon.size = size_new[frameN]
            papillon.draw()
            window_1.flip()
        # Display 2
        if sequence_2_1[aa] == 1:
            square.win = window_2
            square.lineColor = shape_color_2
            square.fillColor = shape_color_2
            square.size = size_new[frameN]
            square.draw()
            window_2.flip()
        if sequence_2_1[aa] == 2:
            xshape.win = window_2
            xshape.lineColor = shape_color_2
            xshape.fillColor = shape_color_2
            xshape.size = size_new[frameN]
            xshape.draw()
            window_2.flip()
        if sequence_2_1[aa] == 3:
            ball.win = window_2
            ball.lineColor = shape_color_2
            ball.fillColor = shape_color_2
            ball.size = size_new[frameN]
            ball.draw()
            window_2.flip()
        if sequence_2_1[aa] == 4:
            triangle.win = window_2
            triangle.lineColor = shape_color_2
            triangle.fillColor = shape_color_2
            triangle.size = size_new[frameN]
            triangle.draw()
            window_2.flip()
        if sequence_2_1[aa] == 5:
            tshape.win = window_2
            tshape.lineColor = shape_color_2
            tshape.fillColor = shape_color_2
            tshape.size = size_new[frameN]
            tshape.draw()
            window_2.flip()
        if sequence_2_1[aa] == 6:
            papillon.win = window_2
            papillon.lineColor = shape_color_2
            papillon.fillColor = shape_color_2
            papillon.size = size_new[frameN]
            papillon.draw()
            window_2.flip()
        if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()

    for frameN in range(0, Nframes, 1):
        # Display 1
        if sequence_1_2[aa] == 1:
            square.win = window_1
            square.lineColor = shape_color_1
            square.fillColor = shape_color_1
            square.size = size_new[frameN]
            square.draw()
            window_1.flip()
        if sequence_1_2[aa] == 2:
            xshape.win = window_1
            xshape.lineColor = shape_color_1
            xshape.fillColor = shape_color_1
            xshape.size = size_new[frameN]
            xshape.draw()
            window_1.flip()
        if sequence_1_2[aa] == 3:
            ball.win = window_1
            ball.lineColor = shape_color_1
            ball.fillColor = shape_color_1
            ball.size = size_new[frameN]
            ball.draw()
            window_1.flip()
        if sequence_1_2[aa] == 4:
            triangle.win = window_1
            triangle.lineColor = shape_color_1
            triangle.fillColor = shape_color_1
            triangle.size = size_new[frameN]
            triangle.draw()
            window_1.flip()
        if sequence_1_2[aa] == 5:
            tshape.win = window_1
            tshape.lineColor = shape_color_1
            tshape.fillColor = shape_color_1
            tshape.size = size_new[frameN]
            tshape.draw()
            window_1.flip()
        if sequence_1_2[aa] == 6:
            papillon.win = window_1
            papillon.lineColor = shape_color_1
            papillon.fillColor = shape_color_1
            papillon.size = size_new[frameN]
            papillon.draw()
            window_1.flip()
        # Display 2
        if sequence_2_2[aa] == 1:
            square.win = window_2
            square.lineColor = shape_color_2
            square.fillColor = shape_color_2
            square.size = size_new[frameN]
            square.draw()
            window_2.flip()
        if sequence_2_2[aa] == 2:
            xshape.win = window_2
            xshape.lineColor = shape_color_2
            xshape.fillColor = shape_color_2
            xshape.size = size_new[frameN]
            xshape.draw()
            window_2.flip()
        if sequence_2_2[aa] == 3:
            ball.win = window_2
            ball.lineColor = shape_color_2
            ball.fillColor = shape_color_2
            ball.size = size_new[frameN]
            ball.draw()
            window_2.flip()
        if sequence_2_2[aa] == 4:
            triangle.win = window_2
            triangle.lineColor = shape_color_2
            triangle.fillColor = shape_color_2
            triangle.size = size_new[frameN]
            triangle.draw()
            window_2.flip()
        if sequence_2_2[aa] == 5:
            tshape.win = window_2
            tshape.lineColor = shape_color_2
            tshape.fillColor = shape_color_2
            tshape.size = size_new[frameN]
            tshape.draw()
            window_2.flip()
        if sequence_2_2[aa] == 6:
            papillon.win = window_2
            papillon.lineColor = shape_color_2
            papillon.fillColor = shape_color_2
            papillon.size = size_new[frameN]
            papillon.draw()
            window_2.flip()
        if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()
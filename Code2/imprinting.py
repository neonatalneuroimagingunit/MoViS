# written by Matteo Caffini
# 18-Jun-2018
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
shape_color = 'red'
background_color = 'black'

# Compute derived parameters
Nframes = monitor_frame_rate*looming_time
initial_size_px = initial_size*monitor_dpi/2.54
final_size_px = final_size*monitor_dpi/2.54
size_new = np.linspace(initial_size_px, final_size_px, Nframes)

# This creates the sequence of shapes
Npairs = np.int(np.round(total_duration*60/4))
sequence = np.random.randint(1,4,Npairs)

# This enables the use of the keyboard during the stimuli presentation
keys = event.BuilderKeyResponse()

# This creates the windows where you draw your stimuli
window_1 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=0, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=background_color)
window_2 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=1, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=background_color)

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
    lineWidth=1, lineColor=shape_color, lineColorSpace='rgb255',
    fillColor=shape_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

xshape = visual.ShapeStim(win=window_1, name='xshape', units='pix',
    vertices=xshape_vertices,
    ori=0, pos=(0,0), size=initial_size_px,
    lineWidth=1, lineColor=shape_color, lineColorSpace='rgb255',
    fillColor=shape_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

ball = visual.Circle(win=window_1, name='ball', units='pix',
    edges=100,
    ori=0, pos=(0,0), size=initial_size_px, 
    lineWidth=1, lineColor=shape_color, lineColorSpace='rgb255',
    fillColor=shape_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

triangle = visual.Polygon(win=window_1, name='triangle', units='pix',
    edges=3,
    ori=0, pos=(0,0), size=initial_size_px,
    lineWidth=1, lineColor=shape_color, lineColorSpace='rgb255',
    fillColor=shape_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

tshape = visual.ShapeStim(win=window_1, name='tshape', units='pix',
    vertices=tshape_vertices,
    ori=0, pos=(0,0), size=initial_size_px,
    lineWidth=1, lineColor=shape_color, lineColorSpace='rgb255',
    fillColor=shape_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)
    
papillon = visual.ShapeStim(win=window_1, name='papillon', units='pix',
    vertices=papillon_vertices,
    ori=0, pos=(0,0), size=initial_size_px,
    lineWidth=1, lineColor=shape_color, lineColorSpace='rgb255',
    fillColor=shape_color, fillColorSpace='rgb255',
    opacity=1,interpolate=True, autoDraw = False)

for aa in range(Npairs):
    if sequence[aa] == 1:
        for frameN in range(0, Nframes, 1):
            # Display 1
            square.win = window_1
            square.size = size_new[frameN]
            square.draw()
            window_1.flip()
            # Display 2
            square.win = window_2
            square.size = size_new[frameN]
            square.draw()
            window_2.flip()
            if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()
        for frameN in range(0, Nframes, 1):
            # Display 1
            xshape.win = window_1
            xshape.size = size_new[frameN]
            xshape.draw()
            window_1.flip()
            # Display 2
            xshape.win = window_2
            xshape.size = size_new[frameN]
            xshape.draw()
            window_2.flip()
            if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()
    
    elif sequence[aa] == 2:
        for frameN in range(0, Nframes, 1):
            # Display 1
            ball.win = window_1
            ball.size = size_new[frameN]
            ball.draw()
            window_1.flip()
            # Display 2
            ball.win = window_2
            ball.size = size_new[frameN]
            ball.draw()
            window_2.flip()
            if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()
        for frameN in range(0, Nframes, 1):
            # Display 1
            triangle.win = window_1
            triangle.size = size_new[frameN]
            triangle.draw()
            window_1.flip()
            # Display 2
            triangle.win = window_2
            triangle.size = size_new[frameN]
            triangle.draw()
            window_2.flip()
            if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()
    
    elif sequence[aa] == 3:
        for frameN in range(0, Nframes, 1):
            # Display 1
            tshape.win = window_1
            tshape.size = size_new[frameN]
            tshape.draw()
            window_1.flip()
            # Display 2
            tshape.win = window_2
            tshape.size = size_new[frameN]
            tshape.draw()
            window_2.flip()
            if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()
        for frameN in range(0, Nframes, 1):
            # Display 1
            papillon.win = window_1
            papillon.size = size_new[frameN]
            papillon.draw()
            window_1.flip()
            # Display 2
            papillon.win = window_2
            papillon.size = size_new[frameN]
            papillon.draw()
            window_2.flip()
            if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()
    
    else:
        window_1.close()
        core.quit()
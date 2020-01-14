# written by Matteo Caffini and Maria Bortot
# 06-Dec-2018
# contact: matteo.caffini@unitn.it

from psychopy import visual, core, event, info, gui
import time as pagno
import numpy as np

# Monitor parameters
monitor_width = 1920
monitor_height = 1200
monitor_frame_rate = 60 # crucial!
monitor_dpi = 102.46
background_color = [0,255,0]
line_color = [0,0,0]    # line color --> if you put line color = background color then you obtain dots without the external line (do not change the script above!)
shape_color = [[255,0,0],[0,0,255]]

# Shapes parameters (radius in cm)
shape_size = 2 # shape radius in cm
#maxdim = 4
#mindim = 2
#granularity = 1 # set unit of measurement (1 is 1 cm, 2 is 0.5 cm, 3 is 0.333.... cm, etc etc)

# Microtime parameters
T1 = 200       # in ms
T2 = 300       # in ms
T3 = 400       # in ms
T4 = 1000      # in ms (should be larger than T1+T2+T3 to avoid time overlaps of groups)
timefactor = 1 # adimensional

# Choose Trial
TRIALNUMBER = 0 # use subsequent values ( increment by 1, if not->print(PD) )

# Arrangement paramenters
nx = 4 # colonne
ny = 2 # righe
nSelected = 2 # nSelected should be less then (2/3*(nx*ny)) / nGroups -> happy xmas


###########################################################################################
#                                                                                         #
###########################################################################################
# This creates the message box to get how many rows and columns
#gui = gui.Dlg()
#gui.addField("Rows:")
#gui.addField("Columns:")
#gui.show()
#ny = gui.data[0]
#nx = gui.data[1]
#nx = np.fromstring(nx, dtype=int, sep=' ')
#ny = np.fromstring(ny, dtype=int, sep=' ')
#nx = nx[0]
#ny = ny[0]
np.random.seed(1)
nPoints = nx*ny; #must be even!
nGroup = len(shape_color)
nSeq = 1000

if nSelected == 0:
    print(0)
    # put here the case for nSelected = 0 (no groups, special case)
elif nSelected < np.floor((nx*ny)/2):
    # Set timing
    T = T1 + T2 + T3 + T4
    I = T * timefactor
    
    # Time to frames
    N1 = T1*monitor_frame_rate
    N2 = T2*monitor_frame_rate
    N3 = T3*monitor_frame_rate
    N4 = T4*monitor_frame_rate

    N1 = np.int(np.round(N1/1000))
    N2 = np.int(np.round(N2/1000))
    N3 = np.int(np.round(N3/1000))
    N4 = np.int(np.round(N4/1000))
    Nt = N1 + N2 + N3 + N4
    Ni = np.int(np.round(Nt*timefactor))
    
    # Set shapes dimensions
    inch2cm = 2.54
    #dims = np.random.randint(granularity*mindim, granularity*maxdim+1, size=nPoints)/granularity
    #dims = dims/inch2cm*monitor_dpi
    shape_size = shape_size/inch2cm*monitor_dpi
    dims = shape_size*np.ones(nPoints, dtype=int)
    dims2 = np.tile(dims, (Nt,1))
    
    # Set centers coordinates
    y = np.linspace(-monitor_height/2, monitor_height/2, 2*ny+1)
    y = y[1:-1:2]
    x = np.linspace(-monitor_width/2, monitor_width/2, 2*nx+1)
    x = x[1:-1:2]
    xv, yv = np.meshgrid(x, y)
    xv = xv.flatten()
    yv = yv.flatten()
    coord = np.stack((xv,yv), axis=1)
    
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
        lineWidth=2,
        lineColorSpace='rgb255',
        fillColorSpace='rgb255',
        lineColor= line_color,
        fillColor= background_color,
        opacity=1,
        interpolate=True,
        autoDraw = True)
    
    # This creates the sequence
    sequence = np.zeros((nPoints,nSeq+10), dtype=bool)
    sequence[np.random.choice(np.arange(nPoints), nSelected*nGroup, replace=False),0] = True
    spam = np.arange(nPoints)
    egg = np.int(np.floor(nSelected*nGroup/2))
    bacon = np.where(sequence[:,0])[0][0:egg] # bacon is not the new sacchetto
    sacchetto = np.setdiff1d(spam, bacon)
    sequence[np.random.choice(sacchetto, nSelected*nGroup, replace=False),1] = True

    for ii in range(2,nSeq+10):
        sacchetto = np.where(np.logical_not(np.logical_and(sequence[:,ii-1],sequence[:,ii-2])))[0]
        sequence[np.random.choice(sacchetto, nSelected*nGroup, replace=False),ii] = True
    sequence = sequence[:,9:] # -> happy birthday
    
    # Set groups
    np.random.seed(seed=None)
    A = np.random.choice(np.where(sequence[:,TRIALNUMBER])[0], nSelected, replace=False)
    B = np.setdiff1d(np.where(sequence[:,TRIALNUMBER])[0], A)
    C = np.setdiff1d(np.arange(nPoints), np.concatenate((A,B)))
    
    while True:
        # Create color boxes
        mycolors = np.tile(background_color, (nPoints,1))
        mycolors = np.dstack([mycolors]*Nt)
          
        mycolors[A, :, 0:N1] = np.dstack([np.tile(shape_color[0], (nSelected,1))]*N1)
        mycolors[A, :, N1:N1+N2] = np.dstack([np.tile(background_color, (nSelected,1))]*N2)
        mycolors[A, :, N1+N2:N1+N2+N3] = np.dstack([np.tile(shape_color[1], (nSelected,1))]*N3)
        mycolors[A, :, N1+N2+N3:N1+N2+N3+N4] = np.dstack([np.tile(background_color, (nSelected,1))]*N4)
        
        mycolors[B, :, 0:N4] = np.dstack([np.tile(background_color, (nSelected,1))]*N4)
        mycolors[B, :, N4:N4+N3] = np.dstack([np.tile(shape_color[1], (nSelected,1))]*N3)
        mycolors[B, :, N4+N3:N4+N3+N2] = np.dstack([np.tile(background_color, (nSelected,1))]*N2)
        mycolors[B, :, N4+N3+N2:N4+N3+N2+N1] = np.dstack([np.tile(shape_color[0], (nSelected,1))]*N1)
        
        mycolors[C, :, :] = np.dstack([np.tile(background_color, (nPoints-2*nSelected,1))]*Nt)
        
        pagnopagno = pagno.time()
        # This plot the shapes
        for n in range(Nt):
            pagnopagno = pagno.time()
            for pp in range(nPoints):
                ball.pos = coord[pp,:]
                ball.radius = dims2[n,pp]
                #ball.setLineColor(mycolors[pp,:,n].tolist())  #uncomment this to have dots whitout external coloured line
                #ball.setFillColor(dummy_color)                #uncomment this to have dots whitout external coloured line
                ball.setFillColor(mycolors[pp,:,n].tolist()) 
                ball.draw()
            print(str(np.int(np.round(1000*(pagno.time()-pagnopagno))))+' ms ('+str(np.int(np.round(1000*1/monitor_frame_rate)))+' ms)')
            window_1.flip()
            #core.wait(2)
            if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()
        for n in range(Ni):
            for pp in range(nPoints):
                ball.pos = coord[pp,:]
                ball.radius = dims2[n,pp]
                #ball.setLineColor(mycolors[pp,:,n].tolist())  #uncomment this to have dots without external coloured line
                #ball.setFillColor(mycolors[pp,:,n].tolist())  #uncomment this to have dots without external coloured line
                ball.setFillColor(background_color)
                ball.draw()
            window_1.flip()
            #core.wait(2)
            if event.getKeys(keyList=["escape"]):
                window_1.close()
                core.quit()
else:
    print('nSelected should be less then half of nx*ny (zero is ok)')
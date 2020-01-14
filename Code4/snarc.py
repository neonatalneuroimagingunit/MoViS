from psychopy import visual, core, event, info, gui
import numpy as np
import serial

# Serial port
#trigger = serial.Serial('COM3', 9600, timeout=0)

# Monitor parameters
monitor_width = 1920
monitor_height = 1200
monitor_frame_rate = 60 # crucial for timing!
monitor_dpi = 96        # crucial for size!

# Stimulus parameters
habituation_total_duration = 10  # in seconds
habituation_image_duration = 0.5 # in seconds
habituation_isi = 0.2            # in seconds
test_total_duration = 10        # in seconds
test_image_duration =  1        # in seconds
test_isi = 1                    # in seconds
background_color = 'grey'
path_to_images = 'G:\My Drive\Lara\SNARC'
#path_to_logfile = 'G:\My Drive\Lara\SNARC\test\test.txt'

# This creates the message box to get measure ID
gui = gui.Dlg()
gui.addField("Subject ID:")
gui.show()

# This creates the windows where you draw your stimuli
window_1 = visual.Window(size=(monitor_width, monitor_height), fullscr=True, screen=0, allowGUI=False, units='pix',
monitor='testMonitor', colorSpace='rgb255', color=background_color)

# Create images
squares_12_1 = visual.ImageStim(window_1, image=path_to_images+'\squares_12_1.png', mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), 
    colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, 
    name=None, autoLog=None, maskParams=None)
squares_12_2 = visual.ImageStim(window_1, image=path_to_images+'\squares_12_2.png', mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), 
    colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, 
    name=None, autoLog=None, maskParams=None)
squares_12_3 = visual.ImageStim(window_1, image=path_to_images+'\squares_12_3.png', mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), 
    colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, 
    name=None, autoLog=None, maskParams=None)
squares_12_4 = visual.ImageStim(window_1, image=path_to_images+'\squares_12_4.png', mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), 
    colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, 
    name=None, autoLog=None, maskParams=None)
squares_12_5 = visual.ImageStim(window_1, image=path_to_images+'\squares_12_5.png', mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), 
    colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, 
    name=None, autoLog=None, maskParams=None)

squares_4 = visual.ImageStim(window_1, image=path_to_images+'\squares_4_1.png', mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), 
    colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, 
    name=None, autoLog=None, maskParams=None)
squares_36 = visual.ImageStim(window_1, image=path_to_images+'\squares_36_1.png', mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0), 
    colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False, flipVert=False, texRes=128, 
    name=None, autoLog=None, maskParams=None)


instructions = visual.TextStim(win=window_1, wrapWidth=1000, height=40)
instructions.text = """Premi un tasto per iniziare l'abituazione\n"""

counter = visual.TextStim(win=window_1, wrapWidth=30, pos=(-monitor_width/2+40, -monitor_height/2+20), height=20)
counter.text = """-"""

# Compute derived parameters
subj_id = gui.data[0]
clock = core.Clock()
responses = []

# Introduction
instructions.draw()
window_1.flip()
event.waitKeys()
window_1.flip()

# Habituation
tmp = clock.getTime()
space_status = 0
display_time = 0
habituation_elapsed_time = 0
while habituation_elapsed_time < habituation_total_duration:
    which_image = np.random.choice(np.array([1,2,3,4,5]),1)
    if space_status == 1:
        if which_image == 1:
            squares_12_1.draw()
        elif which_image == 2:
            squares_12_2.draw()
        elif which_image == 3:
            squares_12_3.draw()
        elif which_image == 4:
            squares_12_4.draw()
        elif which_image == 5:
            squares_12_5.draw()
        counter.text = str(np.round(100*display_time)/100)
        counter.draw()
        window_1.flip()
        core.wait(habituation_image_duration)
        window_1.flip()
        core.wait(habituation_isi)
        display_time += (habituation_image_duration+habituation_isi);
    else:
        if which_image == 1:
            squares_12_1.draw()
        elif which_image == 2:
            squares_12_2.draw()
        elif which_image == 3:
            squares_12_3.draw()
        elif which_image == 4:
            squares_12_4.draw()
        elif which_image == 5:
            squares_12_5.draw()
        counter.text = str(np.round(100*display_time)/100)
        counter.draw()
        window_1.flip()
        core.wait(habituation_image_duration)
        window_1.flip()
        core.wait(habituation_isi)

    keys = event.getKeys(keyList=['space', 'escape'], timeStamped=clock)

    for key in keys:
        if key[0] == 'escape':
            window_1.close()
            #trigger.close()
            core.quit()
        elif key[0] == 'space':
            if space_status == 1:
                elapsed_time = clock.getTime()- time
                habituation_elapsed_time += elapsed_time
                space_status = 0
            else:
                time = clock.getTime()
                space_status = 1

print(subj_id, habituation_elapsed_time)

# Test
tmp = clock.getTime()
display_time = 0
test_elapsed_time = 0
while test_elapsed_time < test_total_duration:
    squares_4.draw()
    #trigger.write(b's') # writes the ascii code of s (smaller) on the serial port
    counter.text = str(np.round(100*display_time)/100)
    counter.draw()
    window_1.flip()
    core.wait(test_image_duration)
    window_1.flip()
    core.wait(test_isi)
    display_time += (test_image_duration+test_isi);
    
    keys = event.getKeys(keyList=['escape'], timeStamped=clock)

    for key in keys:
        if key[0] == 'escape':
            window_1.close()
            #trigger.close()
            core.quit()
    
    squares_36.draw()
    #trigger.write(b'b') # writes the ascii code of b (bigger) on the serial port
    counter.text = str(np.round(100*display_time)/100)
    counter.draw()
    window_1.flip()
    core.wait(test_image_duration)
    window_1.flip()
    core.wait(test_isi)
    display_time += (test_image_duration+test_isi);


window_1.close()
#trigger.close()
core.quit()
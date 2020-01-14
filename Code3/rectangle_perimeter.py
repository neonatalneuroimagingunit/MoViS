# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:06:20 2016

@author: Matteo Caffini
@date: 04-Apr-2016
@institution: CIMeC - University of Trento
@contact: matteo.caffini@unitn.it
"""

import numpy as np
import matplotlib.pyplot as plt
#import tkinter as tk
#import ctypes
import matplotlib.patches as mpatches

# monitor parameters

#my_dpi = 96 # dots per inch

#root = tk.Tk()
#width_px = root.winfo_screenwidth()
#height_px = root.winfo_screenheight() 
#width_mm = root.winfo_screenmmwidth()
#height_mm = root.winfo_screenmmheight() 
# 2.54 cm = in
mm2inch = 25.4
#width_in = width_mm / mm2inch
#height_in = height_mm / mm2inch
#width_dpi = width_px/width_in
#height_dpi = height_px/height_in 

#user32 = ctypes.windll.user32
#user32.SetProcessDPIAware()
#[win_width, win_height] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
#my_dpi = win_width*96/width_px

# use this to overwrite monitor parameters
win_height = 1024 # screen size
win_width = 1280 # screen size
my_dpi = 96 # dots per inch
my_dpmm = my_dpi/mm2inch # dots per mm

# shapes parameters
#total_area = 20000 # total area
total_perimeter = 1000 # 1000 should be a safe value
#min_area = 250 # min area
#max_area = 2500 # max area
#min_area = total_area/10 # min area
#max_area = total_area/2 # max area
min_perimeter = total_perimeter/10 # min area
max_perimeter = total_perimeter/2 # max area
n_points = 5 # how many shapes
#background_color = (0,0,0) # default background RGB color (maybe later we want to make it dependent on something)
#shapes_color = (0,0,0) # default shapes RGB color (maybe later we want to make it dependent on something)
#marker_shape = np.array([[-2, -1], [-2, 1], [2, 1], [2, -1], [-2, -1]]) # use this if you want rectangles
#marker_shape = 'o' # use facecolors='k' in scatter plot if you want them filled (in black) or facecolors='none' if you want only contours

n_figures = 10
centers_distances = np.zeros((n_points, n_points, n_figures))
centers_distances_min = np.zeros(n_figures)
edges_distances = np.zeros((n_points, n_points, n_figures))
edges_distances_min = np.zeros(n_figures)

for hh in np.arange(n_figures):
    figure_name_basis = str(n_points) + '_rectangles_perimeter_'
    figure_file_type = 'png'
    figure_name = figure_name_basis + str(hh) + '.' + figure_file_type

    # get n random areas with given total area
    perimeters = np.zeros(n_points)
    areas = np.zeros(n_points)
    for ii in np.arange(n_points):
        #partial_sum = radii.sum()
        perimeters[ii] = np.random.randint(min_perimeter, max_perimeter)
        #areas[ii] = np.random.randint(min_area, max_area)
    
#    areas = total_area*areas/areas.sum()
#    areas.sort()
#    areas = areas[::-1]
    
    perimeters = total_perimeter*perimeters/perimeters.sum()
    perimeters.sort()
    perimeters = perimeters[::-1]
    radii = perimeters/(2*np.pi)
    check_tot_perimeter = perimeters.sum()
    areas = np.pi*(radii**2)
    
    side_square = perimeters/4
    
    side_a = np.zeros(n_points)
    side_b = np.zeros(n_points)
    perimeter_check = np.zeros(n_points)
    for ii in np.arange(n_points):
        #side_a[ii] = np.random.randint(30, 70) # wrong values, get better ones
        side_a[ii] = side_square[ii]*(1+np.random.choice([-1,1])*np.random.uniform(0,0.3))
        #side_b[ii] = np.random.randint(10, 100)
        side_b[ii] = perimeters[ii]/2-side_a[ii]
        perimeter_check[ii] = 2*(side_a[ii]+side_b[ii])
    
    radii = np.zeros(n_points)
    #radii[:] = np.sqrt(side_a.max()**2 + side_b.max()**2) # too big
    #radii = np.sqrt(areas/np.pi)
    radii[:] = 65
    #check_tot_area = areas.sum()
    check_tot_perimeter = perimeter_check.sum()
    
    # make cartesian grid
    #max_area_real = radii.max()**2*np.pi
    #max_diameter_real = np.sqrt(max_area_real/np.pi)
    #grid_step = max_diameter_real*1.1
    grid_step = 1
    x_max = np.minimum(win_height, win_width)*0.4 # control grid size by monitor size
    y_max = x_max # make grid simmetrical for 90 degrees rotations
    n_x = 2*x_max/grid_step
    n_y = n_x # 90 degrees simmetrical
    x = np.linspace(-x_max, x_max, n_x)
    y = np.linspace(-y_max, y_max, n_y)
    x_matrix, y_matrix = np.meshgrid(x, y) # this produces the actual grid
    
    # plot square grid (comment later, only to check measurments and grid density)
    #grid_fig = plt.figure() 
    #grid_ax_square = grid_fig.add_subplot(131)
    #grid_ax_square.axis('equal')
    #grid_ax_square.set_xlim((-win_width/2, win_width/2))
    #grid_ax_square.set_ylim((-win_height/2, win_height/2))
    #grid_ax_square.plot(x_matrix, y_matrix, color='r', ls='none', marker='.')
    
    # find prohibited anchor points (in this case points outside a circle centered on the screen and with radius equal to x and y grid size)
    r = np.sqrt(x_matrix**2 + y_matrix**2)
    allowed = r < (x_max*0.8-radii.max()*1.2)
    #allowed = r < x_max
    #outside = r >= x_max
    
    # plot circular grid (comment later, only to check measurments and grid density)
    #grid_ax_circ = grid_fig.add_subplot(132)
    #grid_ax_circ.axis('equal')
    #grid_ax_circ.set_xlim((-win_width/2, win_width/2))
    #grid_ax_circ.set_ylim((-win_height/2, win_height/2))
    #grid_ax_circ.plot(x_matrix[allowed], y_matrix[allowed], color='r', ls='none', marker='.')
    #grid_ax_circ.plot(x_matrix[np.logical_not(allowed)], y_matrix[np.logical_not(allowed)], color='b', ls='none', marker='.')
    
    # get random (avoiding prohibited) positions (in cartesian coordinates) for the centers of the shapes
    centers_coords = np.zeros([n_points, 2])
    #grid_fig = plt.figure(facecolor=(0,0,0), figsize=(win_width/my_dpi,win_height/my_dpi))
    #grid_ax = grid_fig.add_subplot(111)
    #grid_ax.axis('equal')
    #grid_ax.set_xlim((-win_width/2, win_width/2))
    #grid_ax.set_ylim((-win_height/2, win_height/2))
    #grid_ax.plot(x_matrix[allowed], y_matrix[allowed], color='r', ls='none', marker='.')
    #grid_ax.plot(x_matrix[np.logical_not(allowed)], y_matrix[np.logical_not(allowed)], color='b', ls='none', marker='.')
    
    for ii in np.arange(radii.size):
        X=np.ma.masked_array(x_matrix, np.logical_not(allowed))
        pos = np.random.choice(X.count(), size=1)
        idx = tuple(np.take((~X.mask).nonzero(), pos, axis=1))
        centers_coords[ii,0] = x_matrix[idx[0][0],idx[1][0]]
        centers_coords[ii,1] = y_matrix[idx[0][0],idx[1][0]]
        r_temp = np.sqrt((x_matrix-centers_coords[ii,0])**2 + (y_matrix-centers_coords[ii,1])**2)
        allowed_temp = r_temp > (radii.max()*3) # you want to play with this (most unfortunate event is two big circles touching if you set to 2 max radius)
        allowed = np.logical_and(allowed, allowed_temp)
    #    grid_ax = grid_fig.add_subplot(3,5,ii+1)
    #    grid_ax.axis('equal')
    #    grid_ax.set_xlim((-win_width/2, win_width/2))
    #    grid_ax.set_ylim((-win_height/2, win_height/2))
    #    grid_ax.plot(x_matrix[allowed], y_matrix[allowed], color='r', ls='none', marker='.')
    #    grid_ax.plot(x_matrix[np.logical_not(allowed)], y_matrix[np.logical_not(allowed)], color='b', ls='none', marker='.')
    
    # compute distances
    spam = np.zeros((n_points,n_points))
    egg = np.zeros((n_points,n_points))
    for aa in np.arange(n_points):
        for bb in np.arange(n_points):
            spam[aa,bb] = np.sqrt(np.sum((centers_coords[aa,:] - centers_coords[bb,:])**2, axis=0))
            egg[aa,bb] = spam[aa,bb] - (side_a[aa]+side_b[aa])/2 - (side_a[bb]+side_b[bb])/2
    centers_distances[:,:,hh] = spam
    centers_distances_min[hh] = np.min(spam[np.nonzero(spam)])
    edges_distances[:,:,hh] = egg.clip(min=0)
    edges_distances_min[hh] = np.min(egg[np.nonzero(egg.clip(min=0))])
    
    # plot circular grid with holes (comment later, only to check measurments and grid density)
    #grid_ax_circ_holes = grid_fig.add_subplot(111)
    #grid_ax_circ_holes.axis('equal')
    #grid_ax_circ_holes.set_xlim((-win_width/2, win_width/2))
    #grid_ax_circ_holes.set_ylim((-win_height/2, win_height/2))
    #grid_ax_circ_holes.plot(x_matrix[allowed], y_matrix[allowed], color='r', ls='none', marker='.')
    #grid_ax_circ_holes.plot(x_matrix[np.logical_not(allowed)], y_matrix[np.logical_not(allowed)], color='b', ls='none', marker='.')
    
    # plot final figure
    fig = plt.figure(facecolor=(0,0,0), figsize=(win_width/my_dpi,win_height/my_dpi))
    ax = fig.add_subplot(111, aspect='equal')
    ax.axis('off')
    ax.set_xlim((-win_width/2, win_width/2))
    ax.set_ylim((-win_height/2, win_height/2))
    # big white circle
    circle = mpatches.Circle((0,0), x_max, facecolor=(1,1,1))
    ax.add_patch(circle)
    # shapes
    for ii in np.arange(radii.size):
        #shape = mpatches.Circle((centers_coords[ii,0], centers_coords[ii,1]), radii[ii], facecolor=(0,0,0))
        shape = mpatches.Rectangle((centers_coords[ii,0], centers_coords[ii,1]), side_a[ii], side_b[ii], facecolor=(0,0,0))
        ax.add_patch(shape)
    fig.savefig(figure_name, facecolor=fig.get_facecolor(), edgecolor='none', dpi=my_dpi)
    
# plot histogram of distances
centers_distances = centers_distances/my_dpmm
centers_distances_min = centers_distances_min/my_dpmm
edges_distances = edges_distances/my_dpmm
edges_distances_min = edges_distances_min/my_dpmm

centers_distances_avg = np.mean(centers_distances[np.nonzero(centers_distances)])
centers_distances_min_avg = centers_distances_min.mean()
edges_distances_avg =np.mean(edges_distances[np.nonzero(edges_distances)])
edges_distances_min_avg = edges_distances_min.mean()

hist_dist_fig, hist_dist_ax = plt.subplots()
bp = plt.boxplot((centers_distances[np.nonzero(centers_distances)], centers_distances_min, edges_distances[np.nonzero(edges_distances)], edges_distances_min), notch=0)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

hist_dist_ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Hide these grid behind plot objects
hist_dist_ax.set_axisbelow(True)
hist_dist_ax.set_title('Recap of distances between objects (mm)')
hist_dist_ax.set_xlabel('Type')
hist_dist_ax.set_ylabel('Value')

boxColors = ['darkkhaki', 'royalblue']

numBoxes = 4
medians = list(range(numBoxes))
for i in range(numBoxes):
    box = bp['boxes'][i]
    boxX = []
    boxY = []
    for j in range(5):
        boxX.append(box.get_xdata()[j])
        boxY.append(box.get_ydata()[j])
    boxCoords = list(zip(boxX, boxY))
    # Alternate between Dark Khaki and Royal Blue
    k = i % 2
    boxPolygon = mpatches.Polygon(boxCoords, facecolor=boxColors[k])
    hist_dist_ax.add_patch(boxPolygon)
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    medianX = []
    medianY = []
    for j in range(2):
        medianX.append(med.get_xdata()[j])
        medianY.append(med.get_ydata()[j])
        plt.plot(medianX, medianY, 'k')
        medians[i] = medianY[0]

# Set the axes ranges and axes labels
hist_dist_ax.set_xlim(0.5, numBoxes + 0.5)
top = centers_distances.max()*1.2
bottom = 0
hist_dist_ax.set_ylim(bottom, top)
xtickNames = plt.setp(hist_dist_ax, xticklabels=('Centers','Centers min','Edges','Edges min'))
plt.setp(xtickNames, rotation=45, fontsize=8)

# Add text
pos = np.arange(numBoxes) + 1
upperLabels = [str(np.round(s, 2)) for s in medians]
weights = ['bold', 'semibold']
for tick, label in zip(range(numBoxes), hist_dist_ax.get_xticklabels()):
    k = tick % 2
    hist_dist_ax.text(pos[tick], top - (top*0.05), upperLabels[tick], horizontalalignment='center', size='medium', weight=weights[k], color=boxColors[k])
# Tells Python which module to import and abbreviates it as plt.
import matplotlib.pyplot as plt

# Tells Python which folder and what class to import from that folder.
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
	
    '''
    Make a random walk, and plot the points. Abbreviates the RandomWalk()
    and call fill_walk() to create and store the points generated. Add
    a value of 50,000 to increase the number of points.
    '''
    
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Set the size of the plotting window.
    plt.figure(figsize = (14, 7))

    '''
    Scatters the x and y points with a point size of 15 and displays.
    Store a list of numbers equal to the points in a walk in variable
    (point_numbers)and remove the black outline around the points. After
    increasing the number of points to 50,000 in the RandomWalk()
    insatnce low the dot size so it is easier to plot.
    '''
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers,
        cmap = plt.cm.Reds, edgecolor = 'none', s = 1)
    '''  
      Emphasize the first and last points. Adding the start and end plot
      just before the call to plt.show() places them on top of the other
      points.
    '''
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'yellow',
        edgecolor = 'none', s = 100)
        
    # Remove the axes.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    '''
    I could not get the above commad to turn the axes off so I found
    a work around that gave me the same result.
    '''
    
    plt.axis('off')
    plt.show()
    
    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break

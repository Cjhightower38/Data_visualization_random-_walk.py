# Tells Python which module to import and abbreviates it as plt.
import matplotlib.pyplot as plt

# Tells Python which folder and what class to import from that folder.
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
	
    '''
    Make a random walk, and plot the points. Abbreviates the RandomWalk()
    and call fill_walk() to create and store the points generated.
    '''
    rw = RandomWalk()
    rw.fill_walk()

    # Scatters the x and y points with a point size of 15 and displays.
    plt.scatter(rw.x_values, rw.y_values, s = 15)
    plt.show()
    
    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break

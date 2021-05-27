from random import choice

class RandomWalk():
	'''A class to generate random walks.'''
	
	'''
	Sets the number of points to 5000 to create quicka and interesting
	walks.
	'''
	
	def __init__(self, num_points = 5000):
		'''Initialize attributes of a walk.'''
		self.num_points = num_points
		
		# All walksare stored in a x or y list and  start at (0, 0).
		self.x_values = [0]
		self.y_values = [0]

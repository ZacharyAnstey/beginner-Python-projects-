"""
This program simulates a single coin toss every time the program is ran
"""

import random

coin = random.randint(0,1) # create a random number between 0 and 1 0 = tails 1 = heads 
if (coin == 1):
	print('heads')
else:
	print('tails ')
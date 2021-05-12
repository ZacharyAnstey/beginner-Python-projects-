# This program takes input from the user to calculate how much paint is reguired to paint a room
# assuming one quart covers 80 square feet 

import math
coverage = 80
length1 = float(input('Please enter the length of the first wall'))
length2 = float(input('Please enter the length of the second wall'))
height = float(input('Please enter the height of the walls'))

area1= 2 *(length1 * height)
area2 = 2 * (length2 * height)
total_area = area1 + area2
num_quarts = math.ceil(total_area/coverage)
print('the number of quarts of paint required to paint a room',total_area,'in size is ', num_quarts)
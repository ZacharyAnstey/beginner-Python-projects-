"""
The following is a program to get the length of 3 sides of a triangle and ouput the type of triangle
"""

# Get the values for the length of the sides of a triangle
side1 = float(input('Enter the length of the first side of your triangle'))
side2 = float(input('Enter the length of the second side of your triangle'))
side3 = float(input('Enter the length of the third side of your triangle'))

# Now to find the type of triangle 
if (side1 * side1 == side2 * side2 +side3 * side3):
	print('This is a right angle triangle')
elif (side1 * side2 > side2 + side2 + side3 * side3):
	print('This is an obtuse triangle')
else:
	print('This is an acute triangle ')
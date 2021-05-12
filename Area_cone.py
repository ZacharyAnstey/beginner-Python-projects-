"""
The following is a program to calculate the area of a cone 
This program will take input from the user for radius and height 
of the cone and calculate its area 
"""
import math
PI = math.pi
radius = int(input('Enter the radius of the base of the cone '))
height = int(input("Enter the height of the cone"))
area = PI * radius *(radius + math.sqrt(math.pow(height,2)+math.pow(radius,2)))
print('The area of a cone with base radius',radius, 'and height',height,'is',area)
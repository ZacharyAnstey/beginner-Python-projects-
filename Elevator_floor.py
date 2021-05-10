""" 
Many Hotels and Buildings do not have a 13th floor.
Instead the floors of the building skiped the 13th floor,
And go directly to the 14th floor. so the floors would go
...10,11,12,14,15,16.....
Bellow is a program to calculate the actual floor that you are on 
"""

# First we need to get an input from the user as to what floor button they pressed in the elevator 
pressed = int(input('Enter the floor number that you pressed in the elevator :'))

# Now we need to calculate the actual floor the user is on
# There are two cases 
# 1) pressed number is greater than 13 
# 2) pressed number is less than 13 

if pressed > 13: # case 1: take one number away from the pressed floor.
	actualFloor = pressed - 1 
else: # case 2 
	actualFloor = pressed

# Now to print the results 
print('You pressed the button to go to floor',pressed,'The actual floor you are going to is ',actualFloor )
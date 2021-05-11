"""
This is a program to test if someone qualifies to be part of a basketball team 
The requirements are that the player must be over 6ft tall 
"""
Height_limit = 6.0

name = input('Enter the name of the potential team member')
height = int(input('Enter the height of the potential team member in feet. '))

# Check height with limit. 
if height >= Height_limit:
    print('Hello',name,'Welcome to the team')
else:
    print('Sorry',name,'You did not make the team you are not tall enough. ')
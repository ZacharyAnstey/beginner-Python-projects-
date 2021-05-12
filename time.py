"""
This program takes a number of second from a user and prints
how many hours, minues, seconds there is 
"""
seconds = int(input('Enter a number of seconds'))

# hours
hours = seconds // 3600
seconds = seconds % 3600

# Minutes
minutes = seconds //60
seconds = seconds % 60 

print('The current time is %02d:%02d:%02d'%(hours,minutes,seconds))
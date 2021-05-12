"""
This program while take as input the percentage of cloud cover 
and print the type of day it is clear, partialy cloudy, cloudy, overcast 
"""

# First we have to set some parameters
Clear_low_limit = 0
Clear_limit = 30
Partly_cloudy_limit = 70
Cloudy_limit = 99
overcast = 100

# Next we have to obtain the percantage of cloud cover from user 
user = int(input('Enter the percentage of cloud cover'))

# Now we have to find the cloud cover for that day
if (user >= Clear_low_limit):
    if(user <= Clear_limit):
        print('It is a clear day')
    elif(user <= Partly_cloudy_limit):
        print('it is partialy cloudy')
    elif(user <= Cloudy_limit):
        print('It is a cloudy day')
    elif(user == overcast):
        print('it is overcast today')
    else:
        print('You did not enter a correct percentage. ')

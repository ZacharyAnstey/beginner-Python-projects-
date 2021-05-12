"""
The following is a program to calculate the cost of a call
"""
initial_time = 3 
inital_rate =1.44
additonal_rate=0.25
callTime = int(input('Enter the length of your call in minues'))
call_cost = (callTime - initial_time) * additonal_rate + inital_rate
print('The cost to make your call is %.2f'%call_cost )
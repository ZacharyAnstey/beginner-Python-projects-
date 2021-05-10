''' 
This is a program to calculate the miles per gallon for your car 
The steps involed in this probmel are 
1) get gas burned by user 
2) get miles driven by user 
3) calculate miles per gallon 
'''
# 1 get gas butned by user 
gas = int(input('Enter the amount of gas you burned in your car in gallons'))

# 2 get miles driven by user
miles = int(input('Enter the number of miles you have driven'))

# 3 Calculate miles per gallon 
mpg = miles / gas 
print('The gas milage for your car is ',mpg,'miles per gallon')

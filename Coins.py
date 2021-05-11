""" 
This program will take a number of pennies and compute how much change you have 
in toonies, loonies, quates, dimes, nickels 
"""

# First we have to get the number of pennies 
pennies = int(input('Enter the number of pennies you have '))

# TOONIES 

# Second we hve to compute the number of toonies that can be given back # note 1 toonie is $2 cad 
toonies = pennies // 200

# Next we have to compute how many pennies are left over. 
pennies = pennies % 200


# LOONIES

# Now to compute how many loones that will be given back # Note 1 loonie is $1 cad
loonies = pennies // 100 

# Once again we have to calculate how many pennies are left over 
pennies = pennies % 100



# QUATERS

# Now to compute how many quaters are left over 
quaters = pennies // 25 

# Once again we have to update pennies 
pennies = pennies % 25 

# DIMES
dimes = pennies // 10 
pennies = pennies % 10 

# Nickels 
Nickels = pennies // 5
pennies = pennies % 5 

# Now to print the results 
print('The number of toonies is  %4d'%toonies)

print('The number of loonies is  %4d'%loonies)

print('The number of quaters is  %4d'%quaters)

print('The number of dimes is  %4d'%dimes)

print('The number of nickels is  %4d'%Nickels)

print('The number of pennies is  %4d'%pennies)


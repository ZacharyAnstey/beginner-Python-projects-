# This program calculates the time required to double an investment 
Rate = int(input('Enter your intrest rate of your investement'))
Initial_balance = int(input('Enter your inital balance'))
target = 2 * Initial_balance
balance = Initial_balance
year = 0
while balance < target:
    year = year + 1
    interest = balance * Rate/100
    balance = balance + interest
print('The investement doubled after', year,'years')
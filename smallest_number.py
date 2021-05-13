"""
The following is a program to take 3 numbers from a user and find the smallest number
"""
num1 = int(input('Enter a number'))
num2 = int(input('Enter a second number'))
num3 = int(input('Enter a third number'))

if num1 <= num2 and num1 <= num3:
    print('The smallest number is', num1)
elif num2 <= num1 and num2 <= num3:
    print('The smallest number is ',num2)
else: 
    print('The smallest number is ', num3)
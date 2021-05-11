"""
This is a program to determine if a random number from 1 - 100 is odd or even
"""
import random
num = random.randint(1,100)
if ((num % 2) == 0):
    print('The number',num,'Is even')
else:
    print('The number',num,'Is odd ')
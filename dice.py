"""
The folowing program simulate rolling a pair of dice 10 times

"""
from random import randint
for i in range(10):
    d1 = randint(1,6)
    d2 = randint(1,6)

    print(d1,d2)
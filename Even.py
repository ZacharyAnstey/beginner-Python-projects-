# This is a python program to find the even numbers for a list 
def even(list):
    for n in list:
        if n%2 == 0:
            print(n,end=' ')
max_num =int(input('How many numbers would you like to add to the list'))
list = []
for _ in range(0,max_num):
    num = int(input('Enter a number to add to the list. '))
    list.append(num)
print('List of numbers')
even(list)
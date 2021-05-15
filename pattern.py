# This program is a recursive function to print a digram 


# First we need to define a function 
def recursivePrint(n,s):
    if n > 0:
        print(s*n)
        recursivePrint(n-1,s)



recursivePrint(8,"*") # call the function where n is how many line in the diagram and , s is the symbol you want to use the draw the diagram 
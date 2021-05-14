"""
This program will take inuts from the user and create a mad lib 
"""
loop = 1 
while loop < 10:
    noun = input('Enter a noun')
    p_noun = input('Enter a plural noun ')
    noun2 = input('Enter a noun ')
    place = input('Enter a place')
    adjective = input('Enter an adjective')
    noun3 = input('Enter a noun ')

# Now to print the story 
    print('----------------------------------------------------------')
    print('Be kind to your', noun,'- footed', p_noun)
    print("for a duck may be somebody's",noun2,',')
    print('Be king to your',p_noun,'in',place)
    print('where the weather is always',adjective)
    print()
    print('You may think that is the',noun3)
    print('well it is ')    
    print('----------------------------------------------------------')
    loop = loop + 1
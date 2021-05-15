"""
This program is for a game of rock paper scissors. To write this program there are a few things we need 


"""
import random 
import os 
import re 


os .system('cls' if os.name=='nt' else 'clear')

while (1<2):
	print('\n')
	print('1, 2, 3, Rock, Paper, Scissors, Gooooo')
	userChoice = input('Make your choice enter R for rock P for paper of S for scissors: ')
	if not re.match('[SsRrPp]',userChoice):
		print('Please choose a letter')
		print("Rock, Scissors or Paper")
		continue 
	# Echo the user choice 
	print('You chose: ' + userChoice)
	choices = ['R','P','S']
	computer = random.choice(choices)
	print("I choose" + computer)
	if computer == str.upper(userChoice):
		print('The game ends in a tie ')
	elif computer == 'R' and userChoice.upper() == 'S':
		print('Scissors beats rock, The computer wins ')
		continue
	elif computer == 'S' and userChoice.upper() =='P':
		print('Scissors bears paper, The computer wins  ')
		continue
	elif computer == 'P' and userChoice.upper() == 'R':
		print('Paper beats rock, The computer wins')
		continue
	else:
		print('You win ')

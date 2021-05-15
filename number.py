"""
This program is a number geussing game. This program will generate a random number from 1 to 10
Then the program will take a number geuss from the user 
The more geusses the lower your score 
"""
import random 
attempts_list = [] 

def show_score():
    if len(attempts_list) <= 0:
        print('Currently there is no high score, it is yours for the taking')
    else:
        print('The current high score is {} attempts'.format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1,10))
    print('Hello welcome to the number geussing game')
    player_name = input('Enter you name')
    wanna_play = input('Hi {}, do you want to play the number geussing game? Enter yes of no '.format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() =='yes':
        try:
            geuss = input('Pick a number between 1 and 10')
            if int(geuss) < 1 or int(geuss) > 10:
                raise ValueError("Please geuss a number within the given range")
            if int(geuss) == random_number:
                print('YOU WIN!!!!!!!!!!!!!!!!!')
                attempts += 1
                attempts_list.append(attempts)
                print('It took you {} attempts'.format(attempts))
                play_again = input('Do you want to play againg enter yes or no ')
                attempts = 0
                show_score()
                random_number = int(random.randint(1,10))
                if play_again.lower() == ' no':
                    print('Good bye')
                    break
            elif int(geuss) > random_number:
                print('Its lower')
                attempts += 1
            elif int(geuss) < random_number:
                print('Its higher')
                attempts +=1
        except ValueError as err: 
            print('that is not a valid number try again ')
            print("({})".format(err))
    else:
        print('Good bye')

if __name__ == '__main__':
    start_game()






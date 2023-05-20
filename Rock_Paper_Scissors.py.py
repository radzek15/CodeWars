'''
Rock Paper Scissors Game written in Python
Game logic is simple:
  - Player chooses one of 3 available choices
  - PC chooses randomly of 3 available choices
Program declares winner and looser or if it is a tie
'''

import random
name = input('Enter your name: ')
options = ['rock', 'paper', 'scissors']

Massages = ['You win', 'You Lose', 'It is a tie']

cp_choice = random.choice(options)
choice = input('Please choose one of {}'.format(options))

def win_or_lose(me,cp):
    results = {'rock':{
            'rock': Massages[2],
            'paper': Massages[1],
            'scissors': Massages[0]},
        'paper' : {
            "rock": Massages[0],
            "paper": Massages[2],
            "scissors": Massages[1]},
        "scissors":{
            "rock": Massages[1],
            "paper": Massages[0],
            "scissors": Massages[2]}}

    return results[me][cp]

try:
    Winner = win_or_lose(choice,cp_choice)
    print('Computer choose {}'.format(cp_choice))
    print(Winner)
except KeyError:
    print('You choose wrong, Please try again')

print('Thank you for playing {}. Play again anytime u want'.format(name))